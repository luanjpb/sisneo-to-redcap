import streamlit as st
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from triagem_models import TbAmostra, TbPessoa
from datetime import datetime

class SisneoConnector:

    def __init__(self):
        self.engine = create_engine(
            st.secrets["database_url"]
        )
        self.session = Session(self.engine)

    def amostra_to_dict(self, amostra):
        return {
            "codigo_amostra": amostra.tb_pessoa.co_ent_pessoa,
            "data_coleta": datetime.strptime(str(amostra.dt_col_amostra), "%Y%m%d") if amostra.dt_col_amostra else None,
            "tipo_amostra": amostra.tb_tipo_amostra.ds_tp_amostra,
            "nome": amostra.tb_pessoa.no_pessoa,
            "nome_mae": amostra.tb_pessoa.no_mae,
            "data_nascimento": datetime.strptime(str(amostra.tb_pessoa.dt_nascimento), "%Y%m%d") if amostra.tb_pessoa.dt_nascimento else None,
            "sexo": amostra.tb_pessoa.se_pessoa,
            "municipio_residencia": amostra.tb_pessoa.tb_endereco_pessoas[0].tb_municipio.no_municipio or "",
            "municipio_coleta": amostra.tb_unidade_saude.tb_municipio.no_municipio or ""
        }
    
    def amostras_to_list(self, amostras):
        return [self.amostra_to_dict(i) for i in amostras]

    def select_amostra_by_code(self, code):
        query = (select(TbAmostra)
            .join(TbAmostra.tb_pessoa)
            .where(
                TbAmostra.tb_pessoa.has(co_ent_pessoa = code)
            )
        )
        return query
    
    def select_amostra_by_nome(self, nome):
        query = (select(TbAmostra)
            .join(TbAmostra.tb_pessoa)
            .where(
                TbPessoa.no_pessoa.ilike(f"%{nome}%")
            )
        )
        return query
    
    def select_amostras(self, limit=100):
        query = (select(TbAmostra))
        return query
    
    def apply_date_filter(self, query, data_inicial, data_final):
        return query.where(
            (
                TbAmostra.dt_col_amostra >= int(f"{data_inicial.year}{data_inicial.month}{data_inicial.day if data_inicial.day > 9 else '0'+ str(data_inicial.day)}")
            ) & (
                TbAmostra.dt_col_amostra <= int(f"{data_final.year}{data_final.month}{data_final.day if data_final.day > 9 else '0' + str(data_final.day)}")
            )
        )
    
    def run_query(self, query, limit=100):
        query = query.limit(limit)
        return self.session.scalars(query)
