import streamlit as st
from sisneo_connector import SisneoConnector
from redcap_connector import RedCapConnector
from datetime import datetime

st.set_page_config(
    page_title="Sisneo to RedCap",
    layout="wide"
)

st.title("Sisneo to RedCap")

redcap_connector = RedCapConnector()

records = [{
    "codigo_amostra": "00245356",
    "data_coleta": datetime.fromisoformat("2023-12-06"),
    "tipo_amostra": "Papel filtro",
    "nome": "AYLLA LOUISE DA COSTA",
    "nome_mae": "LAURA BEATRIZ DA COSTA",
    "data_nascimento": datetime.fromisoformat("2023-11-27"),
    "sexo": "F",
    "municipio_residencia": "Alta Floresta",
    "municipio_coleta": "Alta Floresta"
},
{
    "codigo_amostra": "00245385",
    "data_coleta": datetime.fromisoformat("2023-12-06"),
    "tipo_amostra": "Papel filtro",
    "nome": "GABRIEL NETO SOARES",
    "nome_mae": "LOURICE SOARES DA SILVA",
    "data_nascimento": datetime.fromisoformat("2023-12-02"),
    "sexo": "M",
    "municipio_residencia": "Jangada",
    "municipio_coleta": "Jangada"
}]

redcap_connector.login()

sisneo_connector = SisneoConnector()

amostras = []

with st.form("Pesquisa"):
    codigo_amostra = st.text_input("Código da amostra")

    nome = st.text_input("Nome")

    col_1, col_2 = st.columns(2)

    with col_1:
        data_inicial = st.date_input(
            "Data inicial", format="DD/MM/YYYY", help="Se refere ao campo data de coleta."
        )

    with col_2:
        data_final = st.date_input(
            "Data final", format="DD/MM/YYYY", help="Se refere ao campo data de coleta."
        )

    if st.form_submit_button("Pesquisar"):
        st.session_state.pop("amostras")
        if codigo_amostra:
            query = sisneo_connector.select_amostra_by_code(codigo_amostra)
        elif nome:
            query = sisneo_connector.select_amostra_by_nome(nome)
        else:
            query = sisneo_connector.select_amostras()

        query = sisneo_connector.apply_date_filter(query, data_inicial, data_final)

        amostras = sisneo_connector.run_query(query)

if 'amostras' in st.session_state:
    amostras = st.session_state['amostras']
else:
    amostras = sisneo_connector.amostras_to_list(amostras)
    st.session_state['amostras'] = amostras

st.dataframe(
    amostras,
    use_container_width=True
)

st.write("Limite de 100 resultados por pesquisa")

with st.form("Submissão ao RedCap"):

    amostras_selecionadas = st.multiselect(
        "Amostras selecionadas",
        format_func=lambda x: f"[{x['codigo_amostra']}] - {x['nome']}",
        options=amostras
    )

    submited = st.form_submit_button("Enviar ao RedCap")

    if submited:

        with st.status("Obtendo dados do RedCap", expanded=True) as status:
            redcap_data = redcap_connector.get_redcap_data()

            amostras_ja_enviadas = []
            codigos_ja_enviados = []

            status.write("Checando e enviando amostras")
            for i, amostra in enumerate(amostras_selecionadas):
                amostras_ja_enviadas.append(amostra)
                record = redcap_connector.get_record_in_data(amostra, redcap_data)

                if record.size > 0:
                    amostras_ja_enviadas[i]['id_redcap'] = record.iloc[0].record_id
                    amostras_ja_enviadas[i]['status'] = "Já registrado no RedCap"
                    continue
                elif amostra['codigo_amostra'] in codigos_ja_enviados:
                    amostras_ja_enviadas[i]['id_redcap'] = ""
                    amostras_ja_enviadas[i]['status'] = "Duplicado nos registros do SisNeo. Paciente possui mais de uma amostra."
                    continue

                try:
                    new_record_id = redcap_connector.get_new_record_id()

                    new_record_page_link = redcap_connector.get_new_record_page_link(new_record_id)

                    response = redcap_connector.add_record(
                        new_record_page_link,
                        amostra,
                        new_record_id
                    )

                    amostras_ja_enviadas[i]['id_redcap'] = new_record_id
                    amostras_ja_enviadas[i]['status'] = "Sucesso"
                except Exception as e:
                    amostras_ja_enviadas[i]['id_redcap'] = ""
                    amostras_ja_enviadas[i]['status'] = "Erro ao inserir registro no RedCap"
                    amostras_ja_enviadas[i]['erro'] = f"Erro: {e}"

                codigos_ja_enviados.append(amostra['codigo_amostra'])

            status.update(label="Sucesso!", state="complete", expanded=False)

        st.write("Amostras enviadas")
        st.dataframe(
            amostras_ja_enviadas
        )