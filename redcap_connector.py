from requests_html import HTMLSession
from urllib.parse import urlparse, parse_qs
import streamlit as st
import re
from pandas import DataFrame
from datetime import datetime

class RedCapConnector:

    def __init__(self):
        self.session = HTMLSession()

    def login(self):
        r = self.get(
            "https://redcap.hcpa.ufrgs.br/"
        )

        data = {
            'username': st.secrets['redcap_username'],
            'password': st.secrets['redcap_password']
        }

        for i in r.html.find('input[type=hidden]'):
            data[i.attrs['name']] = i.attrs['value']

        r = self.post(
            "https://redcap.hcpa.ufrgs.br/redcap/index.php?action=myprojects",
            data=data
        )

        try:
            link_projeto = r.html.find('a[class=aGrid]')[0]
        except Exception as e:
            st.error("Não foi possível se conectar ao RedCap. Atualize e tente novamente.")
            st.stop()

        st.session_state["redcap_project_name"] = link_projeto.text
        st.session_state["redcap_pid"] = parse_qs(urlparse(link_projeto.attrs['href']).query)["pid"][0]

        self.get(
            link_projeto.attrs['href']
        )

        return r
    
    def parse_url(self, url: str):
        if url.startswith('http'):
            return url
        return f"https://redcap.hcpa.ufrgs.br{url}"
    
    def get(self, url, *args, **kwargs):
        url = self.parse_url(url)
        return self.session.get(url, *args, **kwargs)
    
    def post(self, url, *args, **kwargs):
        url = self.parse_url(url)
        return self.session.post(url, *args, **kwargs)
    
    def get_redcap_data(self):
        r = self.get(
            f"/redcap/redcap_v13.11.4/DataExport/index.php?pid={st.session_state['redcap_pid']}&report_id=ALL"
        )

        csrf_token = re.search(
            r"redcap_csrf_token *= *'([0-9a-f]+)'",
            r.text
        )[1]

        st.session_state['redcap_csrf_token'] = csrf_token

        r = self.post(
            f"/redcap/redcap_v13.11.4/DataExport/report_ajax.php?pid={st.session_state['redcap_pid']}&pagenum=1",
            data = {
                "report_id": "ALL",
                "redcap_csrf_token": csrf_token
            }
        )

        keys = [
            i.text.replace('\n', '') for i in r.html.xpath('div/table/thead/tr/th/div')
        ]

        data = self.page_data_to_list(r, keys)

        paginas = [
            i.attrs['value'] for i in r.html.find("select[class='report_page_select x-form-text x-form-field']")[0].find('option') if i.attrs['value'] not in ['ALL', '1']
        ]

        for pagina in paginas:
            r = self.post(
                f"/redcap/redcap_v13.11.4/DataExport/report_ajax.php?pid={st.session_state['redcap_pid']}&pagenum={pagina}",
                data = {
                    "report_id": "ALL",
                    "redcap_csrf_token": csrf_token
                }
            )
            data += self.page_data_to_list(r, keys)

        df = DataFrame.from_dict(data)
        df['dob'] = df["dob"].apply(lambda x: datetime.strptime(x, '%d-%m-%Y') if x else None)
        df['participant_name'] = df['participant_name'].apply(lambda x: x.upper().strip())
        df['mother_name'] = df['mother_name'].apply(lambda x: x.upper().strip())
        df['birth_city_mt'] = df['birth_city_mt'].apply(lambda x: re.sub('\(\d+\)', '', x).strip())
        df['sex'] = df['sex'].apply(lambda x: {"Feminino (0)": "F", "Masculino (1)": "M"}.get(x, ""))
        return df

    def page_data_to_list(self, page_data, keys):
        data = [
            {key: value.text for key, value in zip(keys, j.find('td'))} for j in page_data.html.xpath('div/table/tr')
        ]
        return data
    
    def get_new_record_id(self):
        r = self.get(
            f"/redcap/redcap_v13.11.4/DataEntry/record_home.php?pid={st.session_state['redcap_pid']}"
        )
        return re.search(
            r'&id=(\d+-\d+)',
            r.text
        )[1]

    def get_new_record_page_link(self, new_record_id):
        r = self.get(
            f"/redcap/redcap_v13.11.4/DataEntry/record_home.php?pid={st.session_state['redcap_pid']}&id={new_record_id}&auto=1&arm=1"
        )

        for link in r.html.find('#event_grid_table')[0].absolute_links:
            if link.find('page=identificao') != -1:
                return link
            
    def get_record_in_data(self, record, data):
        return data[
            (
                data.participant_name == record['nome'].upper()
            ) & (
                data.birth_city_mt == record['municipio_residencia'].upper()
            ) & (
                data.sex == record["sexo"]
            ) & (
                data.dob == record['data_nascimento']
            )
        ]
    
    def get_cidades_map(self, new_record_page_link):
        if 'cidades' in st.session_state:
            return st.session_state['cidades']
        
        r = self.get(
            new_record_page_link
        )

        cidades = {
            i.text: i.attrs['value'] for i in r.html.find('option[data-mlm-field=birth_city_mt]')
        }

        st.session_state['cidades'] = cidades

        return cidades
    
    def add_record(self, new_record_page_link, record, record_id):
        cidades = self.get_cidades_map(
            new_record_page_link
        )

        r = self.get(
            new_record_page_link
        )

        cidade_nascimento = cidades.get(
            record['municipio_residencia'].upper(), ""
        )

        cidade_coleta = cidades.get(
            record['municipio_coleta'].upper(), ""
        )

        data = {
            "redcap_csrf_token": st.session_state['redcap_csrf_token'],
            "__GROUPID__": r.html.find('input[name=__GROUPID__]')[0].attrs['value'],
            "submit-action": "submit-btn-saverecord",
            "hidden_edit_flag": r.html.find('input[name=hidden_edit_flag]')[0].attrs['value'],
            "participant_name": record["nome"],
            "mother_name": record["nome_mae"],
            "dob": datetime.strftime(record['data_nascimento'], '%d-%m-%Y') if record['data_nascimento'] else "",
            "dob_indisponivel": "" if record['data_nascimento'] else "1",
            "sex": {"F": "0", "M": "1"}.get(record["sexo"], "2"),
            "sex___radio": {"F": "0", "M": "1"}.get(record["sexo"], "2"),
            "state_birth": "2", # MT
            "state_birth___radio": "2", # MT
            "birthcity_outro_rs": "",
            "birth_city_sp": "",
            "birthcity_outro_sp": "",
            "birth_city_mt": cidade_nascimento,
            "birthcity_outro_mt": "" if cidade_nascimento else record['municipio_residencia'].upper(),
            "doc": datetime.strftime(record['data_coleta'], '%d-%m-%Y') if record['data_coleta'] else "",
            "doc_indisponivel": "" if record['data_coleta'] else "1",
            "srtn": "2", # SRTN/MT
            "srtn___radio": "2", # SRTN/MT
            "state_collection": "2", # MT
            "state_collection___radio": "2", # MT
            "city_collection_rs": "",
            "citycollection_outro_rs": "",
            "city_collection_sp": "",
            "citycollection_outro_sp": "",
            "city_collection_mt": cidade_coleta,
            "citycollection_outro_mt": "" if cidade_coleta else record['municipio_coleta'].upper(),
            "identificao_complete": "0", # Incomplete
            "record_id": record_id,
            "external-modules-temporary-record-id": re.search(
                r'"(external-modules-temporary-record-id-\d+-\d+)"',
                r.text
            )[1]
        }

        response = self.post(
            new_record_page_link,
            data=data
        )

        return response