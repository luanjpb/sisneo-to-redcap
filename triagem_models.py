# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
#import sqlalchemy as db


db = SQLAlchemy()



class TbAcaoTransacao(db.Model):
    __tablename__ = 'tb_acao_transacao'

    co_seq_acao_transacao = db.Column(db.Numeric(1, 0), primary_key=True, unique=True)
    ds_acao_transacao = db.Column(db.String(30), nullable=False)



class TbAcessoMonitoramentoOnline(db.Model):
    __tablename__ = 'tb_acesso_monitoramento_online'

    co_seq_acesso_monitoramento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_usuario_monitoramento = db.Column(db.ForeignKey('tb_usuario_monitoramento_online.co_seq_usuario_monitoramento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbAcessoMonitoramentoOnline.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_acesso_monitoramento_onlines')
    tb_usuario_monitoramento_online = db.relationship('TbUsuarioMonitoramentoOnline', primaryjoin='TbAcessoMonitoramentoOnline.co_seq_usuario_monitoramento == TbUsuarioMonitoramentoOnline.co_seq_usuario_monitoramento', backref='tb_acesso_monitoramento_onlines')



class TbAcessoPacienteOnline(db.Model):
    __tablename__ = 'tb_acesso_paciente_online'

    co_seq_acesso_paciente_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_usuapo_paciente_online = db.Column(db.ForeignKey('tb_usuario_paciente_online.co_seq_usuapo_paciente_online', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    ds_senha_paciente_online = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbAcessoPacienteOnline.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_acesso_paciente_onlines')
    tb_usuario_paciente_online = db.relationship('TbUsuarioPacienteOnline', primaryjoin='TbAcessoPacienteOnline.co_seq_usuapo_paciente_online == TbUsuarioPacienteOnline.co_seq_usuapo_paciente_online', backref='tb_acesso_paciente_onlines')



class TbAcessoTriagemOnline(db.Model):
    __tablename__ = 'tb_acesso_triagem_online'

    co_seq_acesso_triagem_online = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    co_seq_usuario_triagem_online = db.Column(db.ForeignKey('tb_usuario_triagem_online.co_seq_usuario_triagem_online', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbAcessoTriagemOnline.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_acesso_triagem_onlines')
    tb_usuario_triagem_online = db.relationship('TbUsuarioTriagemOnline', primaryjoin='TbAcessoTriagemOnline.co_seq_usuario_triagem_online == TbUsuarioTriagemOnline.co_seq_usuario_triagem_online', backref='tb_acesso_triagem_onlines')



class TbAgendamento(db.Model):
    __tablename__ = 'tb_agendamento'

    co_seq_agendamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_nao_comparecimento = db.Column(db.ForeignKey('tb_motivo_nao_comparecimento.co_seq_mot_nao_comparecimento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_canc_agenda = db.Column(db.ForeignKey('tb_motivo_cancelamento_agenda.co_seq_mot_canc_agenda', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_convenio = db.Column(db.ForeignKey('tb_convenio.co_seq_convenio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_local_coleta = db.Column(db.ForeignKey('tb_local_coleta.co_seq_local_coleta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_agendamento = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    hr_agendamento = db.Column(db.String(6), nullable=False)
    no_contato = db.Column(db.String(70))
    obs_agendamento = db.Column(db.String(2000))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_nao_comparecimento = db.Column(db.Numeric(14, 0))
    aut_nao_comparecimento = db.Column(db.String(20))
    dt_hr_registro_comparecimento = db.Column(db.Numeric(14, 0))
    aut_registro_comparecimento = db.Column(db.String(20))
    obs_contato = db.Column(db.String(8000))

    tb_convenio = db.relationship('TbConvenio', primaryjoin='TbAgendamento.co_seq_convenio == TbConvenio.co_seq_convenio', backref='tb_agendamentoes')
    tb_local_coleta = db.relationship('TbLocalColeta', primaryjoin='TbAgendamento.co_seq_local_coleta == TbLocalColeta.co_seq_local_coleta', backref='tb_agendamentoes')
    tb_motivo_cancelamento_agendum = db.relationship('TbMotivoCancelamentoAgendum', primaryjoin='TbAgendamento.co_seq_mot_canc_agenda == TbMotivoCancelamentoAgendum.co_seq_mot_canc_agenda', backref='tb_agendamentoes')
    tb_motivo_nao_comparecimento = db.relationship('TbMotivoNaoComparecimento', primaryjoin='TbAgendamento.co_seq_mot_nao_comparecimento == TbMotivoNaoComparecimento.co_seq_mot_nao_comparecimento', backref='tb_agendamentoes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbAgendamento.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_agendamentoes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbAgendamento.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_agendamentoes')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbAgendamento.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_agendamentoes')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbAgendamento.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_agendamentoes')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbAgendamento.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_agendamentoes')



class TbAgendamentoColeta(db.Model):
    __tablename__ = 'tb_agendamento_coleta'

    co_seq_agendamento_coleta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento = db.Column(db.ForeignKey('tb_agendamento.co_seq_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_coleta = db.Column(db.Numeric(14, 0))
    aut_coleta = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_inicio_coleta = db.Column(db.Numeric(14, 0))
    dt_hr_termino_coleta = db.Column(db.Numeric(14, 0))

    tb_agendamento = db.relationship('TbAgendamento', primaryjoin='TbAgendamentoColeta.co_seq_agendamento == TbAgendamento.co_seq_agendamento', backref='tb_agendamento_coletas')



class TbAgendamentoColetaConsulta(db.Model):
    __tablename__ = 'tb_agendamento_coleta_consulta'

    co_seq_agen_col_consulta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_convenio = db.Column(db.ForeignKey('tb_convenio.co_seq_convenio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_local_coleta = db.Column(db.ForeignKey('tb_local_coleta.co_seq_local_coleta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_primeira_consulta = db.Column(db.String(1))

    tb_convenio = db.relationship('TbConvenio', primaryjoin='TbAgendamentoColetaConsulta.co_seq_convenio == TbConvenio.co_seq_convenio', backref='tb_agendamento_coleta_consultas')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbAgendamentoColetaConsulta.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_agendamento_coleta_consultas')
    tb_local_coleta = db.relationship('TbLocalColeta', primaryjoin='TbAgendamentoColetaConsulta.co_seq_local_coleta == TbLocalColeta.co_seq_local_coleta', backref='tb_agendamento_coleta_consultas')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbAgendamentoColetaConsulta.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_agendamento_coleta_consultas')



class TbAgendamentoConsulta(db.Model):
    __tablename__ = 'tb_agendamento_consulta'

    co_seq_agendamento_consulta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_nao_comparecimento = db.Column(db.ForeignKey('tb_motivo_nao_comparecimento.co_seq_mot_nao_comparecimento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_canc_agenda = db.Column(db.ForeignKey('tb_motivo_cancelamento_agenda.co_seq_mot_canc_agenda', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_agendamento = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    hr_agendamento = db.Column(db.String(6), nullable=False)
    co_seq_unidade_saude_consulta = db.Column(db.Numeric(8, 0))
    obs_agendamento = db.Column(db.String(2000))
    no_contato = db.Column(db.String(70))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_nao_comparecimento = db.Column(db.Numeric(14, 0))
    aut_nao_comparecimento = db.Column(db.String(20))
    co_seq_prof_saude_consulta = db.Column(db.Numeric(8, 0))
    ide_agendamento_previsto = db.Column(db.String(1))
    dt_hr_confirmacao = db.Column(db.Numeric(14, 0))
    aut_confirmacao = db.Column(db.String(20))

    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbAgendamentoConsulta.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_agendamento_consultas')
    tb_motivo_cancelamento_agendum = db.relationship('TbMotivoCancelamentoAgendum', primaryjoin='TbAgendamentoConsulta.co_seq_mot_canc_agenda == TbMotivoCancelamentoAgendum.co_seq_mot_canc_agenda', backref='tb_agendamento_consultas')
    tb_motivo_nao_comparecimento = db.relationship('TbMotivoNaoComparecimento', primaryjoin='TbAgendamentoConsulta.co_seq_mot_nao_comparecimento == TbMotivoNaoComparecimento.co_seq_mot_nao_comparecimento', backref='tb_agendamento_consultas')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbAgendamentoConsulta.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_agendamento_consultas')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbAgendamentoConsulta.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_agendamento_consultas')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbAgendamentoConsulta.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_agendamento_consultas')



class TbAgendamentoConsultaApac(db.Model):
    __tablename__ = 'tb_agendamento_consulta_apac'

    co_seq_agendamento_apac = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento_consulta = db.Column(db.ForeignKey('tb_agendamento_consulta.co_seq_agendamento_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_periodo_ano = db.Column(db.Numeric(2, 0), nullable=False)
    ano_agendamento_apac = db.Column(db.Numeric(4, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_agendamento_consulta = db.relationship('TbAgendamentoConsulta', primaryjoin='TbAgendamentoConsultaApac.co_seq_agendamento_consulta == TbAgendamentoConsulta.co_seq_agendamento_consulta', backref='tb_agendamento_consulta_apacs')



class TbAgendamentoImportadoSite(db.Model):
    __tablename__ = 'tb_agendamento_importado_site'

    co_seq_agen_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento = db.Column(db.ForeignKey('tb_agendamento.co_seq_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_agendamento_consulta = db.Column(db.ForeignKey('tb_agendamento_consulta.co_seq_agendamento_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_agendamento = db.relationship('TbAgendamento', primaryjoin='TbAgendamentoImportadoSite.co_seq_agendamento == TbAgendamento.co_seq_agendamento', backref='tb_agendamento_importado_sites')
    tb_agendamento_consulta = db.relationship('TbAgendamentoConsulta', primaryjoin='TbAgendamentoImportadoSite.co_seq_agendamento_consulta == TbAgendamentoConsulta.co_seq_agendamento_consulta', backref='tb_agendamento_importado_sites')



class TbAgendamentoMedicamento(db.Model):
    __tablename__ = 'tb_agendamento_medicamento'

    co_seq_agen_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_medicamento = db.Column(db.ForeignKey('tb_medicamento.co_seq_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_local_coleta = db.Column(db.ForeignKey('tb_local_coleta.co_seq_local_coleta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_convenio = db.Column(db.ForeignKey('tb_convenio.co_seq_convenio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_dia_agendamento = db.Column(db.Numeric(4, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_convenio = db.relationship('TbConvenio', primaryjoin='TbAgendamentoMedicamento.co_seq_convenio == TbConvenio.co_seq_convenio', backref='tb_agendamento_medicamentoes')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbAgendamentoMedicamento.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_agendamento_medicamentoes')
    tb_local_coleta = db.relationship('TbLocalColeta', primaryjoin='TbAgendamentoMedicamento.co_seq_local_coleta == TbLocalColeta.co_seq_local_coleta', backref='tb_agendamento_medicamentoes')
    tb_medicamento = db.relationship('TbMedicamento', primaryjoin='TbAgendamentoMedicamento.co_seq_medicamento == TbMedicamento.co_seq_medicamento', backref='tb_agendamento_medicamentoes')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbAgendamentoMedicamento.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_agendamento_medicamentoes')



class TbAgendamentoSite(db.Model):
    __tablename__ = 'tb_agendamento_site'

    co_seq_agendamento_geral_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0), nullable=False)
    co_seq_municipio_site = db.Column(db.Numeric(8, 0), nullable=False)
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False)
    co_seq_prof_saude_site = db.Column(db.Numeric(8, 0))
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    no_pessoa = db.Column(db.String(80), nullable=False)
    dt_agendamento = db.Column(db.Numeric(8, 0), nullable=False)
    hr_agendamento = db.Column(db.String(6))
    ide_agendamento_consulta = db.Column(db.String(1), nullable=False)
    co_seq_tp_agendamento_site = db.Column(db.Numeric(2, 0))
    ds_tp_agendamento = db.Column(db.String(80))
    no_municipio = db.Column(db.String(70))
    no_unidade_saude = db.Column(db.String(100))
    no_prof_saude = db.Column(db.String(80))
    dt_hr_cancelamento_site = db.Column(db.Numeric(14, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_doenca_site = db.Column(db.Numeric(4, 0))
    no_doenca = db.Column(db.String(50))
    co_seq_prof_saude_con_site = db.Column(db.Numeric(8, 0))
    co_seq_agendamento_site = db.Column(db.Numeric(7, 0))
    co_seq_agendamento_con_site = db.Column(db.Numeric(8, 0))
    dt_hr_nao_comparecimento = db.Column(db.Numeric(14, 0))
    aut_nao_comparecimento = db.Column(db.String(20))
    ds_endereco = db.Column(db.String(400))
    ds_email = db.Column(db.String(200))
    nu_celular = db.Column(db.String(20))
    nu_telefone = db.Column(db.String(35))
    no_municipio_tratamento = db.Column(db.String(70))
    ds_endereco_unidade = db.Column(db.String(400))



class TbAlelo(db.Model):
    __tablename__ = 'tb_alelo'

    co_seq_alelo = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    no_alelo = db.Column(db.String(40), nullable=False)
    ds_regiao_analse_dna = db.Column(db.String(30))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbAlertaAnaliseExame(db.Model):
    __tablename__ = 'tb_alerta_analise_exame'

    co_seq_alerta_analise_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_operador = db.Column(db.ForeignKey('tb_operador.co_seq_operador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_res_1 = db.Column(db.String(60))
    ds_res_2 = db.Column(db.String(60))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_res_3 = db.Column(db.String(60))
    ds_res_4 = db.Column(db.String(60))
    ds_oper_logico_res_1_res_2 = db.Column(db.String(1))

    tb_operador = db.relationship('TbOperador', primaryjoin='TbAlertaAnaliseExame.co_seq_operador == TbOperador.co_seq_operador', backref='tb_alerta_analise_exames')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAlertaAnaliseExame.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_alerta_analise_exames')



class TbAlertaUnidadeSaude(db.Model):
    __tablename__ = 'tb_alerta_unidade_saude'

    co_seq_alerta_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_alerta_unidade = db.Column(db.ForeignKey('tb_tipo_alerta_unidade.co_seq_tp_alerta_unidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    ds_alerta = db.Column(db.String(2000), nullable=False)
    co_origem_comunicacao = db.Column(db.Numeric(14, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_envio_site = db.Column(db.Numeric(14, 0))
    aut_envio_site = db.Column(db.String(20))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbAlertaUnidadeSaude.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_alerta_unidade_saudes')
    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbAlertaUnidadeSaude.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_alerta_unidade_saudes')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbAlertaUnidadeSaude.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_alerta_unidade_saudes')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbAlertaUnidadeSaude.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_alerta_unidade_saudes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbAlertaUnidadeSaude.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_alerta_unidade_saudes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbAlertaUnidadeSaude.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_alerta_unidade_saudes')
    tb_tipo_alerta_unidade = db.relationship('TbTipoAlertaUnidade', primaryjoin='TbAlertaUnidadeSaude.co_seq_tp_alerta_unidade == TbTipoAlertaUnidade.co_seq_tp_alerta_unidade', backref='tb_alerta_unidade_saudes')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAlertaUnidadeSaude.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_alerta_unidade_saudes')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbAlertaUnidadeSaude.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_alerta_unidade_saudes')



class TbAlertaUnidadeSaudeSite(db.Model):
    __tablename__ = 'tb_alerta_unidade_saude_site'

    co_seq_alerta_unidade_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao_site = db.Column(db.Numeric(8, 0))
    co_seq_doenca_site = db.Column(db.Numeric(4, 0))
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0))
    co_seq_mot_comunicacao_site = db.Column(db.Numeric(4, 0))
    co_seq_providencia_site = db.Column(db.Numeric(4, 0))
    co_seq_recep_amostra_site = db.Column(db.Numeric(14, 0))
    co_seq_tp_exame_site = db.Column(db.Numeric(5, 0))
    co_seq_tp_triagem_site = db.Column(db.Numeric(2, 0))
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0))
    ds_mot_comunicacao = db.Column(db.String(40))
    ds_providencia = db.Column(db.String(80))
    co_seq_amostra_site = db.Column(db.Numeric(14, 0))
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    ide_co_conflito = db.Column(db.String(1), nullable=False)
    nu_amostra = db.Column(db.Numeric(5, 0))
    no_pessoa = db.Column(db.String(80), nullable=False)
    nu_telefone = db.Column(db.String(35))
    nu_celular = db.Column(db.String(20))
    ds_alerta = db.Column(db.String(2000))
    ds_tp_exame = db.Column(db.String(100))
    no_doenca = db.Column(db.String(50))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_visualizacao = db.Column(db.Numeric(14, 0))
    aut_visualizacao = db.Column(db.String(20))
    ds_tp_alerta_unidade = db.Column(db.String(80))



class TbAmostra(db.Model):
    __tablename__ = 'tb_amostra'
    __table_args__ = (
        db.Index('in_amostra_coseqamo_dthrcanc', 'co_seq_amostra', 'dt_hr_cancelamento'),
        db.Index('in_amostra_coseqpes_coseqtpamo_dtrec_dthrcanc', 'co_seq_pessoa', 'co_seq_tp_amostra', 'dt_rec_amostra', 'dt_hr_cancelamento'),
        db.Index('in_amostra_nuamostra_dtrecamo_dthrcanc', 'nu_amostra', 'dt_rec_amostra', 'dt_hr_cancelamento'),
        db.Index('in_amostra_dthrreg_dthrcanc', 'dt_hr_registro', 'dt_hr_cancelamento')
    )

    co_seq_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_material_coletado = db.Column(db.ForeignKey('tb_tipo_material_coletado.co_seq_tp_material_coletado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False, index=True)
    ide_controle_medico = db.Column(db.String(1), nullable=False)
    ide_portador = db.Column(db.String(1), nullable=False)
    dt_col_amostra = db.Column(db.Numeric(8, 0), index=True)
    hr_col_amostra = db.Column(db.String(4))
    dt_post_amostra = db.Column(db.Numeric(8, 0), index=True)
    dt_rec_amostra = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_transfusao_amostra = db.Column(db.String(1))

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbAmostra.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_amostras')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbAmostra.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_amostras')
    tb_tipo_material_coletado = db.relationship('TbTipoMaterialColetado', primaryjoin='TbAmostra.co_seq_tp_material_coletado == TbTipoMaterialColetado.co_seq_tp_material_coletado', backref='tb_amostras')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbAmostra.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_amostras')


class TbAmostraConferencia(TbAmostra):
    __tablename__ = 'tb_amostra_conferencia'

    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbAmostraConferencia.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_amostra_conferencias')



class TbAmostraControleEsquema(db.Model):
    __tablename__ = 'tb_amostra_controle_esquema'

    co_seq_amo_contole_esquema = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amo_controle_externo = db.Column(db.ForeignKey('tb_amostra_controle_externo.co_seq_amo_controle_externo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_esquema_placa = db.Column(db.ForeignKey('tb_esquema_placa.co_seq_esquema_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra_controle_externo = db.relationship('TbAmostraControleExterno', primaryjoin='TbAmostraControleEsquema.co_seq_amo_controle_externo == TbAmostraControleExterno.co_seq_amo_controle_externo', backref='tb_amostra_controle_esquemas')
    tb_esquema_placa = db.relationship('TbEsquemaPlaca', primaryjoin='TbAmostraControleEsquema.co_seq_esquema_placa == TbEsquemaPlaca.co_seq_esquema_placa', backref='tb_amostra_controle_esquemas')



class TbAmostraControleExame(db.Model):
    __tablename__ = 'tb_amostra_controle_exame'

    co_amo_controle_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amo_controle_externo = db.Column(db.ForeignKey('tb_amostra_controle_externo.co_seq_amo_controle_externo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra_controle_externo = db.relationship('TbAmostraControleExterno', primaryjoin='TbAmostraControleExame.co_seq_amo_controle_externo == TbAmostraControleExterno.co_seq_amo_controle_externo', backref='tb_amostra_controle_exames')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAmostraControleExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_amostra_controle_exames')



class TbAmostraControleExterno(db.Model):
    __tablename__ = 'tb_amostra_controle_externo'

    co_seq_amo_controle_externo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_controle_externo = db.Column(db.ForeignKey('tb_controle_qualidade_externo.co_seq_controle_externo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_pos_placa = db.Column(db.ForeignKey('tb_tipo_posicao_placa.co_seq_tp_pos_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_amostra_controle_externo = db.Column(db.String(30))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_controle_qualidade_externo = db.relationship('TbControleQualidadeExterno', primaryjoin='TbAmostraControleExterno.co_seq_controle_externo == TbControleQualidadeExterno.co_seq_controle_externo', backref='tb_amostra_controle_externoes')
    tb_tipo_posicao_placa = db.relationship('TbTipoPosicaoPlaca', primaryjoin='TbAmostraControleExterno.co_seq_tp_pos_placa == TbTipoPosicaoPlaca.co_seq_tp_pos_placa', backref='tb_amostra_controle_externoes')



class TbAmostraControleQualidade(db.Model):
    __tablename__ = 'tb_amostra_controle_qualidade'

    co_amostra_controle_qualidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_controle_qualidade = db.Column(db.ForeignKey('tb_tipo_controle_qualidade.co_seq_tp_controle_qualidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbAmostraControleQualidade.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_amostra_controle_qualidades')
    tb_tipo_controle_qualidade = db.relationship('TbTipoControleQualidade', primaryjoin='TbAmostraControleQualidade.co_seq_tp_controle_qualidade == TbTipoControleQualidade.co_seq_tp_controle_qualidade', backref='tb_amostra_controle_qualidades')



class TbAmostraControleResultado(db.Model):
    __tablename__ = 'tb_amostra_controle_resultado'

    co_seq_controle_resultado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_col_placa = db.Column(db.ForeignKey('tb_tipo_coluna_placa.co_seq_tp_col_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_seq_placa = db.Column(db.ForeignKey('tb_placa.nu_seq_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_medida = db.Column(db.ForeignKey('tb_unidade_medida.co_seq_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_reg_controle_placa = db.Column(db.ForeignKey('tb_controle_placa.co_seq_reg_controle_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amo_controle_externo = db.Column(db.ForeignKey('tb_amostra_controle_externo.co_seq_amo_controle_externo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_informado_analise = db.Column(db.String(100))
    vr_utilizado_int = db.Column(db.String(100))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0))
    ide_amostra_repeticao = db.Column(db.String(1))
    nu_repeticao_amostra_placa = db.Column(db.Numeric(2, 0))
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    nu_placa_analise_liberacao = db.Column(db.String(50))
    tex_referencia = db.Column(db.String(30))

    tb_amostra_controle_externo = db.relationship('TbAmostraControleExterno', primaryjoin='TbAmostraControleResultado.co_seq_amo_controle_externo == TbAmostraControleExterno.co_seq_amo_controle_externo', backref='tb_amostra_controle_resultadoes')
    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbAmostraControleResultado.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_amostra_controle_resultadoes')
    tb_controle_placa = db.relationship('TbControlePlaca', primaryjoin='TbAmostraControleResultado.co_seq_reg_controle_placa == TbControlePlaca.co_seq_reg_controle_placa', backref='tb_amostra_controle_resultadoes')
    tb_tipo_coluna_placa = db.relationship('TbTipoColunaPlaca', primaryjoin='TbAmostraControleResultado.co_seq_tp_col_placa == TbTipoColunaPlaca.co_seq_tp_col_placa', backref='tb_amostra_controle_resultadoes')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraControleResultado.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_controle_resultadoes')
    tb_unidade_medida = db.relationship('TbUnidadeMedida', primaryjoin='TbAmostraControleResultado.co_seq_unidade_medida == TbUnidadeMedida.co_seq_unidade_medida', backref='tb_amostra_controle_resultadoes')
    tb_placa = db.relationship('TbPlaca', primaryjoin='TbAmostraControleResultado.nu_seq_placa == TbPlaca.nu_seq_placa', backref='tb_amostra_controle_resultadoes')



class TbAmostraConvenio(db.Model):
    __tablename__ = 'tb_amostra_convenio'

    co_seq_amostra_convenio = db.Column(db.Numeric(14, 0), primary_key=True, server_default=db.FetchedValue())
    co_seq_convenio = db.Column(db.Numeric(2, 0), nullable=False, index=True)
    co_seq_amostra = db.Column(db.Numeric(14, 0), index=True)
    co_seq_recep_amostra = db.Column(db.Numeric(14, 0), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbAmostraFechamentoMensal(db.Model):
    __tablename__ = 'tb_amostra_fechamento_mensal'

    co_seq_amostra_fch_mensal = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seg_fch_mensal = db.Column(db.ForeignKey('tb_fechamento_mensal.co_seg_fch_mensal', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_faixa_idade_bpa = db.Column(db.ForeignKey('tb_faixa_idade_faturamento.co_seq_faixa_idade_bpa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_pessoa = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.Numeric(8, 0))
    dt_rec_amostra = db.Column(db.Numeric(8, 0), nullable=False)
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    dt_resultado = db.Column(db.Numeric(8, 0))
    no_local_coleta = db.Column(db.String(100))
    ds_endereco = db.Column(db.String(400))
    ds_bairro = db.Column(db.String(80))
    ds_municipio_domicilio = db.Column(db.String(80))
    ds_municipio_coleta = db.Column(db.String(80))
    co_ent_pessoa_fechamento = db.Column(db.String(20))
    ide_amostra_menor_30_dias = db.Column(db.String(1))
    ide_primeira_amostra_liberada = db.Column(db.String(1))
    ide_controle_medico = db.Column(db.String(1))
    ide_amostra_familiar = db.Column(db.String(1))
    ds_email = db.Column(db.String(200))
    nu_cep = db.Column(db.String(8))
    nu_telefone = db.Column(db.String(35))
    no_logradouro = db.Column(db.String(100))
    nu_logradouro = db.Column(db.String(20))
    cmp_nr_logradouro = db.Column(db.String(20))
    se_pessoa = db.Column(db.String(1))
    nu_cns = db.Column(db.String(15))
    co_ibge = db.Column(db.String(10))
    nu_dias_nascimento_coleta = db.Column(db.Numeric(5, 0))

    tb_fechamento_mensal = db.relationship('TbFechamentoMensal', primaryjoin='TbAmostraFechamentoMensal.co_seg_fch_mensal == TbFechamentoMensal.co_seg_fch_mensal', backref='tb_amostra_fechamento_mensals')
    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbAmostraFechamentoMensal.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_amostra_fechamento_mensals')
    tb_faixa_idade_faturamento = db.relationship('TbFaixaIdadeFaturamento', primaryjoin='TbAmostraFechamentoMensal.co_seq_faixa_idade_bpa == TbFaixaIdadeFaturamento.co_seq_faixa_idade_bpa', backref='tb_amostra_fechamento_mensals')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbAmostraFechamentoMensal.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_amostra_fechamento_mensals')



class TbAmostraFechamentoToxo(db.Model):
    __tablename__ = 'tb_amostra_fechamento_toxo'

    co_seq_amostra_fch_toxo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_fch_mensal_toxo = db.Column(db.ForeignKey('tb_fechamento_mensal_toxo.co_seq_fch_mensal_toxo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_ent_pessoa_fch_toxo = db.Column(db.String(20), nullable=False)
    no_pessoa = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.Numeric(8, 0))
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    dt_rec_amostra = db.Column(db.Numeric(8, 0), nullable=False)
    dt_resultado = db.Column(db.Numeric(8, 0), nullable=False)
    no_local_coleta = db.Column(db.String(100), nullable=False)
    ds_municipio_coleta = db.Column(db.String(80), nullable=False)
    ds_municipio_domicilio = db.Column(db.String(80))
    ds_endereco = db.Column(db.String(400))
    ds_bairro = db.Column(db.String(80))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbAmostraFechamentoToxo.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_amostra_fechamento_toxoes')
    tb_fechamento_mensal_toxo = db.relationship('TbFechamentoMensalToxo', primaryjoin='TbAmostraFechamentoToxo.co_seq_fch_mensal_toxo == TbFechamentoMensalToxo.co_seq_fch_mensal_toxo', backref='tb_amostra_fechamento_toxoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbAmostraFechamentoToxo.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_amostra_fechamento_toxoes')



class TbAmostraGeracaoEsquema(db.Model):
    __tablename__ = 'tb_amostra_geracao_esquema'

    co_seq_geracao_esquema = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ent_pessoa = db.Column(db.ForeignKey('tb_codigo_entrada_pessoa.co_ent_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_tp_exame = db.Column(db.ForeignKey('tb_amostra_tipo_exame.co_seq_amostra_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_metodo = db.Column(db.ForeignKey('tb_tipo_metodo.co_seq_tp_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_geracao_placa = db.Column(db.ForeignKey('tb_geracao_placa.co_seq_geracao_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_equip_exame = db.Column(db.String(40))
    ds_tp_exame = db.Column(db.String(100))
    sg_tp_exame = db.Column(db.String(2))
    ide_amostra_repeticao = db.Column(db.String(1))
    nu_amostra_repeticao = db.Column(db.Numeric(2, 0))
    aut_execucao = db.Column(db.String(20))
    dt_hr_execucao = db.Column(db.Numeric(14, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0))
    aut_registro = db.Column(db.String(20))
    dt_rec_recep_amostra = db.Column(db.Numeric(8, 0))
    ide_amostra_inadequada = db.Column(db.String(1))
    ide_prioridade_geracao = db.Column(db.String(1))
    nu_amostra = db.Column(db.Numeric(5, 0))
    ide_controle_medico = db.Column(db.String(1))
    nu_ordem_execucao_placa = db.Column(db.Numeric(1, 0))

    tb_codigo_entrada_pessoa = db.relationship('TbCodigoEntradaPessoa', primaryjoin='TbAmostraGeracaoEsquema.co_ent_pessoa == TbCodigoEntradaPessoa.co_ent_pessoa', backref='tb_amostra_geracao_esquemas')
    tb_amostra_tipo_exame = db.relationship('TbAmostraTipoExame', primaryjoin='TbAmostraGeracaoEsquema.co_seq_amostra_tp_exame == TbAmostraTipoExame.co_seq_amostra_tp_exame', backref='tb_amostra_geracao_esquemas')
    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbAmostraGeracaoEsquema.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_amostra_geracao_esquemas')
    tb_geracao_placa = db.relationship('TbGeracaoPlaca', primaryjoin='TbAmostraGeracaoEsquema.co_seq_geracao_placa == TbGeracaoPlaca.co_seq_geracao_placa', backref='tb_amostra_geracao_esquemas')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAmostraGeracaoEsquema.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_amostra_geracao_esquemas')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAmostraGeracaoEsquema.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_amostra_geracao_esquemas')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraGeracaoEsquema.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_geracao_esquemas')
    tb_tipo_metodo = db.relationship('TbTipoMetodo', primaryjoin='TbAmostraGeracaoEsquema.co_seq_tp_metodo == TbTipoMetodo.co_seq_tp_metodo', backref='tb_amostra_geracao_esquemas')



class TbAmostraInadequacaoSoro(db.Model):
    __tablename__ = 'tb_amostra_inadequacao_soro'

    co_seq_inadequacao_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_soro = db.Column(db.ForeignKey('tb_recepcao_amostra_soro.co_seq_recep_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_mot_inadequacao = db.Column(db.ForeignKey('tb_motivo_inadequacao.co_mot_inadequacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_inadequacao = db.relationship('TbMotivoInadequacao', primaryjoin='TbAmostraInadequacaoSoro.co_mot_inadequacao == TbMotivoInadequacao.co_mot_inadequacao', backref='tb_amostra_inadequacao_soroes')
    tb_recepcao_amostra_soro = db.relationship('TbRecepcaoAmostraSoro', primaryjoin='TbAmostraInadequacaoSoro.co_seq_recep_soro == TbRecepcaoAmostraSoro.co_seq_recep_soro', backref='tb_amostra_inadequacao_soroes')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAmostraInadequacaoSoro.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_amostra_inadequacao_soroes')



t_tb_amostra_maternidade = db.Table(
    'tb_amostra_maternidade',
    db.Column('co_seq_tp_dieta_maternidade', db.ForeignKey('tb_tipo_dieta_maternidade.co_seq_tp_dieta_maternidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_seq_tp_coleta_maternidade', db.ForeignKey('tb_tipo_coleta_maternidade.co_seq_tp_coleta_maternidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_seq_amostra', db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_tp_estado_clinico', db.ForeignKey('tb_tipo_estado_clinico_coleta.co_tp_estado_clinico', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_tp_tempo_inicio_dieta', db.ForeignKey('tb_tipo_tempo_inicio_dieta.co_tp_tempo_inicio_dieta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_seq_tp_local_intenacao', db.ForeignKey('tb_tipo_local_internacao.co_seq_tp_local_intenacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('no_funcionario_coleta', db.String(50)),
    db.Column('obs_amostra', db.String(2000), nullable=False),
    db.Column('dt_hr_ultima_alteracao', db.Numeric(14, 0), nullable=False),
    db.Column('aut_ultima_alteracao', db.String(20), nullable=False),
    db.Column('dt_hr_registro', db.Numeric(14, 0), nullable=False),
    db.Column('aut_registro', db.String(20), nullable=False)
)



class TbAmostraMotivoInadequacao(db.Model):
    __tablename__ = 'tb_amostra_motivo_inadequacao'
    __table_args__ = (
        db.Index('in_amomotinad_coseqrecepamo_coseqtpexa_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame', 'dt_hr_cancelamento'),
        db.Index('in_amomotinad_coseqrecepamo_coseqtpexa', 'co_seq_recep_amostra', 'co_seq_tp_exame')
    )

    co_seq_mot_inadequacao = db.Column(db.Numeric(12, 0), primary_key=True, unique=True)
    co_mot_inadequacao = db.Column(db.ForeignKey('tb_motivo_inadequacao.co_mot_inadequacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_inadequacao = db.relationship('TbMotivoInadequacao', primaryjoin='TbAmostraMotivoInadequacao.co_mot_inadequacao == TbMotivoInadequacao.co_mot_inadequacao', backref='tb_amostra_motivo_inadequacaos')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAmostraMotivoInadequacao.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_amostra_motivo_inadequacaos')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAmostraMotivoInadequacao.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_amostra_motivo_inadequacaos')



class TbAmostraPlaca(db.Model):
    __tablename__ = 'tb_amostra_placa'
    __table_args__ = (
        db.Index('in_amoplac_cotpexa_cotpexamet_coseqrecepamo_nuseqplac_dthrlib', 'co_seq_tp_exame', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_seq_placa', 'dt_hr_liberacao'),
        db.Index('in_amoplaca_nuseqpla_dthrlib_dthrcanc', 'nu_seq_placa', 'dt_hr_liberacao', 'dt_hr_cancelamento'),
        db.Index('in_amoplaca_coseqrecepamo_cotpexa_cotpexamet_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame', 'co_seq_tp_exame_metodo', 'dt_hr_cancelamento'),
        db.Index('in_amoplaca_coseqrecepamo_cotpexa_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame', 'dt_hr_cancelamento'),
        db.Index('in_amoplaca_cotpexa_dthrcanc', 'co_seq_tp_exame', 'dt_hr_cancelamento'),
        db.Index('in_amoplac_coseqamopla_cotpexa_cotpexamet_coseqrecepamo', 'co_seq_amostra_placa', 'co_seq_tp_exame', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_seq_placa'),
        db.Index('in_amoplac_cotpexa_cotpexamet_coseqrecepamo_nuseqplac_dthrlib_d', 'co_seq_tp_exame', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_seq_placa', 'dt_hr_liberacao', 'dt_hr_cancelamento'),
        db.Index('in_amoplaca_dthrlib_dthrcanc', 'dt_hr_liberacao', 'dt_hr_cancelamento'),
        db.Index('in_amoplac_cotpexa_coseqrecepamo_nuseqplac_vrutil', 'co_seq_tp_exame', 'co_seq_recep_amostra', 'nu_seq_placa', 'vr_utilizado_int'),
        db.Index('in_amoplaca_nuseqplac_nuproccontint', 'nu_seq_placa', 'nu_proc_controle_int'),
        db.Index('in_amoplac_cotpexa_cotpexamet_coseqrecepamo_nuseqplac_vrutil', 'co_seq_tp_exame', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_seq_placa', 'vr_utilizado_int'),
        db.Index('in_amoplac_nuseq_dthrlib_dthrcanc', 'nu_seq_placa', 'dt_hr_liberacao', 'dt_hr_cancelamento'),
        db.Index('in_amoplac_coseqtoexa_coseqrecepamo_nuseqplac_vrutil_dthrcanc', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_seq_placa', 'vr_utilizado_int', 'dt_hr_cancelamento'),
        db.Index('in_amoplaca_coseqrecepamo_coseqrecepamo', 'co_seq_recep_amostra', 'co_seq_amostra_placa'),
        db.Index('in_amoplac_cotpexa_cotpexamet_coseqrecepamo_nuseqplac', 'co_seq_tp_exame', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_seq_placa'),
        db.Index('in_amoplaca_coseqrecepamo_coseqrecepamo_coseqint', 'co_seq_recep_amostra', 'co_seq_amostra_placa', 'co_seq_interpretacao'),
        db.Index('in_amoplaca_coseqrecepamo_coseqtpex_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo', 'dt_hr_cancelamento')
    )

    co_seq_amostra_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_arq_res_placa = db.Column(db.ForeignKey('tb_arquivo_resultado_placa.co_seq_arq_res_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_seq_placa = db.Column(db.ForeignKey('tb_placa.nu_seq_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), index=True)
    ide_amostra_inadequada = db.Column(db.String(1))
    ide_amostra_repeticao = db.Column(db.String(1))
    vr_utilizado_int = db.Column(db.String(100), index=True)
    vr_informado_analise = db.Column(db.String(100))
    dt_hr_liberacao = db.Column(db.Numeric(14, 0), index=True)
    aut_liberacao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_arquivo_resultado_placa = db.relationship('TbArquivoResultadoPlaca', primaryjoin='TbAmostraPlaca.co_seq_arq_res_placa == TbArquivoResultadoPlaca.co_seq_arq_res_placa', backref='tb_amostra_placas')
    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbAmostraPlaca.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_amostra_placas')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbAmostraPlaca.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_amostra_placas')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAmostraPlaca.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_amostra_placas')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAmostraPlaca.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_amostra_placas')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraPlaca.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_placas')
    tb_placa = db.relationship('TbPlaca', primaryjoin='TbAmostraPlaca.nu_seq_placa == TbPlaca.nu_seq_placa', backref='tb_amostra_placas')



class TbAmostraPlacaDadosLiberacao(db.Model):
    __tablename__ = 'tb_amostra_placa_dados_liberacao'
    __table_args__ = (
        db.Index('in_amoplacadadlib_coamopla_cotpexamed_corecepamo_nupla_dthrcanc', 'co_seq_amostra_placa', 'co_seq_tp_exame_metodo', 'co_seq_recep_amostra', 'nu_placa_analise_liberacao', 'dt_hr_cancelamento'),
        db.Index('in_amoplacadadlib_nupla_dthrcanc', 'nu_placa_analise_liberacao', 'dt_hr_cancelamento')
    )

    co_seq_placa_dados_liberacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_placa_analise_liberacao = db.Column(db.String(50), index=True)
    pes_nascimento_grama = db.Column(db.Numeric(14, 0))
    ide_dia_res = db.Column(db.Numeric(8, 0))
    ide_primeiro_res = db.Column(db.String(1))
    ide_controle_medico = db.Column(db.String(1))
    ide_somente_encaminhamento = db.Column(db.String(1))
    ide_somente_maternidade = db.Column(db.String(1))
    ide_observacao_clinica = db.Column(db.String(1))
    nu_amostra_alterada = db.Column(db.Numeric(2, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    dt_nascimento = db.Column(db.Numeric(8, 0))
    ide_comportamento_resultado = db.Column(db.String(1))
    ide_uso_corticoide = db.Column(db.String(1))
    co_tp_estado_clinico = db.Column(db.Numeric(2, 0))

    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbAmostraPlacaDadosLiberacao.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_amostra_placa_dados_liberacaos')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAmostraPlacaDadosLiberacao.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_amostra_placa_dados_liberacaos')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraPlacaDadosLiberacao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_placa_dados_liberacaos')



class TbAmostraPlacaInterpretacao(db.Model):
    __tablename__ = 'tb_amostra_placa_interpretacao'

    co_seq_amostra_interpretacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0))
    vr_utilizado_int = db.Column(db.String(100))
    ide_res_liberado_tecnico = db.Column(db.String(1), index=True)

    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbAmostraPlacaInterpretacao.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_amostra_placa_interpretacaos')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbAmostraPlacaInterpretacao.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_amostra_placa_interpretacaos')



class TbAmostraPlacaRepeticao(db.Model):
    __tablename__ = 'tb_amostra_placa_repeticao'

    co_seq_amostra_placa_repeticao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_tp_exame = db.Column(db.ForeignKey('tb_amostra_tipo_exame.co_seq_amostra_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_placa_atual = db.Column(db.String(20), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbAmostraPlacaRepeticao.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_amostra_placa_repeticaos')
    tb_amostra_tipo_exame = db.relationship('TbAmostraTipoExame', primaryjoin='TbAmostraPlacaRepeticao.co_seq_amostra_tp_exame == TbAmostraTipoExame.co_seq_amostra_tp_exame', backref='tb_amostra_placa_repeticaos')



class TbAmostraPlacaTipoExame(db.Model):
    __tablename__ = 'tb_amostra_placa_tipo_exame'

    co_seq_amostra_placa_tp_exame = db.Column(db.Numeric(14, 0), primary_key=True, server_default=db.FetchedValue())
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo'), nullable=False, index=True)
    co_seq_tp_metodo = db.Column(db.ForeignKey('tb_tipo_metodo.co_seq_tp_metodo'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame'), nullable=False, index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao'), index=True)
    int_co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao'), index=True)
    vr_utilizado_int = db.Column(db.String(100))
    vr_informado_analise = db.Column(db.String(100))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbAmostraPlacaTipoExame.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_amostra_placa_tipo_exames')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbAmostraPlacaTipoExame.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tbinterpretacaoexame_tb_amostra_placa_tipo_exames')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbAmostraPlacaTipoExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_amostra_placa_tipo_exames')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraPlacaTipoExame.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_placa_tipo_exames')
    tb_tipo_metodo = db.relationship('TbTipoMetodo', primaryjoin='TbAmostraPlacaTipoExame.co_seq_tp_metodo == TbTipoMetodo.co_seq_tp_metodo', backref='tb_amostra_placa_tipo_exames')
    tb_interpretacao_exame1 = db.relationship('TbInterpretacaoExame', primaryjoin='TbAmostraPlacaTipoExame.int_co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tbinterpretacaoexame_tb_amostra_placa_tipo_exames_0')



t_tb_amostra_pre_natal = db.Table(
    'tb_amostra_pre_natal',
    db.Column('co_seq_amostra', db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('ida_gestacional_semanas', db.Numeric(6, 0)),
    db.Column('ida_gestacional_dias', db.Numeric(2, 0))
)



class TbAmostraSeparadaTecnico(db.Model):
    __tablename__ = 'tb_amostra_separada_tecnico'

    co_seq_amostra_separada_tec = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_amostra_enviada_outro_lab = db.Column(db.String(1))
    dt_hr_envio_outro_lab = db.Column(db.Numeric(14, 0))
    aut_envio_outro_lab = db.Column(db.String(20))

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAmostraSeparadaTecnico.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_amostra_separada_tecnicoes')



class TbAmostraSiteUnidade(db.Model):
    __tablename__ = 'tb_amostra_site_unidade'

    co_seq_amostra_site_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False)
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False)
    no_pessoa = db.Column(db.String(80), nullable=False)
    ide_analise_maternidade = db.Column(db.String(1), nullable=False)
    nu_cns = db.Column(db.String(15), nullable=False)
    pes_nascimento_grama = db.Column(db.Numeric(14, 0))
    ida_nascimento_mes = db.Column(db.Numeric(2, 0))
    se_pessoa = db.Column(db.String(1), nullable=False)
    ide_parto_gemelar = db.Column(db.String(1), nullable=False)
    nu_gemelar = db.Column(db.Numeric(2, 0), nullable=False)
    ide_transfusao_amostra = db.Column(db.String(1))
    dt_transfusao = db.Column(db.Numeric(8, 0))
    ide_transfusao_antes_col = db.Column(db.String(1))
    dt_nascimento = db.Column(db.Numeric(8, 0))
    hr_nascimento = db.Column(db.String(4))
    dt_post_amostra = db.Column(db.Numeric(8, 0))
    dt_col_amostra = db.Column(db.Numeric(8, 0), nullable=False)
    hr_col_amostra = db.Column(db.String(4))
    nu_dnv = db.Column(db.String(20))
    no_mae = db.Column(db.String(70))
    dt_nascimento_mae = db.Column(db.Numeric(8, 0))
    nu_cns_mae = db.Column(db.String(15))
    co_seq_tp_documento_site = db.Column(db.Numeric(2, 0))
    nu_doc_mae = db.Column(db.String(30))
    nu_cep = db.Column(db.String(8), nullable=False)
    co_seq_tp_logradouro_site = db.Column(db.Numeric(2, 0))
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20))
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80), nullable=False)
    co_seq_municipio_site = db.Column(db.Numeric(8, 0), nullable=False)
    co_seq_uf_site = db.Column(db.Numeric(2, 0), nullable=False)
    nu_telefone = db.Column(db.String(35))
    nu_celular = db.Column(db.String(20))
    co_seq_tp_local_intenacao_site = db.Column(db.Numeric(2, 0))
    nu_registro_hosp_nascimento = db.Column(db.String(20))
    co_seq_tp_dieta_maternidade_site = db.Column(db.Numeric(3, 0))
    co_tp_tempo_inicio_dieta_site = db.Column(db.Numeric(2, 0))
    co_tp_estado_clinico_site = db.Column(db.Numeric(2, 0))
    co_seq_tp_coleta_mat_site = db.Column(db.Numeric(2, 0))
    no_funcionario_coleta = db.Column(db.String(50))
    obs_amostra = db.Column(db.String(2000))
    dt_ultima_menstruacao = db.Column(db.Numeric(8, 0))
    nu_aborto_anterior = db.Column(db.Numeric(2, 0))
    nu_gestacao_anterior = db.Column(db.Numeric(2, 0))
    nu_parto_anterior = db.Column(db.Numeric(2, 0))
    nu_sis_pre_natal = db.Column(db.String(20))
    ida_gestacional_dias = db.Column(db.Numeric(2, 0))
    ida_gestacional_semanas = db.Column(db.Numeric(6, 0))
    nu_cpf = db.Column(db.Numeric(11, 0))
    nu_rg = db.Column(db.String(15))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    no_municipio = db.Column(db.String(70))
    no_uf = db.Column(db.String(50))
    no_unidade_saude = db.Column(db.String(100))
    ds_tp_coleta_maternidade = db.Column(db.String(50))
    ds_tp_logradouro = db.Column(db.String(40))
    ds_tp_material_coletado = db.Column(db.String(50))
    ds_tp_estado_clinico = db.Column(db.String(50))
    ds_tp_local_internacao = db.Column(db.String(50))
    ds_dieta_maternidade = db.Column(db.String(100))
    ds_tempo_inicio_dieta = db.Column(db.String(50))
    ds_tp_documento = db.Column(db.String(70))
    ds_tp_transfusao_amostra = db.Column(db.String(200))
    co_seq_tp_transfusao_site = db.Column(db.Numeric(2, 0))
    dt_hr_rec_recep_amostra = db.Column(db.Numeric(14, 0))
    aut_rec_recep_amostra = db.Column(db.String(20))
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0))
    co_seq_tp_triagem_site = db.Column(db.Numeric(2, 0))



class TbAmostraSoro(db.Model):
    __tablename__ = 'tb_amostra_soro'

    co_seq_amostra_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_protocolo_analise = db.Column(db.String(30))
    dt_envio_analise = db.Column(db.Numeric(8, 0))
    dt_hr_envio_analise = db.Column(db.Numeric(14, 0))
    aut_envio_analise = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbAmostraSoro.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_amostra_soroes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbAmostraSoro.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_amostra_soroes')



class TbAmostraSoroTipoExame(db.Model):
    __tablename__ = 'tb_amostra_soro_tipo_exame'

    co_seq_amostra_soro_tp_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_soro = db.Column(db.ForeignKey('tb_amostra_soro.co_seq_amostra_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_repeticao_soro_analise = db.Column(db.ForeignKey('tb_repeticao_soro_analise.co_seq_repeticao_soro_analise', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_lote = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    ide_amostra_repeticao = db.Column(db.String(1))
    dt_hr_execucao = db.Column(db.Numeric(14, 0))
    aut_execucao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0))
    aut_registro = db.Column(db.String(20))

    tb_amostra_soro = db.relationship('TbAmostraSoro', primaryjoin='TbAmostraSoroTipoExame.co_seq_amostra_soro == TbAmostraSoro.co_seq_amostra_soro', backref='tb_amostra_soro_tipo_exames')
    tb_repeticao_soro_analise = db.relationship('TbRepeticaoSoroAnalise', primaryjoin='TbAmostraSoroTipoExame.co_seq_repeticao_soro_analise == TbRepeticaoSoroAnalise.co_seq_repeticao_soro_analise', backref='tb_amostra_soro_tipo_exames')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraSoroTipoExame.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_soro_tipo_exames')



class TbAmostraTesteSuor(db.Model):
    __tablename__ = 'tb_amostra_teste_suor'

    co_seq_amostra_teste_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_col_teste_suor = db.Column(db.ForeignKey('tb_coleta_teste_suor.co_seq_col_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_coleta_teste_suor = db.relationship('TbColetaTesteSuor', primaryjoin='TbAmostraTesteSuor.co_seq_col_teste_suor == TbColetaTesteSuor.co_seq_col_teste_suor', backref='tb_amostra_teste_suors')



class TbAmostraTesteSuorColuna(db.Model):
    __tablename__ = 'tb_amostra_teste_suor_coluna'

    co_seq_amostra_suor_coluna = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_col_amostra_teste_suor = db.Column(db.ForeignKey('tb_coluna_amostra_teste_suor.co_seq_col_amostra_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_teste_suor = db.Column(db.ForeignKey('tb_amostra_teste_suor.co_seq_amostra_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_coluna_nu = db.Column(db.Double(53))
    vr_coluna_tex = db.Column(db.String(300))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra_teste_suor = db.relationship('TbAmostraTesteSuor', primaryjoin='TbAmostraTesteSuorColuna.co_seq_amostra_teste_suor == TbAmostraTesteSuor.co_seq_amostra_teste_suor', backref='tb_amostra_teste_suor_colunas')
    tb_coluna_amostra_teste_suor = db.relationship('TbColunaAmostraTesteSuor', primaryjoin='TbAmostraTesteSuorColuna.co_seq_col_amostra_teste_suor == TbColunaAmostraTesteSuor.co_seq_col_amostra_teste_suor', backref='tb_amostra_teste_suor_colunas')



class TbAmostraTipoExame(db.Model):
    __tablename__ = 'tb_amostra_tipo_exame'
    __table_args__ = (
        db.Index('in_amotpexame_coseqrecp_tpexa_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo', 'dt_hr_cancelamento'),
        db.Index('in_amotpexame_coseqrecp_dthrcanc', 'co_seq_recep_amostra', 'dt_hr_cancelamento'),
        db.Index('in_amotpexame_dthrexe_dthrcanc_coseqequip_coseqtpexa_dthrreg', 'dt_hr_execucao', 'dt_hr_cancelamento', 'co_seq_equip_exame', 'co_seq_tp_exame_metodo', 'dt_hr_registro'),
        db.Index('in_amotpexame_coseqrecp_tpexa_dthrcanc_dthrreg', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo', 'dt_hr_cancelamento', 'dt_hr_registro'),
        db.Index('in_amotpexame_coseqrecp_dthrcanc_dthrexc', 'co_seq_recep_amostra', 'dt_hr_cancelamento', 'dt_hr_execucao'),
        db.Index('in_amotpexame_coseqrecp_tpexa', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo'),
        db.Index('in_amotpexame_coseqrecp_tpexa_dthrreg', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo', 'dt_hr_registro')
    )

    co_seq_amostra_tp_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_amostra_repeticao = db.Column(db.String(1), nullable=False, index=True)
    dt_hr_execucao = db.Column(db.Numeric(14, 0), index=True)
    aut_execucao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_amostra_repeticao = db.Column(db.Numeric(2, 0))
    ide_prioridade_geracao = db.Column(db.String(1))

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbAmostraTipoExame.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_amostra_tipo_exames')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAmostraTipoExame.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_amostra_tipo_exames')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAmostraTipoExame.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_amostra_tipo_exames')



class TbAnaliseAlelo(db.Model):
    __tablename__ = 'tb_analise_alelo'

    co_seq_analise_alelo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_alelo = db.Column(db.ForeignKey('tb_alelo.co_seq_alelo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_soliciatacao_bm = db.Column(db.ForeignKey('tb_solicitacao_biologia_molecular.co_seq_soliciatacao_bm', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_biologia_molecular = db.Column(db.ForeignKey('tb_biologia_molecular.co_seq_biologia_molecular', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_mutacao_alelo_1 = db.Column(db.String(1))
    ide_mutacao_alelo_2 = db.Column(db.String(1))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    no_alelo = db.Column(db.String(40))
    ide_sequenciamento = db.Column(db.String(1), nullable=False)
    ide_resultado_manual = db.Column(db.String(1), nullable=False)

    tb_alelo = db.relationship('TbAlelo', primaryjoin='TbAnaliseAlelo.co_seq_alelo == TbAlelo.co_seq_alelo', backref='tb_analise_aleloes')
    tb_biologia_molecular = db.relationship('TbBiologiaMolecular', primaryjoin='TbAnaliseAlelo.co_seq_biologia_molecular == TbBiologiaMolecular.co_seq_biologia_molecular', backref='tb_analise_aleloes')
    tb_solicitacao_biologia_molecular = db.relationship('TbSolicitacaoBiologiaMolecular', primaryjoin='TbAnaliseAlelo.co_seq_soliciatacao_bm == TbSolicitacaoBiologiaMolecular.co_seq_soliciatacao_bm', backref='tb_analise_aleloes')



class TbAnaliseAmostraSoro(db.Model):
    __tablename__ = 'tb_analise_amostra_soro'

    co_seq_analise_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_arq_res_soro = db.Column(db.ForeignKey('tb_arquivo_resultado_soro.co_arq_res_soro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra_soro_tp_exame = db.Column(db.ForeignKey('tb_amostra_soro_tipo_exame.co_seq_amostra_soro_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_repeticao_soro_analise = db.Column(db.ForeignKey('tb_repeticao_soro_analise.co_seq_repeticao_soro_analise', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    res_analise_soro = db.Column(db.String(100))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    res_equip_soro = db.Column(db.String(100))
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))

    tb_arquivo_resultado_soro = db.relationship('TbArquivoResultadoSoro', primaryjoin='TbAnaliseAmostraSoro.co_arq_res_soro == TbArquivoResultadoSoro.co_arq_res_soro', backref='tb_analise_amostra_soroes')
    tb_amostra_soro_tipo_exame = db.relationship('TbAmostraSoroTipoExame', primaryjoin='TbAnaliseAmostraSoro.co_seq_amostra_soro_tp_exame == TbAmostraSoroTipoExame.co_seq_amostra_soro_tp_exame', backref='tb_analise_amostra_soroes')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbAnaliseAmostraSoro.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_analise_amostra_soroes')
    tb_repeticao_soro_analise = db.relationship('TbRepeticaoSoroAnalise', primaryjoin='TbAnaliseAmostraSoro.co_seq_repeticao_soro_analise == TbRepeticaoSoroAnalise.co_seq_repeticao_soro_analise', backref='tb_analise_amostra_soroes')



class TbAnaliseCriticaQualidade(db.Model):
    __tablename__ = 'tb_analise_critica_qualidade'

    co_seq_analise_qualidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    obs_contole_qualidade = db.Column(db.String(2000), nullable=False)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbAnaliseLiberacao(db.Model):
    __tablename__ = 'tb_analise_liberacao'
    __table_args__ = (
        db.Index('in_analib_coseqamopla_dthrcanc_nuana', 'co_seq_amostra_placa', 'dt_hr_cancelamento', 'nu_analise'),
        db.Index('in_analib_cocontec_coamopla_dthrcanc_nu_placa', 'co_seq_conduta_tecnico', 'co_seq_amostra_placa', 'dt_hr_cancelamento', 'nu_analise'),
        db.Index('in_analib_cocontec_coamopla_dthrcanc', 'co_seq_conduta_tecnico', 'co_seq_amostra_placa', 'dt_hr_cancelamento')
    )

    co_seq_analise_liberacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_conduta_tecnico = db.Column(db.ForeignKey('tb_conduta_tecnico_resultado.co_seq_conduta_tecnico', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_analise = db.Column(db.Numeric(4, 0), nullable=False, index=True)
    vr_informado_analise = db.Column(db.String(100), nullable=False)
    vr_utilizado_int = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_repeticao_amostra_placa = db.Column(db.Numeric(2, 0))
    nu_placa_analise_liberacao = db.Column(db.String(50), index=True)

    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbAnaliseLiberacao.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_analise_liberacaos')
    tb_conduta_tecnico_resultado = db.relationship('TbCondutaTecnicoResultado', primaryjoin='TbAnaliseLiberacao.co_seq_conduta_tecnico == TbCondutaTecnicoResultado.co_seq_conduta_tecnico', backref='tb_analise_liberacaos')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAnaliseLiberacao.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_analise_liberacaos')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAnaliseLiberacao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_analise_liberacaos')



class TbAnaliseTesteSuor(db.Model):
    __tablename__ = 'tb_analise_teste_suor'

    co_seq_analise_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_analise_suor = db.Column(db.ForeignKey('tb_tipo_analise_suor.co_seq_tp_analise_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_teste_suor = db.Column(db.ForeignKey('tb_teste_suor.co_seq_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_teste_suor = db.Column(db.ForeignKey('tb_amostra_teste_suor.co_seq_amostra_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_equip_analise = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra_teste_suor = db.relationship('TbAmostraTesteSuor', primaryjoin='TbAnaliseTesteSuor.co_seq_amostra_teste_suor == TbAmostraTesteSuor.co_seq_amostra_teste_suor', backref='tb_analise_teste_suors')
    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbAnaliseTesteSuor.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_analise_teste_suors')
    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbAnaliseTesteSuor.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_analise_teste_suors')
    tb_teste_suor = db.relationship('TbTesteSuor', primaryjoin='TbAnaliseTesteSuor.co_seq_teste_suor == TbTesteSuor.co_seq_teste_suor', backref='tb_analise_teste_suors')
    tb_tipo_analise_suor = db.relationship('TbTipoAnaliseSuor', primaryjoin='TbAnaliseTesteSuor.co_seq_tp_analise_suor == TbTipoAnaliseSuor.co_seq_tp_analise_suor', backref='tb_analise_teste_suors')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbAnaliseTesteSuor.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_analise_teste_suors')



class TbAnexoDocumentoAnotacao(db.Model):
    __tablename__ = 'tb_anexo_documento_anotacao'

    co_seq_anexo_doc_anotacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_anotacao_geral = db.Column(db.ForeignKey('tb_anotacao_geral.co_seq_anotacao_geral', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_doc_anexo = db.Column(db.String(100), nullable=False)
    doc_anexo = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_anotacao_geral = db.relationship('TbAnotacaoGeral', primaryjoin='TbAnexoDocumentoAnotacao.co_seq_anotacao_geral == TbAnotacaoGeral.co_seq_anotacao_geral', backref='tb_anexo_documento_anotacaos')



class TbAnexoExameConsultaAmb(db.Model):
    __tablename__ = 'tb_anexo_exame_consulta_amb'

    co_seq_anexo_exame_con_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_exame_abulatorial = db.Column(db.ForeignKey('tb_exame_ambulatorial.co_seq_exame_abulatorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    doc_anexo = db.Column(db.LargeBinary, nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_doc_anexo = db.Column(db.String(100))
    ds_endereco_documento = db.Column(db.String(500))

    tb_exame_ambulatorial = db.relationship('TbExameAmbulatorial', primaryjoin='TbAnexoExameConsultaAmb.co_seq_exame_abulatorial == TbExameAmbulatorial.co_seq_exame_abulatorial', backref='tb_anexo_exame_consulta_ambs')



class TbAnotacaoGeral(db.Model):
    __tablename__ = 'tb_anotacao_geral'

    co_seq_anotacao_geral = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_bloco_anotacao_geral = db.Column(db.ForeignKey('tb_bloco_anotacao.co_seq_bloco_anotacao_geral', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_referencia = db.Column(db.Numeric(8, 0))

    tb_bloco_anotacao = db.relationship('TbBlocoAnotacao', primaryjoin='TbAnotacaoGeral.co_seq_bloco_anotacao_geral == TbBlocoAnotacao.co_seq_bloco_anotacao_geral', backref='tb_anotacao_gerals')



class TbAnotacaoGeralAlerta(db.Model):
    __tablename__ = 'tb_anotacao_geral_alerta'

    co_seq_anotacao_geral_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_anotacao_geral = db.Column(db.ForeignKey('tb_anotacao_geral.co_seq_anotacao_geral', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_visualizacao = db.Column(db.Numeric(14, 0))
    aut_visualizacao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_anotacao_geral = db.relationship('TbAnotacaoGeral', primaryjoin='TbAnotacaoGeralAlerta.co_seq_anotacao_geral == TbAnotacaoGeral.co_seq_anotacao_geral', backref='tb_anotacao_geral_alertas')
    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbAnotacaoGeralAlerta.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_anotacao_geral_alertas')



class TbAnotacaoLiberacaoAmostra(db.Model):
    __tablename__ = 'tb_anotacao_liberacao_amostra'

    co_seq_anotacao_lib_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_linha_anotacao = db.Column(db.Numeric(3, 0), nullable=False)
    ds_anotacao = db.Column(db.String(5000), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAnotacaoLiberacaoAmostra.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_anotacao_liberacao_amostras')



class TbAnotacaoPalavraChave(db.Model):
    __tablename__ = 'tb_anotacao_palavra_chave'

    co_seq_anotacao_palavra_chave = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_anotacao_geral = db.Column(db.ForeignKey('tb_anotacao_geral.co_seq_anotacao_geral', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_palavra_chave = db.Column(db.ForeignKey('tb_palavra_chave.co_seq_palavra_chave', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_anotacao_geral = db.relationship('TbAnotacaoGeral', primaryjoin='TbAnotacaoPalavraChave.co_seq_anotacao_geral == TbAnotacaoGeral.co_seq_anotacao_geral', backref='tb_anotacao_palavra_chaves')
    tb_palavra_chave = db.relationship('TbPalavraChave', primaryjoin='TbAnotacaoPalavraChave.co_seq_palavra_chave == TbPalavraChave.co_seq_palavra_chave', backref='tb_anotacao_palavra_chaves')



class TbAnotacaoPessoa(db.Model):
    __tablename__ = 'tb_anotacao_pessoa'

    co_seq_anotacao_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_linha_anotacao = db.Column(db.Numeric(3, 0), nullable=False)
    ds_anotacao = db.Column(db.String(5000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbAnotacaoPessoa.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_anotacao_pessoas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbAnotacaoPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_anotacao_pessoas')



class TbAnotacaoPicote(db.Model):
    __tablename__ = 'tb_anotacao_picote'

    co_seq_anotacao_picote = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_placa = db.Column(db.ForeignKey('tb_numero_placa.nu_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_item_anotacao_picote = db.Column(db.ForeignKey('tb_tipo_item_anotacao_picote.co_seq_item_anotacao_picote', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_outra_anotacao = db.Column(db.String(200))

    tb_tipo_item_anotacao_picote = db.relationship('TbTipoItemAnotacaoPicote', primaryjoin='TbAnotacaoPicote.co_seq_item_anotacao_picote == TbTipoItemAnotacaoPicote.co_seq_item_anotacao_picote', backref='tb_anotacao_picotes')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbAnotacaoPicote.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_anotacao_picotes')
    tb_numero_placa = db.relationship('TbNumeroPlaca', primaryjoin='TbAnotacaoPicote.nu_placa == TbNumeroPlaca.nu_placa', backref='tb_anotacao_picotes')



class TbArquivoImpressaoAi(db.Model):
    __tablename__ = 'tb_arquivo_impressao_ai'

    co_seq_arq_res_ai = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_arq = db.Column(db.String(100), nullable=False)
    arq_res = db.Column(db.LargeBinary, nullable=False)
    tex_filtro_impressao = db.Column(db.String(2000), nullable=False)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbArquivoImpressaoFamiliar(db.Model):
    __tablename__ = 'tb_arquivo_impressao_familiar'

    co_seq_arq_res_familiar = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_arq = db.Column(db.String(100), nullable=False)
    arq_res = db.Column(db.LargeBinary, nullable=False)
    tex_filtro_impressao = db.Column(db.String(2000), nullable=False)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbArquivoImpressaoResultado(db.Model):
    __tablename__ = 'tb_arquivo_impressao_resultado'

    co_seq_arq_res = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_arq = db.Column(db.String(100), nullable=False)
    arq_res = db.Column(db.LargeBinary, nullable=False)
    tex_filtro_impressao = db.Column(db.String(2000), nullable=False)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbArquivoLeituraPicotador(db.Model):
    __tablename__ = 'tb_arquivo_leitura_picotador'

    co_seq_arquivo_picotador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_geracao_placa = db.Column(db.ForeignKey('tb_geracao_placa.co_seq_geracao_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_arq = db.Column(db.String(100), nullable=False)
    arq_placa = db.Column(db.LargeBinary, nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_geracao_placa = db.relationship('TbGeracaoPlaca', primaryjoin='TbArquivoLeituraPicotador.co_seq_geracao_placa == TbGeracaoPlaca.co_seq_geracao_placa', backref='tb_arquivo_leitura_picotadors')



class TbArquivoResultadoPlaca(db.Model):
    __tablename__ = 'tb_arquivo_resultado_placa'

    co_seq_arq_res_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_reg_arq_res_placa = db.Column(db.ForeignKey('tb_arquivo_resultado_placa_anexo.co_seq_reg_arq_res_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_lin_arq_res_placa = db.Column(db.Integer, nullable=False)
    lin_arq_res_placa = db.Column(db.String(8000), nullable=False)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), nullable=False)

    tb_arquivo_resultado_placa_anexo = db.relationship('TbArquivoResultadoPlacaAnexo', primaryjoin='TbArquivoResultadoPlaca.co_seq_reg_arq_res_placa == TbArquivoResultadoPlacaAnexo.co_seq_reg_arq_res_placa', backref='tb_arquivo_resultado_placas')



class TbArquivoResultadoPlacaAnexo(db.Model):
    __tablename__ = 'tb_arquivo_resultado_placa_anexo'

    co_seq_reg_arq_res_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_arq = db.Column(db.String(100), index=True)
    arq_placa = db.Column(db.LargeBinary, nullable=False)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbArquivoResultadoSoro(db.Model):
    __tablename__ = 'tb_arquivo_resultado_soro'

    co_arq_res_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    arq_res = db.Column(db.LargeBinary, nullable=False)
    no_arq = db.Column(db.String(100), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_lote = db.Column(db.String(10))



class TbAtendimento(db.Model):
    __tablename__ = 'tb_atendimento'

    co_seq_atendimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_enc_atendimento = db.Column(db.ForeignKey('tb_encaminhamento_atendimento.co_seq_enc_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_canc_atendimento = db.Column(db.ForeignKey('tb_motivo_cancelamento_atendi.co_seq_mot_canc_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_conclusao_atendimento = db.Column(db.ForeignKey('tb_conclusao_atendimento.co_seq_conclusao_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_atendimento = db.Column(db.ForeignKey('tb_motivo_atendimento.co_seq_mot_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_atendimento = db.Column(db.Numeric(8, 0), nullable=False)
    ds_conclusao = db.Column(db.String(2000))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_conclusao_atendimento = db.relationship('TbConclusaoAtendimento', primaryjoin='TbAtendimento.co_seq_conclusao_atendimento == TbConclusaoAtendimento.co_seq_conclusao_atendimento', backref='tb_atendimentoes')
    tb_encaminhamento_atendimento = db.relationship('TbEncaminhamentoAtendimento', primaryjoin='TbAtendimento.co_seq_enc_atendimento == TbEncaminhamentoAtendimento.co_seq_enc_atendimento', backref='tb_atendimentoes')
    tb_motivo_atendimento = db.relationship('TbMotivoAtendimento', primaryjoin='TbAtendimento.co_seq_mot_atendimento == TbMotivoAtendimento.co_seq_mot_atendimento', backref='tb_atendimentoes')
    tb_motivo_cancelamento_atendi = db.relationship('TbMotivoCancelamentoAtendi', primaryjoin='TbAtendimento.co_seq_mot_canc_atendimento == TbMotivoCancelamentoAtendi.co_seq_mot_canc_atendimento', backref='tb_atendimentoes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbAtendimento.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_atendimentoes')



class TbAtendimentoMunicipio(db.Model):
    __tablename__ = 'tb_atendimento_municipio'

    co_seq_atendimento_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_conclusao_municipio = db.Column(db.ForeignKey('tb_conclusao_municipio.co_seq_conclusao_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_atendimento_municipio = db.Column(db.ForeignKey('tb_motivo_atendimento_municipio.co_seq_mot_atendimento_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_enc_municipio = db.Column(db.ForeignKey('tb_encaminhamento_municipio.co_seq_enc_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_atendimento = db.Column(db.Numeric(8, 0), nullable=False)
    ds_conclusao = db.Column(db.String(2000))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_conclusao_municipio = db.relationship('TbConclusaoMunicipio', primaryjoin='TbAtendimentoMunicipio.co_seq_conclusao_municipio == TbConclusaoMunicipio.co_seq_conclusao_municipio', backref='tb_atendimento_municipios')
    tb_encaminhamento_municipio = db.relationship('TbEncaminhamentoMunicipio', primaryjoin='TbAtendimentoMunicipio.co_seq_enc_municipio == TbEncaminhamentoMunicipio.co_seq_enc_municipio', backref='tb_atendimento_municipios')
    tb_motivo_atendimento_municipio = db.relationship('TbMotivoAtendimentoMunicipio', primaryjoin='TbAtendimentoMunicipio.co_seq_mot_atendimento_municipio == TbMotivoAtendimentoMunicipio.co_seq_mot_atendimento_municipio', backref='tb_atendimento_municipios')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbAtendimentoMunicipio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_atendimento_municipios')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbAtendimentoMunicipio.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_atendimento_municipios')



class TbAtualizacaoPessoa(db.Model):
    __tablename__ = 'tb_atualizacao_pessoa'

    co_seq_atualizacao_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_registro_efetuado = db.Column(db.String(1), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_registro_efetuado_soro = db.Column(db.String(1), nullable=False)
    ide_registro_efetuado_com = db.Column(db.String(1), nullable=False)
    ide_registro_efetuado_hipo = db.Column(db.String(1), nullable=False)
    ide_registro_efetuado_agen = db.Column(db.String(1), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbAtualizacaoPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_atualizacao_pessoas')



class TbBiologiaMolecular(db.Model):
    __tablename__ = 'tb_biologia_molecular'

    co_seq_biologia_molecular = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_parentesco = db.Column(db.ForeignKey('tb_tipo_parentesco.co_seq_tp_parentesco', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_cid = db.Column(db.ForeignKey('tb_cid.co_seq_cid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_solicitacao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_envio_biologia_molecular = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_liberacao = db.Column(db.Numeric(8, 0))
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))
    co_laboratorio_genetica = db.Column(db.String(20))
    dt_recep_resultado = db.Column(db.Numeric(8, 0))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbBiologiaMolecular.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_biologia_moleculars')
    tb_cid = db.relationship('TbCid', primaryjoin='TbBiologiaMolecular.co_seq_cid == TbCid.co_seq_cid', backref='tb_biologia_moleculars')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbBiologiaMolecular.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_biologia_moleculars')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbBiologiaMolecular.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_biologia_moleculars')
    tb_tipo_parentesco = db.relationship('TbTipoParentesco', primaryjoin='TbBiologiaMolecular.co_seq_tp_parentesco == TbTipoParentesco.co_seq_tp_parentesco', backref='tb_biologia_moleculars')



class TbBlocoAnotacao(db.Model):
    __tablename__ = 'tb_bloco_anotacao'

    co_seq_bloco_anotacao_geral = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_bloco_anotacao_geral = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbBloqueioAgendamento(db.Model):
    __tablename__ = 'tb_bloqueio_agendamento'

    co_seq_bloqueio_agendamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ide_agendamento_consulta = db.Column(db.String(1))
    dt_agendamento = db.Column(db.Numeric(8, 0), nullable=False)
    hr_agendamento_ini = db.Column(db.String(4))
    hr_agendamento_ter = db.Column(db.String(4))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbBloqueioAgendamento.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_bloqueio_agendamentoes')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbBloqueioAgendamento.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_bloqueio_agendamentoes')



class TbBpaCConsolidado(db.Model):
    __tablename__ = 'tb_bpa_c_consolidado'

    co_seq_bpa_c_consolidado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_bpa_cabecalho = db.Column(db.ForeignKey('tb_bpa_cabecalho.co_seq_bpa_cabecalho', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    prd_ident = db.Column(db.Numeric(2, 0))
    prd_cnes = db.Column(db.Numeric(7, 0))
    prd_cmp = db.Column(db.Numeric(6, 0))
    prd_cbo = db.Column(db.String(6))
    prd_flh = db.Column(db.Numeric(3, 0))
    prd_seq = db.Column(db.Numeric(2, 0))
    prd_pa = db.Column(db.Numeric(10, 0))
    prd_ldade = db.Column(db.Numeric(3, 0))
    prd_qt = db.Column(db.Numeric(6, 0))
    prd_org = db.Column(db.String(3))

    tb_bpa_cabecalho = db.relationship('TbBpaCabecalho', primaryjoin='TbBpaCConsolidado.co_seq_bpa_cabecalho == TbBpaCabecalho.co_seq_bpa_cabecalho', backref='tb_bpa_c_consolidadoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbBpaCConsolidado.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_bpa_c_consolidadoes')



class TbBpaCabecalho(db.Model):
    __tablename__ = 'tb_bpa_cabecalho'

    co_seq_bpa_cabecalho = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seg_fch_mensal = db.Column(db.ForeignKey('tb_fechamento_mensal.co_seg_fch_mensal', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cbc_hdr_1 = db.Column(db.Numeric(1, 0))
    cbc_hdr_2 = db.Column(db.String(5))
    cbc_mvm = db.Column(db.Numeric(6, 0))
    cbc_lin = db.Column(db.Numeric(6, 0))
    cbc_flh = db.Column(db.Numeric(6, 0))
    cbc_smt_vrf = db.Column(db.Numeric(4, 0))
    cbc_rsp = db.Column(db.String(30))
    cbc_sgl = db.Column(db.String(6))
    cbc_cgccpf = db.Column(db.Numeric(14, 0))
    cbc_dst = db.Column(db.String(40))
    cbc_dst_in = db.Column(db.String(1))
    cbc_versao = db.Column(db.String(10))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    arq_mes = db.Column(db.LargeBinary)

    tb_fechamento_mensal = db.relationship('TbFechamentoMensal', primaryjoin='TbBpaCabecalho.co_seg_fch_mensal == TbFechamentoMensal.co_seg_fch_mensal', backref='tb_bpa_cabecalhoes')



class TbBpaCaracteristicaProc(db.Model):
    __tablename__ = 'tb_bpa_caracteristica_proc'

    co_seq_carac_proc_bpa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_servico_bpa = db.Column(db.ForeignKey('tb_bpa_tipo_servico.co_seq_tp_servico_bpa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_carac_bpa = db.Column(db.ForeignKey('tb_bpa_tipo_caracteristica.co_seq_tp_carac_bpa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_comp = db.Column(db.Numeric(6, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_bpa_tipo_caracteristica = db.relationship('TbBpaTipoCaracteristica', primaryjoin='TbBpaCaracteristicaProc.co_seq_tp_carac_bpa == TbBpaTipoCaracteristica.co_seq_tp_carac_bpa', backref='tb_bpa_caracteristica_procs')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbBpaCaracteristicaProc.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_bpa_caracteristica_procs')
    tb_bpa_tipo_servico = db.relationship('TbBpaTipoServico', primaryjoin='TbBpaCaracteristicaProc.co_seq_tp_servico_bpa == TbBpaTipoServico.co_seq_tp_servico_bpa', backref='tb_bpa_caracteristica_procs')



class TbBpaCepDatasu(db.Model):
    __tablename__ = 'tb_bpa_cep_datasus'
    __table_args__ = (
        db.Index('in_bpaceodatasus_coibge_nucep', 'co_ibge', 'nu_cep'),
    )

    co_seq_cep_datasus = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ibge = db.Column(db.String(10), index=True)
    nu_cep = db.Column(db.String(8), index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbBpaIIndividualizado(db.Model):
    __tablename__ = 'tb_bpa_i_individualizado'

    co_seq_bpa_i_individualizado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_bpa_procedimento = db.Column(db.ForeignKey('tb_bpa_procedimento.co_seq_bpa_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_bpa_cabecalho = db.Column(db.ForeignKey('tb_bpa_cabecalho.co_seq_bpa_cabecalho', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    prd_ident = db.Column(db.Numeric(2, 0))
    prd_cnes = db.Column(db.Numeric(7, 0))
    prd_cmp = db.Column(db.Numeric(6, 0))
    prd_cnsmed = db.Column(db.Numeric(15, 0))
    prd_cbo = db.Column(db.String(6))
    prd_dtaten = db.Column(db.Numeric(8, 0))
    prd_flh = db.Column(db.Numeric(3, 0))
    prd_seq = db.Column(db.Numeric(2, 0))
    prd_pa = db.Column(db.Numeric(10, 0))
    prd_cnspac = db.Column(db.Numeric(15, 0))
    prd_sexo = db.Column(db.String(1))
    prd_ibge = db.Column(db.Numeric(6, 0))
    prd_cid = db.Column(db.String(4))
    prd_ldade = db.Column(db.Numeric(3, 0))
    prd_qt = db.Column(db.Numeric(6, 0))
    prd_caten = db.Column(db.Numeric(2, 0))
    prd_naut = db.Column(db.String(13))
    prd_org = db.Column(db.String(3))
    prd_nmpac = db.Column(db.String(30))
    prd_dtnasc = db.Column(db.Numeric(8, 0))
    prd_raca = db.Column(db.String(2))
    prd_etnia = db.Column(db.String(4))
    prd_nac = db.Column(db.Numeric(3, 0))
    prd_srv = db.Column(db.Numeric(3, 0))
    prd_clf = db.Column(db.Numeric(3, 0))
    prd_equipe_seq = db.Column(db.Numeric(8, 0))
    prd_equipe_area = db.Column(db.Numeric(4, 0))
    prd_cnpj = db.Column(db.Numeric(14, 0))
    prd_cep_pcnte = db.Column(db.Numeric(8, 0))
    prd_lograd_pcnte = db.Column(db.Numeric(3, 0))
    prd_end_pcnte = db.Column(db.String(30))
    prd_compl_pcnte = db.Column(db.Numeric(10, 0))
    prd_num_pcnte = db.Column(db.Numeric(5, 0))
    prd_bairro_pcnte = db.Column(db.String(30))
    prd_ddtel_pcnte = db.Column(db.Numeric(11, 0))
    prd_email_pcnte = db.Column(db.String(40))

    tb_bpa_cabecalho = db.relationship('TbBpaCabecalho', primaryjoin='TbBpaIIndividualizado.co_seq_bpa_cabecalho == TbBpaCabecalho.co_seq_bpa_cabecalho', backref='tb_bpa_i_individualizadoes')
    tb_bpa_procedimento = db.relationship('TbBpaProcedimento', primaryjoin='TbBpaIIndividualizado.co_seq_bpa_procedimento == TbBpaProcedimento.co_seq_bpa_procedimento', backref='tb_bpa_i_individualizadoes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbBpaIIndividualizado.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_bpa_i_individualizadoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbBpaIIndividualizado.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_bpa_i_individualizadoes')



class TbBpaPaciente(db.Model):
    __tablename__ = 'tb_bpa_paciente'

    co_seq_bpa_paciente = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbBpaPaciente.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_bpa_pacientes')



class TbBpaParametro(db.Model):
    __tablename__ = 'tb_bpa_parametro'

    co_seq_parametro_bpa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_orgao_responsavel = db.Column(db.String(100), nullable=False)
    sg_orgao_responsavel = db.Column(db.String(20), nullable=False)
    no_orgao_destino = db.Column(db.String(100), nullable=False)
    ide_orgao_destino = db.Column(db.String(1), nullable=False)
    ds_versao_sistema = db.Column(db.String(50), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    cgc_cpf_prestador = db.Column(db.String(20), nullable=False)
    nu_cnes = db.Column(db.String(30))



class TbBpaProcedimento(db.Model):
    __tablename__ = 'tb_bpa_procedimento'

    co_seq_bpa_procedimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_cid = db.Column(db.ForeignKey('tb_cid.co_seq_cid', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_bpa_paciente = db.Column(db.ForeignKey('tb_bpa_paciente.co_seq_bpa_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_atendimento = db.Column(db.Numeric(8, 0), nullable=False)

    tb_bpa_paciente = db.relationship('TbBpaPaciente', primaryjoin='TbBpaProcedimento.co_seq_bpa_paciente == TbBpaPaciente.co_seq_bpa_paciente', backref='tb_bpa_procedimentoes')
    tb_cid = db.relationship('TbCid', primaryjoin='TbBpaProcedimento.co_seq_cid == TbCid.co_seq_cid', backref='tb_bpa_procedimentoes')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbBpaProcedimento.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_bpa_procedimentoes')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbBpaProcedimento.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_bpa_procedimentoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbBpaProcedimento.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_bpa_procedimentoes')



class TbBpaProfissionalProcedimento(db.Model):
    __tablename__ = 'tb_bpa_profissional_procedimento'

    co_seq_prof_procedimento_bpa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_cid = db.Column(db.ForeignKey('tb_cid.co_seq_cid', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_cid = db.relationship('TbCid', primaryjoin='TbBpaProfissionalProcedimento.co_seq_cid == TbCid.co_seq_cid', backref='tb_bpa_profissional_procedimentoes')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbBpaProfissionalProcedimento.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_bpa_profissional_procedimentoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbBpaProfissionalProcedimento.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_bpa_profissional_procedimentoes')



class TbBpaTipoCaracteristica(db.Model):
    __tablename__ = 'tb_bpa_tipo_caracteristica'

    co_seq_tp_carac_bpa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_servico_bpa = db.Column(db.ForeignKey('tb_bpa_tipo_servico.co_seq_tp_servico_bpa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_carac_bpa = db.Column(db.String(100), nullable=False)
    co_tp_carac_bpa = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_bpa_tipo_servico = db.relationship('TbBpaTipoServico', primaryjoin='TbBpaTipoCaracteristica.co_seq_tp_servico_bpa == TbBpaTipoServico.co_seq_tp_servico_bpa', backref='tb_bpa_tipo_caracteristicas')



class TbBpaTipoServico(db.Model):
    __tablename__ = 'tb_bpa_tipo_servico'

    co_seq_tp_servico_bpa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_servico_bpa = db.Column(db.String(100), nullable=False)
    co_tp_servico_bpa = db.Column(db.String(10), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbCampoEntrada(db.Model):
    __tablename__ = 'tb_campo_entrada'

    co_seq_campo_entrada = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_campo_entrada = db.Column(db.String(50), nullable=False)

    tb_transacao = db.relationship('TbTransacao', secondary='tb_campo_entrada_transacao', backref='tb_campo_entradas')



t_tb_campo_entrada_transacao = db.Table(
    'tb_campo_entrada_transacao',
    db.Column('co_seq_campo_entrada', db.ForeignKey('tb_campo_entrada.co_seq_campo_entrada', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_seq_transacao', db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
)



class TbCampoFichaAmbulatorio(db.Model):
    __tablename__ = 'tb_campo_ficha_ambulatorio'

    co_seq_campo_ficha_amb = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_campo_ficha = db.Column(db.String(80), nullable=False)
    ds_completa_campo_ficha = db.Column(db.String(400))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbCancelamentoComunicaExame(db.Model):
    __tablename__ = 'tb_cancelamento_comunica_exame'

    co_seq_canc_comunicacao_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_canc_comunicacao = db.Column(db.ForeignKey('tb_motivo_cancelamento_comunicar.co_seq_mot_canc_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao_tipo_exame = db.Column(db.ForeignKey('tb_comunicacao_tipo_exame.co_seq_comunicacao_tipo_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_comunicacao_tipo_exame = db.relationship('TbComunicacaoTipoExame', primaryjoin='TbCancelamentoComunicaExame.co_seq_comunicacao_tipo_exame == TbComunicacaoTipoExame.co_seq_comunicacao_tipo_exame', backref='tb_cancelamento_comunica_exames')
    tb_motivo_cancelamento_comunicar = db.relationship('TbMotivoCancelamentoComunicar', primaryjoin='TbCancelamentoComunicaExame.co_seq_mot_canc_comunicacao == TbMotivoCancelamentoComunicar.co_seq_mot_canc_comunicacao', backref='tb_cancelamento_comunica_exames')



class TbCancelarBiologiaMolecular(db.Model):
    __tablename__ = 'tb_cancelar_biologia_molecular'

    co_seq_canc_biologia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbCancelarBiologiaMolecular.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_cancelar_biologia_moleculars')



class TbCancelarPreparacaoEnvio(db.Model):
    __tablename__ = 'tb_cancelar_preparacao_envio'

    co_seq_canc_preparacao_envio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento = db.Column(db.ForeignKey('tb_agendamento.co_seq_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_agendamento = db.relationship('TbAgendamento', primaryjoin='TbCancelarPreparacaoEnvio.co_seq_agendamento == TbAgendamento.co_seq_agendamento', backref='tb_cancelar_preparacao_envios')
    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbCancelarPreparacaoEnvio.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_cancelar_preparacao_envios')



class TbCargo(db.Model):
    __tablename__ = 'tb_cargo'

    co_seq_cargo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_cargo = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbCategoriaMenu(db.Model):
    __tablename__ = 'tb_categoria_menu'

    co_seq_tp_categoria = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_categoria = db.Column(db.String(50), nullable=False)



class TbCertificadoDigital(db.Model):
    __tablename__ = 'tb_certificado_digital'

    co_seq_certificado_digital = db.Column(db.Numeric(14, 0), primary_key=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra'), nullable=False, index=True)
    co_seq_colaborador = db.Column(db.Numeric(5, 0), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_conteudo_para_certificar = db.Column(db.Text)
    ds_chave = db.Column(db.Text)
    ds_conteudo_certificado = db.Column(db.Text)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbCertificadoDigital.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_certificado_digitals')



class TbCid(db.Model):
    __tablename__ = 'tb_cid'

    co_seq_cid = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    co_seq_proced_cid_doenca = db.Column(db.Integer, index=True)
    ds_cid = db.Column(db.String(40), nullable=False)



class TbCodigoEntradaPadrao(db.Model):
    __tablename__ = 'tb_codigo_entrada_padrao'

    co_seq_ent_padrao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_ent_padrao = db.Column(db.ForeignKey('tb_tipo_entrada_padrao.co_seq_tp_ent_padrao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_ent_padrao = db.Column(db.String(3), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_entrada_padrao = db.relationship('TbTipoEntradaPadrao', primaryjoin='TbCodigoEntradaPadrao.co_seq_tp_ent_padrao == TbTipoEntradaPadrao.co_seq_tp_ent_padrao', backref='tb_codigo_entrada_padraos')



class TbCodigoEntradaPessoa(db.Model):
    __tablename__ = 'tb_codigo_entrada_pessoa'

    co_ent_pessoa = db.Column(db.String(20), primary_key=True, unique=True)



class TbCodigoLaboratorio(db.Model):
    __tablename__ = 'tb_codigo_laboratorio'

    co_amostra_labotatorio = db.Column(db.String(25), primary_key=True, unique=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbCodigoLaboratorio.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_codigo_laboratorios')



class TbCodigoUnidade(db.Model):
    __tablename__ = 'tb_codigo_unidade'

    co_seq_co_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_controle_co_unidade = db.Column(db.ForeignKey('tb_controle_codigo_unidade.co_seq_controle_co_unidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_ent_pessoa_unidade = db.Column(db.String(20), nullable=False)
    nu_seq_pessoa = db.Column(db.Numeric(14, 0), nullable=False)

    tb_controle_codigo_unidade = db.relationship('TbControleCodigoUnidade', primaryjoin='TbCodigoUnidade.co_seq_controle_co_unidade == TbControleCodigoUnidade.co_seq_controle_co_unidade', backref='tb_codigo_unidades')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbCodigoUnidade.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_codigo_unidades')



class TbColaborador(db.Model):
    __tablename__ = 'tb_colaborador'
    __table_args__ = (
        db.Index('in_colab_coseqcolab_cosequsu', 'co_seq_colaborador', 'co_seq_usuario'),
    )

    co_seq_colaborador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_usuario = db.Column(db.ForeignKey('tb_usuario.co_seq_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_funcao_colaborador = db.Column(db.ForeignKey('tb_funcao_colaborador.co_seq_funcao_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_colaborador = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.Numeric(8, 0), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    nu_celular = db.Column(db.String(20), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_registro = db.Column(db.String(30), nullable=False)

    tb_funcao_colaborador = db.relationship('TbFuncaoColaborador', primaryjoin='TbColaborador.co_seq_funcao_colaborador == TbFuncaoColaborador.co_seq_funcao_colaborador', backref='tb_colaboradors')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbColaborador.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_colaboradors')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbColaborador.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_colaboradors')
    tb_usuario = db.relationship('TbUsuario', primaryjoin='TbColaborador.co_seq_usuario == TbUsuario.co_seq_usuario', backref='tb_colaboradors')



class TbColaboradorBlocoAnotacao(db.Model):
    __tablename__ = 'tb_colaborador_bloco_anotacao'

    co_seq_colaborador_bloco = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_bloco_anotacao_geral = db.Column(db.ForeignKey('tb_bloco_anotacao.co_seq_bloco_anotacao_geral', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_bloco_anotacao = db.relationship('TbBlocoAnotacao', primaryjoin='TbColaboradorBlocoAnotacao.co_seq_bloco_anotacao_geral == TbBlocoAnotacao.co_seq_bloco_anotacao_geral', backref='tb_colaborador_bloco_anotacaos')
    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbColaboradorBlocoAnotacao.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_colaborador_bloco_anotacaos')



class TbColaboradorControleAlerta(db.Model):
    __tablename__ = 'tb_colaborador_controle_alerta'

    co_seq_colaborador_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_controle_alerta = db.Column(db.ForeignKey('tb_controle_alerta.co_seq_controle_alerta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_visualizacao = db.Column(db.Numeric(14, 0))
    aut_visualizacao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbColaboradorControleAlerta.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_colaborador_controle_alertas')
    tb_controle_alerta = db.relationship('TbControleAlerta', primaryjoin='TbColaboradorControleAlerta.co_seq_controle_alerta == TbControleAlerta.co_seq_controle_alerta', backref='tb_colaborador_controle_alertas')



class TbColaboradorDoenca(db.Model):
    __tablename__ = 'tb_colaborador_doenca'
    __table_args__ = (
        db.Index('in_colabdoe_coseqcolab_coseqdoe_dthrcanc', 'co_seq_colaborador', 'co_seq_doenca', 'dt_hr_cancelamento'),
        db.Index('in_colabdoe_coseqcolab_dthrcanc', 'co_seq_colaborador', 'dt_hr_cancelamento')
    )

    co_seq_colaborador_doenca = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbColaboradorDoenca.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_colaborador_doencas')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbColaboradorDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_colaborador_doencas')



class TbColaboradorExame(db.Model):
    __tablename__ = 'tb_colaborador_exame'
    __table_args__ = (
        db.Index('in_colabexa_coseqtpexa_coseqcolab', 'co_seq_tp_exame', 'co_seq_colaborador'),
    )

    co_seq_colaborador_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbColaboradorExame.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_colaborador_exames')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbColaboradorExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_colaborador_exames')



class TbColaboradorMacro(db.Model):
    __tablename__ = 'tb_colaborador_macro'
    __table_args__ = (
        db.Index('in_colabmacro_coseqcolab_coseqmac_dthrcanc', 'co_seq_colaborador', 'co_seq_macroregiao', 'dt_hr_cancelamento'),
        db.Index('in_colabmacro_coseqcolab_dthrcanc', 'co_seq_colaborador', 'dt_hr_cancelamento')
    )

    co_seq_colaborador_macro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_macroregiao = db.Column(db.ForeignKey('tb_macroregiao.co_seq_macroregiao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbColaboradorMacro.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_colaborador_macros')
    tb_macroregiao = db.relationship('TbMacroregiao', primaryjoin='TbColaboradorMacro.co_seq_macroregiao == TbMacroregiao.co_seq_macroregiao', backref='tb_colaborador_macros')



class TbColetaTesteSuor(db.Model):
    __tablename__ = 'tb_coleta_teste_suor'

    co_seq_col_teste_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_indutor_suor = db.Column(db.ForeignKey('tb_indutor_suor.co_seq_indutor_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_teste_suor = db.Column(db.ForeignKey('tb_teste_suor.co_seq_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_equip_indutor_suor = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    pes_grama = db.Column(db.Numeric(14, 0))
    ide_col_duas_amostra = db.Column(db.String(1))

    tb_indutor_suor = db.relationship('TbIndutorSuor', primaryjoin='TbColetaTesteSuor.co_seq_indutor_suor == TbIndutorSuor.co_seq_indutor_suor', backref='tb_coleta_teste_suors')
    tb_teste_suor = db.relationship('TbTesteSuor', primaryjoin='TbColetaTesteSuor.co_seq_teste_suor == TbTesteSuor.co_seq_teste_suor', backref='tb_coleta_teste_suors')



class TbColunaAmostraPlaca(db.Model):
    __tablename__ = 'tb_coluna_amostra_placa'

    co_seq_col_amostra_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_col_amostra_placa = db.Column(db.ForeignKey('tb_tipo_coluna_amostra_placa.co_seq_tp_col_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_texto = db.Column(db.String(2000), index=True)
    cont_col_numero = db.Column(db.Double(53), index=True)
    ide_col_comp_lin_corte = db.Column(db.String(1), nullable=False)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0))

    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbColunaAmostraPlaca.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_coluna_amostra_placas')
    tb_tipo_coluna_amostra_placa = db.relationship('TbTipoColunaAmostraPlaca', primaryjoin='TbColunaAmostraPlaca.co_seq_tp_col_amostra_placa == TbTipoColunaAmostraPlaca.co_seq_tp_col_amostra_placa', backref='tb_coluna_amostra_placas')



class TbColunaAmostraTesteSuor(db.Model):
    __tablename__ = 'tb_coluna_amostra_teste_suor'

    co_seq_col_amostra_teste_suor = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_col_amostra_teste_suor = db.Column(db.String(30), nullable=False)



class TbColunaArquivoInterface(db.Model):
    __tablename__ = 'tb_coluna_arquivo_interface'
    __table_args__ = (
        db.Index('in_conarqint_cointesqexa_coarqintexa_cotpcolamo_dthrcalc', 'co_seq_int_equip_exame', 'co_seq_arq_int_exame', 'co_seq_tp_col_amostra_placa', 'dt_hr_cancelamento'),
    )

    co_seq_arq_int_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_int_equip_exame = db.Column(db.ForeignKey('tb_interface_equipamento_exame.co_seq_int_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_col_amostra_placa = db.Column(db.ForeignKey('tb_tipo_coluna_amostra_placa.co_seq_tp_col_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_col_arq = db.Column(db.Numeric(2, 0), nullable=False)
    ide_col_comp_lin_corte = db.Column(db.String(1), nullable=False)
    nu_ini_caracter = db.Column(db.Numeric(4, 0))
    nu_ter_caracter = db.Column(db.Numeric(4, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_formula_calculo = db.Column(db.String(200))

    tb_interface_equipamento_exame = db.relationship('TbInterfaceEquipamentoExame', primaryjoin='TbColunaArquivoInterface.co_seq_int_equip_exame == TbInterfaceEquipamentoExame.co_seq_int_equip_exame', backref='tb_coluna_arquivo_interfaces')
    tb_tipo_coluna_amostra_placa = db.relationship('TbTipoColunaAmostraPlaca', primaryjoin='TbColunaArquivoInterface.co_seq_tp_col_amostra_placa == TbTipoColunaAmostraPlaca.co_seq_tp_col_amostra_placa', backref='tb_coluna_arquivo_interfaces')



class TbColunaComunicacaoSerial(db.Model):
    __tablename__ = 'tb_coluna_comunicacao_serial'

    co_seq_col_porta_serial = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_col_amostra_placa = db.Column(db.ForeignKey('tb_tipo_coluna_amostra_placa.co_seq_tp_col_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_com_porta_serial = db.Column(db.ForeignKey('tb_comunicacao_porta_serial.co_seq_com_porta_serial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_soro_tp_exame = db.Column(db.ForeignKey('tb_amostra_soro_tipo_exame.co_seq_amostra_soro_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), nullable=False)
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    ide_col_comp_lin_corte = db.Column(db.String(1), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbColunaComunicacaoSerial.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_coluna_comunicacao_serials')
    tb_amostra_soro_tipo_exame = db.relationship('TbAmostraSoroTipoExame', primaryjoin='TbColunaComunicacaoSerial.co_seq_amostra_soro_tp_exame == TbAmostraSoroTipoExame.co_seq_amostra_soro_tp_exame', backref='tb_coluna_comunicacao_serials')
    tb_comunicacao_porta_serial = db.relationship('TbComunicacaoPortaSerial', primaryjoin='TbColunaComunicacaoSerial.co_seq_com_porta_serial == TbComunicacaoPortaSerial.co_seq_com_porta_serial', backref='tb_coluna_comunicacao_serials')
    tb_tipo_coluna_amostra_placa = db.relationship('TbTipoColunaAmostraPlaca', primaryjoin='TbColunaComunicacaoSerial.co_seq_tp_col_amostra_placa == TbTipoColunaAmostraPlaca.co_seq_tp_col_amostra_placa', backref='tb_coluna_comunicacao_serials')



class TbColunaConsulta(db.Model):
    __tablename__ = 'tb_coluna_consulta'

    co_seq_coluna_consulta = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_tabela_virtual = db.Column(db.ForeignKey('tb_tabela_virtual.co_seq_tabela_virtual', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_coluna = db.Column(db.String(200), nullable=False)
    ds_completa_coluna = db.Column(db.String(2000))
    ds_grupo = db.Column(db.String(200))
    ds_secao = db.Column(db.String(200))
    nu_ordem_grupo = db.Column(db.Numeric(3, 0))
    nu_ordem_secao = db.Column(db.Numeric(3, 0))
    nu_ordem_item = db.Column(db.Numeric(3, 0))

    tb_tabela_virtual = db.relationship('TbTabelaVirtual', primaryjoin='TbColunaConsulta.co_seq_tabela_virtual == TbTabelaVirtual.co_seq_tabela_virtual', backref='tb_coluna_consultas')



class TbColunaConsultaAmbulatorial(db.Model):
    __tablename__ = 'tb_coluna_consulta_ambulatorial'

    co_seq_coluna_consulta_amb = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_tabela_amb = db.Column(db.ForeignKey('tb_tabela_virtual_ambulatorio.co_seq_tabela_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_seq_coluna_consulta_amb = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tabela_virtual_ambulatorio = db.relationship('TbTabelaVirtualAmbulatorio', primaryjoin='TbColunaConsultaAmbulatorial.co_seq_tabela_amb == TbTabelaVirtualAmbulatorio.co_seq_tabela_amb', backref='tb_coluna_consulta_ambulatorials')



class TbColunaControlePlaca(db.Model):
    __tablename__ = 'tb_coluna_controle_placa'

    co_seq_col_controle_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_col_amostra_placa = db.Column(db.ForeignKey('tb_tipo_coluna_amostra_placa.co_seq_tp_col_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_reg_controle_placa = db.Column(db.ForeignKey('tb_controle_placa.co_seq_reg_controle_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    nu_proc_controle_int = db.Column(db.Numeric(14, 0))
    ide_col_comp_lin_corte = db.Column(db.String(1))

    tb_controle_placa = db.relationship('TbControlePlaca', primaryjoin='TbColunaControlePlaca.co_seq_reg_controle_placa == TbControlePlaca.co_seq_reg_controle_placa', backref='tb_coluna_controle_placas')
    tb_tipo_coluna_amostra_placa = db.relationship('TbTipoColunaAmostraPlaca', primaryjoin='TbColunaControlePlaca.co_seq_tp_col_amostra_placa == TbTipoColunaAmostraPlaca.co_seq_tp_col_amostra_placa', backref='tb_coluna_controle_placas')



class TbColunaItemConsultaAmb(db.Model):
    __tablename__ = 'tb_coluna_item_consulta_amb'

    co_seq_col_item_consulta_amb = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    co_seq_coluna_consulta_amb = db.Column(db.ForeignKey('tb_coluna_consulta_ambulatorial.co_seq_coluna_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tb_coluna_item_consulta_amb_co_seq_col_item_consul = db.Column(db.ForeignKey('tb_coluna_item_consulta_amb.co_seq_col_item_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_col_item_consulta_amb = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_consulta_ambulatorial = db.relationship('TbColunaConsultaAmbulatorial', primaryjoin='TbColunaItemConsultaAmb.co_seq_coluna_consulta_amb == TbColunaConsultaAmbulatorial.co_seq_coluna_consulta_amb', backref='tb_coluna_item_consulta_ambs')
    parent = db.relationship('TbColunaItemConsultaAmb', remote_side=[co_seq_col_item_consulta_amb], primaryjoin='TbColunaItemConsultaAmb.tb_coluna_item_consulta_amb_co_seq_col_item_consul == TbColunaItemConsultaAmb.co_seq_col_item_consulta_amb', backref='tb_coluna_item_consulta_ambs')



class TbColunaItemPacienteAmb(db.Model):
    __tablename__ = 'tb_coluna_item_paciente_amb'

    co_seq_col_item_paciente_amb = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    tb_coluna_item_paciente_amb_co_seq_col_item_pacien = db.Column(db.ForeignKey('tb_coluna_item_paciente_amb.co_seq_col_item_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_coluna_paciente_amb = db.Column(db.ForeignKey('tb_coluna_paciente_anbulatorial.co_seq_coluna_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_col_item_paciente_amb = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_paciente_anbulatorial = db.relationship('TbColunaPacienteAnbulatorial', primaryjoin='TbColunaItemPacienteAmb.co_seq_coluna_paciente_amb == TbColunaPacienteAnbulatorial.co_seq_coluna_paciente_amb', backref='tb_coluna_item_paciente_ambs')
    parent = db.relationship('TbColunaItemPacienteAmb', remote_side=[co_seq_col_item_paciente_amb], primaryjoin='TbColunaItemPacienteAmb.tb_coluna_item_paciente_amb_co_seq_col_item_pacien == TbColunaItemPacienteAmb.co_seq_col_item_paciente_amb', backref='tb_coluna_item_paciente_ambs')



class TbColunaPaciente(db.Model):
    __tablename__ = 'tb_coluna_paciente'

    co_seq_coluna_paciente = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_tabela_virtual = db.Column(db.ForeignKey('tb_tabela_virtual.co_seq_tabela_virtual', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_coluna = db.Column(db.String(200), nullable=False)
    ds_completa_coluna = db.Column(db.String(2000))
    nu_ordem_grupo = db.Column(db.Numeric(3, 0))
    nu_ordem_secao = db.Column(db.Numeric(3, 0))
    nu_ordem_item = db.Column(db.Numeric(3, 0))
    ds_grupo = db.Column(db.String(200))
    ds_secao = db.Column(db.String(200))

    tb_tabela_virtual = db.relationship('TbTabelaVirtual', primaryjoin='TbColunaPaciente.co_seq_tabela_virtual == TbTabelaVirtual.co_seq_tabela_virtual', backref='tb_coluna_pacientes')



class TbColunaPacienteAnbulatorial(db.Model):
    __tablename__ = 'tb_coluna_paciente_anbulatorial'

    co_seq_coluna_paciente_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tabela_amb = db.Column(db.ForeignKey('tb_tabela_virtual_ambulatorio.co_seq_tabela_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_coluna_paciente_amb = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tabela_virtual_ambulatorio = db.relationship('TbTabelaVirtualAmbulatorio', primaryjoin='TbColunaPacienteAnbulatorial.co_seq_tabela_amb == TbTabelaVirtualAmbulatorio.co_seq_tabela_amb', backref='tb_coluna_paciente_anbulatorials')



class TbColunaPlaca(db.Model):
    __tablename__ = 'tb_coluna_placa'

    co_seq_col_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_col_placa = db.Column(db.ForeignKey('tb_tipo_coluna_placa.co_seq_tp_col_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_seq_placa = db.Column(db.ForeignKey('tb_placa.nu_seq_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_texto = db.Column(db.String(2000))
    cont_col_numero = db.Column(db.Double(53))

    tb_tipo_coluna_placa = db.relationship('TbTipoColunaPlaca', primaryjoin='TbColunaPlaca.co_seq_tp_col_placa == TbTipoColunaPlaca.co_seq_tp_col_placa', backref='tb_coluna_placas')
    tb_placa = db.relationship('TbPlaca', primaryjoin='TbColunaPlaca.nu_seq_placa == TbPlaca.nu_seq_placa', backref='tb_coluna_placas')



class TbColunaResultado(db.Model):
    __tablename__ = 'tb_coluna_resultado'

    co_seq_col_resultado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_col_resultado = db.Column(db.ForeignKey('tb_tipo_coluna_resultado.co_seq_tp_col_resultado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_texto = db.Column(db.String(2000))
    cont_col_numero = db.Column(db.Double(53))

    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbColunaResultado.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_coluna_resultadoes')
    tb_tipo_coluna_resultado = db.relationship('TbTipoColunaResultado', primaryjoin='TbColunaResultado.co_seq_tp_col_resultado == TbTipoColunaResultado.co_seq_tp_col_resultado', backref='tb_coluna_resultadoes')



class TbCompetencia(db.Model):
    __tablename__ = 'tb_competencia'

    dt_competencia = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))



class TbComposicaoKitMaterial(db.Model):
    __tablename__ = 'tb_composicao_kit_material'

    co_seq_composicao_kit = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_kit_material = db.Column(db.ForeignKey('tb_kit_material.co_seq_kit_material', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tip_co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_percentual_valor = db.Column(db.String(1), nullable=False)
    percentual_valor = db.Column(db.Double(53), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_kit_material = db.relationship('TbKitMaterial', primaryjoin='TbComposicaoKitMaterial.co_seq_kit_material == TbKitMaterial.co_seq_kit_material', backref='tb_composicao_kit_materials')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbComposicaoKitMaterial.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tbtipomaterial_tb_composicao_kit_materials')
    tb_tipo_material1 = db.relationship('TbTipoMaterial', primaryjoin='TbComposicaoKitMaterial.tip_co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tbtipomaterial_tb_composicao_kit_materials_0')



class TbComunicacao(db.Model):
    __tablename__ = 'tb_comunicacao'
    __table_args__ = (
        db.Index('in_comunicacao_dtrefbusaticonchrlibcanc', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_hr_lib_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_dthrcanccoseqmotcon', 'dt_hr_cancelamento', 'co_seq_mot_comunicacao'),
        db.Index('in_comunicacao_mot_coseqrecep', 'co_seq_recep_amostra', 'co_seq_mot_comunicacao'),
        db.Index('in_comunicacao_coseqpes_coseqprov_dthrcon_dthrlib_dthrconc', 'co_seq_pessoa', 'co_seq_providencia', 'dt_hr_lib_comunicacao', 'dt_hr_conclusao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_dthrcanccoseqprovcon', 'dt_hr_cancelamento', 'co_seq_providencia'),
        db.Index('in_comunicacao_provdthrconccanc', 'co_seq_providencia', 'dt_hr_conclusao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_coseqpesconcdthrlibcanc', 'co_seq_pessoa', 'dt_hr_conclusao', 'dt_hr_lib_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_mot_coseqrecep_dthrcanc', 'co_seq_recep_amostra', 'co_seq_mot_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_dthrlibcanc', 'dt_hr_cancelamento', 'dt_lib_comunicacao'),
        db.Index('in_comunicacao_dthrconccanc', 'dt_hr_conclusao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_motdthrconccanc', 'co_seq_mot_comunicacao', 'dt_hr_conclusao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_coprov_dtrefbusati_dthrcon_dthrcanc', 'co_seq_providencia', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_dtlib_dthrcanc_dthrreg', 'dt_hr_cancelamento', 'dt_lib_comunicacao', 'dt_hr_registro'),
        db.Index('in_comunicacao_dtlibcanc', 'dt_hr_cancelamento', 'dt_hr_lib_comunicacao'),
        db.Index('in_comunicacao_coprov_dtrefbusati_dthrcon_dthrcanc_copes', 'co_seq_providencia', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_hr_cancelamento', 'co_seq_pessoa'),
        db.Index('in_comunicacao_coseqpesconclibcanc', 'co_seq_pessoa', 'dt_hr_conclusao', 'dt_lib_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_coprov_dtrefbusati_dthrcon_dthrcanc_copes_dthrca', 'co_seq_providencia', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_hr_cancelamento', 'co_seq_pessoa', 'dt_hr_cancelamento_busca'),
        db.Index('in_comunicacao_coseqpes_dtregbusativ_dthrcon_dthrlib_dthrconc', 'co_seq_pessoa', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_hr_lib_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_dtlib_dthrcanc_dthrreg_dtemis', 'dt_hr_cancelamento', 'dt_lib_comunicacao', 'dt_hr_registro', 'dt_emissao'),
        db.Index('in_comunicacao_coseqpes_dtregbusativ_dthrcon_dtlib_dthrconc', 'co_seq_pessoa', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_lib_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_dtrefbusaticonclibcanc', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_lib_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comunicacao_coprov_dtrefbusati_dthrcon_dthrcanc_dthrcancbusc', 'co_seq_providencia', 'dt_referencia_busca_ativa', 'dt_hr_conclusao', 'dt_hr_cancelamento', 'dt_hr_cancelamento_busca')
    )

    co_seq_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_comunicacao = db.Column(db.ForeignKey('tb_tipo_comunicacao.co_seq_tp_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_canc_comunicacao = db.Column(db.ForeignKey('tb_motivo_cancelamento_comunicar.co_seq_mot_canc_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_emissao = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_lib_comunicacao = db.Column(db.Numeric(8, 0), index=True)
    dt_hr_lib_comunicacao = db.Column(db.Numeric(14, 0), index=True)
    aut_lib_comunicacao = db.Column(db.String(20))
    obs_comunicacao = db.Column(db.String(2000))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0), index=True)
    aut_conclusao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_referencia_busca_ativa = db.Column(db.Numeric(8, 0), index=True)
    dt_hr_cancelamento_busca = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento_busca = db.Column(db.String(20))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbComunicacao.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_comunicacaos')
    tb_motivo_cancelamento_comunicar = db.relationship('TbMotivoCancelamentoComunicar', primaryjoin='TbComunicacao.co_seq_mot_canc_comunicacao == TbMotivoCancelamentoComunicar.co_seq_mot_canc_comunicacao', backref='tb_comunicacaos')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbComunicacao.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_comunicacaos')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbComunicacao.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_comunicacaos')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbComunicacao.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_comunicacaos')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbComunicacao.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_comunicacaos')
    tb_tipo_comunicacao = db.relationship('TbTipoComunicacao', primaryjoin='TbComunicacao.co_seq_tp_comunicacao == TbTipoComunicacao.co_seq_tp_comunicacao', backref='tb_comunicacaos')



class TbComunicacaoAgendamento(db.Model):
    __tablename__ = 'tb_comunicacao_agendamento'

    co_seq_comunicacao_agen = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_medicamento = db.Column(db.ForeignKey('tb_medicamento.co_seq_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_dia_agendamento = db.Column(db.Numeric(4, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbComunicacaoAgendamento.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_comunicacao_agendamentoes')
    tb_medicamento = db.relationship('TbMedicamento', primaryjoin='TbComunicacaoAgendamento.co_seq_medicamento == TbMedicamento.co_seq_medicamento', backref='tb_comunicacao_agendamentoes')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbComunicacaoAgendamento.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_comunicacao_agendamentoes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbComunicacaoAgendamento.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_comunicacao_agendamentoes')



class TbComunicacaoAutomatica(db.Model):
    __tablename__ = 'tb_comunicacao_automatica'

    co_seq_comunicacao_automatica = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_origem_comunicacao = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoAutomatica.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_automaticas')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbComunicacaoAutomatica.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_comunicacao_automaticas')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbComunicacaoAutomatica.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_comunicacao_automaticas')



class TbComunicacaoDoenca(db.Model):
    __tablename__ = 'tb_comunicacao_doenca'
    __table_args__ = (
        db.Index('in_comdoe_coseqcom_coseqdoe', 'co_seq_comunicacao', 'co_seq_doenca'),
    )

    co_seq_comunicacao_doenca = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoDoenca.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_doencas')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbComunicacaoDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_comunicacao_doencas')



class TbComunicacaoImportadaOnline(db.Model):
    __tablename__ = 'tb_comunicacao_importada_online'

    co_seq_comunicacao_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoImportadaOnline.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_importada_onlines')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbComunicacaoImportadaOnline.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_comunicacao_importada_onlines')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbComunicacaoImportadaOnline.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_comunicacao_importada_onlines')



class TbComunicacaoOrigem(db.Model):
    __tablename__ = 'tb_comunicacao_origem'

    co_seq_comunicacao_origem = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao_tipo_exame = db.Column(db.ForeignKey('tb_comunicacao_tipo_exame.co_seq_comunicacao_tipo_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_comunicacao_doenca = db.Column(db.ForeignKey('tb_comunicacao_doenca.co_seq_comunicacao_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_origem_comunicacao = db.Column(db.Numeric(14, 0), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoOrigem.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_origems')
    tb_comunicacao_doenca = db.relationship('TbComunicacaoDoenca', primaryjoin='TbComunicacaoOrigem.co_seq_comunicacao_doenca == TbComunicacaoDoenca.co_seq_comunicacao_doenca', backref='tb_comunicacao_origems')
    tb_comunicacao_tipo_exame = db.relationship('TbComunicacaoTipoExame', primaryjoin='TbComunicacaoOrigem.co_seq_comunicacao_tipo_exame == TbComunicacaoTipoExame.co_seq_comunicacao_tipo_exame', backref='tb_comunicacao_origems')



class TbComunicacaoPortaSerial(db.Model):
    __tablename__ = 'tb_comunicacao_porta_serial'

    co_seq_com_porta_serial = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0))
    ide_linha_processada = db.Column(db.String(1), nullable=False)
    ds_linha = db.Column(db.String(1000), nullable=False)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbComunicacaoPortaSerial.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_comunicacao_porta_serials')



class TbComunicacaoResGenetica(db.Model):
    __tablename__ = 'tb_comunicacao_res_genetica'

    co_seq_com_resultado_genetica = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_biologia_molecular = db.Column(db.ForeignKey('tb_resultado_biologia_molecular.co_seq_res_biologia_molecular', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoResGenetica.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_res_geneticas')
    tb_resultado_biologia_molecular = db.relationship('TbResultadoBiologiaMolecular', primaryjoin='TbComunicacaoResGenetica.co_seq_res_biologia_molecular == TbResultadoBiologiaMolecular.co_seq_res_biologia_molecular', backref='tb_comunicacao_res_geneticas')



class TbComunicacaoTipoExame(db.Model):
    __tablename__ = 'tb_comunicacao_tipo_exame'
    __table_args__ = (
        db.Index('in_comtpexa_coseqcom_dthrcanc', 'co_seq_comunicacao', 'dt_hr_cancelamento'),
        db.Index('in_comtpexa_coseqcom_coseqtpexa', 'co_seq_comunicacao', 'co_seq_tp_exame'),
        db.Index('in_comtpexa_coseqcom_coseqtpexa_dthrcanc', 'co_seq_comunicacao', 'co_seq_tp_exame', 'dt_hr_cancelamento')
    )

    co_seq_comunicacao_tipo_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoTipoExame.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_tipo_exames')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbComunicacaoTipoExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_comunicacao_tipo_exames')



class TbComunicacaoTipoMotivo(db.Model):
    __tablename__ = 'tb_comunicacao_tipo_motivo'

    co_seq_comunicacao_tp_mot = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_mot_comunicacao = db.Column(db.ForeignKey('tb_tipo_motivo_comunicacao.co_seq_tp_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_comunicacao_tp_mot = db.Column(db.String(200), nullable=False)
    obs_conclusao = db.Column(db.String(2000))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_conclusao_laboratorio = db.Column(db.Numeric(14, 0))
    autor_conclusao_laboratorio = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbComunicacaoTipoMotivo.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_comunicacao_tipo_motivoes')
    tb_tipo_motivo_comunicacao = db.relationship('TbTipoMotivoComunicacao', primaryjoin='TbComunicacaoTipoMotivo.co_seq_tp_mot_comunicacao == TbTipoMotivoComunicacao.co_seq_tp_mot_comunicacao', backref='tb_comunicacao_tipo_motivoes')



class TbComunicacaoTriagem(db.Model):
    __tablename__ = 'tb_comunicacao_triagem'
    __table_args__ = (
        db.Index('in_comtriagem_cotptriagem_dthrcanc', 'co_seq_tp_triagem_site', 'dt_hr_cancelamento_site'),
        db.Index('in_comtriagem_coseqrecepamo_coseqprov_dthrcanc', 'co_seq_recep_amostra_site', 'co_seq_providencia_site', 'dt_hr_cancelamento'),
        db.Index('in_comtriagem_cousa_coseqprov_dthrcanc', 'co_seq_unidade_saude_site', 'co_seq_providencia_site', 'dt_hr_cancelamento_site'),
        db.Index('in_comtriagem_cotptriagem_cousa', 'co_seq_tp_triagem_site', 'co_seq_unidade_saude_site'),
        db.Index('in_comtriagem_cousa_dthrcanc', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento_site'),
        db.Index('in_comtriagem_copes_dthrcanc_coprov_dtrefbusativ', 'co_seq_pessoa_site', 'dt_hr_cancelamento_site', 'co_seq_providencia_site', 'dt_referencia_busca_ativa')
    )

    co_seq_comunicacao_triagem = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao_site = db.Column(db.Numeric(8, 0), nullable=False)
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0), nullable=False, index=True)
    co_seq_recep_amostra_site = db.Column(db.Numeric(14, 0), index=True)
    co_seq_mot_comunicacao_site = db.Column(db.Numeric(4, 0))
    co_seq_providencia_site = db.Column(db.Numeric(4, 0))
    dt_emissao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_lib_comunicacao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_referencia_busca_ativa = db.Column(db.Numeric(8, 0), nullable=False)
    co_seq_tp_exame_site = db.Column(db.Numeric(5, 0))
    co_seq_doenca_site = db.Column(db.Numeric(4, 0))
    ds_providencia = db.Column(db.String(80))
    ds_tp_exame = db.Column(db.String(100))
    ds_mot_comunicacao = db.Column(db.String(40))
    no_doenca = db.Column(db.String(50))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento_site = db.Column(db.Numeric(14, 0), index=True)
    co_seq_tp_triagem_site = db.Column(db.Numeric(2, 0), index=True)
    dt_resultado = db.Column(db.Numeric(8, 0))
    tex_referencia_res = db.Column(db.String(2000))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    res_impresso = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    dt_rec_amostra = db.Column(db.Numeric(8, 0))
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    co_ent_pessoa_site = db.Column(db.String(20))
    no_pessoa = db.Column(db.String(80))
    ds_endereco_formatado = db.Column(db.String(200))
    no_municipio = db.Column(db.String(70))
    ds_tp_material = db.Column(db.String(200))
    no_unidade_saude = db.Column(db.String(100))
    ds_unidade_medida = db.Column(db.String(50))
    ds_tp_metodo = db.Column(db.String(80))
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), index=True)
    nu_telefone = db.Column(db.String(35))
    dt_nascimento = db.Column(db.Numeric(8, 0))
    ds_mot_inadequacao_site = db.Column(db.String(2000))
    dt_hr_visualizacao = db.Column(db.Numeric(14, 0))
    ds_pendencia_cadastro = db.Column(db.String(2000))



class TbConclusaoAtendimento(db.Model):
    __tablename__ = 'tb_conclusao_atendimento'

    co_seq_conclusao_atendimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_conclusao_atendimento = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbConclusaoMunicipio(db.Model):
    __tablename__ = 'tb_conclusao_municipio'

    co_seq_conclusao_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_conclusao_municipio = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbCondicaoMaterial(db.Model):
    __tablename__ = 'tb_condicao_material'

    co_seq_condicao_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_condicao_material = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbCondicaoMaterialSoro(db.Model):
    __tablename__ = 'tb_condicao_material_soro'

    co_seq_condicao_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_soro = db.Column(db.ForeignKey('tb_recepcao_amostra_soro.co_seq_recep_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_condicao_material = db.Column(db.ForeignKey('tb_condicao_material.co_seq_condicao_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_condicao_material = db.relationship('TbCondicaoMaterial', primaryjoin='TbCondicaoMaterialSoro.co_seq_condicao_material == TbCondicaoMaterial.co_seq_condicao_material', backref='tb_condicao_material_soroes')
    tb_recepcao_amostra_soro = db.relationship('TbRecepcaoAmostraSoro', primaryjoin='TbCondicaoMaterialSoro.co_seq_recep_soro == TbRecepcaoAmostraSoro.co_seq_recep_soro', backref='tb_condicao_material_soroes')



class TbCondicaoPacienteColeta(db.Model):
    __tablename__ = 'tb_condicao_paciente_coleta'

    co_seq_condicao_pac_coleta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.Numeric(14, 0), nullable=False)
    ide_uso_antibiotico = db.Column(db.String(1))
    ds_antibiotico_uso = db.Column(db.String(200))
    ide_uso_corticoide = db.Column(db.String(1))
    dt_ini_uso_corticoide = db.Column(db.Numeric(8, 0))
    dt_ter_uso_corticoide = db.Column(db.Numeric(8, 0))
    ds_corticoide_uso = db.Column(db.String(200))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbCondutaConsulta(db.Model):
    __tablename__ = 'tb_conduta_consulta'

    co_seq_conduta_consulta = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_conduta_consulta = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1), nullable=False)



class TbCondutaTecnicoResultado(db.Model):
    __tablename__ = 'tb_conduta_tecnico_resultado'

    co_seq_conduta_tecnico = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_conduta_tecnico_res = db.Column(db.String(200), nullable=False)
    ds_smp_conduta_tecnico_res = db.Column(db.String(20), nullable=False)



class TbConferenciaAmostraPicotador(db.Model):
    __tablename__ = 'tb_conferencia_amostra_picotador'

    co_seq_conferencia_picotador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_ent_pessoa_envelope = db.Column(db.String(20), nullable=False)
    ide_co_conflito_envelope = db.Column(db.String(1), nullable=False)
    co_ent_pessoa_amostra = db.Column(db.String(20), nullable=False)
    ide_co_conflito_amostra = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbConferenciaAmostraPicotador.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_conferencia_amostra_picotadors')



class TbConferenciaDigitacaoAmostra(db.Model):
    __tablename__ = 'tb_conferencia_digitacao_amostra'

    co_seq_conferencia_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbConferenciaDigitacaoAmostra.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_conferencia_digitacao_amostras')



class TbConferenciaSoroControle(db.Model):
    __tablename__ = 'tb_conferencia_soro_controle'

    co_seq_conferencia_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_soro = db.Column(db.ForeignKey('tb_amostra_soro.co_seq_amostra_soro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_conduta_soro = db.Column(db.ForeignKey('tb_tipo_conduta_soro.co_seq_tp_conduta_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_res_outro_laboratorio = db.Column(db.ForeignKey('tb_resultado_outro_laboratorio.co_seq_res_outro_laboratorio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    tex_repasse_res = db.Column(db.String(4000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_envio_carta_mae = db.Column(db.String(1))
    ide_fax_medico = db.Column(db.String(1))
    dt_contato_mae = db.Column(db.Numeric(8, 0))
    dt_contato_medico = db.Column(db.Numeric(8, 0))
    ds_conduta_alteracao_dose = db.Column(db.String(1))
    dt_referencia = db.Column(db.Numeric(8, 0))

    tb_amostra_soro = db.relationship('TbAmostraSoro', primaryjoin='TbConferenciaSoroControle.co_seq_amostra_soro == TbAmostraSoro.co_seq_amostra_soro', backref='tb_conferencia_soro_controles')
    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbConferenciaSoroControle.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_conferencia_soro_controles')
    tb_resultado_outro_laboratorio = db.relationship('TbResultadoOutroLaboratorio', primaryjoin='TbConferenciaSoroControle.co_seq_res_outro_laboratorio == TbResultadoOutroLaboratorio.co_seq_res_outro_laboratorio', backref='tb_conferencia_soro_controles')
    tb_tipo_conduta_soro = db.relationship('TbTipoCondutaSoro', primaryjoin='TbConferenciaSoroControle.co_seq_tp_conduta_soro == TbTipoCondutaSoro.co_seq_tp_conduta_soro', backref='tb_conferencia_soro_controles')



class TbConfiguracaoAmostraPlaca(db.Model):
    __tablename__ = 'tb_configuracao_amostra_placa'

    co_seq_conf_amostra_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_conf_placa = db.Column(db.ForeignKey('tb_configuracao_placa.co_seq_conf_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_pos_placa = db.Column(db.ForeignKey('tb_tipo_posicao_placa.co_seq_tp_pos_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_lin_placa = db.Column(db.Numeric(3, 0), nullable=False)
    nu_col_placa = db.Column(db.Numeric(3, 0), nullable=False)
    ide_arq_ret_placa = db.Column(db.String(1), nullable=False)
    ide_arq_ent_placa = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_configuracao_placa = db.relationship('TbConfiguracaoPlaca', primaryjoin='TbConfiguracaoAmostraPlaca.co_seq_conf_placa == TbConfiguracaoPlaca.co_seq_conf_placa', backref='tb_configuracao_amostra_placas')
    tb_tipo_posicao_placa = db.relationship('TbTipoPosicaoPlaca', primaryjoin='TbConfiguracaoAmostraPlaca.co_seq_tp_pos_placa == TbTipoPosicaoPlaca.co_seq_tp_pos_placa', backref='tb_configuracao_amostra_placas')



class TbConfiguracaoPlaca(db.Model):
    __tablename__ = 'tb_configuracao_placa'

    co_seq_conf_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_conf_placa = db.Column(db.Numeric(2, 0), nullable=False)
    nu_lin_placa = db.Column(db.Numeric(3, 0), nullable=False)
    nu_col_placa = db.Column(db.Numeric(3, 0), nullable=False)
    ide_leitura_linha_coluna = db.Column(db.String(1), nullable=False)
    ide_co_duplicado = db.Column(db.String(1), nullable=False)
    ide_work_list_placa = db.Column(db.String(1), nullable=False)
    nu_repeticao_amostra_placa = db.Column(db.Numeric(2, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbConfiguracaoPlaca.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_configuracao_placas')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbConfiguracaoPlaca.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_configuracao_placas')



class TbConselhoTutelar(db.Model):
    __tablename__ = 'tb_conselho_tutelar'

    co_seq_conselho_tutelar = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_conselho_tutelar = db.Column(db.String(70), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    no_bairro = db.Column(db.String(80), nullable=False)
    co_seq_municipio_endereco = db.Column(db.Numeric(8, 0), nullable=False)
    no_contato = db.Column(db.String(70), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_celular = db.Column(db.String(20), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    no_responsavel = db.Column(db.String(70), nullable=False)
    ds_email_responsavel = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbConselhoTutelar.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_conselho_tutelars')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbConselhoTutelar.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_conselho_tutelars')



class TbConsorcio(db.Model):
    __tablename__ = 'tb_consorcio'

    co_seq_consorcio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_ext_consorcio = db.Column(db.String(20), nullable=False)
    no_consorcio = db.Column(db.String(70), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20), nullable=False)
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_fax = db.Column(db.String(35), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbConsorcio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_consorcios')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbConsorcio.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_consorcios')



class TbConsulta(db.Model):
    __tablename__ = 'tb_consulta'

    co_seq_consulta = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_agendamento_consulta = db.Column(db.ForeignKey('tb_agendamento_consulta.co_seq_agendamento_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_diagnostico_consulta = db.Column(db.ForeignKey('tb_diagnostico_consulta.co_seq_diagnostico_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_conduta_consulta = db.Column(db.ForeignKey('tb_conduta_consulta.co_seq_conduta_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_consulta = db.Column(db.Numeric(8, 0), nullable=False)
    dt_proxima_consulta = db.Column(db.Numeric(8, 0))
    obs_consulta = db.Column(db.String(2000))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    ide_consulta_concluida = db.Column(db.String(1))
    hr_proxima_consulta = db.Column(db.String(6))
    ds_outro_diagnostico = db.Column(db.String(50))
    ide_primeira_consulta = db.Column(db.String(1))
    ide_diagnostico_confirmado = db.Column(db.String(1))

    tb_agendamento_consulta = db.relationship('TbAgendamentoConsulta', primaryjoin='TbConsulta.co_seq_agendamento_consulta == TbAgendamentoConsulta.co_seq_agendamento_consulta', backref='tb_consultas')
    tb_conduta_consulta = db.relationship('TbCondutaConsulta', primaryjoin='TbConsulta.co_seq_conduta_consulta == TbCondutaConsulta.co_seq_conduta_consulta', backref='tb_consultas')
    tb_diagnostico_consulta = db.relationship('TbDiagnosticoConsulta', primaryjoin='TbConsulta.co_seq_diagnostico_consulta == TbDiagnosticoConsulta.co_seq_diagnostico_consulta', backref='tb_consultas')
    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbConsulta.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_consultas')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbConsulta.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_consultas')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbConsulta.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_consultas')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbConsulta.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_consultas')



class TbConsultaAmbulatorio(db.Model):
    __tablename__ = 'tb_consulta_ambulatorio'

    co_seq_consulta_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_status_consulta_amb = db.Column(db.ForeignKey('tb_status_consulta_ambulatorial.co_seq_status_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_agendamento_consulta = db.Column(db.ForeignKey('tb_agendamento_consulta.co_seq_agendamento_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_especialidade = db.Column(db.ForeignKey('tb_especialidade.co_seq_especialidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_consulta = db.Column(db.Numeric(8, 0), nullable=False)
    dt_proxima_consulta = db.Column(db.Numeric(8, 0))
    hr_proxima_consulta = db.Column(db.String(6))
    obs_consulta = db.Column(db.String(2000))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    ide_consulta_centro_ref = db.Column(db.String(1))

    tb_agendamento_consulta = db.relationship('TbAgendamentoConsulta', primaryjoin='TbConsultaAmbulatorio.co_seq_agendamento_consulta == TbAgendamentoConsulta.co_seq_agendamento_consulta', backref='tb_consulta_ambulatorios')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbConsultaAmbulatorio.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_consulta_ambulatorios')
    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbConsultaAmbulatorio.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_consulta_ambulatorios')
    tb_especialidade = db.relationship('TbEspecialidade', primaryjoin='TbConsultaAmbulatorio.co_seq_especialidade == TbEspecialidade.co_seq_especialidade', backref='tb_consulta_ambulatorios')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbConsultaAmbulatorio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_consulta_ambulatorios')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbConsultaAmbulatorio.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_consulta_ambulatorios')
    tb_status_consulta_ambulatorial = db.relationship('TbStatusConsultaAmbulatorial', primaryjoin='TbConsultaAmbulatorio.co_seq_status_consulta_amb == TbStatusConsultaAmbulatorial.co_seq_status_consulta_amb', backref='tb_consulta_ambulatorios')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbConsultaAmbulatorio.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_consulta_ambulatorios')



class TbConsultaColuna(db.Model):
    __tablename__ = 'tb_consulta_coluna'

    co_seq_consulta_coluna = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_coluna_consulta = db.Column(db.ForeignKey('tb_coluna_consulta.co_seq_coluna_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_registro_lin_con = db.Column(db.Numeric(14, 0))
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_consulta = db.relationship('TbColunaConsulta', primaryjoin='TbConsultaColuna.co_seq_coluna_consulta == TbColunaConsulta.co_seq_coluna_consulta', backref='tb_consulta_colunas')
    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbConsultaColuna.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_consulta_colunas')



class TbConsultaColunaAmbulatorial(db.Model):
    __tablename__ = 'tb_consulta_coluna_ambulatorial'

    co_seq_consulta_coluna_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_consulta_amb = db.Column(db.ForeignKey('tb_consulta_ambulatorio.co_seq_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_col_item_consulta_amb = db.Column(db.ForeignKey('tb_coluna_item_consulta_amb.co_seq_col_item_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_item_ficha_amb = db.Column(db.ForeignKey('tb_item_ficha_ambulatorial.co_seq_item_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_coluna_consulta_amb = db.Column(db.ForeignKey('tb_coluna_consulta_ambulatorial.co_seq_coluna_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_registro_lin_con = db.Column(db.Numeric(14, 0))
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    cont_col_texto_longo = db.Column(db.Text)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_item_consulta_amb = db.relationship('TbColunaItemConsultaAmb', primaryjoin='TbConsultaColunaAmbulatorial.co_seq_col_item_consulta_amb == TbColunaItemConsultaAmb.co_seq_col_item_consulta_amb', backref='tb_consulta_coluna_ambulatorials')
    tb_coluna_consulta_ambulatorial = db.relationship('TbColunaConsultaAmbulatorial', primaryjoin='TbConsultaColunaAmbulatorial.co_seq_coluna_consulta_amb == TbColunaConsultaAmbulatorial.co_seq_coluna_consulta_amb', backref='tb_consulta_coluna_ambulatorials')
    tb_consulta_ambulatorio = db.relationship('TbConsultaAmbulatorio', primaryjoin='TbConsultaColunaAmbulatorial.co_seq_consulta_amb == TbConsultaAmbulatorio.co_seq_consulta_amb', backref='tb_consulta_coluna_ambulatorials')
    tb_item_ficha_ambulatorial = db.relationship('TbItemFichaAmbulatorial', primaryjoin='TbConsultaColunaAmbulatorial.co_seq_item_ficha_amb == TbItemFichaAmbulatorial.co_seq_item_ficha_amb', backref='tb_consulta_coluna_ambulatorials')



class TbConsultaColunaItemAmb(db.Model):
    __tablename__ = 'tb_consulta_coluna_item_amb'

    co_seq_consulta_col_item_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_col_item_consulta_amb = db.Column(db.ForeignKey('tb_coluna_item_consulta_amb.co_seq_col_item_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta_coluna_amb = db.Column(db.ForeignKey('tb_consulta_coluna_ambulatorial.co_seq_consulta_coluna_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_item_consulta_amb = db.relationship('TbColunaItemConsultaAmb', primaryjoin='TbConsultaColunaItemAmb.co_seq_col_item_consulta_amb == TbColunaItemConsultaAmb.co_seq_col_item_consulta_amb', backref='tb_consulta_coluna_item_ambs')
    tb_consulta_coluna_ambulatorial = db.relationship('TbConsultaColunaAmbulatorial', primaryjoin='TbConsultaColunaItemAmb.co_seq_consulta_coluna_amb == TbConsultaColunaAmbulatorial.co_seq_consulta_coluna_amb', backref='tb_consulta_coluna_item_ambs')



class TbConsultaDesdobramentoItem(db.Model):
    __tablename__ = 'tb_consulta_desdobramento_item'

    co_seq_consulta_desd_item_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_desd_item_consulta_amb = db.Column(db.ForeignKey('tb_desdobramento_item_consulta.co_seq_desd_item_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta_col_item_amb = db.Column(db.ForeignKey('tb_consulta_coluna_item_amb.co_seq_consulta_col_item_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_consulta_coluna_item_amb = db.relationship('TbConsultaColunaItemAmb', primaryjoin='TbConsultaDesdobramentoItem.co_seq_consulta_col_item_amb == TbConsultaColunaItemAmb.co_seq_consulta_col_item_amb', backref='tb_consulta_desdobramento_items')
    tb_desdobramento_item_consulta = db.relationship('TbDesdobramentoItemConsulta', primaryjoin='TbConsultaDesdobramentoItem.co_seq_desd_item_consulta_amb == TbDesdobramentoItemConsulta.co_seq_desd_item_consulta_amb', backref='tb_consulta_desdobramento_items')



class TbContato(db.Model):
    __tablename__ = 'tb_contato'
    __table_args__ = (
        db.Index('in_cont_dthrcanc_comotcontnaoefet', 'dt_hr_cancelamento', 'co_mot_contato_nao_efetivado'),
    )

    co_seq_contato = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_mot_contato_nao_efetivado = db.Column(db.ForeignKey('tb_motivo_contato_nao_efetivado.co_mot_contato_nao_efetivado', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_contato = db.Column(db.ForeignKey('tb_motivo_contato.co_seq_mot_contato', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_demanda = db.Column(db.ForeignKey('tb_motivo_demanda_espontanea.co_seq_mot_demanda', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_contato = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    obs_contato = db.Column(db.String(8000), nullable=False)
    ide_contato_nao_efetivado = db.Column(db.String(1), nullable=False)
    no_profissao = db.Column(db.String(100))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False, index=True)
    ide_contato_email = db.Column(db.String(1), nullable=False)
    ide_contato_site = db.Column(db.String(1), nullable=False)
    ide_contato_resposta_site = db.Column(db.String(1))
    dt_hr_visualizacao = db.Column(db.Numeric(14, 0))
    aut_visualizacao = db.Column(db.String(20))
    ide_contato_whatsapp = db.Column(db.String(1))

    tb_motivo_contato_nao_efetivado = db.relationship('TbMotivoContatoNaoEfetivado', primaryjoin='TbContato.co_mot_contato_nao_efetivado == TbMotivoContatoNaoEfetivado.co_mot_contato_nao_efetivado', backref='tb_contatoes')
    tb_motivo_contato = db.relationship('TbMotivoContato', primaryjoin='TbContato.co_seq_mot_contato == TbMotivoContato.co_seq_mot_contato', backref='tb_contatoes')
    tb_motivo_demanda_espontanea = db.relationship('TbMotivoDemandaEspontanea', primaryjoin='TbContato.co_seq_mot_demanda == TbMotivoDemandaEspontanea.co_seq_mot_demanda', backref='tb_contatoes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbContato.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_contatoes')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbContato.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_contatoes')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbContato.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_contatoes')



class TbContatoPessoa(db.Model):
    __tablename__ = 'tb_contato_pessoa'

    co_seq_contato_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_contato = db.Column(db.ForeignKey('tb_tipo_contato.co_seq_tp_contato', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_contato_pessoa = db.Column(db.String(200), nullable=False)
    obs_contato_pessoa = db.Column(db.String(70))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbContatoPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_contato_pessoas')
    tb_tipo_contato = db.relationship('TbTipoContato', primaryjoin='TbContatoPessoa.co_seq_tp_contato == TbTipoContato.co_seq_tp_contato', backref='tb_contato_pessoas')



class TbContatoSite(db.Model):
    __tablename__ = 'tb_contato_site'
    __table_args__ = (
        db.Index('in_contsite_copes_dtcont', 'co_seq_pessoa_site', 'dt_contato'),
    )

    co_seq_contato_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0), nullable=False, index=True)
    dt_contato = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    obs_contato = db.Column(db.String(8000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbControleAcessoPendencia(db.Model):
    __tablename__ = 'tb_controle_acesso_pendencia'

    co_seq_acesso_pendencia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_controle_tratamento = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_controle_busca_ativa = db.Column(db.String(1))

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbControleAcessoPendencia.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_controle_acesso_pendencias')



class TbControleAlerta(db.Model):
    __tablename__ = 'tb_controle_alerta'

    co_seq_controle_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_alerta = db.Column(db.String(2000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbControleAmostraSoro(db.Model):
    __tablename__ = 'tb_controle_amostra_soro'

    co_seq_controle_amostra_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_temperatura_refrigerado = db.Column(db.Numeric(14, 5))
    vr_temperatura_congelado = db.Column(db.Numeric(14, 5))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_lote = db.Column(db.String(30))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbControleAmostraSoro.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_controle_amostra_soroes')



class TbControleCodigoUnidade(db.Model):
    __tablename__ = 'tb_controle_codigo_unidade'

    co_seq_controle_co_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_reempressao = db.Column(db.String(1), nullable=False)
    qt_etiqueta = db.Column(db.Numeric(8, 0), nullable=False)
    co_inicio = db.Column(db.Numeric(14, 0))
    co_termino = db.Column(db.Numeric(14, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbControleCodigoUnidade.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_controle_codigo_unidades')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbControleCodigoUnidade.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_controle_codigo_unidades')



class TbControleExecucaoGuardiao(db.Model):
    __tablename__ = 'tb_controle_execucao_guardiao'

    co_seq_execucao_guardiao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_execucao_guardiao = db.Column(db.ForeignKey('tb_tipo_execucao_guardiao.co_seq_tp_execucao_guardiao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_programacao_guardiao = db.Column(db.ForeignKey('tb_programacao_guardiao.co_seq_programacao_guardiao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ide_execucao_manual = db.Column(db.String(1), nullable=False)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_erro_execucao = db.Column(db.String(1))

    tb_programacao_guardiao = db.relationship('TbProgramacaoGuardiao', primaryjoin='TbControleExecucaoGuardiao.co_seq_programacao_guardiao == TbProgramacaoGuardiao.co_seq_programacao_guardiao', backref='tb_controle_execucao_guardiaos')
    tb_tipo_execucao_guardiao = db.relationship('TbTipoExecucaoGuardiao', primaryjoin='TbControleExecucaoGuardiao.co_seq_tp_execucao_guardiao == TbTipoExecucaoGuardiao.co_seq_tp_execucao_guardiao', backref='tb_controle_execucao_guardiaos')



class TbControlePlaca(db.Model):
    __tablename__ = 'tb_controle_placa'

    co_seq_reg_controle_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_arq_res_placa = db.Column(db.ForeignKey('tb_arquivo_resultado_placa.co_seq_arq_res_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_seq_placa = db.Column(db.ForeignKey('tb_placa.nu_seq_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0))

    tb_arquivo_resultado_placa = db.relationship('TbArquivoResultadoPlaca', primaryjoin='TbControlePlaca.co_seq_arq_res_placa == TbArquivoResultadoPlaca.co_seq_arq_res_placa', backref='tb_controle_placas')
    tb_placa = db.relationship('TbPlaca', primaryjoin='TbControlePlaca.nu_seq_placa == TbPlaca.nu_seq_placa', backref='tb_controle_placas')



class TbControlePlacaManual(db.Model):
    __tablename__ = 'tb_controle_placa_manual'

    co_seq_controle_placa_manual = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_conf_amostra_placa = db.Column(db.ForeignKey('tb_configuracao_amostra_placa.co_seq_conf_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_placa = db.Column(db.ForeignKey('tb_numero_placa.nu_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_seq_placa = db.Column(db.ForeignKey('tb_placa.nu_seq_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_pos_placa = db.Column(db.ForeignKey('tb_tipo_posicao_placa.co_seq_tp_pos_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_contole = db.Column(db.String(50), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_configuracao_amostra_placa = db.relationship('TbConfiguracaoAmostraPlaca', primaryjoin='TbControlePlacaManual.co_seq_conf_amostra_placa == TbConfiguracaoAmostraPlaca.co_seq_conf_amostra_placa', backref='tb_controle_placa_manuals')
    tb_tipo_posicao_placa = db.relationship('TbTipoPosicaoPlaca', primaryjoin='TbControlePlacaManual.co_seq_tp_pos_placa == TbTipoPosicaoPlaca.co_seq_tp_pos_placa', backref='tb_controle_placa_manuals')
    tb_numero_placa = db.relationship('TbNumeroPlaca', primaryjoin='TbControlePlacaManual.nu_placa == TbNumeroPlaca.nu_placa', backref='tb_controle_placa_manuals')
    tb_placa = db.relationship('TbPlaca', primaryjoin='TbControlePlacaManual.nu_seq_placa == TbPlaca.nu_seq_placa', backref='tb_controle_placa_manuals')



class TbControleQualidadeExterno(db.Model):
    __tablename__ = 'tb_controle_qualidade_externo'

    co_seq_controle_externo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    dt_emissao = db.Column(db.Numeric(8, 0))
    dt_rec_amostra = db.Column(db.Numeric(8, 0), nullable=False)
    ds_analise_critica = db.Column(db.String(2000))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))



class TbControleSistemaPicotador(db.Model):
    __tablename__ = 'tb_controle_sistema_picotador'

    co_seq_controle_sis_picotador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_pos_placa = db.Column(db.ForeignKey('tb_tipo_posicao_placa.co_seq_tp_pos_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_controle_picotador = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_posicao_placa = db.relationship('TbTipoPosicaoPlaca', primaryjoin='TbControleSistemaPicotador.co_seq_tp_pos_placa == TbTipoPosicaoPlaca.co_seq_tp_pos_placa', backref='tb_controle_sistema_picotadors')



class TbConvenio(db.Model):
    __tablename__ = 'tb_convenio'

    co_seq_convenio = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_convenio = db.Column(db.String(50), nullable=False)
    ide_fora_triagem = db.Column(db.String(1), nullable=False)



class TbCuti(db.Model):
    __tablename__ = 'tb_cutis'

    co_seq_cutis = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_cutis = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbDescentralizacaoMunicipio(db.Model):
    __tablename__ = 'tb_descentralizacao_municipio'

    co_seq_descentralizacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_descentralizacao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_canc_descentralizacao = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbDescentralizacaoMunicipio.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_descentralizacao_municipios')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbDescentralizacaoMunicipio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_descentralizacao_municipios')



class TbDescricaoMotivoInadequacao(db.Model):
    __tablename__ = 'tb_descricao_motivo_inadequacao'

    co_seq_ds_mot_inadequacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_mot_inadequacao = db.Column(db.ForeignKey('tb_motivo_inadequacao.co_mot_inadequacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_comp_mot_inadequacao = db.Column(db.String(2000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_inadequacao = db.relationship('TbMotivoInadequacao', primaryjoin='TbDescricaoMotivoInadequacao.co_mot_inadequacao == TbMotivoInadequacao.co_mot_inadequacao', backref='tb_descricao_motivo_inadequacaos')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbDescricaoMotivoInadequacao.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_descricao_motivo_inadequacaos')



class TbDesdobramentoItemConsulta(db.Model):
    __tablename__ = 'tb_desdobramento_item_consulta'

    co_seq_desd_item_consulta_amb = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    co_seq_col_item_consulta_amb = db.Column(db.ForeignKey('tb_coluna_item_consulta_amb.co_seq_col_item_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_desd_item_consulta_amb = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_item_consulta_amb = db.relationship('TbColunaItemConsultaAmb', primaryjoin='TbDesdobramentoItemConsulta.co_seq_col_item_consulta_amb == TbColunaItemConsultaAmb.co_seq_col_item_consulta_amb', backref='tb_desdobramento_item_consultas')



class TbDesdobramentoItemPaciente(db.Model):
    __tablename__ = 'tb_desdobramento_item_paciente'

    co_seq_desd_item_paciente_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_col_item_paciente_amb = db.Column(db.ForeignKey('tb_coluna_item_paciente_amb.co_seq_col_item_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_desd_item_paciente_amb = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_item_paciente_amb = db.relationship('TbColunaItemPacienteAmb', primaryjoin='TbDesdobramentoItemPaciente.co_seq_col_item_paciente_amb == TbColunaItemPacienteAmb.co_seq_col_item_paciente_amb', backref='tb_desdobramento_item_pacientes')



class TbDiagnosticoConsulta(db.Model):
    __tablename__ = 'tb_diagnostico_consulta'

    co_seq_diagnostico_consulta = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_diagnostico_consulta = db.Column(db.String(50), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_outro_diagnostico = db.Column(db.String(1), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbDiagnosticoConsulta.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_diagnostico_consultas')



class TbDiretorioGeral(db.Model):
    __tablename__ = 'tb_diretorio_geral'

    co_seq_diretorio_geral = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_diretorio = db.Column(db.ForeignKey('tb_tipo_diretorio.co_seq_tp_diretorio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_diretorio = db.Column(db.String(300), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_diretorio = db.relationship('TbTipoDiretorio', primaryjoin='TbDiretorioGeral.co_seq_tp_diretorio == TbTipoDiretorio.co_seq_tp_diretorio', backref='tb_diretorio_gerals')



class TbDistrito(db.Model):
    __tablename__ = 'tb_distrito'

    co_seq_distrito = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_distrito = db.Column(db.String(70), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20), nullable=False)
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    no_contato = db.Column(db.String(70), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_fax = db.Column(db.String(35), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    obs_distrito = db.Column(db.String(2000), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbDistrito.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_distritoes')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbDistrito.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_distritoes')



class TbDocumentoAnexoMunicipio(db.Model):
    __tablename__ = 'tb_documento_anexo_municipio'

    co_seq_doc_anexo_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_arq = db.Column(db.ForeignKey('tb_tipo_arquivo.co_seq_tp_arq', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_doc_anexo = db.Column(db.String(100), nullable=False)
    ds_doc_anexo = db.Column(db.String(100), nullable=False)
    doc_anexo = db.Column(db.LargeBinary, nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbDocumentoAnexoMunicipio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_documento_anexo_municipios')
    tb_tipo_arquivo = db.relationship('TbTipoArquivo', primaryjoin='TbDocumentoAnexoMunicipio.co_seq_tp_arq == TbTipoArquivo.co_seq_tp_arq', backref='tb_documento_anexo_municipios')



class TbDocumentoAnexoPessoa(db.Model):
    __tablename__ = 'tb_documento_anexo_pessoa'

    co_seq_doc_anexo_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_arq = db.Column(db.ForeignKey('tb_tipo_arquivo.co_seq_tp_arq', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_doc_anexo = db.Column(db.String(100), nullable=False)
    ds_doc_anexo = db.Column(db.String(100), nullable=False)
    doc_anexo = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbDocumentoAnexoPessoa.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_documento_anexo_pessoas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbDocumentoAnexoPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_documento_anexo_pessoas')
    tb_tipo_arquivo = db.relationship('TbTipoArquivo', primaryjoin='TbDocumentoAnexoPessoa.co_seq_tp_arq == TbTipoArquivo.co_seq_tp_arq', backref='tb_documento_anexo_pessoas')



class TbDocumentoAnexoUnidade(db.Model):
    __tablename__ = 'tb_documento_anexo_unidade'

    co_seq_doc_anexo_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_arq = db.Column(db.ForeignKey('tb_tipo_arquivo.co_seq_tp_arq', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_doc_anexo = db.Column(db.String(100), nullable=False)
    ds_doc_anexo = db.Column(db.String(100), nullable=False)
    doc_anexo = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_arquivo = db.relationship('TbTipoArquivo', primaryjoin='TbDocumentoAnexoUnidade.co_seq_tp_arq == TbTipoArquivo.co_seq_tp_arq', backref='tb_documento_anexo_unidades')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbDocumentoAnexoUnidade.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_documento_anexo_unidades')



class TbDoenca(db.Model):
    __tablename__ = 'tb_doenca'

    co_seq_doenca = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    no_doenca = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    doe_co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca'), index=True)
    ds_doenca_analisada = db.Column(db.String(2000))
    ds_obs_laudo = db.Column(db.String(2000))
    co_seq_grupo_caract_doenca = db.Column(db.ForeignKey('tb_grupo_caracteristica_doenca.co_seq_grupo_caract_doenca'), index=True)

    tb_grupo_caracteristica_doenca = db.relationship('TbGrupoCaracteristicaDoenca', primaryjoin='TbDoenca.co_seq_grupo_caract_doenca == TbGrupoCaracteristicaDoenca.co_seq_grupo_caract_doenca', backref='tb_doencas')
    parent = db.relationship('TbDoenca', remote_side=[co_seq_doenca], primaryjoin='TbDoenca.doe_co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_doencas')



class TbDoencaCid(db.Model):
    __tablename__ = 'tb_doenca_cid'

    co_seq_doenca_cid = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_cid = db.Column(db.ForeignKey('tb_cid.co_seq_cid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_cid_contra_referencia = db.Column(db.String(1))

    tb_cid = db.relationship('TbCid', primaryjoin='TbDoencaCid.co_seq_cid == TbCid.co_seq_cid', backref='tb_doenca_cids')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbDoencaCid.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_doenca_cids')



class TbDoencaCidAlelo(db.Model):
    __tablename__ = 'tb_doenca_cid_alelo'

    co_seq_doenca_cid_alelo = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_doenca_cid = db.Column(db.ForeignKey('tb_doenca_cid.co_seq_doenca_cid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_alelo = db.Column(db.ForeignKey('tb_alelo.co_seq_alelo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_alelo = db.relationship('TbAlelo', primaryjoin='TbDoencaCidAlelo.co_seq_alelo == TbAlelo.co_seq_alelo', backref='tb_doenca_cid_aleloes')
    tb_doenca_cid = db.relationship('TbDoencaCid', primaryjoin='TbDoencaCidAlelo.co_seq_doenca_cid == TbDoencaCid.co_seq_doenca_cid', backref='tb_doenca_cid_aleloes')



class TbDoencaPaciente(db.Model):
    __tablename__ = 'tb_doenca_paciente'
    __table_args__ = (
        db.Index('in_doepac_coseqpac_coseqdoe', 'co_seq_paciente', 'co_seq_doenca'),
    )

    co_seq_doenca_paciente = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_cid = db.Column(db.ForeignKey('tb_cid.co_seq_cid', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_paciente = db.Column(db.ForeignKey('tb_paciente.co_seq_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini_tratamento = db.Column(db.Numeric(8, 0))
    dt_alta_tratamento = db.Column(db.Numeric(8, 0))
    aut_alta_tratamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_prontuario = db.Column(db.String(20))
    nu_prontuario_antigo = db.Column(db.String(20))

    tb_cid = db.relationship('TbCid', primaryjoin='TbDoencaPaciente.co_seq_cid == TbCid.co_seq_cid', backref='tb_doenca_pacientes')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbDoencaPaciente.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_doenca_pacientes')
    tb_paciente = db.relationship('TbPaciente', primaryjoin='TbDoencaPaciente.co_seq_paciente == TbPaciente.co_seq_paciente', backref='tb_doenca_pacientes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbDoencaPaciente.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_doenca_pacientes')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbDoencaPaciente.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_doenca_pacientes')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbDoencaPaciente.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_doenca_pacientes')



class TbEctPai(db.Model):
    __tablename__ = 'tb_ect_pais'

    pai_sg = db.Column(db.String(2), primary_key=True, unique=True)
    pai_sg_alternativa = db.Column(db.String(3))
    pai_no_portugues = db.Column(db.String(72))
    pai_no_ingles = db.Column(db.String(72))
    pai_no_frances = db.Column(db.String(72))
    pai_abreviatura = db.Column(db.String(36))



class TbEmailPendencia(db.Model):
    __tablename__ = 'tb_email_pendencia'

    co_seq_email_pendencia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_email_para = db.Column(db.String(200), nullable=False)
    ds_email_copia = db.Column(db.String(200))
    ds_titulo_email = db.Column(db.String(100), nullable=False)
    ds_conteudo_email = db.Column(db.String(2000), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbEmailPendencia.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_email_pendencias')



class TbEmailPendenciaComunicacao(db.Model):
    __tablename__ = 'tb_email_pendencia_comunicacao'

    co_seq_email_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_email_pessoa = db.Column(db.ForeignKey('tb_email_pendencia_pessoa.co_seq_email_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbEmailPendenciaComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_email_pendencia_comunicacaos')
    tb_email_pendencia_pessoa = db.relationship('TbEmailPendenciaPessoa', primaryjoin='TbEmailPendenciaComunicacao.co_seq_email_pessoa == TbEmailPendenciaPessoa.co_seq_email_pessoa', backref='tb_email_pendencia_comunicacaos')



class TbEmailPendenciaPessoa(db.Model):
    __tablename__ = 'tb_email_pendencia_pessoa'

    co_seq_email_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_email_pendencia = db.Column(db.ForeignKey('tb_email_pendencia.co_seq_email_pendencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_email_pendencia = db.relationship('TbEmailPendencia', primaryjoin='TbEmailPendenciaPessoa.co_seq_email_pendencia == TbEmailPendencia.co_seq_email_pendencia', backref='tb_email_pendencia_pessoas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbEmailPendenciaPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_email_pendencia_pessoas')



class TbEncaminhamentoAtendimento(db.Model):
    __tablename__ = 'tb_encaminhamento_atendimento'

    co_seq_enc_atendimento = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_canc_atendimento = db.Column(db.ForeignKey('tb_motivo_cancelamento_atendi.co_seq_mot_canc_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_enc_setor = db.Column(db.ForeignKey('tb_setor_encaminhamento.co_seq_enc_setor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_atendimento = db.Column(db.ForeignKey('tb_motivo_atendimento.co_seq_mot_atendimento'), db.ForeignKey('tb_motivo_atendimento.co_seq_mot_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_encaminhamento = db.Column(db.Numeric(8, 0), nullable=False)
    ds_encaminhamento = db.Column(db.String(2000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbEncaminhamentoAtendimento.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_encaminhamento_atendimentoes')
    tb_setor_encaminhamento = db.relationship('TbSetorEncaminhamento', primaryjoin='TbEncaminhamentoAtendimento.co_seq_enc_setor == TbSetorEncaminhamento.co_seq_enc_setor', backref='tb_encaminhamento_atendimentoes')
    tb_motivo_atendimento = db.relationship('TbMotivoAtendimento', primaryjoin='TbEncaminhamentoAtendimento.co_seq_mot_atendimento == TbMotivoAtendimento.co_seq_mot_atendimento', backref='tbmotivoatendimento_tb_encaminhamento_atendimentoes')
    tb_motivo_atendimento1 = db.relationship('TbMotivoAtendimento', primaryjoin='TbEncaminhamentoAtendimento.co_seq_mot_atendimento == TbMotivoAtendimento.co_seq_mot_atendimento', backref='tbmotivoatendimento_tb_encaminhamento_atendimentoes_0')
    tb_motivo_cancelamento_atendi = db.relationship('TbMotivoCancelamentoAtendi', primaryjoin='TbEncaminhamentoAtendimento.co_seq_mot_canc_atendimento == TbMotivoCancelamentoAtendi.co_seq_mot_canc_atendimento', backref='tb_encaminhamento_atendimentoes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbEncaminhamentoAtendimento.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_encaminhamento_atendimentoes')



class TbEncaminhamentoColaborador(db.Model):
    __tablename__ = 'tb_encaminhamento_colaborador'

    co_seq_enc_colaborador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_enc_setor = db.Column(db.ForeignKey('tb_setor_encaminhamento.co_seq_enc_setor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbEncaminhamentoColaborador.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_encaminhamento_colaboradors')
    tb_setor_encaminhamento = db.relationship('TbSetorEncaminhamento', primaryjoin='TbEncaminhamentoColaborador.co_seq_enc_setor == TbSetorEncaminhamento.co_seq_enc_setor', backref='tb_encaminhamento_colaboradors')



class TbEncaminhamentoMunicipio(db.Model):
    __tablename__ = 'tb_encaminhamento_municipio'

    co_seq_enc_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_atendimento_municipio = db.Column(db.ForeignKey('tb_motivo_atendimento_municipio.co_seq_mot_atendimento_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_encaminhamento = db.Column(db.Numeric(8, 0), nullable=False)
    ds_encaminhamento = db.Column(db.String(2000))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_atendimento_municipio = db.relationship('TbMotivoAtendimentoMunicipio', primaryjoin='TbEncaminhamentoMunicipio.co_seq_mot_atendimento_municipio == TbMotivoAtendimentoMunicipio.co_seq_mot_atendimento_municipio', backref='tb_encaminhamento_municipios')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbEncaminhamentoMunicipio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_encaminhamento_municipios')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbEncaminhamentoMunicipio.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_encaminhamento_municipios')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbEncaminhamentoMunicipio.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_encaminhamento_municipios')



class TbEnderecoPessoa(db.Model):
    __tablename__ = 'tb_endereco_pessoa'
    __table_args__ = (
        db.Index('in_endpes_nutel_nutelcel', 'nu_telefone', 'nu_celular'),
        db.Index('pk_i_endereco_pessoa', 'co_seq_pessoa', 'co_seq_tp_endereco'),
        db.Index('in_endpes_coseqpes_coseqtpend', 'co_seq_pessoa', 'co_seq_tp_endereco'),
        db.Index('in_endpes_coseqpes_nutel_nutelcel', 'co_seq_pessoa', 'nu_telefone', 'nu_celular')
    )

    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_tp_endereco = db.Column(db.ForeignKey('tb_tipo_endereco.co_seq_tp_endereco', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_logradouro = db.Column(db.String(100), nullable=False, index=True)
    nu_logradouro = db.Column(db.String(60), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20), nullable=False)
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False, index=True)
    nu_telefone = db.Column(db.String(35), nullable=False, index=True)
    nu_celular = db.Column(db.String(60), nullable=False, index=True)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbEnderecoPessoa.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_endereco_pessoas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbEnderecoPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_endereco_pessoas')
    tb_tipo_endereco = db.relationship('TbTipoEndereco', primaryjoin='TbEnderecoPessoa.co_seq_tp_endereco == TbTipoEndereco.co_seq_tp_endereco', backref='tb_endereco_pessoas')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbEnderecoPessoa.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_endereco_pessoas')



class TbEnvioMaterial(db.Model):
    __tablename__ = 'tb_envio_material'

    co_seq_envio_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_distrito = db.Column(db.ForeignKey('tb_distrito.co_seq_distrito', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_envio_material = db.Column(db.ForeignKey('tb_tipo_envio_material.co_seq_tp_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_solicitacao_material = db.Column(db.ForeignKey('tb_solicitacao_material.co_seq_solicitacao_material', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_envio_material = db.Column(db.Numeric(8, 0), nullable=False)
    qt_envio_material = db.Column(db.Numeric(5, 0), nullable=False)
    nu_lote_material = db.Column(db.String(30))
    nu_correio = db.Column(db.String(60))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_distrito = db.relationship('TbDistrito', primaryjoin='TbEnvioMaterial.co_seq_distrito == TbDistrito.co_seq_distrito', backref='tb_envio_materials')
    tb_solicitacao_material = db.relationship('TbSolicitacaoMaterial', primaryjoin='TbEnvioMaterial.co_seq_solicitacao_material == TbSolicitacaoMaterial.co_seq_solicitacao_material', backref='tb_envio_materials')
    tb_tipo_envio_material = db.relationship('TbTipoEnvioMaterial', primaryjoin='TbEnvioMaterial.co_seq_tp_envio_material == TbTipoEnvioMaterial.co_seq_tp_envio_material', backref='tb_envio_materials')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbEnvioMaterial.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tb_envio_materials')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbEnvioMaterial.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_envio_materials')



class TbEquipamentoExame(db.Model):
    __tablename__ = 'tb_equipamento_exame'

    co_seq_equip_exame = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_tp_spr_col_arq = db.Column(db.ForeignKey('tb_tipo_separacao_coluna_arquivo.co_tp_spr_col_arq', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_equip_exame = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_col_comunicacao_serial = db.Column(db.Numeric(3, 0))
    out_separador = db.Column(db.String(10))
    nu_ini_caracter = db.Column(db.Numeric(4, 0))
    nu_ter_caracter = db.Column(db.Numeric(4, 0))
    ds_caracter_controle_exame = db.Column(db.String(50))
    nu_coluna_controle_exame = db.Column(db.Numeric(4, 0))
    ide_int_somente_um_exame = db.Column(db.String(1))
    ide_int_retorno_completo = db.Column(db.String(1))
    co_tp_int = db.Column(db.Numeric(2, 0))

    tb_tipo_separacao_coluna_arquivo = db.relationship('TbTipoSeparacaoColunaArquivo', primaryjoin='TbEquipamentoExame.co_tp_spr_col_arq == TbTipoSeparacaoColunaArquivo.co_tp_spr_col_arq', backref='tb_equipamento_exames')



class TbEquipamentoTipoExameMetodo(db.Model):
    __tablename__ = 'tb_equipamento_tipo_exame_metodo'

    co_seq_equip_tp_exame_metodo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbEquipamentoTipoExameMetodo.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_equipamento_tipo_exame_metodoes')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbEquipamentoTipoExameMetodo.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_equipamento_tipo_exame_metodoes')



class TbErroExecucaoSistema(db.Model):
    __tablename__ = 'tb_erro_execucao_sistema'

    co_seq_execucao_sistema = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    nu_lin_erro = db.Column(db.Numeric(8, 0), nullable=False)
    ds_classe_programa = db.Column(db.String(200), nullable=False)
    ds_funcao_procedimento = db.Column(db.String(200), nullable=False)
    ds_erro = db.Column(db.String(2000), nullable=False)
    ds_erro_completo = db.Column(db.String(2000), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbEspecialidade(db.Model):
    __tablename__ = 'tb_especialidade'

    co_seq_especialidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_profissao = db.Column(db.ForeignKey('tb_profissao.co_seq_profissao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_especialidade = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_profissao = db.relationship('TbProfissao', primaryjoin='TbEspecialidade.co_seq_profissao == TbProfissao.co_seq_profissao', backref='tb_especialidades')



class TbEsquemaPlaca(db.Model):
    __tablename__ = 'tb_esquema_placa'
    __table_args__ = (
        db.Index('in_esqplac_coseqrecepamo_coseqtpexa_dthrreg_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame', 'dt_hr_registro', 'dt_hr_cancelamento'),
        db.Index('in_esqplac_coseqrecepamo_coseqtpexa', 'co_seq_recep_amostra', 'co_seq_tp_exame'),
        db.Index('in_esqplac_coseqrecepamo_dthrreg', 'co_seq_recep_amostra', 'dt_hr_registro'),
        db.Index('in_esqplac_coseqrecepamo_coseqtpexa_dthrreg', 'co_seq_recep_amostra', 'co_seq_tp_exame', 'dt_hr_registro'),
        db.Index('in_esqplac_coseqtpexa_coseqtpmed_coseqexa_dthrcanc', 'co_seq_tp_exame', 'co_seq_tp_metodo', 'co_seq_equip_exame', 'dt_hr_cancelamento'),
        db.Index('in_esqplac_coseqrecepamo_coseqtpexa_dthrcanc', 'co_seq_recep_amostra', 'co_seq_tp_exame', 'dt_hr_cancelamento')
    )

    co_seq_esquema_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_metodo = db.Column(db.ForeignKey('tb_tipo_metodo.co_seq_tp_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_pos_placa = db.Column(db.ForeignKey('tb_tipo_posicao_placa.co_seq_tp_pos_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_placa = db.Column(db.ForeignKey('tb_numero_placa.nu_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_seq_amostra_placa = db.Column(db.Numeric(5, 0), nullable=False)
    nu_coluna_placa = db.Column(db.Numeric(2, 0), nullable=False)
    nu_linha_placa = db.Column(db.Numeric(2, 0), nullable=False)
    nu_seq_amostra_repeticao = db.Column(db.Numeric(2, 0), index=True)
    ide_arq_ent_placa = db.Column(db.String(1), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbEsquemaPlaca.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_esquema_placas')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbEsquemaPlaca.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_esquema_placas')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbEsquemaPlaca.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_esquema_placas')
    tb_tipo_metodo = db.relationship('TbTipoMetodo', primaryjoin='TbEsquemaPlaca.co_seq_tp_metodo == TbTipoMetodo.co_seq_tp_metodo', backref='tb_esquema_placas')
    tb_tipo_posicao_placa = db.relationship('TbTipoPosicaoPlaca', primaryjoin='TbEsquemaPlaca.co_seq_tp_pos_placa == TbTipoPosicaoPlaca.co_seq_tp_pos_placa', backref='tb_esquema_placas')
    tb_numero_placa = db.relationship('TbNumeroPlaca', primaryjoin='TbEsquemaPlaca.nu_placa == TbNumeroPlaca.nu_placa', backref='tb_esquema_placas')



class TbEstadoResultado(db.Model):
    __tablename__ = 'tb_estado_resultado'

    co_seq_res_estado = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_res_estado = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)



class TbEstoqueMedicamento(db.Model):
    __tablename__ = 'tb_estoque_medicamento'

    co_seq_estoque_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_medicamento = db.Column(db.ForeignKey('tb_medicamento.co_seq_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_evento_estoque = db.Column(db.ForeignKey('tb_evento_estoque.co_seq_evento_estoque', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_envio_material = db.Column(db.ForeignKey('tb_tipo_envio_material.co_seq_tp_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_movimentacao = db.Column(db.Numeric(8, 0), nullable=False)
    qt_movimentacao = db.Column(db.Numeric(8, 0), nullable=False)
    obs_movimentacao = db.Column(db.String(1000))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0))
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_evento_estoque = db.relationship('TbEventoEstoque', primaryjoin='TbEstoqueMedicamento.co_seq_evento_estoque == TbEventoEstoque.co_seq_evento_estoque', backref='tb_estoque_medicamentoes')
    tb_medicamento = db.relationship('TbMedicamento', primaryjoin='TbEstoqueMedicamento.co_seq_medicamento == TbMedicamento.co_seq_medicamento', backref='tb_estoque_medicamentoes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbEstoqueMedicamento.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_estoque_medicamentoes')
    tb_tipo_envio_material = db.relationship('TbTipoEnvioMaterial', primaryjoin='TbEstoqueMedicamento.co_seq_tp_envio_material == TbTipoEnvioMaterial.co_seq_tp_envio_material', backref='tb_estoque_medicamentoes')



class TbEstudoFamiliar(db.Model):
    __tablename__ = 'tb_estudo_familiar'

    co_seq_estudo_familiar = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_estudo_familiar = db.Column(db.ForeignKey('tb_tipo_estudo_familiar.co_seq_tp_estudo_familiar', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbEstudoFamiliar.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_estudo_familiars')
    tb_tipo_estudo_familiar = db.relationship('TbTipoEstudoFamiliar', primaryjoin='TbEstudoFamiliar.co_seq_tp_estudo_familiar == TbTipoEstudoFamiliar.co_seq_tp_estudo_familiar', backref='tb_estudo_familiars')



class TbEventoEstoque(db.Model):
    __tablename__ = 'tb_evento_estoque'

    co_seq_evento_estoque = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_evento_estoque = db.Column(db.String(30), nullable=False)
    oper_sobre_saldo = db.Column(db.Numeric(1, 0), nullable=False)



class TbExameAmbulatorial(db.Model):
    __tablename__ = 'tb_exame_ambulatorial'

    co_seq_exame_abulatorial = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta_amb = db.Column(db.ForeignKey('tb_consulta_ambulatorio.co_seq_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame_consulta_amb = db.Column(db.ForeignKey('tb_tipo_exame_consulta_amb.co_seq_tp_exame_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    ds_tp_exame_consulta_amb = db.Column(db.String(200))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_comp_exame = db.Column(db.Text)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)

    tb_consulta_ambulatorio = db.relationship('TbConsultaAmbulatorio', primaryjoin='TbExameAmbulatorial.co_seq_consulta_amb == TbConsultaAmbulatorio.co_seq_consulta_amb', backref='tb_exame_ambulatorials')
    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbExameAmbulatorial.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_exame_ambulatorials')
    tb_tipo_exame_consulta_amb = db.relationship('TbTipoExameConsultaAmb', primaryjoin='TbExameAmbulatorial.co_seq_tp_exame_consulta_amb == TbTipoExameConsultaAmb.co_seq_tp_exame_consulta_amb', backref='tb_exame_ambulatorials')



class TbExameComplementar(db.Model):
    __tablename__ = 'tb_exame_complementar'

    co_seq_exame_complementar = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_exame_padrao = db.Column(db.Numeric(2, 0), nullable=False)
    co_seq_unidade_saude = db.Column(db.Numeric(8, 0))
    co_seq_municipio = db.Column(db.Numeric(8, 0))
    ide_registro_automatico = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbExameConsulta(db.Model):
    __tablename__ = 'tb_exame_consulta'

    co_seq_exame_consulta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao_consulta = db.Column(db.ForeignKey('tb_interpretacao_exame_consulta.co_seq_interpretacao_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame_controle = db.Column(db.ForeignKey('tb_tipo_exame_controle.co_seq_tp_exame_controle', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame_consulta = db.Column(db.ForeignKey('tb_tipo_exame_consulta.co_seq_tp_exame_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    no_exame_manual = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    ds_outras_interpretacao = db.Column(db.String(2000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbExameConsulta.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_exame_consultas')
    tb_interpretacao_exame_consulta = db.relationship('TbInterpretacaoExameConsulta', primaryjoin='TbExameConsulta.co_seq_interpretacao_consulta == TbInterpretacaoExameConsulta.co_seq_interpretacao_consulta', backref='tb_exame_consultas')
    tb_tipo_exame_consulta = db.relationship('TbTipoExameConsulta', primaryjoin='TbExameConsulta.co_seq_tp_exame_consulta == TbTipoExameConsulta.co_seq_tp_exame_consulta', backref='tb_exame_consultas')
    tb_tipo_exame_controle = db.relationship('TbTipoExameControle', primaryjoin='TbExameConsulta.co_seq_tp_exame_controle == TbTipoExameControle.co_seq_tp_exame_controle', backref='tb_exame_consultas')



class TbExameConsultaAmbulatorial(db.Model):
    __tablename__ = 'tb_exame_consulta_ambulatorial'

    co_seq_exame_consulta_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_item_exame_consulta_amb = db.Column(db.ForeignKey('tb_item_exame_consulta_amb.co_seq_item_exame_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta_amb = db.Column(db.ForeignKey('tb_consulta_ambulatorio.co_seq_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_exame_abulatorial = db.Column(db.ForeignKey('tb_exame_ambulatorial.co_seq_exame_abulatorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_int_exame_amb = db.Column(db.ForeignKey('tb_tipo_interpretacao_exame_amb.co_seq_tp_int_exame_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    no_exame_manual = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    ds_outras_interpretacao = db.Column(db.String(2000))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_resultado_manual = db.Column(db.String(1))

    tb_consulta_ambulatorio = db.relationship('TbConsultaAmbulatorio', primaryjoin='TbExameConsultaAmbulatorial.co_seq_consulta_amb == TbConsultaAmbulatorio.co_seq_consulta_amb', backref='tb_exame_consulta_ambulatorials')
    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbExameConsultaAmbulatorial.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_exame_consulta_ambulatorials')
    tb_exame_ambulatorial = db.relationship('TbExameAmbulatorial', primaryjoin='TbExameConsultaAmbulatorial.co_seq_exame_abulatorial == TbExameAmbulatorial.co_seq_exame_abulatorial', backref='tb_exame_consulta_ambulatorials')
    tb_item_exame_consulta_amb = db.relationship('TbItemExameConsultaAmb', primaryjoin='TbExameConsultaAmbulatorial.co_seq_item_exame_consulta_amb == TbItemExameConsultaAmb.co_seq_item_exame_consulta_amb', backref='tb_exame_consulta_ambulatorials')
    tb_tipo_interpretacao_exame_amb = db.relationship('TbTipoInterpretacaoExameAmb', primaryjoin='TbExameConsultaAmbulatorial.co_seq_tp_int_exame_amb == TbTipoInterpretacaoExameAmb.co_seq_tp_int_exame_amb', backref='tb_exame_consulta_ambulatorials')



class TbExameConsultaDocumento(db.Model):
    __tablename__ = 'tb_exame_consulta_documento'

    co_seq_exame_consulta_doc = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_exame_consulta = db.Column(db.ForeignKey('tb_exame_consulta.co_seq_exame_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doc_anexo_pessoa = db.Column(db.ForeignKey('tb_documento_anexo_pessoa.co_seq_doc_anexo_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_documento_anexo_pessoa = db.relationship('TbDocumentoAnexoPessoa', primaryjoin='TbExameConsultaDocumento.co_seq_doc_anexo_pessoa == TbDocumentoAnexoPessoa.co_seq_doc_anexo_pessoa', backref='tb_exame_consulta_documentoes')
    tb_exame_consulta = db.relationship('TbExameConsulta', primaryjoin='TbExameConsultaDocumento.co_seq_exame_consulta == TbExameConsulta.co_seq_exame_consulta', backref='tb_exame_consulta_documentoes')



class TbExameControleMedicoDoenca(db.Model):
    __tablename__ = 'tb_exame_controle_medico_doenca'

    co_seq_exame_controle_medico = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_amostra_repeticao = db.Column(db.Numeric(2, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbExameControleMedicoDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_exame_controle_medico_doencas')
    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbExameControleMedicoDoenca.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_exame_controle_medico_doencas')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbExameControleMedicoDoenca.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_exame_controle_medico_doencas')



class TbExameExcepcional(db.Model):
    __tablename__ = 'tb_exame_excepcional'

    co_seq_par_exame_excepcional = db.Column(db.Numeric(8, 0), primary_key=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca'), index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento'), index=True)
    nu_dia_realizacao_exame = db.Column(db.Numeric(5, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbExameExcepcional.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_exame_excepcionals')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbExameExcepcional.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_exame_excepcionals')



class TbExameFechamentoMensal(db.Model):
    __tablename__ = 'tb_exame_fechamento_mensal'
    __table_args__ = (
        db.Index('in_exafecmen_dtcompt', 'co_seq_amostra_fch_mensal', 'co_seq_tp_procedimento'),
    )

    co_seq_exame_fechamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_fch_mensal = db.Column(db.ForeignKey('tb_amostra_fechamento_mensal.co_seq_amostra_fch_mensal', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial_soro = db.Column(db.ForeignKey('tb_resultado_laboratorial_soro.co_seq_res_laboratorial_soro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    res_laboratorial = db.Column(db.String(100), nullable=False)
    nu_folha = db.Column(db.Numeric(6, 0))
    nu_linha = db.Column(db.Numeric(8, 0))

    tb_amostra_fechamento_mensal = db.relationship('TbAmostraFechamentoMensal', primaryjoin='TbExameFechamentoMensal.co_seq_amostra_fch_mensal == TbAmostraFechamentoMensal.co_seq_amostra_fch_mensal', backref='tb_exame_fechamento_mensals')
    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbExameFechamentoMensal.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_exame_fechamento_mensals')
    tb_resultado_laboratorial_soro = db.relationship('TbResultadoLaboratorialSoro', primaryjoin='TbExameFechamentoMensal.co_seq_res_laboratorial_soro == TbResultadoLaboratorialSoro.co_seq_res_laboratorial_soro', backref='tb_exame_fechamento_mensals')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbExameFechamentoMensal.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_exame_fechamento_mensals')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbExameFechamentoMensal.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_exame_fechamento_mensals')



class TbExameFechamentoMensalToxo(db.Model):
    __tablename__ = 'tb_exame_fechamento_mensal_toxo'
    __table_args__ = (
        db.Index('in_exafecmentx_coamo_tpproc', 'co_seq_amostra_fch_toxo', 'co_seq_tp_procedimento'),
        db.Index('in_exafecmentx_coamo_tpproc_vrproc', 'co_seq_amostra_fch_toxo', 'co_seq_tp_procedimento', 'vr_procedimento')
    )

    co_seq_exame_fechamento_toxo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_fch_toxo = db.Column(db.ForeignKey('tb_amostra_fechamento_toxo.co_seq_amostra_fch_toxo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial_soro = db.Column(db.ForeignKey('tb_resultado_laboratorial_soro.co_seq_res_laboratorial_soro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    res_laboratorial = db.Column(db.String(100), nullable=False)
    res_impresso = db.Column(db.String(100), nullable=False)
    vr_procedimento = db.Column(db.Numeric(12, 2), nullable=False)

    tb_amostra_fechamento_toxo = db.relationship('TbAmostraFechamentoToxo', primaryjoin='TbExameFechamentoMensalToxo.co_seq_amostra_fch_toxo == TbAmostraFechamentoToxo.co_seq_amostra_fch_toxo', backref='tb_exame_fechamento_mensal_toxoes')
    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbExameFechamentoMensalToxo.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_exame_fechamento_mensal_toxoes')
    tb_resultado_laboratorial_soro = db.relationship('TbResultadoLaboratorialSoro', primaryjoin='TbExameFechamentoMensalToxo.co_seq_res_laboratorial_soro == TbResultadoLaboratorialSoro.co_seq_res_laboratorial_soro', backref='tb_exame_fechamento_mensal_toxoes')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbExameFechamentoMensalToxo.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_exame_fechamento_mensal_toxoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbExameFechamentoMensalToxo.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_exame_fechamento_mensal_toxoes')



class TbExameLiberacaoBloqueado(db.Model):
    __tablename__ = 'tb_exame_liberacao_bloqueado'

    co_seq_exame_bloqueado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_municipio = db.Column(db.String(1))

    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbExameLiberacaoBloqueado.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_exame_liberacao_bloqueadoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbExameLiberacaoBloqueado.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_exame_liberacao_bloqueadoes')



class TbExamePadrao(db.Model):
    __tablename__ = 'tb_exame_padrao'

    co_seq_exame_padrao = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_exame_padrao = db.Column(db.String(50), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0))
    aut_registro = db.Column(db.String(20))



class TbExecucaoLaboratorio(db.Model):
    __tablename__ = 'tb_execucao_laboratorio'

    co_seq_execucao_laboratorio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_canc_placa = db.Column(db.ForeignKey('tb_motivo_cancelamento_placa.co_seq_mot_canc_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_placa_execucao = db.Column(db.String(30), nullable=False)
    co_seq_colaborador_picote = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_realizou = db.Column(db.Numeric(5, 0))
    nu_equip_analise = db.Column(db.String(20))
    nu_lote = db.Column(db.String(10))
    dt_picote = db.Column(db.Numeric(8, 0))
    dt_realizou = db.Column(db.Numeric(8, 0))
    dt_hr_picote = db.Column(db.Numeric(14, 0))
    dt_hr_realizou = db.Column(db.Numeric(14, 0))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    nu_equip_lavadora = db.Column(db.String(20))
    nu_equip_estufa = db.Column(db.String(20))
    nu_equip_plataforma_picotagem = db.Column(db.String(20))
    nu_equip_picotagem = db.Column(db.String(20))
    ide_somente_uma_analise = db.Column(db.String(1))
    dt_hr_termino_execucao = db.Column(db.Numeric(14, 0))

    tb_motivo_cancelamento_placa = db.relationship('TbMotivoCancelamentoPlaca', primaryjoin='TbExecucaoLaboratorio.co_seq_mot_canc_placa == TbMotivoCancelamentoPlaca.co_seq_mot_canc_placa', backref='tb_execucao_laboratorios')



class TbExecucaoPicoteManual(db.Model):
    __tablename__ = 'tb_execucao_picote_manual'
    __table_args__ = (
        db.Index('in_execpicman_nuwork_coseqwork_coseqtpexamet_coseqequi_autreg_d', 'nu_worklist', 'co_seq_worklist', 'co_seq_tp_exame_metodo', 'co_seq_equip_exame', 'aut_registro', 'dt_hr_cancelamento', 'dt_hr_conclusao'),
    )

    co_seq_execucao_picote_manual = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_worklist = db.Column(db.Numeric(14, 0), nullable=False)
    co_seq_worklist = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_geracao_placa = db.Column(db.Numeric(14, 0))
    aut_geracao_placa = db.Column(db.String(20))

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbExecucaoPicoteManual.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_execucao_picote_manuals')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbExecucaoPicoteManual.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_execucao_picote_manuals')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbExecucaoPicoteManual.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_execucao_picote_manuals')



class TbExecucaoPicoteManualPlaca(db.Model):
    __tablename__ = 'tb_execucao_picote_manual_placa'

    co_seq_picote_manual_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_execucao_picote_manual = db.Column(db.ForeignKey('tb_execucao_picote_manual.co_seq_execucao_picote_manual', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_placa = db.Column(db.ForeignKey('tb_numero_placa.nu_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_execucao_picote_manual = db.relationship('TbExecucaoPicoteManual', primaryjoin='TbExecucaoPicoteManualPlaca.co_seq_execucao_picote_manual == TbExecucaoPicoteManual.co_seq_execucao_picote_manual', backref='tb_execucao_picote_manual_placas')
    tb_numero_placa = db.relationship('TbNumeroPlaca', primaryjoin='TbExecucaoPicoteManualPlaca.nu_placa == TbNumeroPlaca.nu_placa', backref='tb_execucao_picote_manual_placas')



class TbExecucaoProjetoPesquisa(db.Model):
    __tablename__ = 'tb_execucao_projeto_pesquisa'

    co_seq_execucao_pesquisa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_projeto_pesquisa = db.Column(db.ForeignKey('tb_projeto_pesquisa.co_seq_projeto_pesquisa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini = db.Column(db.Numeric(8, 0))
    dt_ter = db.Column(db.Numeric(8, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_projeto_pesquisa = db.relationship('TbProjetoPesquisa', primaryjoin='TbExecucaoProjetoPesquisa.co_seq_projeto_pesquisa == TbProjetoPesquisa.co_seq_projeto_pesquisa', backref='tb_execucao_projeto_pesquisas')



class TbExecucaoProtocoloRecoleta(db.Model):
    __tablename__ = 'tb_execucao_protocolo_recoleta'

    co_seq_execucao_protocolo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_protocolo_recoleta = db.Column(db.ForeignKey('tb_protocolo_recoleta.co_seq_protocolo_recoleta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_protocolo_recoleta = db.relationship('TbProtocoloRecoleta', primaryjoin='TbExecucaoProtocoloRecoleta.co_seq_protocolo_recoleta == TbProtocoloRecoleta.co_seq_protocolo_recoleta', backref='tb_execucao_protocolo_recoletas')



class TbFabricanteMedicamento(db.Model):
    __tablename__ = 'tb_fabricante_medicamento'

    co_seq_fabricante_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_fabricante_medicamento = db.Column(db.String(80), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbFaixaIdadeFaturamento(db.Model):
    __tablename__ = 'tb_faixa_idade_faturamento'

    co_seq_faixa_idade_bpa = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_faixa_idade_bpa = db.Column(db.String(80), nullable=False)
    ida_ini = db.Column(db.Numeric(3, 0))
    ida_ter = db.Column(db.Numeric(3, 0))



class TbFasePrograma(db.Model):
    __tablename__ = 'tb_fase_programa'

    co_fase_programa = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_fase_programa = db.Column(db.String(50), nullable=False)



class TbFechamentoMensal(db.Model):
    __tablename__ = 'tb_fechamento_mensal'

    co_seg_fch_mensal = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    dt_competencia = db.Column(db.ForeignKey('tb_competencia.dt_competencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_inicio_liberacao = db.Column(db.Numeric(8, 0))
    dt_termino_liberacao = db.Column(db.Numeric(8, 0))
    dia_limite_liberacao = db.Column(db.Numeric(2, 0))
    ide_fechamento_mesmo_mes = db.Column(db.String(1))

    tb_competencia = db.relationship('TbCompetencia', primaryjoin='TbFechamentoMensal.dt_competencia == TbCompetencia.dt_competencia', backref='tb_fechamento_mensals')



class TbFechamentoMensalToxo(db.Model):
    __tablename__ = 'tb_fechamento_mensal_toxo'

    co_seq_fch_mensal_toxo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    dt_competencia = db.Column(db.ForeignKey('tb_competencia.dt_competencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_competencia = db.relationship('TbCompetencia', primaryjoin='TbFechamentoMensalToxo.dt_competencia == TbCompetencia.dt_competencia', backref='tb_fechamento_mensal_toxoes')



class TbFichaAmbulatorial(db.Model):
    __tablename__ = 'tb_ficha_ambulatorial'

    co_seq_ficha_amb = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_especialidade = db.Column(db.ForeignKey('tb_especialidade.co_seq_especialidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_primeira_consulta = db.Column(db.String(1))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbFichaAmbulatorial.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_ficha_ambulatorials')
    tb_especialidade = db.relationship('TbEspecialidade', primaryjoin='TbFichaAmbulatorial.co_seq_especialidade == TbEspecialidade.co_seq_especialidade', backref='tb_ficha_ambulatorials')



class TbFiltroRelatorioControle(db.Model):
    __tablename__ = 'tb_filtro_relatorio_controle'

    co_seq_filtro_relatorio = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_filtro_relatorio = db.Column(db.String(50), nullable=False)
    no_transacao = db.Column(db.String(70), nullable=False)



class TbFuncao(db.Model):
    __tablename__ = 'tb_funcao'

    co_seq_funcao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_funcao = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbFuncaoColaborador(db.Model):
    __tablename__ = 'tb_funcao_colaborador'

    co_seq_funcao_colaborador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_funcao_colaborador = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbGeracaoPlaca(db.Model):
    __tablename__ = 'tb_geracao_placa'

    co_seq_geracao_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_geracao_placa = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_geracao_placa = db.Column(db.String(20), nullable=False)



class TbGeracaoPlacaProcesso(db.Model):
    __tablename__ = 'tb_geracao_placa_processo'
    __table_args__ = (
        db.Index('in_gerplaproc_cotpexa_coseqequipexa', 'co_seq_tp_exame_metodo', 'co_seq_equip_exame'),
    )

    co_seq_geracao_placa_processo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_geracao_placa = db.Column(db.ForeignKey('tb_geracao_placa.co_seq_geracao_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbGeracaoPlacaProcesso.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_geracao_placa_processoes')
    tb_geracao_placa = db.relationship('TbGeracaoPlaca', primaryjoin='TbGeracaoPlacaProcesso.co_seq_geracao_placa == TbGeracaoPlaca.co_seq_geracao_placa', backref='tb_geracao_placa_processoes')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbGeracaoPlacaProcesso.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_geracao_placa_processoes')



class TbGrupo(db.Model):
    __tablename__ = 'tb_grupo'

    co_seq_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_grupo = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbGrupoCaracteristicaDoenca(db.Model):
    __tablename__ = 'tb_grupo_caracteristica_doenca'

    co_seq_grupo_caract_doenca = db.Column(db.Numeric(8, 0), primary_key=True, server_default=db.FetchedValue())
    ds_grupo_caract_doenca = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbGrupoFichaAtendimento(db.Model):
    __tablename__ = 'tb_grupo_ficha_atendimento'

    co_seq_grupo_ficha_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ficha_amb = db.Column(db.ForeignKey('tb_ficha_ambulatorial.co_seq_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_grupo_ficha_amb = db.Column(db.String(400), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)

    tb_ficha_ambulatorial = db.relationship('TbFichaAmbulatorial', primaryjoin='TbGrupoFichaAtendimento.co_seq_ficha_amb == TbFichaAmbulatorial.co_seq_ficha_amb', backref='tb_grupo_ficha_atendimentoes')



class TbGrupoInterpretacao(db.Model):
    __tablename__ = 'tb_grupo_interpretacao'

    co_seq_grupo_intepretacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_liberacao_obrigatoria = db.Column(db.String(1), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbGrupoInterpretacao.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_grupo_interpretacaos')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbGrupoInterpretacao.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_grupo_interpretacaos')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbGrupoInterpretacao.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_grupo_interpretacaos')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbGrupoInterpretacao.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_grupo_interpretacaos')



class TbGrupoResultado(db.Model):
    __tablename__ = 'tb_grupo_resultado'

    co_seq_grupo_res = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_grupo = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbGrupoResultado.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_grupo_resultadoes')



class TbGrupoResultadoDoenca(db.Model):
    __tablename__ = 'tb_grupo_resultado_doenca'

    co_seq_grupo_doenca = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_grupo_doenca = db.Column(db.String(80), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbGrupoResultadoDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_grupo_resultado_doencas')



class TbGrupoTransacao(db.Model):
    __tablename__ = 'tb_grupo_transacao'
    __table_args__ = (
        db.Index('pk_i_grupo_transacao', 'co_seq_acao_transacao', 'co_seq_transacao', 'co_seq_grupo'),
    )

    co_seq_acao_transacao = db.Column(db.ForeignKey('tb_acao_transacao.co_seq_acao_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_grupo = db.Column(db.ForeignKey('tb_grupo.co_seq_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_acao_transacao = db.relationship('TbAcaoTransacao', primaryjoin='TbGrupoTransacao.co_seq_acao_transacao == TbAcaoTransacao.co_seq_acao_transacao', backref='tb_grupo_transacaos')
    tb_grupo = db.relationship('TbGrupo', primaryjoin='TbGrupoTransacao.co_seq_grupo == TbGrupo.co_seq_grupo', backref='tb_grupo_transacaos')
    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbGrupoTransacao.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_grupo_transacaos')



class TbHistoricoAlteracao(db.Model):
    __tablename__ = 'tb_historico_alteracao'
    __table_args__ = (
        db.Index('pk_i_historico_alteracao', 'co_seq_usuario', 'co_seq_hist_alteracao'),
    )

    co_seq_usuario = db.Column(db.ForeignKey('tb_usuario.co_seq_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_hist_alteracao = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    co_seq_acao_transacao = db.Column(db.ForeignKey('tb_acao_transacao.co_seq_acao_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tabela_sistema = db.Column(db.ForeignKey('tb_tabela_sistema.co_seq_tabela_sistema', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_alteracao_origem = db.Column(db.Numeric(14, 0), nullable=False)
    ds_hist_alteracao = db.Column(db.String(100), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0))
    aut_registro = db.Column(db.String(20))

    tb_acao_transacao = db.relationship('TbAcaoTransacao', primaryjoin='TbHistoricoAlteracao.co_seq_acao_transacao == TbAcaoTransacao.co_seq_acao_transacao', backref='tb_historico_alteracaos')
    tb_tabela_sistema = db.relationship('TbTabelaSistema', primaryjoin='TbHistoricoAlteracao.co_seq_tabela_sistema == TbTabelaSistema.co_seq_tabela_sistema', backref='tb_historico_alteracaos')
    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbHistoricoAlteracao.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_historico_alteracaos')
    tb_usuario = db.relationship('TbUsuario', primaryjoin='TbHistoricoAlteracao.co_seq_usuario == TbUsuario.co_seq_usuario', backref='tb_historico_alteracaos')



class TbHistoricoMunicipio(db.Model):
    __tablename__ = 'tb_historico_municipio'

    co_seq_hist_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_credenciamento = db.Column(db.Numeric(8, 0), nullable=False)
    dt_canc_credenciamento = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbHistoricoMunicipio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_historico_municipios')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbHistoricoMunicipio.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_historico_municipios')



class TbHistoricoProfissional(db.Model):
    __tablename__ = 'tb_historico_profissional'

    co_seq_hist_prof_saude = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini_hist_prof_saude = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter_hist_prof_saude = db.Column(db.Numeric(8, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbHistoricoProfissional.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_historico_profissionals')



class TbHistoricoResultadoColunaSuor(db.Model):
    __tablename__ = 'tb_historico_resultado_coluna_suor'

    co_seq_historico_res_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_suor = db.Column(db.ForeignKey('tb_resultado_laboratorial_suor.co_seq_res_laboratorial_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_col_amostra_teste_suor = db.Column(db.ForeignKey('tb_coluna_amostra_teste_suor.co_seq_col_amostra_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_coluna_nu = db.Column(db.Double(53))
    vr_coluna_tex = db.Column(db.String(300))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_amostra = db.Column(db.Numeric(5, 0))

    tb_coluna_amostra_teste_suor = db.relationship('TbColunaAmostraTesteSuor', primaryjoin='TbHistoricoResultadoColunaSuor.co_seq_col_amostra_teste_suor == TbColunaAmostraTesteSuor.co_seq_col_amostra_teste_suor', backref='tb_historico_resultado_coluna_suors')
    tb_resultado_laboratorial_suor = db.relationship('TbResultadoLaboratorialSuor', primaryjoin='TbHistoricoResultadoColunaSuor.co_seq_res_laboratorial_suor == TbResultadoLaboratorialSuor.co_seq_res_laboratorial_suor', backref='tb_historico_resultado_coluna_suors')



class TbHistoricoUnidade(db.Model):
    __tablename__ = 'tb_historico_unidade'

    co_seq_hist_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini_hist_unidade = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter_hist_unidade = db.Column(db.Numeric(8, 0))
    ide_faz_coleta = db.Column(db.String(1), nullable=False)
    ide_portador_envio_material = db.Column(db.String(1), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    aut_termino = db.Column(db.String(20))

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbHistoricoUnidade.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_historico_unidades')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbHistoricoUnidade.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_historico_unidades')



class TbHistoricoUnidadePessoa(db.Model):
    __tablename__ = 'tb_historico_unidade_pessoa'

    co_seq_hist_unidade_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    pes_co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini_hist = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter_hist = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbHistoricoUnidadePessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tbpessoa_tb_historico_unidade_pessoas')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbHistoricoUnidadePessoa.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_historico_unidade_pessoas')
    tb_pessoa1 = db.relationship('TbPessoa', primaryjoin='TbHistoricoUnidadePessoa.pes_co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tbpessoa_tb_historico_unidade_pessoas_0')



class TbImpressaoBiologiaMolecular(db.Model):
    __tablename__ = 'tb_impressao_biologia_molecular'

    co_seq_impressao_bm = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_biologia_molecular = db.Column(db.ForeignKey('tb_resultado_biologia_molecular.co_seq_res_biologia_molecular', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_biologia_molecular = db.relationship('TbResultadoBiologiaMolecular', primaryjoin='TbImpressaoBiologiaMolecular.co_seq_res_biologia_molecular == TbResultadoBiologiaMolecular.co_seq_res_biologia_molecular', backref='tb_impressao_biologia_moleculars')



class TbImpressaoComunicacao(db.Model):
    __tablename__ = 'tb_impressao_comunicacao'

    co_seq_impressao_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbImpressaoComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_impressao_comunicacaos')



class TbImpressaoConferenciaSoro(db.Model):
    __tablename__ = 'tb_impressao_conferencia_soro'

    co_seq_impressao_conferencia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_conferencia_soro = db.Column(db.ForeignKey('tb_conferencia_soro_controle.co_seq_conferencia_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_conferencia_soro_controle = db.relationship('TbConferenciaSoroControle', primaryjoin='TbImpressaoConferenciaSoro.co_seq_conferencia_soro == TbConferenciaSoroControle.co_seq_conferencia_soro', backref='tb_impressao_conferencia_soroes')



class TbImpressaoFamiliar(db.Model):
    __tablename__ = 'tb_impressao_familiar'

    co_seq_impressao_familiar = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_impressao_res_familiar = db.Column(db.ForeignKey('tb_impressao_resultado_familiar.co_seq_impressao_res_familiar', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_impressao_resultado_familiar = db.relationship('TbImpressaoResultadoFamiliar', primaryjoin='TbImpressaoFamiliar.co_seq_impressao_res_familiar == TbImpressaoResultadoFamiliar.co_seq_impressao_res_familiar', backref='tb_impressao_familiars')
    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbImpressaoFamiliar.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_impressao_familiars')



class TbImpressaoResGrupoSoro(db.Model):
    __tablename__ = 'tb_impressao_res_grupo_soro'

    co_seq_impressao_res_grupo_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_lab_grupo_soro = db.Column(db.ForeignKey('tb_res_laboratorial_grupo_soro.co_seq_res_lab_grupo_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_res_laboratorial_grupo_soro = db.relationship('TbResLaboratorialGrupoSoro', primaryjoin='TbImpressaoResGrupoSoro.co_seq_res_lab_grupo_soro == TbResLaboratorialGrupoSoro.co_seq_res_lab_grupo_soro', backref='tb_impressao_res_grupo_soroes')



class TbImpressaoResultadoAi(db.Model):
    __tablename__ = 'tb_impressao_resultado_ai'
    __table_args__ = (
        db.Index('in_impresai_dtreg_coseqamotpexa', 'dt_registro', 'co_seq_amostra_tp_exame'),
    )

    co_seq_impressao_res_ai = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra_tp_exame = db.Column(db.ForeignKey('tb_amostra_tipo_exame.co_seq_amostra_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra_tipo_exame = db.relationship('TbAmostraTipoExame', primaryjoin='TbImpressaoResultadoAi.co_seq_amostra_tp_exame == TbAmostraTipoExame.co_seq_amostra_tp_exame', backref='tb_impressao_resultado_ais')



class TbImpressaoResultadoAmostra(db.Model):
    __tablename__ = 'tb_impressao_resultado_amostra'
    __table_args__ = (
        db.Index('in_imprresamo_dtreg_coseqreslab', 'dt_registro', 'co_seq_res_laboratorial'),
    )

    co_seq_impressao_res_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbImpressaoResultadoAmostra.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_impressao_resultado_amostras')



class TbImpressaoResultadoFamiliar(db.Model):
    __tablename__ = 'tb_impressao_resultado_familiar'

    co_seq_impressao_res_familiar = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_estudo_familiar = db.Column(db.ForeignKey('tb_estudo_familiar.co_seq_estudo_familiar', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_estudo_familiar = db.relationship('TbEstudoFamiliar', primaryjoin='TbImpressaoResultadoFamiliar.co_seq_estudo_familiar == TbEstudoFamiliar.co_seq_estudo_familiar', backref='tb_impressao_resultado_familiars')



class TbImpressaoResultadoGrupo(db.Model):
    __tablename__ = 'tb_impressao_resultado_grupo'

    co_seq_impressao_res_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_grupo = db.Column(db.ForeignKey('tb_resultado_laboratorial_grupo.co_seq_res_laboratorial_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial_grupo = db.relationship('TbResultadoLaboratorialGrupo', primaryjoin='TbImpressaoResultadoGrupo.co_seq_res_laboratorial_grupo == TbResultadoLaboratorialGrupo.co_seq_res_laboratorial_grupo', backref='tb_impressao_resultado_grupoes')



class TbImpressaoResultadoSoro(db.Model):
    __tablename__ = 'tb_impressao_resultado_soro'

    co_seq_impressao_amostra_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_soro = db.Column(db.ForeignKey('tb_resultado_laboratorial_soro.co_seq_res_laboratorial_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial_soro = db.relationship('TbResultadoLaboratorialSoro', primaryjoin='TbImpressaoResultadoSoro.co_seq_res_laboratorial_soro == TbResultadoLaboratorialSoro.co_seq_res_laboratorial_soro', backref='tb_impressao_resultado_soroes')



class TbImpressaoResultadoSuor(db.Model):
    __tablename__ = 'tb_impressao_resultado_suor'

    co_seq_impressao_res_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_suor = db.Column(db.ForeignKey('tb_resultado_laboratorial_suor.co_seq_res_laboratorial_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial_suor = db.relationship('TbResultadoLaboratorialSuor', primaryjoin='TbImpressaoResultadoSuor.co_seq_res_laboratorial_suor == TbResultadoLaboratorialSuor.co_seq_res_laboratorial_suor', backref='tb_impressao_resultado_suors')



class TbIndutorSuor(db.Model):
    __tablename__ = 'tb_indutor_suor'

    co_seq_indutor_suor = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_indutor_suor = db.Column(db.String(50), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbInterfaceEquipamentoExame(db.Model):
    __tablename__ = 'tb_interface_equipamento_exame'

    co_seq_int_equip_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_tp_spr_col_arq = db.Column(db.ForeignKey('tb_tipo_separacao_coluna_arquivo.co_tp_spr_col_arq', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_metodo = db.Column(db.ForeignKey('tb_tipo_metodo.co_seq_tp_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tmp_arq_entrada = db.Column(db.String(2000), nullable=False)
    ide_gera_arq_entrada = db.Column(db.String(1), nullable=False)
    ide_arq_ent_esquema_separado = db.Column(db.String(1), nullable=False)
    cbc_arq_entrada = db.Column(db.String(2000), nullable=False)
    nu_ini_lin_arq_retorno = db.Column(db.Numeric(2, 0), nullable=False)
    out_separador = db.Column(db.String(10))
    no_arq_entrada_worklist = db.Column(db.String(50))
    no_arq_extensao = db.Column(db.String(3))
    dir_arq_entrada = db.Column(db.String(200))
    dir_arq_retorno = db.Column(db.String(200))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_placa_completa = db.Column(db.String(1), nullable=False)
    nu_placa_multiplo = db.Column(db.Numeric(2, 0), nullable=False)
    ide_primeira_geracao_controle = db.Column(db.String(1), nullable=False)
    nu_limite_worklist = db.Column(db.Numeric(8, 0), nullable=False)
    ide_worklist_completa_geracao = db.Column(db.String(1), nullable=False)
    ide_calculo_variant = db.Column(db.String(1), nullable=False)
    ide_nome_arquivo = db.Column(db.String(1), nullable=False)
    no_exame_equip = db.Column(db.String(80), index=True)
    ds_caractr_controle_equip = db.Column(db.String(2000))
    rdp_arq_entrada = db.Column(db.String(2000))
    ide_nome_arquivo_sequencia = db.Column(db.String(1))
    nu_coluna_cabecalho = db.Column(db.Numeric(4, 0))
    nu_coluna_identificacao_paciente = db.Column(db.Numeric(4, 0))
    nu_coluna_exame = db.Column(db.Numeric(4, 0))
    nu_coluna_resultado = db.Column(db.Numeric(4, 0))
    nu_carcater_rodape = db.Column(db.Numeric(4, 0))
    ide_arquivo_mais_resultado = db.Column(db.String(1))
    ds_linha_desconsiderar = db.Column(db.String(2000))
    nu_coluna_desconsiderar = db.Column(db.Numeric(4, 0))
    ds_linha_inicio_leitura = db.Column(db.String(2000))
    ds_linha_termino_leitura = db.Column(db.String(2000))

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbInterfaceEquipamentoExame.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_interface_equipamento_exames')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbInterfaceEquipamentoExame.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_interface_equipamento_exames')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbInterfaceEquipamentoExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_interface_equipamento_exames')
    tb_tipo_metodo = db.relationship('TbTipoMetodo', primaryjoin='TbInterfaceEquipamentoExame.co_seq_tp_metodo == TbTipoMetodo.co_seq_tp_metodo', backref='tb_interface_equipamento_exames')
    tb_tipo_separacao_coluna_arquivo = db.relationship('TbTipoSeparacaoColunaArquivo', primaryjoin='TbInterfaceEquipamentoExame.co_tp_spr_col_arq == TbTipoSeparacaoColunaArquivo.co_tp_spr_col_arq', backref='tb_interface_equipamento_exames')



class TbInterpretacaoAnaliseSoro(db.Model):
    __tablename__ = 'tb_interpretacao_analise_soro'

    co_seq_inter_analise_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_analise_soro = db.Column(db.ForeignKey('tb_analise_amostra_soro.co_seq_analise_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    res_equip_soro = db.Column(db.String(100), nullable=False)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_analise_amostra_soro = db.relationship('TbAnaliseAmostraSoro', primaryjoin='TbInterpretacaoAnaliseSoro.co_seq_analise_soro == TbAnaliseAmostraSoro.co_seq_analise_soro', backref='tb_interpretacao_analise_soroes')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoAnaliseSoro.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_analise_soroes')



class TbInterpretacaoExame(db.Model):
    __tablename__ = 'tb_interpretacao_exame'

    co_seq_interpretacao = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_metodo = db.Column(db.ForeignKey('tb_tipo_metodo.co_seq_tp_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_estado = db.Column(db.ForeignKey('tb_estado_resultado.co_seq_res_estado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini_lib_res_interpretacao = db.Column(db.Numeric(8, 0))
    dt_ter_lib_res_interpretacao = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_estado_resultado = db.relationship('TbEstadoResultado', primaryjoin='TbInterpretacaoExame.co_seq_res_estado == TbEstadoResultado.co_seq_res_estado', backref='tb_interpretacao_exames')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbInterpretacaoExame.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_interpretacao_exames')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbInterpretacaoExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_interpretacao_exames')
    tb_tipo_metodo = db.relationship('TbTipoMetodo', primaryjoin='TbInterpretacaoExame.co_seq_tp_metodo == TbTipoMetodo.co_seq_tp_metodo', backref='tb_interpretacao_exames')



class TbInterpretacaoExameConsulta(db.Model):
    __tablename__ = 'tb_interpretacao_exame_consulta'

    co_seq_interpretacao_consulta = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_interpretacao_consulta = db.Column(db.String(50), nullable=False)



class TbInterpretacaoExameGrupo(db.Model):
    __tablename__ = 'tb_interpretacao_exame_grupo'

    co_seq_interpretacao_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_estado = db.Column(db.ForeignKey('tb_estado_resultado.co_seq_res_estado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_grupo_doenca = db.Column(db.ForeignKey('tb_grupo_resultado_doenca.co_seq_grupo_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_referencia_res = db.Column(db.String(2000))
    res_impresso = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    obs_res_impresso = db.Column(db.String(2000))
    nu_mes_emissao_comunicacao = db.Column(db.Numeric(2, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_analisa_ida_gestacional = db.Column(db.String(1), nullable=False)
    nu_ida_ini_gestacional = db.Column(db.Numeric(2, 0))
    nu_ida_ter_gestacional = db.Column(db.Numeric(2, 0))
    ide_comunicacao_automatica = db.Column(db.String(1))
    ide_analise_nu_amostra = db.Column(db.String(1))
    ide_primeiro_res = db.Column(db.String(1))
    nu_semana_emissao_comunicacao = db.Column(db.Numeric(4, 0))
    nu_semana_comunicacao_dt_col = db.Column(db.Numeric(4, 0))
    ide_analisa_municipio = db.Column(db.String(1))
    ide_analise_encaminhamento = db.Column(db.String(1))
    ide_somente_encaminhamento = db.Column(db.String(1))
    vr_indice_peso = db.Column(db.Numeric(4, 0))
    ide_analise_maternidade = db.Column(db.String(1))
    ide_somente_maternidade = db.Column(db.String(1))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbInterpretacaoExameGrupo.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_interpretacao_exame_grupoes')
    tb_grupo_resultado_doenca = db.relationship('TbGrupoResultadoDoenca', primaryjoin='TbInterpretacaoExameGrupo.co_seq_grupo_doenca == TbGrupoResultadoDoenca.co_seq_grupo_doenca', backref='tb_interpretacao_exame_grupoes')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbInterpretacaoExameGrupo.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_interpretacao_exame_grupoes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbInterpretacaoExameGrupo.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_interpretacao_exame_grupoes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbInterpretacaoExameGrupo.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_interpretacao_exame_grupoes')
    tb_estado_resultado = db.relationship('TbEstadoResultado', primaryjoin='TbInterpretacaoExameGrupo.co_seq_res_estado == TbEstadoResultado.co_seq_res_estado', backref='tb_interpretacao_exame_grupoes')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbInterpretacaoExameGrupo.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_interpretacao_exame_grupoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbInterpretacaoExameGrupo.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_interpretacao_exame_grupoes')



class TbInterpretacaoExameLiberacao(db.Model):
    __tablename__ = 'tb_interpretacao_exame_liberacao'

    co_seq_int_exame_liberacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_interpretacao_liberado = db.Column(db.Numeric(6, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoExameLiberacao.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_exame_liberacaos')



class TbInterpretacaoExameToxo(db.Model):
    __tablename__ = 'tb_interpretacao_exame_toxo'

    co_seq_toxo_intepretacao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_lin_corte = db.Column(db.ForeignKey('tb_linha_corte.co_seq_lin_corte', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_conduta_tecnico = db.Column(db.ForeignKey('tb_conduta_tecnico_resultado.co_seq_conduta_tecnico', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_conduta_tecnico_resultado = db.relationship('TbCondutaTecnicoResultado', primaryjoin='TbInterpretacaoExameToxo.co_seq_conduta_tecnico == TbCondutaTecnicoResultado.co_seq_conduta_tecnico', backref='tb_interpretacao_exame_toxoes')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoExameToxo.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_exame_toxoes')
    tb_linha_corte = db.relationship('TbLinhaCorte', primaryjoin='TbInterpretacaoExameToxo.co_seq_lin_corte == TbLinhaCorte.co_seq_lin_corte', backref='tb_interpretacao_exame_toxoes')



class TbInterpretacaoExameTriagem(db.Model):
    __tablename__ = 'tb_interpretacao_exame_triagem'

    co_seq_res_trg_interpretacao = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_conduta_tecnico = db.Column(db.ForeignKey('tb_conduta_tecnico_resultado.co_seq_conduta_tecnico', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_lin_corte = db.Column(db.ForeignKey('tb_linha_corte.co_seq_lin_corte', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ide_analise_ida = db.Column(db.String(1), nullable=False)
    ide_analise_peso = db.Column(db.String(1), nullable=False)
    ida_ini_interpretacao = db.Column(db.Numeric(6, 0))
    ida_ter_interpretacao = db.Column(db.Numeric(6, 0))
    pes_ini_grama = db.Column(db.Numeric(5, 0))
    pes_ter_grama = db.Column(db.Numeric(5, 0))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_referencia_res = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    res_impresso = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    ide_analise_nu_amostra = db.Column(db.String(1))
    ide_primeiro_res = db.Column(db.String(1))
    ide_controle_medico = db.Column(db.String(1))
    ide_observacao_clinica = db.Column(db.String(1))
    ide_analise_maternidade = db.Column(db.String(1))
    ide_somente_maternidade = db.Column(db.String(1))
    ide_analise_encaminhamento = db.Column(db.String(1))
    ide_somente_encaminhamento = db.Column(db.String(1))
    ide_nu_amostra_alterada = db.Column(db.String(1))
    nu_amostra_alterada = db.Column(db.Numeric(2, 0))
    ide_analise_res_fora_triagem = db.Column(db.String(1))
    ide_paciente_fora_triagem = db.Column(db.String(1))
    vr_indice_peso = db.Column(db.Numeric(4, 0))
    ide_analise_estabilidade_crinica = db.Column(db.String(1))
    co_tp_estado_clinico = db.Column(db.Numeric(2, 0))
    ide_analisa_resultado_anterior = db.Column(db.String(1))
    ide_comportamento_resultado = db.Column(db.String(1))
    ide_analisa_uso_corticoide = db.Column(db.String(1))
    ide_uso_corticoide = db.Column(db.String(1))
    nu_dia_comunicacao_dt_coleta = db.Column(db.Numeric(8, 0))

    tb_conduta_tecnico_resultado = db.relationship('TbCondutaTecnicoResultado', primaryjoin='TbInterpretacaoExameTriagem.co_seq_conduta_tecnico == TbCondutaTecnicoResultado.co_seq_conduta_tecnico', backref='tb_interpretacao_exame_triagems')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoExameTriagem.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_exame_triagems')
    tb_linha_corte = db.relationship('TbLinhaCorte', primaryjoin='TbInterpretacaoExameTriagem.co_seq_lin_corte == TbLinhaCorte.co_seq_lin_corte', backref='tb_interpretacao_exame_triagems')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbInterpretacaoExameTriagem.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_interpretacao_exame_triagems')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbInterpretacaoExameTriagem.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_interpretacao_exame_triagems')



class TbInterpretacaoHemoglobina(db.Model):
    __tablename__ = 'tb_interpretacao_hemoglobina'

    co_seq_res_hb_interpretacao = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    co_seq_res_subgrupo = db.Column(db.ForeignKey('tb_subgrupo_resultado.co_seq_res_subgrupo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_regra_emissao_res = db.Column(db.ForeignKey('tb_regra_emissao_hb_resultado.co_seq_regra_emissao_res', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_conduta_tecnico = db.Column(db.ForeignKey('tb_conduta_tecnico_resultado.co_seq_conduta_tecnico', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    sub_co_seq_res_subgrupo = db.Column(db.ForeignKey('tb_subgrupo_resultado.co_seq_res_subgrupo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ida_ini_interpretacao = db.Column(db.Numeric(6, 0))
    ida_ter_interpretacao = db.Column(db.Numeric(6, 0))
    res_laboratorial = db.Column(db.String(100), nullable=False)
    res_impresso = db.Column(db.String(100), nullable=False)
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    nu_mes_emissao_comunicacao = db.Column(db.Numeric(2, 0))
    ide_analise_nu_amostra = db.Column(db.String(1))
    ide_primeiro_res = db.Column(db.String(1))
    tex_referencia_res = db.Column(db.String(2000))
    ide_analise_res_fora_triagem = db.Column(db.String(1))
    ide_paciente_fora_triagem = db.Column(db.String(1))

    tb_conduta_tecnico_resultado = db.relationship('TbCondutaTecnicoResultado', primaryjoin='TbInterpretacaoHemoglobina.co_seq_conduta_tecnico == TbCondutaTecnicoResultado.co_seq_conduta_tecnico', backref='tb_interpretacao_hemoglobinas')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoHemoglobina.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_hemoglobinas')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbInterpretacaoHemoglobina.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_interpretacao_hemoglobinas')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbInterpretacaoHemoglobina.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_interpretacao_hemoglobinas')
    tb_regra_emissao_hb_resultado = db.relationship('TbRegraEmissaoHbResultado', primaryjoin='TbInterpretacaoHemoglobina.co_seq_regra_emissao_res == TbRegraEmissaoHbResultado.co_seq_regra_emissao_res', backref='tb_interpretacao_hemoglobinas')
    tb_subgrupo_resultado = db.relationship('TbSubgrupoResultado', primaryjoin='TbInterpretacaoHemoglobina.co_seq_res_subgrupo == TbSubgrupoResultado.co_seq_res_subgrupo', backref='tbsubgruporesultado_tb_interpretacao_hemoglobinas')
    tb_subgrupo_resultado1 = db.relationship('TbSubgrupoResultado', primaryjoin='TbInterpretacaoHemoglobina.sub_co_seq_res_subgrupo == TbSubgrupoResultado.co_seq_res_subgrupo', backref='tbsubgruporesultado_tb_interpretacao_hemoglobinas_0')



class TbInterpretacaoRepeticao(db.Model):
    __tablename__ = 'tb_interpretacao_repeticao'

    co_seq_int_repeticao = db.Column(db.Numeric(8, 0), primary_key=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame'), nullable=False, index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao'), index=True)
    res_laboratorial = db.Column(db.String(100))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoRepeticao.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_repeticaos')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbInterpretacaoRepeticao.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_interpretacao_repeticaos')



class TbInterpretacaoResultadoGenetica(db.Model):
    __tablename__ = 'tb_interpretacao_resultado_genetica'

    co_seq_intepretacao_genetica = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_painel_mutacao = db.Column(db.ForeignKey('tb_painel_mutacao.co_seq_painel_mutacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_metodologia = db.Column(db.Text)
    ds_resultado = db.Column(db.Text)
    ds_conclusao_genetica = db.Column(db.Text)
    ds_obs_resultado = db.Column(db.Text)
    ide_analisa_painel = db.Column(db.String(1), nullable=False)
    ide_liberado_impressao = db.Column(db.String(1), nullable=False)
    ide_analisa_sequenciamento = db.Column(db.String(1), nullable=False)
    ide_sequenciamento = db.Column(db.String(1))
    ide_analisa_heterozigotivo = db.Column(db.String(1), nullable=False)
    ide_heterozigotico = db.Column(db.String(1))
    ide_mutacao_encontrada = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_heterozigotico_composto = db.Column(db.String(1))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbInterpretacaoResultadoGenetica.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_interpretacao_resultado_geneticas')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbInterpretacaoResultadoGenetica.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_interpretacao_resultado_geneticas')
    tb_painel_mutacao = db.relationship('TbPainelMutacao', primaryjoin='TbInterpretacaoResultadoGenetica.co_seq_painel_mutacao == TbPainelMutacao.co_seq_painel_mutacao', backref='tb_interpretacao_resultado_geneticas')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbInterpretacaoResultadoGenetica.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_interpretacao_resultado_geneticas')



class TbInterpretacaoResultadoGrupo(db.Model):
    __tablename__ = 'tb_interpretacao_resultado_grupo'

    co_seq_interpretacao_res_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao_grupo = db.Column(db.ForeignKey('tb_interpretacao_exame_grupo.co_seq_interpretacao_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_res_grupo_obrigatorio = db.Column(db.String(1), nullable=False)

    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbInterpretacaoResultadoGrupo.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_interpretacao_resultado_grupoes')
    tb_interpretacao_exame_grupo = db.relationship('TbInterpretacaoExameGrupo', primaryjoin='TbInterpretacaoResultadoGrupo.co_seq_interpretacao_grupo == TbInterpretacaoExameGrupo.co_seq_interpretacao_grupo', backref='tb_interpretacao_resultado_grupoes')



class TbItemColunaConsulta(db.Model):
    __tablename__ = 'tb_item_coluna_consulta'

    co_seq_item_coluna_consulta = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_coluna_consulta = db.Column(db.ForeignKey('tb_coluna_consulta.co_seq_coluna_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_item_coluna = db.Column(db.String(70), nullable=False)

    tb_coluna_consulta = db.relationship('TbColunaConsulta', primaryjoin='TbItemColunaConsulta.co_seq_coluna_consulta == TbColunaConsulta.co_seq_coluna_consulta', backref='tb_item_coluna_consultas')



class TbItemColunaPaciente(db.Model):
    __tablename__ = 'tb_item_coluna_paciente'

    co_seq_item_coluna_paciente = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_coluna_paciente = db.Column(db.ForeignKey('tb_coluna_paciente.co_seq_coluna_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_item_coluna = db.Column(db.String(70), nullable=False)

    tb_coluna_paciente = db.relationship('TbColunaPaciente', primaryjoin='TbItemColunaPaciente.co_seq_coluna_paciente == TbColunaPaciente.co_seq_coluna_paciente', backref='tb_item_coluna_pacientes')



class TbItemConsultaComunicacao(db.Model):
    __tablename__ = 'tb_item_consulta_comunicacao'

    co_seq_consulta_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_item_coluna_consulta = db.Column(db.ForeignKey('tb_item_coluna_consulta.co_seq_item_coluna_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbItemConsultaComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_item_consulta_comunicacaos')
    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbItemConsultaComunicacao.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_item_consulta_comunicacaos')
    tb_item_coluna_consulta = db.relationship('TbItemColunaConsulta', primaryjoin='TbItemConsultaComunicacao.co_seq_item_coluna_consulta == TbItemColunaConsulta.co_seq_item_coluna_consulta', backref='tb_item_consulta_comunicacaos')



class TbItemControleAlerta(db.Model):
    __tablename__ = 'tb_item_controle_alerta'

    co_seq_item_controle_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_controle_alerta = db.Column(db.ForeignKey('tb_controle_alerta.co_seq_controle_alerta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_alerta = db.Column(db.ForeignKey('tb_tipo_alerta.co_seq_tp_alerta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbItemControleAlerta.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_item_controle_alertas')
    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbItemControleAlerta.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_item_controle_alertas')
    tb_controle_alerta = db.relationship('TbControleAlerta', primaryjoin='TbItemControleAlerta.co_seq_controle_alerta == TbControleAlerta.co_seq_controle_alerta', backref='tb_item_controle_alertas')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbItemControleAlerta.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_item_controle_alertas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbItemControleAlerta.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_item_controle_alertas')
    tb_tipo_alerta = db.relationship('TbTipoAlerta', primaryjoin='TbItemControleAlerta.co_seq_tp_alerta == TbTipoAlerta.co_seq_tp_alerta', backref='tb_item_controle_alertas')



class TbItemExameConsultaAmb(db.Model):
    __tablename__ = 'tb_item_exame_consulta_amb'

    co_seq_item_exame_consulta_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_consulta_amb = db.Column(db.ForeignKey('tb_tipo_exame_consulta_amb.co_seq_tp_exame_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_item_exame_consulta_amb = db.Column(db.String(400), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame_consulta_amb = db.relationship('TbTipoExameConsultaAmb', primaryjoin='TbItemExameConsultaAmb.co_seq_tp_exame_consulta_amb == TbTipoExameConsultaAmb.co_seq_tp_exame_consulta_amb', backref='tb_item_exame_consulta_ambs')



class TbItemFichaAmbulatorial(db.Model):
    __tablename__ = 'tb_item_ficha_ambulatorial'

    co_seq_item_ficha_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_coluna_consulta_amb = db.Column(db.ForeignKey('tb_coluna_consulta_ambulatorial.co_seq_coluna_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_secao_ficha_amb = db.Column(db.ForeignKey('tb_secao_ficha_atendimento.co_seq_secao_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_coluna_paciente_amb = db.Column(db.ForeignKey('tb_coluna_paciente_anbulatorial.co_seq_coluna_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_grupo_ficha_amb = db.Column(db.ForeignKey('tb_grupo_ficha_atendimento.co_seq_grupo_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ficha_amb = db.Column(db.ForeignKey('tb_ficha_ambulatorial.co_seq_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_item_pre_progrmado_amb = db.Column(db.ForeignKey('tb_item_pre_programado_amb.co_seq_item_pre_progrmado_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_campo_ficha_amb = db.Column(db.ForeignKey('tb_campo_ficha_ambulatorio.co_seq_campo_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_coluna = db.Column(db.Numeric(2, 0), nullable=False)
    nu_linha = db.Column(db.Numeric(8, 0))
    nu_caracter = db.Column(db.Numeric(5, 0), nullable=False)
    ide_somente_numero = db.Column(db.String(1), nullable=False)
    ds_mascara = db.Column(db.String(200))
    ide_campo_obrigatorio = db.Column(db.String(1))
    ds_mensagem_campo_obrigatorio = db.Column(db.String(200))
    ds_campo_invalido = db.Column(db.String(200))
    ds_coluna = db.Column(db.String(200))
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)
    ds_conteudo_coluna = db.Column(db.String(100))
    nu_item_linha = db.Column(db.Numeric(3, 0))
    ds_regexp = db.Column(db.String(200))
    ds_mensagem_regexp = db.Column(db.String(200))
    ds_mensagem_limite_caracter = db.Column(db.String(200))
    nu_ini_limite = db.Column(db.Numeric(8, 0))
    nu_ter_limite = db.Column(db.Numeric(8, 0))
    ide_item_multline = db.Column(db.String(1))
    ds_secao_campo = db.Column(db.String(200))
    nu_coluna_campo = db.Column(db.Numeric(2, 0))

    tb_campo_ficha_ambulatorio = db.relationship('TbCampoFichaAmbulatorio', primaryjoin='TbItemFichaAmbulatorial.co_seq_campo_ficha_amb == TbCampoFichaAmbulatorio.co_seq_campo_ficha_amb', backref='tb_item_ficha_ambulatorials')
    tb_coluna_consulta_ambulatorial = db.relationship('TbColunaConsultaAmbulatorial', primaryjoin='TbItemFichaAmbulatorial.co_seq_coluna_consulta_amb == TbColunaConsultaAmbulatorial.co_seq_coluna_consulta_amb', backref='tb_item_ficha_ambulatorials')
    tb_coluna_paciente_anbulatorial = db.relationship('TbColunaPacienteAnbulatorial', primaryjoin='TbItemFichaAmbulatorial.co_seq_coluna_paciente_amb == TbColunaPacienteAnbulatorial.co_seq_coluna_paciente_amb', backref='tb_item_ficha_ambulatorials')
    tb_ficha_ambulatorial = db.relationship('TbFichaAmbulatorial', primaryjoin='TbItemFichaAmbulatorial.co_seq_ficha_amb == TbFichaAmbulatorial.co_seq_ficha_amb', backref='tb_item_ficha_ambulatorials')
    tb_grupo_ficha_atendimento = db.relationship('TbGrupoFichaAtendimento', primaryjoin='TbItemFichaAmbulatorial.co_seq_grupo_ficha_amb == TbGrupoFichaAtendimento.co_seq_grupo_ficha_amb', backref='tb_item_ficha_ambulatorials')
    tb_item_pre_programado_amb = db.relationship('TbItemPreProgramadoAmb', primaryjoin='TbItemFichaAmbulatorial.co_seq_item_pre_progrmado_amb == TbItemPreProgramadoAmb.co_seq_item_pre_progrmado_amb', backref='tb_item_ficha_ambulatorials')
    tb_secao_ficha_atendimento = db.relationship('TbSecaoFichaAtendimento', primaryjoin='TbItemFichaAmbulatorial.co_seq_secao_ficha_amb == TbSecaoFichaAtendimento.co_seq_secao_ficha_amb', backref='tb_item_ficha_ambulatorials')



class TbItemPerguntaSuor(db.Model):
    __tablename__ = 'tb_item_pergunta_suor'

    co_seq_item_pergunta_suor = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    co_seq_pergunta_suor = db.Column(db.ForeignKey('tb_pergunta_questionario_suor.co_seq_pergunta_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_item_pergunta_suor = db.Column(db.String(50), nullable=False)

    tb_pergunta_questionario_suor = db.relationship('TbPerguntaQuestionarioSuor', primaryjoin='TbItemPerguntaSuor.co_seq_pergunta_suor == TbPerguntaQuestionarioSuor.co_seq_pergunta_suor', backref='tb_item_pergunta_suors')



class TbItemPreProgramadoAmb(db.Model):
    __tablename__ = 'tb_item_pre_programado_amb'

    co_seq_item_pre_progrmado_amb = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    ds_item_pre_progrmado_amb = db.Column(db.String(50), nullable=False)



class TbItemSolicitacaoAtualizacao(db.Model):
    __tablename__ = 'tb_item_solicitacao_atualizacao'

    co_seq_item_solicitacao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_item_solicitacao = db.Column(db.String(50), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbItemSolicitacaoAtualizacao.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_item_solicitacao_atualizacaos')



class TbKitMaterial(db.Model):
    __tablename__ = 'tb_kit_material'

    co_seq_kit_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_kit_material = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbLiberacaoResultadoGenetica(db.Model):
    __tablename__ = 'tb_liberacao_resultado_genetica'

    co_seq_liberacao_genetica = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_biologia_molecular = db.Column(db.ForeignKey('tb_resultado_biologia_molecular.co_seq_res_biologia_molecular', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_biologia_molecular = db.relationship('TbResultadoBiologiaMolecular', primaryjoin='TbLiberacaoResultadoGenetica.co_seq_res_biologia_molecular == TbResultadoBiologiaMolecular.co_seq_res_biologia_molecular', backref='tb_liberacao_resultado_geneticas')



class TbLiberacaoSoro(db.Model):
    __tablename__ = 'tb_liberacao_soro'

    co_seq_liberacao_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_soro = db.Column(db.ForeignKey('tb_resultado_laboratorial_soro.co_seq_res_laboratorial_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial_soro = db.relationship('TbResultadoLaboratorialSoro', primaryjoin='TbLiberacaoSoro.co_seq_res_laboratorial_soro == TbResultadoLaboratorialSoro.co_seq_res_laboratorial_soro', backref='tb_liberacao_soroes')



class TbLimiteValorImpressao(db.Model):
    __tablename__ = 'tb_limite_valor_impressao'

    co_seq_limite_valor_resultado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_limite_inferior = db.Column(db.Numeric(14, 5))
    vr_limite_superior = db.Column(db.Numeric(14, 5))
    tex_resultado_limite_inferior = db.Column(db.String(30))
    tex_resultado_limite_superior = db.Column(db.String(30))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbLimiteValorImpressao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_limite_valor_impressaos')



class TbLinhaAnotacaoGeral(db.Model):
    __tablename__ = 'tb_linha_anotacao_geral'

    co_seq_linha_anotacao_geral = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ano_co_seq_anotacao_geral = db.Column(db.ForeignKey('tb_anotacao_geral.co_seq_anotacao_geral', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)
    ds_linha = db.Column(db.String(1000), nullable=False)

    tb_anotacao_geral = db.relationship('TbAnotacaoGeral', primaryjoin='TbLinhaAnotacaoGeral.ano_co_seq_anotacao_geral == TbAnotacaoGeral.co_seq_anotacao_geral', backref='tb_linha_anotacao_gerals')



class TbLinhaCorte(db.Model):
    __tablename__ = 'tb_linha_corte'

    co_seq_lin_corte = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_operador = db.Column(db.ForeignKey('tb_operador.co_seq_operador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_medida = db.Column(db.ForeignKey('tb_unidade_medida.co_seq_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_ini_ref_lin_corte = db.Column(db.Double(53))
    vr_ter_ref_lin_corte = db.Column(db.Double(53))
    dt_ini_corte = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter_corte = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    vr_limite_inferior = db.Column(db.Numeric(14, 5))
    nu_repeticao_limite_inferior = db.Column(db.Numeric(2, 0))
    vr_limite_superior = db.Column(db.Numeric(14, 5))
    nu_repeticao_limite_superior = db.Column(db.Numeric(2, 0))
    ide_ponto_flutuante = db.Column(db.String(1))
    vr_resultado_repeticao = db.Column(db.String(2000))
    ide_ai_limite_inferior = db.Column(db.String(1))
    ds_motivo_ai_limite_inferior = db.Column(db.String(50))
    ide_ai_limite_superior = db.Column(db.String(1))
    ds_motivo_ai_limite_superior = db.Column(db.String(50))

    tb_operador = db.relationship('TbOperador', primaryjoin='TbLinhaCorte.co_seq_operador == TbOperador.co_seq_operador', backref='tb_linha_cortes')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbLinhaCorte.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_linha_cortes')
    tb_unidade_medida = db.relationship('TbUnidadeMedida', primaryjoin='TbLinhaCorte.co_seq_unidade_medida == TbUnidadeMedida.co_seq_unidade_medida', backref='tb_linha_cortes')



class TbLinhaCortePontoFlutuante(db.Model):
    __tablename__ = 'tb_linha_corte_ponto_flutuante'
    __table_args__ = (
        db.Index('in_lincortpontflut_cotpexamet_coseqlincorte', 'co_seq_tp_exame_metodo', 'co_seq_lin_corte'),
    )

    co_seq_lin_corte_flutuante = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_lin_corte = db.Column(db.ForeignKey('tb_linha_corte.co_seq_lin_corte', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), index=True)
    no_arq = db.Column(db.String(100), index=True)
    nu_worklist = db.Column(db.Numeric(14, 0))
    vr_ini_ref_lin_corte = db.Column(db.Double(53), nullable=False)
    vr_ter_ref_lin_corte = db.Column(db.Double(53))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    vr_limite_superior = db.Column(db.Numeric(14, 5))

    tb_linha_corte = db.relationship('TbLinhaCorte', primaryjoin='TbLinhaCortePontoFlutuante.co_seq_lin_corte == TbLinhaCorte.co_seq_lin_corte', backref='tb_linha_corte_ponto_flutuantes')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbLinhaCortePontoFlutuante.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_linha_corte_ponto_flutuantes')



class TbLocalColeta(db.Model):
    __tablename__ = 'tb_local_coleta'

    co_seq_local_coleta = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_local_coleta = db.Column(db.String(50), nullable=False)
    ide_controla_horario_coleta = db.Column(db.String(1), nullable=False)



class TbLogBairro(db.Model):
    __tablename__ = 'tb_log_bairro'

    bai_nu = db.Column(db.Integer, primary_key=True, unique=True)
    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ufe_sg = db.Column(db.String(2))
    bai_no = db.Column(db.String(72))
    bai_no_abrev = db.Column(db.String(36))

    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogBairro.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_bairroes')



class TbLogCpc(db.Model):
    __tablename__ = 'tb_log_cpc'

    cpc_nu = db.Column(db.Integer, primary_key=True, unique=True)
    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ufe_sg = db.Column(db.String(2))
    cpc_no = db.Column(db.String(72))
    cpc_endereco = db.Column(db.String(100))
    cep = db.Column(db.String(8))

    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogCpc.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_cpcs')



class TbLogFaixaBairro(db.Model):
    __tablename__ = 'tb_log_faixa_bairro'
    __table_args__ = (
        db.Index('pk_i_log_faixa_bairro', 'bai_nu', 'fcb_cep_ini'),
    )

    bai_nu = db.Column(db.ForeignKey('tb_log_bairro.bai_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    fcb_cep_ini = db.Column(db.String(8), primary_key=True, nullable=False)
    fcb_cep_fim = db.Column(db.String(8))

    tb_log_bairro = db.relationship('TbLogBairro', primaryjoin='TbLogFaixaBairro.bai_nu == TbLogBairro.bai_nu', backref='tb_log_faixa_bairroes')



class TbLogFaixaCpc(db.Model):
    __tablename__ = 'tb_log_faixa_cpc'
    __table_args__ = (
        db.Index('pk_i_log_faixa_cpc', 'cpc_nu', 'cpc_inicial'),
    )

    cpc_nu = db.Column(db.ForeignKey('tb_log_cpc.cpc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    cpc_inicial = db.Column(db.String(6), primary_key=True, nullable=False)
    cpc_final = db.Column(db.String(6))

    tb_log_cpc = db.relationship('TbLogCpc', primaryjoin='TbLogFaixaCpc.cpc_nu == TbLogCpc.cpc_nu', backref='tb_log_faixa_cpcs')



class TbLogFaixaLocalidade(db.Model):
    __tablename__ = 'tb_log_faixa_localidade'
    __table_args__ = (
        db.Index('pk_i_log_faixa_localidade', 'loc_nu', 'loc_cep_ini'),
    )

    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    loc_cep_ini = db.Column(db.String(8), primary_key=True, nullable=False)
    loc_cep_fim = db.Column(db.String(8))

    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogFaixaLocalidade.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_faixa_localidades')



class TbLogFaixaUf(db.Model):
    __tablename__ = 'tb_log_faixa_uf'
    __table_args__ = (
        db.Index('pk_i_log_faixa_uf', 'ufe_sg', 'ufe_cep_ini'),
    )

    ufe_sg = db.Column(db.String(2), primary_key=True, nullable=False)
    ufe_cep_ini = db.Column(db.String(8), primary_key=True, nullable=False)
    ufe_cep_fim = db.Column(db.String(8))



class TbLogFaixaUop(db.Model):
    __tablename__ = 'tb_log_faixa_uop'
    __table_args__ = (
        db.Index('pk_i_log_faixa_uop', 'uop_nu', 'fnc_inicial'),
    )

    uop_nu = db.Column(db.ForeignKey('tb_log_unid_oper.uop_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    fnc_inicial = db.Column(db.String(8), primary_key=True, nullable=False)
    fnc_final = db.Column(db.String(6))

    tb_log_unid_oper = db.relationship('TbLogUnidOper', primaryjoin='TbLogFaixaUop.uop_nu == TbLogUnidOper.uop_nu', backref='tb_log_faixa_uops')



class TbLogGrandeUsuario(db.Model):
    __tablename__ = 'tb_log_grande_usuario'

    gru_nu = db.Column(db.Integer, primary_key=True, unique=True)
    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    bai_nu = db.Column(db.ForeignKey('tb_log_bairro.bai_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    log_nu = db.Column(db.ForeignKey('tb_log_logradouro.log_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ufe_sg = db.Column(db.String(2))
    gru_no = db.Column(db.String(72))
    gru_endereco = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    gru_no_abrev = db.Column(db.String(36))

    tb_log_bairro = db.relationship('TbLogBairro', primaryjoin='TbLogGrandeUsuario.bai_nu == TbLogBairro.bai_nu', backref='tb_log_grande_usuarios')
    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogGrandeUsuario.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_grande_usuarios')
    tb_log_logradouro = db.relationship('TbLogLogradouro', primaryjoin='TbLogGrandeUsuario.log_nu == TbLogLogradouro.log_nu', backref='tb_log_grande_usuarios')



class TbLogLocalidade(db.Model):
    __tablename__ = 'tb_log_localidade'

    loc_nu = db.Column(db.Integer, primary_key=True, unique=True)
    ufe_sg = db.Column(db.String(2))
    loc_no = db.Column(db.String(72), index=True)
    cep = db.Column(db.String(8))
    loc_in_sit = db.Column(db.String(1))
    loc_in_tipo_loc = db.Column(db.String(1))
    loc_nu_sub = db.Column(db.Integer)
    loc_no_abrev = db.Column(db.String(36))
    mun_nu = db.Column(db.Integer)



class TbLogLogradouro(db.Model):
    __tablename__ = 'tb_log_logradouro'
    __table_args__ = (
        db.Index('in_log_no_sg', 'log_no', 'ufe_sg'),
    )

    log_nu = db.Column(db.Integer, primary_key=True, unique=True)
    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ufe_sg = db.Column(db.String(2))
    bai_nu_ini = db.Column(db.Integer)
    bai_nu_fim = db.Column(db.Integer)
    log_no = db.Column(db.String(100))
    log_complemento = db.Column(db.String(100))
    cep = db.Column(db.String(8), index=True)
    tlo_tx = db.Column(db.String(36))
    log_sta_tlo = db.Column(db.String(1))
    log_no_abrev = db.Column(db.String(36))

    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogLogradouro.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_logradouroes')



t_tb_log_num_sec = db.Table(
    'tb_log_num_sec',
    db.Column('log_nu', db.ForeignKey('tb_log_logradouro.log_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True),
    db.Column('sec_nu_ini', db.String(10)),
    db.Column('sec_nu_fim', db.String(10)),
    db.Column('sec_in_lado', db.String(1))
)



class TbLogUnidOper(db.Model):
    __tablename__ = 'tb_log_unid_oper'

    uop_nu = db.Column(db.Integer, primary_key=True, unique=True)
    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    bai_nu = db.Column(db.ForeignKey('tb_log_bairro.bai_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    log_nu = db.Column(db.ForeignKey('tb_log_logradouro.log_nu', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ufe_sg = db.Column(db.String(2))
    uop_no = db.Column(db.String(100))
    uop_endereco = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    uop_in_cp = db.Column(db.String(1))
    uop_no_abrev = db.Column(db.String(36))

    tb_log_bairro = db.relationship('TbLogBairro', primaryjoin='TbLogUnidOper.bai_nu == TbLogBairro.bai_nu', backref='tb_log_unid_opers')
    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogUnidOper.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_unid_opers')
    tb_log_logradouro = db.relationship('TbLogLogradouro', primaryjoin='TbLogUnidOper.log_nu == TbLogLogradouro.log_nu', backref='tb_log_unid_opers')



class TbLogVarBai(db.Model):
    __tablename__ = 'tb_log_var_bai'
    __table_args__ = (
        db.Index('pk_i_log_var_bai', 'bai_nu', 'vdb_nu'),
    )

    bai_nu = db.Column(db.ForeignKey('tb_log_bairro.bai_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    vdb_nu = db.Column(db.Integer, primary_key=True, nullable=False)
    vdb_tx = db.Column(db.String(72))

    tb_log_bairro = db.relationship('TbLogBairro', primaryjoin='TbLogVarBai.bai_nu == TbLogBairro.bai_nu', backref='tb_log_var_bais')



class TbLogVarLoc(db.Model):
    __tablename__ = 'tb_log_var_loc'
    __table_args__ = (
        db.Index('pk_i_log_var_loc', 'loc_nu', 'val_nu'),
    )

    loc_nu = db.Column(db.ForeignKey('tb_log_localidade.loc_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    val_nu = db.Column(db.Integer, primary_key=True, nullable=False)
    val_tx = db.Column(db.String(72))

    tb_log_localidade = db.relationship('TbLogLocalidade', primaryjoin='TbLogVarLoc.loc_nu == TbLogLocalidade.loc_nu', backref='tb_log_var_locs')



class TbLogVarLog(db.Model):
    __tablename__ = 'tb_log_var_log'
    __table_args__ = (
        db.Index('pk_i_log_var_log', 'log_nu', 'vlo_nu'),
    )

    log_nu = db.Column(db.ForeignKey('tb_log_logradouro.log_nu', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    vlo_nu = db.Column(db.Integer, primary_key=True, nullable=False)
    tlo_tx = db.Column(db.String(36))
    vlo_tx = db.Column(db.String(150))

    tb_log_logradouro = db.relationship('TbLogLogradouro', primaryjoin='TbLogVarLog.log_nu == TbLogLogradouro.log_nu', backref='tb_log_var_logs')



class TbMacroregiao(db.Model):
    __tablename__ = 'tb_macroregiao'

    co_seq_macroregiao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_macroregiao = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMaterialFechamentoToxo(db.Model):
    __tablename__ = 'tb_material_fechamento_toxo'

    co_seq_material_fch_toxo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_fch_mensal_toxo = db.Column(db.ForeignKey('tb_fechamento_mensal_toxo.co_seq_fch_mensal_toxo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_envio_material = db.Column(db.ForeignKey('tb_envio_material.co_seq_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_envio_material = db.Column(db.Numeric(8, 0), nullable=False)
    qt_envio_material = db.Column(db.Numeric(5, 0), nullable=False)
    vr_procedimento = db.Column(db.Numeric(12, 2), nullable=False)

    tb_envio_material = db.relationship('TbEnvioMaterial', primaryjoin='TbMaterialFechamentoToxo.co_seq_envio_material == TbEnvioMaterial.co_seq_envio_material', backref='tb_material_fechamento_toxoes')
    tb_fechamento_mensal_toxo = db.relationship('TbFechamentoMensalToxo', primaryjoin='TbMaterialFechamentoToxo.co_seq_fch_mensal_toxo == TbFechamentoMensalToxo.co_seq_fch_mensal_toxo', backref='tb_material_fechamento_toxoes')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbMaterialFechamentoToxo.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tb_material_fechamento_toxoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbMaterialFechamentoToxo.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_material_fechamento_toxoes')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbMaterialFechamentoToxo.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_material_fechamento_toxoes')



class TbMaterialProjetoPesquisa(db.Model):
    __tablename__ = 'tb_material_projeto_pesquisa'

    co_seq_material_pesquisa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_execucao_pesquisa = db.Column(db.ForeignKey('tb_execucao_projeto_pesquisa.co_seq_execucao_pesquisa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_execucao_projeto_pesquisa = db.relationship('TbExecucaoProjetoPesquisa', primaryjoin='TbMaterialProjetoPesquisa.co_seq_execucao_pesquisa == TbExecucaoProjetoPesquisa.co_seq_execucao_pesquisa', backref='tb_material_projeto_pesquisas')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbMaterialProjetoPesquisa.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tb_material_projeto_pesquisas')



class TbMaternidadePessoa(db.Model):
    __tablename__ = 'tb_maternidade_pessoa'

    co_seq_maternidade_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_alta_maternidade = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbMaternidadePessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_maternidade_pessoas')



class TbMedicamento(db.Model):
    __tablename__ = 'tb_medicamento'

    co_seq_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_fabricante_medicamento = db.Column(db.ForeignKey('tb_fabricante_medicamento.co_seq_fabricante_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tip_unidade_medida = db.Column(db.ForeignKey('tb_tipo_unidade_medida.co_seq_tip_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_medicamento = db.Column(db.String(300), nullable=False)
    qt_medida_medicamento = db.Column(db.Numeric(4, 0), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_medicamento_arquivo_ms = db.Column(db.String(10))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbMedicamento.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_medicamentoes')
    tb_fabricante_medicamento = db.relationship('TbFabricanteMedicamento', primaryjoin='TbMedicamento.co_seq_fabricante_medicamento == TbFabricanteMedicamento.co_seq_fabricante_medicamento', backref='tb_medicamentoes')
    tb_tipo_unidade_medida = db.relationship('TbTipoUnidadeMedida', primaryjoin='TbMedicamento.co_seq_tip_unidade_medida == TbTipoUnidadeMedida.co_seq_tip_unidade_medida', backref='tb_medicamentoes')



class TbMedicamentoAmbulatorio(db.Model):
    __tablename__ = 'tb_medicamento_ambulatorio'

    co_seq_medicamento_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_via_medicamento = db.Column(db.ForeignKey('tb_tipo_via_medicamento.co_seq_tp_via_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_forma_prescricao = db.Column(db.ForeignKey('tb_tipo_forma_prescricao.co_seq_tp_forma_prescricao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_medicamento = db.Column(db.String(300), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_forma_prescricao = db.relationship('TbTipoFormaPrescricao', primaryjoin='TbMedicamentoAmbulatorio.co_seq_tp_forma_prescricao == TbTipoFormaPrescricao.co_seq_tp_forma_prescricao', backref='tb_medicamento_ambulatorios')
    tb_tipo_via_medicamento = db.relationship('TbTipoViaMedicamento', primaryjoin='TbMedicamentoAmbulatorio.co_seq_tp_via_medicamento == TbTipoViaMedicamento.co_seq_tp_via_medicamento', backref='tb_medicamento_ambulatorios')



class TbMesoregiao(db.Model):
    __tablename__ = 'tb_mesoregiao'

    co_seq_mesoregiao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_mesoregiao = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMicroregiao(db.Model):
    __tablename__ = 'tb_microregiao'

    co_seq_microregiao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_microregiao = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMigracao(db.Model):
    __tablename__ = 'tb_migracao'
    __table_args__ = (
        db.Index('in_mig_comig_cosisori', 'co_controle', 'co_sis_origem'),
        db.Index('pk_i_migracao', 'co_sis_origem', 'co_sis_atual', 'co_controle'),
        db.Index('in_mig_comig_cosisatu', 'co_controle', 'co_sis_atual'),
        db.Index('in_mig_comig_cosisatu_cosisori', 'co_controle', 'co_sis_atual', 'co_sis_origem')
    )

    co_sis_origem = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    co_sis_atual = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    co_controle = db.Column(db.Integer, primary_key=True, nullable=False, index=True)



t_tb_migracao_bm_fibrose = db.Table(
    'tb_migracao_bm_fibrose',
    db.Column('co_genetica', db.String(20)),
    db.Column('co_triagem', db.String(20)),
    db.Column('ide_508_mais_mais', db.String(1)),
    db.Column('ide_508_mais_menos', db.String(1)),
    db.Column('ide_508_menos_menos', db.String(1)),
    db.Column('ide_kit_29_mut', db.String(1)),
    db.Column('ds_genotipo_estudado', db.String(40)),
    db.Column('ide_estudar', db.String(1)),
    db.Column('ds_g542x', db.String(20)),
    db.Column('ds_g85e', db.String(20)),
    db.Column('ds_3120_mais_1g_maior_a', db.String(20)),
    db.Column('ds_n1303k', db.String(20)),
    db.Column('ds_711_mais_1g_maior_t', db.String(20)),
    db.Column('ds_r1162x', db.String(20)),
    db.Column('ds_w1282x', db.String(20)),
    db.Column('ds_genotipo_resultado', db.String(40)),
    db.Column('ds_status', db.String(30)),
    db.Column('obs_migracao', db.String(2000)),
    db.Column('ds_cidade', db.String(80))
)



t_tb_migracao_soro_funed = db.Table(
    'tb_migracao_soro_funed',
    db.Column('co_funed', db.String(20)),
    db.Column('co_nupad', db.String(20)),
    db.Column('no_pessoa', db.String(80)),
    db.Column('dt_col_amostra', db.Numeric(8, 0)),
    db.Column('dt_rec_amostra', db.Numeric(8, 0)),
    db.Column('vr_res_igg_funed', db.String(20)),
    db.Column('ds_interpretacao_igg_funed', db.String(20)),
    db.Column('vr_res_igm_funed', db.String(20)),
    db.Column('ds_interpretacao_igm_funed', db.String(20)),
    db.Column('vr_res_avidez_funed', db.String(20)),
    db.Column('ds_interpretacao_avidez_funed', db.String(20))
)



class TbMotivoAlteracaoTransacao(db.Model):
    __tablename__ = 'tb_motivo_alteracao_transacao'

    co_seq_atualizacao_transacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_atualizacao_cad = db.Column(db.ForeignKey('tb_motivo_atualizacao_cadastro.co_seq_mot_atualizacao_cad', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tabela_sistema = db.Column(db.ForeignKey('tb_tabela_sistema.co_seq_tabela_sistema', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_alteracao_origem = db.Column(db.Numeric(14, 0))

    tb_motivo_atualizacao_cadastro = db.relationship('TbMotivoAtualizacaoCadastro', primaryjoin='TbMotivoAlteracaoTransacao.co_seq_mot_atualizacao_cad == TbMotivoAtualizacaoCadastro.co_seq_mot_atualizacao_cad', backref='tb_motivo_alteracao_transacaos')
    tb_tabela_sistema = db.relationship('TbTabelaSistema', primaryjoin='TbMotivoAlteracaoTransacao.co_seq_tabela_sistema == TbTabelaSistema.co_seq_tabela_sistema', backref='tb_motivo_alteracao_transacaos')
    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbMotivoAlteracaoTransacao.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_motivo_alteracao_transacaos')



class TbMotivoAtendimento(db.Model):
    __tablename__ = 'tb_motivo_atendimento'

    co_seq_mot_atendimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_atendimento = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))



class TbMotivoAtendimentoMunicipio(db.Model):
    __tablename__ = 'tb_motivo_atendimento_municipio'

    co_seq_mot_atendimento_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_atendimento = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoAtualizacaoCadastro(db.Model):
    __tablename__ = 'tb_motivo_atualizacao_cadastro'

    co_seq_mot_atualizacao_cad = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_mot_atualizacao_cad = db.Column(db.String(60), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1), nullable=False)



class TbMotivoCancExameExcepcional(db.Model):
    __tablename__ = 'tb_motivo_canc_exame_excepcional'

    co_seq_mot_canc_exame_excep = db.Column(db.Numeric(4, 0), primary_key=True)
    ds_mot_canc_exame_excep = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoCancelamentoAgendum(db.Model):
    __tablename__ = 'tb_motivo_cancelamento_agenda'

    co_seq_mot_canc_agenda = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_canc_agenda = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1), nullable=False)
    ide_cria_pendencia = db.Column(db.String(1))
    ide_cria_pendencia_agenda = db.Column(db.String(1))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))



class TbMotivoCancelamentoAtendi(db.Model):
    __tablename__ = 'tb_motivo_cancelamento_atendi'

    co_seq_mot_canc_atendimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_canc_atendimento = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoCancelamentoComunicar(db.Model):
    __tablename__ = 'tb_motivo_cancelamento_comunicar'

    co_seq_mot_canc_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_seq_mot_canc_comunicacao = db.Column(db.String(80), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_res_influencia_resultado = db.Column(db.String(1), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1), nullable=False)



class TbMotivoCancelamentoPlaca(db.Model):
    __tablename__ = 'tb_motivo_cancelamento_placa'

    co_seq_mot_canc_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_canc_placa = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoCancelamentoResultado(db.Model):
    __tablename__ = 'tb_motivo_cancelamento_resultado'

    co_mot_canc_res = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_mot_canc_res = db.Column(db.String(600), nullable=False)
    ide_res_influencia_resultado = db.Column(db.String(1), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1))
    ide_gera_laudo_retificacao = db.Column(db.String(1))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))



class TbMotivoComunicacao(db.Model):
    __tablename__ = 'tb_motivo_comunicacao'

    co_seq_mot_comunicacao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_mot_comunicacao = db.Column(db.String(40), nullable=False)



class TbMotivoContato(db.Model):
    __tablename__ = 'tb_motivo_contato'

    co_seq_mot_contato = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_contato = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoContatoNaoEfetivado(db.Model):
    __tablename__ = 'tb_motivo_contato_nao_efetivado'

    co_mot_contato_nao_efetivado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_contato_nao_efetivado = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoDemandaEspontanea(db.Model):
    __tablename__ = 'tb_motivo_demanda_espontanea'

    co_seq_mot_demanda = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_demanda = db.Column(db.String(70), nullable=False)



class TbMotivoEntradaPrograma(db.Model):
    __tablename__ = 'tb_motivo_entrada_programa'

    co_seq_mot_entrada_programa = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_mot_entrada_programa = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1))



class TbMotivoInadequacao(db.Model):
    __tablename__ = 'tb_motivo_inadequacao'

    co_mot_inadequacao = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_mot_inadequacao = db.Column(db.String(80), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_outro = db.Column(db.String(1), nullable=False)



class TbMotivoNaoComparecimento(db.Model):
    __tablename__ = 'tb_motivo_nao_comparecimento'

    co_seq_mot_nao_comparecimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_nao_comparecimento = db.Column(db.String(100), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1))



class TbMotivoObito(db.Model):
    __tablename__ = 'tb_motivo_obito'

    co_seq_mot_obito = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_obito = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoReimpressaoResultado(db.Model):
    __tablename__ = 'tb_motivo_reimpressao_resultado'

    co_seq_mot_reimpressao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_reimpressao = db.Column(db.String(50), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbMotivoSaidaPrograma(db.Model):
    __tablename__ = 'tb_motivo_saida_programa'

    co_seq_mot_saida_programa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_mot_saida_programa = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))



class TbMsAgendamento(db.Model):
    __tablename__ = 'tb_ms_agendamento'

    co_seq_ms_agendamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento_consulta = db.Column(db.ForeignKey('tb_agendamento_consulta.co_seq_agendamento_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_paciente = db.Column(db.ForeignKey('tb_ms_paciente.co_seq_ms_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_reg_agen = db.Column(db.Numeric(8, 0), nullable=False)
    dt_agen = db.Column(db.Numeric(8, 0), nullable=False)

    tb_agendamento_consulta = db.relationship('TbAgendamentoConsulta', primaryjoin='TbMsAgendamento.co_seq_agendamento_consulta == TbAgendamentoConsulta.co_seq_agendamento_consulta', backref='tb_ms_agendamentoes')
    tb_ms_paciente = db.relationship('TbMsPaciente', primaryjoin='TbMsAgendamento.co_seq_ms_paciente == TbMsPaciente.co_seq_ms_paciente', backref='tb_ms_agendamentoes')



class TbMsAmostra(db.Model):
    __tablename__ = 'tb_ms_amostra'
    __table_args__ = (
        db.Index('in_msamostra_copes_coibge', 'co_seq_ms_pessoa', 'co_mun_ibge'),
    )

    co_seq_ms_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_pessoa = db.Column(db.ForeignKey('tb_ms_pessoa.co_seq_ms_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_amo = db.Column(db.Numeric(6, 0), nullable=False)
    dt_col = db.Column(db.Numeric(8, 0))
    dt_pos = db.Column(db.Numeric(8, 0))
    dt_rec = db.Column(db.Numeric(8, 0), nullable=False)
    dt_imp = db.Column(db.Numeric(8, 0), nullable=False)
    dt_dig = db.Column(db.Numeric(8, 0), nullable=False)
    co_mun_ibge = db.Column(db.String(20))
    nu_cnes = db.Column(db.String(30))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbMsAmostra.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_ms_amostras')
    tb_ms_pessoa = db.relationship('TbMsPessoa', primaryjoin='TbMsAmostra.co_seq_ms_pessoa == TbMsPessoa.co_seq_ms_pessoa', backref='tb_ms_amostras')



class TbMsAmostraInadequada(db.Model):
    __tablename__ = 'tb_ms_amostra_inadequada'

    co_seq_ms_amostra_inadequada = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_motivo_inadequacao = db.Column(db.ForeignKey('tb_ms_motivo_inadequacao.co_seq_ms_motivo_inadequacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_comunicacao = db.Column(db.ForeignKey('tb_ms_comunicacao.co_seq_ms_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    out_mot_inad = db.Column(db.String(80))

    tb_ms_comunicacao = db.relationship('TbMsComunicacao', primaryjoin='TbMsAmostraInadequada.co_seq_ms_comunicacao == TbMsComunicacao.co_seq_ms_comunicacao', backref='tb_ms_amostra_inadequadas')
    tb_ms_motivo_inadequacao = db.relationship('TbMsMotivoInadequacao', primaryjoin='TbMsAmostraInadequada.co_seq_ms_motivo_inadequacao == TbMsMotivoInadequacao.co_seq_ms_motivo_inadequacao', backref='tb_ms_amostra_inadequadas')



class TbMsComunicacao(db.Model):
    __tablename__ = 'tb_ms_comunicacao'

    co_seq_ms_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_exame = db.Column(db.ForeignKey('tb_ms_exame.co_seq_ms_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_mot_comunicacao = db.Column(db.ForeignKey('tb_ms_motivo_comunicacao.co_seq_ms_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_providencia = db.Column(db.ForeignKey('tb_ms_providencia.co_seq_ms_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_ms_mot_cancelamento = db.Column(db.ForeignKey('tb_ms_motivo_cancelamento.co_seq_ms_mot_cancelamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_emi = db.Column(db.Numeric(8, 0), nullable=False)
    dt_lib = db.Column(db.Numeric(8, 0), nullable=False)
    dt_sol = db.Column(db.Numeric(8, 0))
    out_mot_com = db.Column(db.String(80))
    out_prov = db.Column(db.String(80))
    dt_canc = db.Column(db.Numeric(8, 0))
    out_mot_canc = db.Column(db.String(80))

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbMsComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_ms_comunicacaos')
    tb_ms_exame = db.relationship('TbMsExame', primaryjoin='TbMsComunicacao.co_seq_ms_exame == TbMsExame.co_seq_ms_exame', backref='tb_ms_comunicacaos')
    tb_ms_motivo_cancelamento = db.relationship('TbMsMotivoCancelamento', primaryjoin='TbMsComunicacao.co_seq_ms_mot_cancelamento == TbMsMotivoCancelamento.co_seq_ms_mot_cancelamento', backref='tb_ms_comunicacaos')
    tb_ms_motivo_comunicacao = db.relationship('TbMsMotivoComunicacao', primaryjoin='TbMsComunicacao.co_seq_ms_mot_comunicacao == TbMsMotivoComunicacao.co_seq_ms_mot_comunicacao', backref='tb_ms_comunicacaos')
    tb_ms_providencia = db.relationship('TbMsProvidencia', primaryjoin='TbMsComunicacao.co_seq_ms_providencia == TbMsProvidencia.co_seq_ms_providencia', backref='tb_ms_comunicacaos')



class TbMsConsulta(db.Model):
    __tablename__ = 'tb_ms_consulta'

    co_seq_ms_consulta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_paciente = db.Column(db.ForeignKey('tb_ms_paciente.co_seq_ms_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_agendamento_consulta = db.Column(db.ForeignKey('tb_agendamento_consulta.co_seq_agendamento_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_con = db.Column(db.Numeric(8, 0), nullable=False)
    ide_com = db.Column(db.String(1), nullable=False)

    tb_agendamento_consulta = db.relationship('TbAgendamentoConsulta', primaryjoin='TbMsConsulta.co_seq_agendamento_consulta == TbAgendamentoConsulta.co_seq_agendamento_consulta', backref='tb_ms_consultas')
    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbMsConsulta.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_ms_consultas')
    tb_ms_paciente = db.relationship('TbMsPaciente', primaryjoin='TbMsConsulta.co_seq_ms_paciente == TbMsPaciente.co_seq_ms_paciente', backref='tb_ms_consultas')



class TbMsDoenca(db.Model):
    __tablename__ = 'tb_ms_doenca'

    co_seq_ms_doenca = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_doe = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbMsDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_ms_doencas')



class TbMsExame(db.Model):
    __tablename__ = 'tb_ms_exame'

    co_seq_ms_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_amostra = db.Column(db.ForeignKey('tb_ms_amostra.co_seq_ms_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_ms_tp_exame = db.Column(db.ForeignKey('tb_ms_tipo_exame.co_seq_ms_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_res = db.Column(db.Numeric(8, 0), nullable=False)
    dt_imp = db.Column(db.Numeric(8, 0), nullable=False)
    res_exa = db.Column(db.String(200), nullable=False)
    ref_exa = db.Column(db.String(200))

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbMsExame.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_ms_exames')
    tb_ms_amostra = db.relationship('TbMsAmostra', primaryjoin='TbMsExame.co_seq_ms_amostra == TbMsAmostra.co_seq_ms_amostra', backref='tb_ms_exames')
    tb_ms_tipo_exame = db.relationship('TbMsTipoExame', primaryjoin='TbMsExame.co_seq_ms_tp_exame == TbMsTipoExame.co_seq_ms_tp_exame', backref='tb_ms_exames')
    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbMsExame.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_ms_exames')



class TbMsIdentificacaoPrograma(db.Model):
    __tablename__ = 'tb_ms_identificacao_programa'

    co_seq_ms_id_programa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_fase_programa = db.Column(db.ForeignKey('tb_fase_programa.co_fase_programa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_comp = db.Column(db.Numeric(6, 0), nullable=False)
    no_prog = db.Column(db.String(200), nullable=False)
    sg_uf = db.Column(db.String(2), nullable=False)
    nu_unidade_saude_ativa = db.Column(db.Numeric(6, 0), nullable=False)
    ds_hash = db.Column(db.String(200))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_fase_programa = db.relationship('TbFasePrograma', primaryjoin='TbMsIdentificacaoPrograma.co_fase_programa == TbFasePrograma.co_fase_programa', backref='tb_ms_identificacao_programas')



class TbMsMedicamento(db.Model):
    __tablename__ = 'tb_ms_medicamento'

    co_seq_ms_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_tp_medicamento = db.Column(db.ForeignKey('tb_ms_tipo_medicamento.co_seq_ms_tp_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_paciente = db.Column(db.ForeignKey('tb_ms_paciente.co_seq_ms_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_exp = db.Column(db.Numeric(8, 0))
    out_med = db.Column(db.String(80))
    qt_med = db.Column(db.Numeric(5, 0))

    tb_ms_paciente = db.relationship('TbMsPaciente', primaryjoin='TbMsMedicamento.co_seq_ms_paciente == TbMsPaciente.co_seq_ms_paciente', backref='tb_ms_medicamentoes')
    tb_ms_tipo_medicamento = db.relationship('TbMsTipoMedicamento', primaryjoin='TbMsMedicamento.co_seq_ms_tp_medicamento == TbMsTipoMedicamento.co_seq_ms_tp_medicamento', backref='tb_ms_medicamentoes')



class TbMsMotivoCancelamento(db.Model):
    __tablename__ = 'tb_ms_motivo_cancelamento'

    co_seq_ms_mot_cancelamento = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_mot_canc_comunicacao = db.Column(db.ForeignKey('tb_motivo_cancelamento_comunicar.co_seq_mot_canc_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_mot_canc = db.Column(db.String(20), nullable=False)

    tb_motivo_cancelamento_comunicar = db.relationship('TbMotivoCancelamentoComunicar', primaryjoin='TbMsMotivoCancelamento.co_seq_mot_canc_comunicacao == TbMotivoCancelamentoComunicar.co_seq_mot_canc_comunicacao', backref='tb_ms_motivo_cancelamentoes')



class TbMsMotivoComunicacao(db.Model):
    __tablename__ = 'tb_ms_motivo_comunicacao'

    co_seq_ms_mot_comunicacao = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_mot_com = db.Column(db.String(20), nullable=False)

    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbMsMotivoComunicacao.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_ms_motivo_comunicacaos')



class TbMsMotivoInadequacao(db.Model):
    __tablename__ = 'tb_ms_motivo_inadequacao'

    co_seq_ms_motivo_inadequacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_mot_inadequacao = db.Column(db.ForeignKey('tb_motivo_inadequacao.co_mot_inadequacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_mot_inad = db.Column(db.String(20), nullable=False)

    tb_motivo_inadequacao = db.relationship('TbMotivoInadequacao', primaryjoin='TbMsMotivoInadequacao.co_mot_inadequacao == TbMotivoInadequacao.co_mot_inadequacao', backref='tb_ms_motivo_inadequacaos')



class TbMsPaciente(db.Model):
    __tablename__ = 'tb_ms_paciente'
    __table_args__ = (
        db.Index('in_mspaciente_copes_coibge', 'co_seq_ms_pessoa', 'co_mun_ibge'),
    )

    co_seq_ms_paciente = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_pessoa = db.Column(db.ForeignKey('tb_ms_pessoa.co_seq_ms_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_tp_ocorrencia = db.Column(db.ForeignKey('tb_ms_tipo_ocorrencia.co_seq_ms_tp_ocorrencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_ms_doenca = db.Column(db.ForeignKey('tb_ms_doenca.co_seq_ms_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_tipo_diagnostico = db.Column(db.ForeignKey('tb_ms_tipo_diagnostico.co_seq_ms_tipo_diagnostico', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    out_diag = db.Column(db.String(80))
    dt_diag_conf = db.Column(db.Numeric(8, 0))
    dt_ini_trat = db.Column(db.Numeric(8, 0))
    dt_ocor = db.Column(db.Numeric(8, 0))
    co_mun_ibge = db.Column(db.String(20))
    nu_cnes = db.Column(db.String(30))
    ds_perfil = db.Column(db.String(60))
    dt_prim_agendamento = db.Column(db.Numeric(8, 0))

    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbMsPaciente.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_ms_pacientes')
    tb_ms_doenca = db.relationship('TbMsDoenca', primaryjoin='TbMsPaciente.co_seq_ms_doenca == TbMsDoenca.co_seq_ms_doenca', backref='tb_ms_pacientes')
    tb_ms_pessoa = db.relationship('TbMsPessoa', primaryjoin='TbMsPaciente.co_seq_ms_pessoa == TbMsPessoa.co_seq_ms_pessoa', backref='tb_ms_pacientes')
    tb_ms_tipo_diagnostico = db.relationship('TbMsTipoDiagnostico', primaryjoin='TbMsPaciente.co_seq_ms_tipo_diagnostico == TbMsTipoDiagnostico.co_seq_ms_tipo_diagnostico', backref='tb_ms_pacientes')
    tb_ms_tipo_ocorrencia = db.relationship('TbMsTipoOcorrencia', primaryjoin='TbMsPaciente.co_seq_ms_tp_ocorrencia == TbMsTipoOcorrencia.co_seq_ms_tp_ocorrencia', backref='tb_ms_pacientes')



class TbMsPessoa(db.Model):
    __tablename__ = 'tb_ms_pessoa'

    co_seq_ms_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_id_programa = db.Column(db.ForeignKey('tb_ms_identificacao_programa.co_seq_ms_id_programa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_id_pes_prog = db.Column(db.String(20), nullable=False)
    nu_cns = db.Column(db.String(15))
    nu_dnv = db.Column(db.String(20))
    no_pes = db.Column(db.String(80))
    no_mae = db.Column(db.String(70))
    nu_cns_mae = db.Column(db.String(15))
    dt_nas = db.Column(db.Numeric(8, 0))
    dt_nas_mae = db.Column(db.Numeric(8, 0))
    co_mun_ibge = db.Column(db.String(20))
    nu_cpf = db.Column(db.Numeric(11, 0))

    tb_ms_identificacao_programa = db.relationship('TbMsIdentificacaoPrograma', primaryjoin='TbMsPessoa.co_seq_ms_id_programa == TbMsIdentificacaoPrograma.co_seq_ms_id_programa', backref='tb_ms_pessoas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbMsPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_ms_pessoas')



class TbMsProvidencia(db.Model):
    __tablename__ = 'tb_ms_providencia'

    co_seq_ms_providencia = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_prov = db.Column(db.String(20), nullable=False)

    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbMsProvidencia.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_ms_providencias')



class TbMsReferenciaExame(db.Model):
    __tablename__ = 'tb_ms_referencia_exame'

    co_seq_ms_referencia_exa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_ms_tp_exame = db.Column(db.ForeignKey('tb_ms_tipo_exame.co_seq_ms_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ms_id_programa = db.Column(db.ForeignKey('tb_ms_identificacao_programa.co_seq_ms_id_programa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_referencia_exame = db.Column(db.String(400), nullable=False)

    tb_ms_identificacao_programa = db.relationship('TbMsIdentificacaoPrograma', primaryjoin='TbMsReferenciaExame.co_seq_ms_id_programa == TbMsIdentificacaoPrograma.co_seq_ms_id_programa', backref='tb_ms_referencia_exames')
    tb_ms_tipo_exame = db.relationship('TbMsTipoExame', primaryjoin='TbMsReferenciaExame.co_seq_ms_tp_exame == TbMsTipoExame.co_seq_ms_tp_exame', backref='tb_ms_referencia_exames')



class TbMsTipoDiagnostico(db.Model):
    __tablename__ = 'tb_ms_tipo_diagnostico'

    co_seq_ms_tipo_diagnostico = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_diagnostico_consulta = db.Column(db.ForeignKey('tb_diagnostico_consulta.co_seq_diagnostico_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_diag = db.Column(db.String(20), nullable=False)

    tb_diagnostico_consulta = db.relationship('TbDiagnosticoConsulta', primaryjoin='TbMsTipoDiagnostico.co_seq_diagnostico_consulta == TbDiagnosticoConsulta.co_seq_diagnostico_consulta', backref='tb_ms_tipo_diagnosticoes')



class TbMsTipoExame(db.Model):
    __tablename__ = 'tb_ms_tipo_exame'

    co_seq_ms_tp_exame = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_exa = db.Column(db.String(5), nullable=False)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbMsTipoExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_ms_tipo_exames')



class TbMsTipoMedicamento(db.Model):
    __tablename__ = 'tb_ms_tipo_medicamento'

    co_seq_ms_tp_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_medicamento = db.Column(db.ForeignKey('tb_medicamento.co_seq_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_med = db.Column(db.String(20), nullable=False)

    tb_medicamento = db.relationship('TbMedicamento', primaryjoin='TbMsTipoMedicamento.co_seq_medicamento == TbMedicamento.co_seq_medicamento', backref='tb_ms_tipo_medicamentoes')



class TbMsTipoOcorrencia(db.Model):
    __tablename__ = 'tb_ms_tipo_ocorrencia'

    co_seq_ms_tp_ocorrencia = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    co_seq_mot_saida_programa = db.Column(db.ForeignKey('tb_motivo_saida_programa.co_seq_mot_saida_programa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_tp_ocor = db.Column(db.String(20), nullable=False)

    tb_motivo_saida_programa = db.relationship('TbMotivoSaidaPrograma', primaryjoin='TbMsTipoOcorrencia.co_seq_mot_saida_programa == TbMotivoSaidaPrograma.co_seq_mot_saida_programa', backref='tb_ms_tipo_ocorrencias')



class TbMunicipio(db.Model):
    __tablename__ = 'tb_municipio'

    co_seq_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_macroregiao = db.Column(db.ForeignKey('tb_macroregiao.co_seq_macroregiao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_distrito = db.Column(db.Integer, index=True)
    co_seq_mesoregiao = db.Column(db.ForeignKey('tb_mesoregiao.co_seq_mesoregiao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_uf = db.Column(db.ForeignKey('tb_uf.co_seq_uf', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_regional = db.Column(db.Integer, index=True)
    co_seq_polo = db.Column(db.ForeignKey('tb_polo.co_seq_polo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_microregiao = db.Column(db.ForeignKey('tb_microregiao.co_seq_microregiao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_consorcio = db.Column(db.Integer, index=True)
    co_ibge = db.Column(db.String(10), nullable=False, index=True)
    no_municipio = db.Column(db.String(70), nullable=False)
    dst_centro_referencia = db.Column(db.Numeric(8, 0))
    obs_municipio = db.Column(db.String(2000))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_macroregiao = db.relationship('TbMacroregiao', primaryjoin='TbMunicipio.co_seq_macroregiao == TbMacroregiao.co_seq_macroregiao', backref='tb_municipios')
    tb_mesoregiao = db.relationship('TbMesoregiao', primaryjoin='TbMunicipio.co_seq_mesoregiao == TbMesoregiao.co_seq_mesoregiao', backref='tb_municipios')
    tb_microregiao = db.relationship('TbMicroregiao', primaryjoin='TbMunicipio.co_seq_microregiao == TbMicroregiao.co_seq_microregiao', backref='tb_municipios')
    tb_polo = db.relationship('TbPolo', primaryjoin='TbMunicipio.co_seq_polo == TbPolo.co_seq_polo', backref='tb_municipios')
    tb_uf = db.relationship('TbUf', primaryjoin='TbMunicipio.co_seq_uf == TbUf.co_seq_uf', backref='tb_municipios')


class TbPrefeitura(TbMunicipio):
    __tablename__ = 'tb_prefeitura'

    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_prefeito = db.Column(db.String(70), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    nu_telefone = db.Column(db.String(35))
    nu_fax = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)

    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbPrefeitura.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_prefeituras')


class TbSecretariaSaude(TbMunicipio):
    __tablename__ = 'tb_secretaria_saude'

    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    co_seq_profissao = db.Column(db.ForeignKey('tb_profissao.co_seq_profissao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_secretario_saude = db.Column(db.String(70), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    nu_celular = db.Column(db.String(20))
    nu_telefone = db.Column(db.String(35))
    nu_fax = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)

    tb_profissao = db.relationship('TbProfissao', primaryjoin='TbSecretariaSaude.co_seq_profissao == TbProfissao.co_seq_profissao', backref='tb_secretaria_saudes')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbSecretariaSaude.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_secretaria_saudes')



class TbMunicipioEnvioCentralizado(db.Model):
    __tablename__ = 'tb_municipio_envio_centralizado'

    co_seq_mun_envio_centralizado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_envio_material = db.Column(db.String(1), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbMunicipioEnvioCentralizado.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_municipio_envio_centralizadoes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbMunicipioEnvioCentralizado.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_municipio_envio_centralizadoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbMunicipioEnvioCentralizado.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_municipio_envio_centralizadoes')



class TbMunicipioIbge(db.Model):
    __tablename__ = 'tb_municipio_ibge'

    co_seq_ibge = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ano_referenca = db.Column(db.Numeric(4, 0), nullable=False)
    nu_populacao_urbana = db.Column(db.Numeric(8, 0), nullable=False)
    nu_populacao_rural = db.Column(db.Numeric(8, 0), nullable=False)
    tp_classe_tamanho_populacao = db.Column(db.String(50), nullable=False)
    nu_nascido_vivo = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbMunicipioIbge.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_municipio_ibges')



class TbMunicipioLiberacaoBloqueado(db.Model):
    __tablename__ = 'tb_municipio_liberacao_bloqueado'

    co_seq_municipio_bloqueado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_exame_bloqueado = db.Column(db.ForeignKey('tb_exame_liberacao_bloqueado.co_seq_exame_bloqueado', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_exame_liberacao_bloqueado = db.relationship('TbExameLiberacaoBloqueado', primaryjoin='TbMunicipioLiberacaoBloqueado.co_seq_exame_bloqueado == TbExameLiberacaoBloqueado.co_seq_exame_bloqueado', backref='tb_municipio_liberacao_bloqueadoes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbMunicipioLiberacaoBloqueado.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_municipio_liberacao_bloqueadoes')



class TbMunicipioResultadoImpresso(db.Model):
    __tablename__ = 'tb_municipio_resultado_impresso'

    co_seq_municipio_res_impresso = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbMunicipioResultadoImpresso.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_municipio_resultado_impressoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbMunicipioResultadoImpresso.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_municipio_resultado_impressoes')



class TbMunicipioUnidadeCentralizada(db.Model):
    __tablename__ = 'tb_municipio_unidade_centralizada'

    co_seq_unidade_centralizada = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbMunicipioUnidadeCentralizada.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_municipio_unidade_centralizadas')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbMunicipioUnidadeCentralizada.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_municipio_unidade_centralizadas')



t_tb_neonatal_prenatal = db.Table(
    'tb_neonatal_prenatal',
    db.Column('co_seq_pessoa', db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('pes_co_seq_pessoa', db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True),
    db.Column('co_pessoa_sistema_antigo', db.Numeric(14, 0)),
    db.Column('dt_hr_ultima_alteracao', db.Numeric(14, 0), nullable=False),
    db.Column('aut_ultima_alteracao', db.String(20), nullable=False),
    db.Column('dt_hr_registro', db.Numeric(14, 0), nullable=False),
    db.Column('aut_registro', db.String(20), nullable=False)
)



class TbNumeroAnaliseLiberacao(db.Model):
    __tablename__ = 'tb_numero_analise_liberacao'

    co_seq_nu_analise_liberacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_analise_liberacao = db.Column(db.Numeric(3, 0), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbNumeroAnaliseLiberacao.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_numero_analise_liberacaos')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbNumeroAnaliseLiberacao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_numero_analise_liberacaos')



class TbNumeroPlaca(db.Model):
    __tablename__ = 'tb_numero_placa'
    __table_args__ = (
        db.Index('in_nuplac_coseqtexamet_equip_dthrcanc_nuseqreg', 'co_seq_tp_exame_metodo', 'co_seq_equip_exame', 'dt_hr_cancelamento', 'nu_seq_registro'),
        db.Index('in_nuplac_nuplac_dthrcanc', 'nu_placa', 'dt_hr_cancelamento'),
        db.Index('in_nuplac_dtreg_coseqtexamet_equip', 'dt_registro', 'co_seq_tp_exame_metodo', 'co_seq_equip_exame')
    )

    nu_placa = db.Column(db.String(30), primary_key=True, unique=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_geracao_placa = db.Column(db.ForeignKey('tb_geracao_placa.co_seq_geracao_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_worklist = db.Column(db.Numeric(14, 0), index=True)
    co_seq_worklist = db.Column(db.Numeric(14, 0), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_seq_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbNumeroPlaca.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_numero_placas')
    tb_geracao_placa = db.relationship('TbGeracaoPlaca', primaryjoin='TbNumeroPlaca.co_seq_geracao_placa == TbGeracaoPlaca.co_seq_geracao_placa', backref='tb_numero_placas')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbNumeroPlaca.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_numero_placas')



class TbNumeroPlacaCodigoPlaca(db.Model):
    __tablename__ = 'tb_numero_placa_codigo_placa'

    co_seq_nu_placa_co_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    nu_placa_equipamento = db.Column(db.String(50), nullable=False)
    co_placa_equipamento = db.Column(db.String(50), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))



class TbObservacaoResSoroSite(db.Model):
    __tablename__ = 'tb_observacao_res_soro_site'

    co_seq_obs_res_soro_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_soro_site = db.Column(db.ForeignKey('tb_resultado_soro_site.co_seq_res_soro_site', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_site = db.Column(db.Numeric(5, 0), nullable=False)
    ds_tp_exame = db.Column(db.String(100))
    obs_res_impresso = db.Column(db.String(2000))

    tb_resultado_soro_site = db.relationship('TbResultadoSoroSite', primaryjoin='TbObservacaoResSoroSite.co_seq_res_soro_site == TbResultadoSoroSite.co_seq_res_soro_site', backref='tb_observacao_res_soro_sites')



class TbOcorrencia(db.Model):
    __tablename__ = 'tb_ocorrencia'

    co_seq_ocorrencia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_ocorrencia = db.Column(db.ForeignKey('tb_tipo_ocorrencia.co_seq_tp_ocorrencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_atendimento = db.Column(db.ForeignKey('tb_atendimento.co_seq_atendimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ocorrencia = db.Column(db.Numeric(8, 0), nullable=False)
    obs_ocorrencia = db.Column(db.String(2000), nullable=False)
    no_contato = db.Column(db.String(70))
    nu_celular = db.Column(db.String(20))
    nu_telefone = db.Column(db.String(35))
    nu_fax = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_atendimento = db.relationship('TbAtendimento', primaryjoin='TbOcorrencia.co_seq_atendimento == TbAtendimento.co_seq_atendimento', backref='tb_ocorrencias')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbOcorrencia.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_ocorrencias')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbOcorrencia.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_ocorrencias')
    tb_tipo_ocorrencia = db.relationship('TbTipoOcorrencia', primaryjoin='TbOcorrencia.co_seq_tp_ocorrencia == TbTipoOcorrencia.co_seq_tp_ocorrencia', backref='tb_ocorrencias')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbOcorrencia.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_ocorrencias')



class TbOcorrenciaControleAlerta(db.Model):
    __tablename__ = 'tb_ocorrencia_controle_alerta'

    co_seq_ocorrencia_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_controle_alerta = db.Column(db.ForeignKey('tb_controle_alerta.co_seq_controle_alerta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_controle_alerta = db.Column(db.ForeignKey('tb_tipo_ocorrencia_alerta.co_seq_tp_controle_alerta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ocorrencia = db.Column(db.Numeric(8, 0), nullable=False)
    ds_ocorrencia_alerta = db.Column(db.String(2000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_controle_alerta = db.relationship('TbControleAlerta', primaryjoin='TbOcorrenciaControleAlerta.co_seq_controle_alerta == TbControleAlerta.co_seq_controle_alerta', backref='tb_ocorrencia_controle_alertas')
    tb_tipo_ocorrencia_alerta = db.relationship('TbTipoOcorrenciaAlerta', primaryjoin='TbOcorrenciaControleAlerta.co_seq_tp_controle_alerta == TbTipoOcorrenciaAlerta.co_seq_tp_controle_alerta', backref='tb_ocorrencia_controle_alertas')



class TbOcorrenciaMunicipio(db.Model):
    __tablename__ = 'tb_ocorrencia_municipio'

    co_seq_ocorrencia_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_atendimento_municipio = db.Column(db.ForeignKey('tb_atendimento_municipio.co_seq_atendimento_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_tp_ocorrencia_municipio = db.Column(db.ForeignKey('tb_tipo_ocorrencia_municipio.co_tp_ocorrencia_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ocorrencia = db.Column(db.Numeric(8, 0), nullable=False)
    obs_ocorrencia = db.Column(db.String(2000))
    no_contato = db.Column(db.String(70))
    nu_celular = db.Column(db.String(20))
    nu_telefone = db.Column(db.String(35))
    nu_fax = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_atendimento_municipio = db.relationship('TbAtendimentoMunicipio', primaryjoin='TbOcorrenciaMunicipio.co_seq_atendimento_municipio == TbAtendimentoMunicipio.co_seq_atendimento_municipio', backref='tb_ocorrencia_municipios')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbOcorrenciaMunicipio.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_ocorrencia_municipios')
    tb_tipo_ocorrencia_municipio = db.relationship('TbTipoOcorrenciaMunicipio', primaryjoin='TbOcorrenciaMunicipio.co_tp_ocorrencia_municipio == TbTipoOcorrenciaMunicipio.co_tp_ocorrencia_municipio', backref='tb_ocorrencia_municipios')



class TbOperador(db.Model):
    __tablename__ = 'tb_operador'

    co_seq_operador = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_operador = db.Column(db.String(30), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)



class TbPaciente(db.Model):
    __tablename__ = 'tb_paciente'

    co_seq_paciente = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_saida_programa = db.Column(db.ForeignKey('tb_motivo_saida_programa.co_seq_mot_saida_programa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_entrada_programa = db.Column(db.ForeignKey('tb_motivo_entrada_programa.co_seq_mot_entrada_programa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_entrada_programa = db.Column(db.Numeric(8, 0), nullable=False)
    dt_saida_programa = db.Column(db.Numeric(8, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_saida_programa = db.Column(db.Numeric(14, 0))
    aut_registro_saida_programa = db.Column(db.String(20))

    tb_motivo_entrada_programa = db.relationship('TbMotivoEntradaPrograma', primaryjoin='TbPaciente.co_seq_mot_entrada_programa == TbMotivoEntradaPrograma.co_seq_mot_entrada_programa', backref='tb_pacientes')
    tb_motivo_saida_programa = db.relationship('TbMotivoSaidaPrograma', primaryjoin='TbPaciente.co_seq_mot_saida_programa == TbMotivoSaidaPrograma.co_seq_mot_saida_programa', backref='tb_pacientes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbPaciente.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pacientes')



class TbPacienteColuna(db.Model):
    __tablename__ = 'tb_paciente_coluna'

    co_seq_paciente_coluna = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_coluna_paciente = db.Column(db.ForeignKey('tb_coluna_paciente.co_seq_coluna_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_registro_lin_con = db.Column(db.Numeric(14, 0))
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_paciente = db.relationship('TbColunaPaciente', primaryjoin='TbPacienteColuna.co_seq_coluna_paciente == TbColunaPaciente.co_seq_coluna_paciente', backref='tb_paciente_colunas')
    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbPacienteColuna.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_paciente_colunas')
    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbPacienteColuna.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_paciente_colunas')



class TbPacienteColunaAmbulatorial(db.Model):
    __tablename__ = 'tb_paciente_coluna_ambulatorial'

    co_seq_pacinte_coluna_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_coluna_paciente_amb = db.Column(db.ForeignKey('tb_coluna_paciente_anbulatorial.co_seq_coluna_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_col_item_paciente_amb = db.Column(db.ForeignKey('tb_coluna_item_paciente_amb.co_seq_col_item_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_item_ficha_amb = db.Column(db.ForeignKey('tb_item_ficha_ambulatorial.co_seq_item_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta_amb = db.Column(db.ForeignKey('tb_consulta_ambulatorio.co_seq_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_registro_lin_con = db.Column(db.Numeric(14, 0))
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    cont_col_texto_longo = db.Column(db.Text)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_item_paciente_amb = db.relationship('TbColunaItemPacienteAmb', primaryjoin='TbPacienteColunaAmbulatorial.co_seq_col_item_paciente_amb == TbColunaItemPacienteAmb.co_seq_col_item_paciente_amb', backref='tb_paciente_coluna_ambulatorials')
    tb_coluna_paciente_anbulatorial = db.relationship('TbColunaPacienteAnbulatorial', primaryjoin='TbPacienteColunaAmbulatorial.co_seq_coluna_paciente_amb == TbColunaPacienteAnbulatorial.co_seq_coluna_paciente_amb', backref='tb_paciente_coluna_ambulatorials')
    tb_consulta_ambulatorio = db.relationship('TbConsultaAmbulatorio', primaryjoin='TbPacienteColunaAmbulatorial.co_seq_consulta_amb == TbConsultaAmbulatorio.co_seq_consulta_amb', backref='tb_paciente_coluna_ambulatorials')
    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbPacienteColunaAmbulatorial.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_paciente_coluna_ambulatorials')
    tb_item_ficha_ambulatorial = db.relationship('TbItemFichaAmbulatorial', primaryjoin='TbPacienteColunaAmbulatorial.co_seq_item_ficha_amb == TbItemFichaAmbulatorial.co_seq_item_ficha_amb', backref='tb_paciente_coluna_ambulatorials')



class TbPacienteColunaItemAmb(db.Model):
    __tablename__ = 'tb_paciente_coluna_item_amb'

    co_seq_paciente_col_item_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_col_item_paciente_amb = db.Column(db.ForeignKey('tb_coluna_item_paciente_amb.co_seq_col_item_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pacinte_coluna_amb = db.Column(db.ForeignKey('tb_paciente_coluna_ambulatorial.co_seq_pacinte_coluna_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coluna_item_paciente_amb = db.relationship('TbColunaItemPacienteAmb', primaryjoin='TbPacienteColunaItemAmb.co_seq_col_item_paciente_amb == TbColunaItemPacienteAmb.co_seq_col_item_paciente_amb', backref='tb_paciente_coluna_item_ambs')
    tb_paciente_coluna_ambulatorial = db.relationship('TbPacienteColunaAmbulatorial', primaryjoin='TbPacienteColunaItemAmb.co_seq_pacinte_coluna_amb == TbPacienteColunaAmbulatorial.co_seq_pacinte_coluna_amb', backref='tb_paciente_coluna_item_ambs')



class TbPacienteDesdobramentoItem(db.Model):
    __tablename__ = 'tb_paciente_desdobramento_item'

    co_seq_paciente_desd_item_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_desd_item_paciente_amb = db.Column(db.ForeignKey('tb_desdobramento_item_paciente.co_seq_desd_item_paciente_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_paciente_col_item_amb = db.Column(db.ForeignKey('tb_paciente_coluna_item_amb.co_seq_paciente_col_item_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cont_col_numero = db.Column(db.Double(53))
    cont_col_texto = db.Column(db.String(2000))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_desdobramento_item_paciente = db.relationship('TbDesdobramentoItemPaciente', primaryjoin='TbPacienteDesdobramentoItem.co_seq_desd_item_paciente_amb == TbDesdobramentoItemPaciente.co_seq_desd_item_paciente_amb', backref='tb_paciente_desdobramento_items')
    tb_paciente_coluna_item_amb = db.relationship('TbPacienteColunaItemAmb', primaryjoin='TbPacienteDesdobramentoItem.co_seq_paciente_col_item_amb == TbPacienteColunaItemAmb.co_seq_paciente_col_item_amb', backref='tb_paciente_desdobramento_items')



class TbPainelMutacao(db.Model):
    __tablename__ = 'tb_painel_mutacao'

    co_seq_painel_mutacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_painel_mutacao = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbPainelMutacao.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_painel_mutacaos')



class TbPainelMutacaoAlelo(db.Model):
    __tablename__ = 'tb_painel_mutacao_alelo'

    co_seq_painel_mutacao_alelo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_painel_mutacao = db.Column(db.ForeignKey('tb_painel_mutacao.co_seq_painel_mutacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_alelo = db.Column(db.ForeignKey('tb_alelo.co_seq_alelo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_alelo = db.relationship('TbAlelo', primaryjoin='TbPainelMutacaoAlelo.co_seq_alelo == TbAlelo.co_seq_alelo', backref='tb_painel_mutacao_aleloes')
    tb_painel_mutacao = db.relationship('TbPainelMutacao', primaryjoin='TbPainelMutacaoAlelo.co_seq_painel_mutacao == TbPainelMutacao.co_seq_painel_mutacao', backref='tb_painel_mutacao_aleloes')



class TbPalavraChave(db.Model):
    __tablename__ = 'tb_palavra_chave'

    co_seq_palavra_chave = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_palavra_chave = db.Column(db.String(50), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbParamentroControleQualidade(db.Model):
    __tablename__ = 'tb_paramentro_controle_qualidade'

    co_seq_par_controle_qualidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_controle_qualidade = db.Column(db.ForeignKey('tb_tipo_controle_qualidade.co_seq_tp_controle_qualidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    qt_pendencia = db.Column(db.Numeric(3, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbParamentroControleQualidade.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_paramentro_controle_qualidades')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbParamentroControleQualidade.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_paramentro_controle_qualidades')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbParamentroControleQualidade.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_paramentro_controle_qualidades')
    tb_tipo_controle_qualidade = db.relationship('TbTipoControleQualidade', primaryjoin='TbParamentroControleQualidade.co_seq_tp_controle_qualidade == TbTipoControleQualidade.co_seq_tp_controle_qualidade', backref='tb_paramentro_controle_qualidades')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbParamentroControleQualidade.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_paramentro_controle_qualidades')



class TbParamentroTipoAgendamento(db.Model):
    __tablename__ = 'tb_paramentro_tipo_agendamento'

    co_seq_parametro_tp_agen = db.Column(db.Integer, primary_key=True, unique=True)
    co_seq_tp_agendamento = db.Column(db.Numeric(2, 0), nullable=False)
    nu_etiqueta = db.Column(db.Numeric(2, 0), nullable=False)
    obs_etiqueta = db.Column(db.String(50))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbParametroAgendamento(db.Model):
    __tablename__ = 'tb_parametro_agendamento'

    co_seq_parametro_agendamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_local_coleta = db.Column(db.ForeignKey('tb_local_coleta.co_seq_local_coleta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_convenio = db.Column(db.ForeignKey('tb_convenio.co_seq_convenio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    hr_agendamento = db.Column(db.String(6), nullable=False)
    nu_agendamento = db.Column(db.Numeric(2, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_convenio = db.relationship('TbConvenio', primaryjoin='TbParametroAgendamento.co_seq_convenio == TbConvenio.co_seq_convenio', backref='tb_parametro_agendamentoes')
    tb_local_coleta = db.relationship('TbLocalColeta', primaryjoin='TbParametroAgendamento.co_seq_local_coleta == TbLocalColeta.co_seq_local_coleta', backref='tb_parametro_agendamentoes')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbParametroAgendamento.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_parametro_agendamentoes')



class TbParametroAmostraSoro(db.Model):
    __tablename__ = 'tb_parametro_amostra_soro'

    co_seq_parametro_amostra_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_versao_esquema = db.Column(db.String(20))
    co_laboratorio = db.Column(db.String(20))
    co_pedido = db.Column(db.String(20))
    co_exame = db.Column(db.String(40))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    obs_arquivo_primeira_amostra = db.Column(db.String(200))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    obs_arquivo = db.Column(db.String(200))

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbParametroAmostraSoro.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_parametro_amostra_soroes')



class TbParametroArquivoEntrada(db.Model):
    __tablename__ = 'tb_parametro_arquivo_entrada'

    co_seq_parametro_arq_entrada = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.Numeric(4, 0), nullable=False)
    co_seq_tp_pos_placa = db.Column(db.Numeric(3, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_colunas = db.Column(db.String(2000), nullable=False)
    vr_coluna_1 = db.Column(db.String(200))
    vr_coluna_2 = db.Column(db.String(200))
    vr_coluna_3 = db.Column(db.String(200))
    vr_coluna_4 = db.Column(db.String(200))
    vr_coluna_5 = db.Column(db.String(200))
    vr_coluna_6 = db.Column(db.String(200))
    vr_coluna_7 = db.Column(db.String(200))
    vr_coluna_8 = db.Column(db.String(200))
    vr_coluna_9 = db.Column(db.String(200))
    vr_coluna_10 = db.Column(db.String(200))
    vr_coluna_11 = db.Column(db.String(200))
    vr_coluna_12 = db.Column(db.String(200))



class TbParametroArquivoPicotador(db.Model):
    __tablename__ = 'tb_parametro_arquivo_picotador'

    co_seq_parametro_picotador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_exame = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbParametroArquivoPicotador.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_parametro_arquivo_picotadors')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbParametroArquivoPicotador.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_parametro_arquivo_picotadors')



class TbParametroMonitoramento(db.Model):
    __tablename__ = 'tb_parametro_monitoramento'

    co_seq_par_monitoramento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_mot_comunicacao = db.Column(db.ForeignKey('tb_tipo_motivo_comunicacao.co_seq_tp_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_regra = db.Column(db.String(200), nullable=False)
    ide_analise_maternidade = db.Column(db.String(1), nullable=False)
    nu_contato_monitoramento = db.Column(db.Numeric(3, 0))
    ide_contato_site = db.Column(db.String(1), nullable=False)
    ide_analisa_ida_gestacional = db.Column(db.String(1))
    ida_gestacional_semanas = db.Column(db.Numeric(6, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_pendencia_tratamento = db.Column(db.String(1))

    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbParametroMonitoramento.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_parametro_monitoramentoes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbParametroMonitoramento.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_parametro_monitoramentoes')
    tb_tipo_motivo_comunicacao = db.relationship('TbTipoMotivoComunicacao', primaryjoin='TbParametroMonitoramento.co_seq_tp_mot_comunicacao == TbTipoMotivoComunicacao.co_seq_tp_mot_comunicacao', backref='tb_parametro_monitoramentoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbParametroMonitoramento.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_parametro_monitoramentoes')



class TbParametroTipoAgendamento(db.Model):
    __tablename__ = 'tb_parametro_tipo_agendamento'

    co_seq_parametro_tp_agen = db.Column(db.Integer, primary_key=True, unique=True)
    co_seq_tp_agendamento = db.Column(db.Numeric(2, 0), nullable=False)
    co_seq_tp_amostra = db.Column(db.Numeric(3, 0), nullable=False)
    nu_etiqueta = db.Column(db.Numeric(2, 0), nullable=False)
    obs_etiqueta = db.Column(db.String(50))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbParametroVolumeSuor(db.Model):
    __tablename__ = 'tb_parametro_volume_suor'

    co_seq_parametro_volume_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbParametroVolumeSuor.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_parametro_volume_suors')



class TbParametrosGeralSistema(db.Model):
    __tablename__ = 'tb_parametros_geral_sistema'

    co_seq_parametro_sistema = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_fase_programa = db.Column(db.ForeignKey('tb_fase_programa.co_fase_programa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_uf = db.Column(db.ForeignKey('tb_uf.co_seq_uf', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_ent_pessoa = db.Column(db.ForeignKey('tb_tipo_codigo_entrada_pessoa.co_seq_tp_ent_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    ide_autenticacao_ad = db.Column(db.String(1), nullable=False)
    dir_ad = db.Column(db.String(30), nullable=False)
    nu_seg_recep_foto = db.Column(db.Numeric(2, 0), nullable=False)
    no_centro_referencia = db.Column(db.String(200), nullable=False)
    sg_centro_referencia = db.Column(db.String(15), nullable=False)
    end_centro_referencia = db.Column(db.String(400), nullable=False)
    tel_1_centro_referencia = db.Column(db.String(30), nullable=False)
    tel_2_centro_referencia = db.Column(db.String(30), nullable=False)
    log_centro_referencia = db.Column(db.LargeBinary)
    co_interno_controle_amostra = db.Column(db.String(4), nullable=False)
    co_interno_rotina_amostra = db.Column(db.String(4), nullable=False)
    img_assinatura_laudo = db.Column(db.LargeBinary)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_analise_cadastro_amostra = db.Column(db.String(1), nullable=False)
    img_assinatura_comunicacao_1 = db.Column(db.LargeBinary)
    img_assinatura_comunicacao_2 = db.Column(db.LargeBinary)
    img_assinatura_comunicacao_3 = db.Column(db.LargeBinary)
    co_seq_colaborador_1 = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_2 = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_3 = db.Column(db.Numeric(5, 0))
    co_modelo_impressao_resultado = db.Column(db.Numeric(1, 0))
    ide_relaciona_prenatal = db.Column(db.String(1))
    co_ordem_geracao_placa = db.Column(db.Numeric(2, 0))
    ide_placa_amostra_inadequanda = db.Column(db.String(1))
    dt_liberacao_impressao = db.Column(db.Numeric(8, 0))
    co_modelo_impressao_placa = db.Column(db.Numeric(2, 0))
    ide_site_impressao_resultado = db.Column(db.String(1))
    ide_gera_ai_mot_9 = db.Column(db.String(1))
    ide_consiste_controle_cad = db.Column(db.String(1))
    ide_imprime_resultado_ai = db.Column(db.String(1))
    ide_ai_cadastro_amostra = db.Column(db.String(1))
    co_programa_ms = db.Column(db.String(15))
    dt_ini_conferencia_amostra_pf = db.Column(db.Numeric(8, 0))
    ide_gera_ai_mot_13 = db.Column(db.String(1))
    img_assinatura_laudo_prenatal = db.Column(db.LargeBinary)
    img_assinatura_com_prenatal_1 = db.Column(db.LargeBinary)
    img_assinatura_com_prenatal_2 = db.Column(db.LargeBinary)
    img_assinatura_com_prenatal_3 = db.Column(db.LargeBinary)
    co_seq_colaborador_prenatal_1 = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_prenatal_2 = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_prenatal_3 = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_laudo = db.Column(db.Numeric(5, 0))
    dt_lib_impressao_prenatal = db.Column(db.Numeric(8, 0))
    ide_controla_mot_atualizacao = db.Column(db.String(1))
    ds_email_geracao_placa = db.Column(db.String(2000))
    ide_controla_anotacao_geral = db.Column(db.String(1))
    ide_controla_busca_amostra = db.Column(db.String(1))
    ide_consiste_cep_datasus = db.Column(db.String(1))
    nu_registro_laboratorio = db.Column(db.String(50))
    nu_segundo_conf_amostra = db.Column(db.Numeric(3, 0))
    ide_res_apresentar_regional = db.Column(db.String(1))
    nu_dia_contato_verde_controle = db.Column(db.Numeric(2, 0))
    nu_dia_contato_verde_maternidade = db.Column(db.Numeric(2, 0))
    nu_dia_cadastro_dt_coleta = db.Column(db.Numeric(5, 0))
    ide_controle_reimpressao = db.Column(db.String(1))
    hr_inicio_recepcao = db.Column(db.String(5))
    hr_termino_recepcao = db.Column(db.String(5))
    ide_controle_qualidade = db.Column(db.String(1))
    ds_email_de = db.Column(db.String(200))
    sen_servido_email = db.Column(db.String(50))
    nu_porta_servido_email = db.Column(db.String(50))
    no_servido_email = db.Column(db.String(200))
    no_de_email = db.Column(db.String(200))
    ds_email_monitoramento = db.Column(db.String(200))
    no_impressora_padrao = db.Column(db.String(200))
    no_usuario_servico = db.Column(db.String(60))
    ds_senha_servico = db.Column(db.String(60))
    nu_cnes = db.Column(db.String(30))
    no_usuario_cnes = db.Column(db.String(60))
    img_cabecalho = db.Column(db.LargeBinary)
    img_rodape = db.Column(db.LargeBinary)
    co_seq_colaborador_genetica_1 = db.Column(db.Numeric(5, 0))
    co_seq_colaborador_genetica_2 = db.Column(db.Numeric(5, 0))
    ide_autenticacao_ssl = db.Column(db.String(1))
    ide_imp_etiqueta_cad_amostra = db.Column(db.String(1))
    qt_etiqueta_cad_amostra = db.Column(db.Numeric(2, 0))
    qt_minima_solicitacao_unidade = db.Column(db.Numeric(4, 0))
    ide_certificacao_laudo = db.Column(db.String(1))
    nu_serial_certificado = db.Column(db.Text)
    co_motivo_ai_dias_coleta = db.Column(db.Numeric(2, 0))
    nu_dias_coleta_ai = db.Column(db.Numeric(2, 0))
    dt_ini_certificacao = db.Column(db.Numeric(8, 0))
    nu_cnpj = db.Column(db.Numeric(11, 0))

    tb_fase_programa = db.relationship('TbFasePrograma', primaryjoin='TbParametrosGeralSistema.co_fase_programa == TbFasePrograma.co_fase_programa', backref='tb_parametros_geral_sistemas')
    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbParametrosGeralSistema.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_parametros_geral_sistemas')
    tb_tipo_codigo_entrada_pessoa = db.relationship('TbTipoCodigoEntradaPessoa', primaryjoin='TbParametrosGeralSistema.co_seq_tp_ent_pessoa == TbTipoCodigoEntradaPessoa.co_seq_tp_ent_pessoa', backref='tb_parametros_geral_sistemas')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbParametrosGeralSistema.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_parametros_geral_sistemas')
    tb_uf = db.relationship('TbUf', primaryjoin='TbParametrosGeralSistema.co_seq_uf == TbUf.co_seq_uf', backref='tb_parametros_geral_sistemas')



class TbParecerTecnico(db.Model):
    __tablename__ = 'tb_parecer_tecnico'

    co_seq_parecer_tecnico = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbParecerTecnico.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_parecer_tecnicoes')



class TbPerguntaQuestionarioSuor(db.Model):
    __tablename__ = 'tb_pergunta_questionario_suor'

    co_seq_pergunta_suor = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    ds_pergunta_suor = db.Column(db.String(200), nullable=False)



class TbPessoa(db.Model):
    __tablename__ = 'tb_pessoa'
    __table_args__ = (
        db.Index('in_pes_cosequsa_coseqtptria', 'co_seq_unidade_saude', 'co_seq_tp_triagem'),
        db.Index('in_pes_cotptriam_dthrcanc', 'co_seq_tp_triagem', 'dt_hr_cancelamento'),
        db.Index('in_pes_tptriagen_nudocmae_dthrreg_dthrcanc', 'co_seq_tp_triagem', 'nu_doc_mae', 'dt_hr_registro', 'dt_hr_cancelamento'),
        db.Index('in_pes_cotptriam_dthrcanc_dthrreg', 'co_seq_tp_triagem', 'dt_hr_cancelamento', 'dt_hr_registro'),
        db.Index('in_pes_pescopes_coent_idecoconf', 'pes_co_seq_pessoa', 'co_ent_pessoa', 'ide_co_conflito'),
        db.Index('in_pes_dthrreg_cototria_nopes', 'dt_hr_registro', 'co_seq_tp_triagem', 'no_pessoa'),
        db.Index('in_pes_pescopes_coentpes_idecoconf', 'pes_co_seq_pessoa', 'co_ent_pessoa', 'ide_co_conflito'),
        db.Index('in_pes_tptriagen_dtnasc_dthrreg_dthrcanc', 'co_seq_tp_triagem', 'dt_nascimento', 'dt_hr_registro', 'dt_hr_cancelamento'),
        db.Index('in_pes_tptriagen_nopes', 'co_seq_tp_triagem', 'no_pessoa'),
        db.Index('in_pes_idecoconf_pescoseqpes_cosequni', 'ide_co_conflito', 'pes_co_seq_pessoa', 'co_seq_unidade_saude'),
        db.Index('in_pes_tptriagen_nucns', 'co_seq_tp_triagem', 'nu_cns'),
        db.Index('in_pes_tptriagen_nopes_dtnasc', 'co_seq_tp_triagem', 'no_pessoa', 'dt_nascimento'),
        db.Index('in_pes_coent_dtnasc', 'co_ent_pessoa', 'dt_nascimento'),
        db.Index('in_pes_nudocmae_nurg_nucns_cnsmae_nu_dnv', 'nu_doc_mae', 'nu_rg', 'nu_cns', 'nu_cns_mae', 'nu_dnv'),
        db.Index('in_pes_tptriagen_nucns_dthrreg_dthrcanc', 'co_seq_tp_triagem', 'nu_cns', 'dt_hr_registro', 'dt_hr_cancelamento'),
        db.Index('in_pes_coentpes_idecoconf', 'co_ent_pessoa', 'ide_co_conflito'),
        db.Index('in_pes_tptriagen_nucns_dthrreg', 'co_seq_tp_triagem', 'nu_cns', 'dt_hr_registro'),
        db.Index('in_pes_nucns_tptriam_dthrcanc', 'nu_cns', 'co_seq_tp_triagem', 'dt_hr_cancelamento'),
        db.Index('in_pes_coseqpes_nopes', 'co_seq_pessoa', 'no_pessoa'),
        db.Index('in_pes_coseqpes_coseqtptria', 'co_seq_pessoa', 'co_seq_tp_triagem'),
        db.Index('in_pes_tptriagen_nudocmae', 'co_seq_tp_triagem', 'nu_doc_mae')
    )

    co_seq_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_obito = db.Column(db.ForeignKey('tb_motivo_obito.co_seq_mot_obito', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_cutis = db.Column(db.ForeignKey('tb_cutis.co_seq_cutis', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_parentesco = db.Column(db.ForeignKey('tb_tipo_parentesco.co_seq_tp_parentesco', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_documento = db.Column(db.ForeignKey('tb_tipo_documento.co_seq_tp_documento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_ent_pessoa = db.Column(db.ForeignKey('tb_codigo_entrada_pessoa.co_ent_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    pes_co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_co_conflito = db.Column(db.String(1), nullable=False, index=True)
    no_pessoa = db.Column(db.String(80), nullable=False, index=True)
    se_pessoa = db.Column(db.String(1), nullable=False)
    dt_nascimento = db.Column(db.Numeric(8, 0), index=True)
    hr_nascimento = db.Column(db.String(4))
    no_mae = db.Column(db.String(70))
    dt_nascimento_mae = db.Column(db.Numeric(8, 0))
    nu_cns_mae = db.Column(db.String(15), index=True)
    nu_doc_mae = db.Column(db.String(30), index=True)
    co_doc_emissor = db.Column(db.String(100))
    dt_obito = db.Column(db.Numeric(8, 0), index=True)
    nu_dnv = db.Column(db.String(20), index=True)
    nu_cns = db.Column(db.String(15), index=True)
    nu_rg = db.Column(db.String(15), index=True)
    dt_rg_emissao = db.Column(db.Numeric(8, 0))
    co_rg_emissor = db.Column(db.String(4))
    sg_rg_uf = db.Column(db.String(2))
    nu_cpf = db.Column(db.Numeric(11, 0), index=True)
    nu_certidao_registro = db.Column(db.String(100))
    nu_certidao_livro = db.Column(db.String(8))
    nu_certidao_folha = db.Column(db.String(4))
    dt_certidao_emissao = db.Column(db.Numeric(8, 0))
    pes_nascimento_grama = db.Column(db.Numeric(14, 0))
    ida_nascimento_mes = db.Column(db.Numeric(2, 0))
    ide_prematuro = db.Column(db.String(1))
    ide_parto_gemelar = db.Column(db.String(1))
    no_hosp_nascimento = db.Column(db.String(70))
    nu_registro_hosp_nascimento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_gemelar = db.Column(db.Numeric(2, 0))
    ide_triada_maternidade = db.Column(db.String(1), index=True)
    nu_protocolo_familia = db.Column(db.Numeric(8, 0))
    no_pai = db.Column(db.String(70))
    dt_nascimento_pai = db.Column(db.Numeric(8, 0))
    ide_fez_pre_natal = db.Column(db.String(1))
    ide_mae_uso_corticoide = db.Column(db.String(1))
    dt_ini_uso_corticoide_mae = db.Column(db.Numeric(8, 0))
    dt_ter_uso_corticoide_mae = db.Column(db.Numeric(8, 0))
    ds_corticoide_uso_mae = db.Column(db.String(200))
    no_pessoa_busca = db.Column(db.String(200))
    no_mae_busca = db.Column(db.String(200))

    tb_codigo_entrada_pessoa = db.relationship('TbCodigoEntradaPessoa', primaryjoin='TbPessoa.co_ent_pessoa == TbCodigoEntradaPessoa.co_ent_pessoa', backref='tb_pessoas')
    tb_cuti = db.relationship('TbCuti', primaryjoin='TbPessoa.co_seq_cutis == TbCuti.co_seq_cutis', backref='tb_pessoas')
    tb_motivo_obito = db.relationship('TbMotivoObito', primaryjoin='TbPessoa.co_seq_mot_obito == TbMotivoObito.co_seq_mot_obito', backref='tb_pessoas')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbPessoa.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_pessoas')
    tb_tipo_documento = db.relationship('TbTipoDocumento', primaryjoin='TbPessoa.co_seq_tp_documento == TbTipoDocumento.co_seq_tp_documento', backref='tb_pessoas')
    tb_tipo_parentesco = db.relationship('TbTipoParentesco', primaryjoin='TbPessoa.co_seq_tp_parentesco == TbTipoParentesco.co_seq_tp_parentesco', backref='tb_pessoas')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbPessoa.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_pessoas')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbPessoa.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_pessoas')
    parent = db.relationship('TbPessoa', remote_side=[co_seq_pessoa], primaryjoin='TbPessoa.pes_co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pessoas')



class TbPessoaCampoModificacao(db.Model):
    __tablename__ = 'tb_pessoa_campo_modificacao'

    co_seq_pessoa_campo_mod = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_campo_modificacao = db.Column(db.ForeignKey('tb_tipo_campo_modificacao.co_campo_modificacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa_mot_atualizacao = db.Column(db.ForeignKey('tb_pessoa_motivo_atualizacao.co_seq_pessoa_mot_atualizacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_atual = db.Column(db.String(2000), nullable=False)
    vr_anterior = db.Column(db.String(2000), nullable=False)

    tb_tipo_campo_modificacao = db.relationship('TbTipoCampoModificacao', primaryjoin='TbPessoaCampoModificacao.co_campo_modificacao == TbTipoCampoModificacao.co_campo_modificacao', backref='tb_pessoa_campo_modificacaos')
    tb_pessoa_motivo_atualizacao = db.relationship('TbPessoaMotivoAtualizacao', primaryjoin='TbPessoaCampoModificacao.co_seq_pessoa_mot_atualizacao == TbPessoaMotivoAtualizacao.co_seq_pessoa_mot_atualizacao', backref='tb_pessoa_campo_modificacaos')



class TbPessoaKitParticular(db.Model):
    __tablename__ = 'tb_pessoa_kit_particular'

    co_seq_pessoa_kit_particular = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbPessoaKitParticular.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pessoa_kit_particulars')



class TbPessoaMotivoAtualizacao(db.Model):
    __tablename__ = 'tb_pessoa_motivo_atualizacao'

    co_seq_pessoa_mot_atualizacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_atualizacao_cad = db.Column(db.ForeignKey('tb_motivo_atualizacao_cadastro.co_seq_mot_atualizacao_cad', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbPessoaMotivoAtualizacao.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_pessoa_motivo_atualizacaos')
    tb_motivo_atualizacao_cadastro = db.relationship('TbMotivoAtualizacaoCadastro', primaryjoin='TbPessoaMotivoAtualizacao.co_seq_mot_atualizacao_cad == TbMotivoAtualizacaoCadastro.co_seq_mot_atualizacao_cad', backref='tb_pessoa_motivo_atualizacaos')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbPessoaMotivoAtualizacao.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pessoa_motivo_atualizacaos')



class TbPessoaPreNatal(db.Model):
    __tablename__ = 'tb_pessoa_pre_natal'

    co_seq_pessoa_pre_natal = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ultima_menstruacao = db.Column(db.Numeric(8, 0))
    nu_gestacao_anterior = db.Column(db.Numeric(2, 0))
    nu_parto_anterior = db.Column(db.Numeric(2, 0))
    nu_aborto_anterior = db.Column(db.Numeric(2, 0))
    nu_sis_pre_natal = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_aborto = db.Column(db.Numeric(8, 0))
    dt_nascimento_crianca = db.Column(db.Numeric(8, 0))

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbPessoaPreNatal.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pessoa_pre_natals')



class TbPessoaProjetoPesquisa(db.Model):
    __tablename__ = 'tb_pessoa_projeto_pesquisa'

    co_seq_pessoa_pesquisa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_execucao_pesquisa = db.Column(db.ForeignKey('tb_execucao_projeto_pesquisa.co_seq_execucao_pesquisa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbPessoaProjetoPesquisa.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_pessoa_projeto_pesquisas')
    tb_execucao_projeto_pesquisa = db.relationship('TbExecucaoProjetoPesquisa', primaryjoin='TbPessoaProjetoPesquisa.co_seq_execucao_pesquisa == TbExecucaoProjetoPesquisa.co_seq_execucao_pesquisa', backref='tb_pessoa_projeto_pesquisas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbPessoaProjetoPesquisa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pessoa_projeto_pesquisas')



class TbPessoaToxoplasmosePbh(db.Model):
    __tablename__ = 'tb_pessoa_toxoplasmose_pbh'

    co_seq_pessoa_toxo_pbh = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_pessoa = db.Column(db.String(80), nullable=False)
    se_pessoa = db.Column(db.String(1))
    dt_nascimento = db.Column(db.Numeric(8, 0))
    ds_idade_pessoa = db.Column(db.String(10))
    no_mae = db.Column(db.String(70))
    nu_cns = db.Column(db.String(15))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbPessoaToxoplasmosePbh.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_pessoa_toxoplasmose_pbhs')



class TbPicoteManual(db.Model):
    __tablename__ = 'tb_picote_manual'

    co_seq_picote_manual = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbPicoteManual.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_picote_manuals')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbPicoteManual.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_picote_manuals')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbPicoteManual.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_picote_manuals')



class TbPlaca(db.Model):
    __tablename__ = 'tb_placa'
    __table_args__ = (
        db.Index('in_placa_nupla_dthrcanc', 'nu_placa', 'dt_hr_cancelamento'),
        db.Index('in_placa_nupla_dthrcanc_nuporccontint', 'nu_placa', 'nu_proc_controle_int', 'dt_hr_cancelamento'),
        db.Index('in_placa_nuseqpla_nupla_dthrcanc_nuporccontint', 'nu_seq_placa', 'nu_placa', 'nu_proc_controle_int', 'dt_hr_cancelamento')
    )

    nu_seq_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    nu_placa = db.Column(db.ForeignKey('tb_numero_placa.nu_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), index=True)
    no_placa = db.Column(db.String(50))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_numero_placa = db.relationship('TbNumeroPlaca', primaryjoin='TbPlaca.nu_placa == TbNumeroPlaca.nu_placa', backref='tb_placas')



class TbPolo(db.Model):
    __tablename__ = 'tb_polo'

    co_seq_polo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_polo = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbPortador(db.Model):
    __tablename__ = 'tb_portador'

    co_seq_portador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_distrito = db.Column(db.ForeignKey('tb_distrito.co_seq_distrito', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_portador = db.Column(db.String(70), nullable=False)
    nu_doc_identificacao = db.Column(db.String(20), nullable=False)
    nu_telefone = db.Column(db.String(35))
    nu_celular = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_distrito = db.relationship('TbDistrito', primaryjoin='TbPortador.co_seq_distrito == TbDistrito.co_seq_distrito', backref='tb_portadors')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbPortador.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_portadors')



class TbPortadorEnvio(db.Model):
    __tablename__ = 'tb_portador_envio'

    co_seq_portador_envio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_portador = db.Column(db.ForeignKey('tb_portador.co_seq_portador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_envio_material = db.Column(db.ForeignKey('tb_envio_material.co_seq_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_envio_material = db.relationship('TbEnvioMaterial', primaryjoin='TbPortadorEnvio.co_seq_envio_material == TbEnvioMaterial.co_seq_envio_material', backref='tb_portador_envios')
    tb_portador = db.relationship('TbPortador', primaryjoin='TbPortadorEnvio.co_seq_portador == TbPortador.co_seq_portador', backref='tb_portador_envios')



class TbPreparaCancResultado(db.Model):
    __tablename__ = 'tb_prepara_canc_resultado'

    co_seq_prepara_canc_resultado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_mot_canc_res = db.Column(db.ForeignKey('tb_motivo_cancelamento_resultado.co_mot_canc_res', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    aut_liberacao = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_cancelamento_resultado = db.relationship('TbMotivoCancelamentoResultado', primaryjoin='TbPreparaCancResultado.co_mot_canc_res == TbMotivoCancelamentoResultado.co_mot_canc_res', backref='tb_prepara_canc_resultadoes')
    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbPreparaCancResultado.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_prepara_canc_resultadoes')



class TbPrescricaoMedicamento(db.Model):
    __tablename__ = 'tb_prescricao_medicamento'

    co_seq_prescricao_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_medicamento = db.Column(db.ForeignKey('tb_medicamento.co_seq_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_dose_medicamento = db.Column(db.Double(53))
    dt_ini = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbPrescricaoMedicamento.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_prescricao_medicamentoes')
    tb_medicamento = db.relationship('TbMedicamento', primaryjoin='TbPrescricaoMedicamento.co_seq_medicamento == TbMedicamento.co_seq_medicamento', backref='tb_prescricao_medicamentoes')



class TbPrescricaoMedicamentoAmb(db.Model):
    __tablename__ = 'tb_prescricao_medicamento_amb'

    co_seq_prescricao_medicamento_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_consulta_amb = db.Column(db.ForeignKey('tb_consulta_ambulatorio.co_seq_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_periodo_prescricao = db.Column(db.ForeignKey('tb_tipo_periodicidade_prescricao.co_seq_tp_periodo_prescricao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_adm_medicamento = db.Column(db.ForeignKey('tb_tipo_adm_medicamento_amb.co_seq_adm_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_via_medicamento = db.Column(db.ForeignKey('tb_tipo_via_medicamento.co_seq_tp_via_medicamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_forma_prescricao = db.Column(db.ForeignKey('tb_tipo_forma_prescricao.co_seq_tp_forma_prescricao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_medicamento_amb = db.Column(db.ForeignKey('tb_medicamento_ambulatorio.co_seq_medicamento_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_dose_medicamento = db.Column(db.Double(53))
    qt_periodicidade = db.Column(db.Numeric(14, 0))
    qt_total_medicamento = db.Column(db.Numeric(14, 0))
    ide_usu_continuo = db.Column(db.String(1), nullable=False)
    ds_orientacao_medica = db.Column(db.String(2000))
    ds_orientacao_receita = db.Column(db.String(2000))
    ide_prescricao_medicamento = db.Column(db.String(1), nullable=False)
    dt_prevista_termino = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_adm_medicamento_amb = db.relationship('TbTipoAdmMedicamentoAmb', primaryjoin='TbPrescricaoMedicamentoAmb.co_seq_adm_medicamento == TbTipoAdmMedicamentoAmb.co_seq_adm_medicamento', backref='tb_prescricao_medicamento_ambs')
    tb_consulta_ambulatorio = db.relationship('TbConsultaAmbulatorio', primaryjoin='TbPrescricaoMedicamentoAmb.co_seq_consulta_amb == TbConsultaAmbulatorio.co_seq_consulta_amb', backref='tb_prescricao_medicamento_ambs')
    tb_medicamento_ambulatorio = db.relationship('TbMedicamentoAmbulatorio', primaryjoin='TbPrescricaoMedicamentoAmb.co_seq_medicamento_amb == TbMedicamentoAmbulatorio.co_seq_medicamento_amb', backref='tb_prescricao_medicamento_ambs')
    tb_tipo_forma_prescricao = db.relationship('TbTipoFormaPrescricao', primaryjoin='TbPrescricaoMedicamentoAmb.co_seq_tp_forma_prescricao == TbTipoFormaPrescricao.co_seq_tp_forma_prescricao', backref='tb_prescricao_medicamento_ambs')
    tb_tipo_periodicidade_prescricao = db.relationship('TbTipoPeriodicidadePrescricao', primaryjoin='TbPrescricaoMedicamentoAmb.co_seq_tp_periodo_prescricao == TbTipoPeriodicidadePrescricao.co_seq_tp_periodo_prescricao', backref='tb_prescricao_medicamento_ambs')
    tb_tipo_via_medicamento = db.relationship('TbTipoViaMedicamento', primaryjoin='TbPrescricaoMedicamentoAmb.co_seq_tp_via_medicamento == TbTipoViaMedicamento.co_seq_tp_via_medicamento', backref='tb_prescricao_medicamento_ambs')



class TbProcedimentoApac(db.Model):
    __tablename__ = 'tb_procedimento_apac'

    co_seq_procedimento_apac = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_procedimento_ano = db.Column(db.Numeric(4, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_nu_procedimento_ano = db.Column(db.String(20))
    ide_procedimento_ambulatorial = db.Column(db.String(1))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbProcedimentoApac.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_procedimento_apacs')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbProcedimentoApac.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_procedimento_apacs')



class TbProcedimentoCidDoenca(db.Model):
    __tablename__ = 'tb_procedimento_cid_doenca'

    co_seq_proced_cid_doenca = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca_cid = db.Column(db.ForeignKey('tb_doenca_cid.co_seq_doenca_cid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca_cid = db.relationship('TbDoencaCid', primaryjoin='TbProcedimentoCidDoenca.co_seq_doenca_cid == TbDoencaCid.co_seq_doenca_cid', backref='tb_procedimento_cid_doencas')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbProcedimentoCidDoenca.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_procedimento_cid_doencas')



class TbProfissao(db.Model):
    __tablename__ = 'tb_profissao'

    co_seq_profissao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_profissao = db.Column(db.String(100), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_cbo = db.Column(db.String(15))



class TbProfissionalDoenca(db.Model):
    __tablename__ = 'tb_profissional_doenca'

    co_seq_prof_doenca = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbProfissionalDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_profissional_doencas')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbProfissionalDoenca.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_profissional_doencas')



class TbProfissionalEspecialidade(db.Model):
    __tablename__ = 'tb_profissional_especialidade'

    co_seq_prof_especialidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_especialidade = db.Column(db.ForeignKey('tb_especialidade.co_seq_especialidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_especialidade = db.relationship('TbEspecialidade', primaryjoin='TbProfissionalEspecialidade.co_seq_especialidade == TbEspecialidade.co_seq_especialidade', backref='tb_profissional_especialidades')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbProfissionalEspecialidade.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_profissional_especialidades')



class TbProfissionalResponsavelCid(db.Model):
    __tablename__ = 'tb_profissional_responsavel_cid'

    co_seq_prof_responsavel_cid = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_cid = db.Column(db.ForeignKey('tb_cid.co_seq_cid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_cid = db.relationship('TbCid', primaryjoin='TbProfissionalResponsavelCid.co_seq_cid == TbCid.co_seq_cid', backref='tb_profissional_responsavel_cids')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbProfissionalResponsavelCid.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_profissional_responsavel_cids')



class TbProfissionalSaude(db.Model):
    __tablename__ = 'tb_profissional_saude'

    co_seq_prof_saude = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_profissao = db.Column(db.ForeignKey('tb_profissao.co_seq_profissao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_cargo = db.Column(db.ForeignKey('tb_cargo.co_seq_cargo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_prof_saude = db.Column(db.String(80), nullable=False)
    nu_cpf = db.Column(db.Numeric(11, 0))
    nu_cns = db.Column(db.String(15))
    nu_registro = db.Column(db.String(30))
    no_logradouro = db.Column(db.String(100))
    nu_logradouro = db.Column(db.String(20))
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80))
    nu_cep = db.Column(db.String(8))
    nu_celular = db.Column(db.String(20))
    nu_telefone = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    obs_prof_saude = db.Column(db.String(2000))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_cargo = db.relationship('TbCargo', primaryjoin='TbProfissionalSaude.co_seq_cargo == TbCargo.co_seq_cargo', backref='tb_profissional_saudes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbProfissionalSaude.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_profissional_saudes')
    tb_profissao = db.relationship('TbProfissao', primaryjoin='TbProfissionalSaude.co_seq_profissao == TbProfissao.co_seq_profissao', backref='tb_profissional_saudes')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbProfissionalSaude.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_profissional_saudes')



class TbProfissionalTipoTriagem(db.Model):
    __tablename__ = 'tb_profissional_tipo_triagem'

    co_seq_prof_tp_triagem = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbProfissionalTipoTriagem.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_profissional_tipo_triagems')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbProfissionalTipoTriagem.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_profissional_tipo_triagems')



class TbProfissionalUnidade(db.Model):
    __tablename__ = 'tb_profissional_unidade'

    co_seq_prof_unidade_saude = db.Column(db.Numeric(14, 0), primary_key=True, unique=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbProfissionalUnidade.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_profissional_unidades')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbProfissionalUnidade.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_profissional_unidades')



class TbProfissionalUnidadeDoenca(db.Model):
    __tablename__ = 'tb_profissional_unidade_doenca'

    co_seq_unidade_prof_doenca = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_unidade_saude = db.Column(db.ForeignKey('tb_profissional_unidade.co_seq_prof_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbProfissionalUnidadeDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_profissional_unidade_doencas')
    tb_profissional_unidade = db.relationship('TbProfissionalUnidade', primaryjoin='TbProfissionalUnidadeDoenca.co_seq_prof_unidade_saude == TbProfissionalUnidade.co_seq_prof_unidade_saude', backref='tb_profissional_unidade_doencas')



class TbProfissionalUnidadeFuncao(db.Model):
    __tablename__ = 'tb_profissional_unidade_funcao'

    co_seq_unidade_funcao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_prof_unidade_saude = db.Column(db.ForeignKey('tb_profissional_unidade.co_seq_prof_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_funcao = db.Column(db.ForeignKey('tb_funcao.co_seq_funcao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_funcao = db.relationship('TbFuncao', primaryjoin='TbProfissionalUnidadeFuncao.co_seq_funcao == TbFuncao.co_seq_funcao', backref='tb_profissional_unidade_funcaos')
    tb_profissional_unidade = db.relationship('TbProfissionalUnidade', primaryjoin='TbProfissionalUnidadeFuncao.co_seq_prof_unidade_saude == TbProfissionalUnidade.co_seq_prof_unidade_saude', backref='tb_profissional_unidade_funcaos')



class TbProgramaExecucaoProtocolo(db.Model):
    __tablename__ = 'tb_programa_execucao_protocolo'

    co_seq_programa_execucao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    no_programa_execucao = db.Column(db.String(50), nullable=False)



class TbProgramacaoGuardiao(db.Model):
    __tablename__ = 'tb_programacao_guardiao'

    co_seq_programacao_guardiao = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    dt_ini_execucao = db.Column(db.Numeric(8, 0), nullable=False)
    hr_agendamento = db.Column(db.String(6))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_envio_resultado = db.Column(db.String(1))
    ide_somente_comunicacao = db.Column(db.String(1))



class TbProgramacaoRecoleta(db.Model):
    __tablename__ = 'tb_programacao_recoleta'

    co_seq_programacao_recoleta = db.Column(db.Numeric(7, 0), primary_key=True, unique=True)
    co_seq_protocolo_recoleta = db.Column(db.ForeignKey('tb_protocolo_recoleta.co_seq_protocolo_recoleta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_tp_estado_clinico = db.Column(db.ForeignKey('tb_tipo_estado_clinico_coleta.co_tp_estado_clinico', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_comunicacao = db.Column(db.ForeignKey('tb_tipo_comunicacao.co_seq_tp_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_programacao = db.Column(db.String(100), nullable=False)
    nu_dia_dt_nascimento = db.Column(db.Numeric(5, 0))
    nu_dia_dt_coleta = db.Column(db.Numeric(5, 0))
    tp_operador_programacao = db.Column(db.String(1), nullable=False)
    ide_analise_ida = db.Column(db.String(1), nullable=False)
    ide_analise_peso = db.Column(db.String(1), nullable=False)
    ide_analise_ida_gestacional = db.Column(db.String(1), nullable=False)
    ide_analise_estado_clinico = db.Column(db.String(1), nullable=False)
    ide_analise_nu_amostra = db.Column(db.String(1), nullable=False)
    ide_triado_maternidade = db.Column(db.String(1), nullable=False)
    ida_ini = db.Column(db.Numeric(3, 0))
    ida_ter = db.Column(db.Numeric(3, 0))
    peso_ini = db.Column(db.Numeric(5, 0))
    peso_ter = db.Column(db.Numeric(5, 0))
    ida_gestacional_ini = db.Column(db.Numeric(2, 0))
    ida_gestacional_ter = db.Column(db.Numeric(2, 0))
    nu_amostra_ini = db.Column(db.Numeric(4, 0))
    nu_amostra_ter = db.Column(db.Numeric(4, 0))
    cmp_res_final = db.Column(db.String(200))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_analise_prematuro = db.Column(db.String(1))
    ide_prematuro = db.Column(db.String(1))
    ide_analise_transfusao = db.Column(db.String(1))
    ide_transfusao = db.Column(db.String(1))
    ide_analisa_uso_corticoide = db.Column(db.String(1))
    ide_uso_corticoide = db.Column(db.String(1))

    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbProgramacaoRecoleta.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_programacao_recoletas')
    tb_protocolo_recoleta = db.relationship('TbProtocoloRecoleta', primaryjoin='TbProgramacaoRecoleta.co_seq_protocolo_recoleta == TbProtocoloRecoleta.co_seq_protocolo_recoleta', backref='tb_programacao_recoletas')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbProgramacaoRecoleta.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_programacao_recoletas')
    tb_tipo_comunicacao = db.relationship('TbTipoComunicacao', primaryjoin='TbProgramacaoRecoleta.co_seq_tp_comunicacao == TbTipoComunicacao.co_seq_tp_comunicacao', backref='tb_programacao_recoletas')
    tb_tipo_estado_clinico_coleta = db.relationship('TbTipoEstadoClinicoColeta', primaryjoin='TbProgramacaoRecoleta.co_tp_estado_clinico == TbTipoEstadoClinicoColeta.co_tp_estado_clinico', backref='tb_programacao_recoletas')



class TbProjetoPesquisa(db.Model):
    __tablename__ = 'tb_projeto_pesquisa'

    co_seq_projeto_pesquisa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_externo_projeto = db.Column(db.String(30), nullable=False)
    no_projeto_pesquisa = db.Column(db.String(80), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbProtocoloRecoleta(db.Model):
    __tablename__ = 'tb_protocolo_recoleta'

    co_seq_protocolo_recoleta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_programa_execucao = db.Column(db.ForeignKey('tb_programa_execucao_protocolo.co_seq_programa_execucao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_protocolo = db.Column(db.ForeignKey('tb_tipo_protocolo.co_seq_tp_protocolo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_periodicidade = db.Column(db.ForeignKey('tb_tipo_periodicidade.co_seq_tp_periodicidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_protocolo = db.Column(db.String(200), nullable=False)
    dt_ini_execucao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_programa_execucao_protocolo = db.relationship('TbProgramaExecucaoProtocolo', primaryjoin='TbProtocoloRecoleta.co_seq_programa_execucao == TbProgramaExecucaoProtocolo.co_seq_programa_execucao', backref='tb_protocolo_recoletas')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbProtocoloRecoleta.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_protocolo_recoletas')
    tb_tipo_periodicidade = db.relationship('TbTipoPeriodicidade', primaryjoin='TbProtocoloRecoleta.co_seq_tp_periodicidade == TbTipoPeriodicidade.co_seq_tp_periodicidade', backref='tb_protocolo_recoletas')
    tb_tipo_protocolo = db.relationship('TbTipoProtocolo', primaryjoin='TbProtocoloRecoleta.co_seq_tp_protocolo == TbTipoProtocolo.co_seq_tp_protocolo', backref='tb_protocolo_recoletas')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbProtocoloRecoleta.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_protocolo_recoletas')



class TbProtocoloRecoletaAmostra(db.Model):
    __tablename__ = 'tb_protocolo_recoleta_amostra'

    co_seq_protocolo_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_programacao_recoleta = db.Column(db.ForeignKey('tb_programacao_recoleta.co_seq_programacao_recoleta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    cmp_res_final = db.Column(db.String(200), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_programacao_recoleta = db.relationship('TbProgramacaoRecoleta', primaryjoin='TbProtocoloRecoletaAmostra.co_seq_programacao_recoleta == TbProgramacaoRecoleta.co_seq_programacao_recoleta', backref='tb_protocolo_recoleta_amostras')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbProtocoloRecoletaAmostra.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_protocolo_recoleta_amostras')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbProtocoloRecoletaAmostra.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_protocolo_recoleta_amostras')



class TbProvidencia(db.Model):
    __tablename__ = 'tb_providencia'

    co_seq_providencia = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_providencia = db.Column(db.String(80), nullable=False)
    ide_pendencia_busca_ativa = db.Column(db.String(1), nullable=False)
    ide_pendencia_tratamento = db.Column(db.String(1), nullable=False)
    nu_dia_geracao_pendencia = db.Column(db.Numeric(2, 0), nullable=False)
    ide_conclusao_manual = db.Column(db.String(1))
    ide_gera_agendamento = db.Column(db.String(1))
    co_tp_agendamento = db.Column(db.Numeric(2, 0))
    ide_envia_material_soro = db.Column(db.String(1))
    ide_providencia_site = db.Column(db.String(1))



class TbQuantificacaoHemoglobina(db.Model):
    __tablename__ = 'tb_quantificacao_hemoglobina'

    co_seq_quantificacao_hb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_hb = db.Column(db.ForeignKey('tb_tipo_hemoglobina.co_seq_tp_hb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    percentual_quantificacao_hb = db.Column(db.Numeric(12, 5), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbQuantificacaoHemoglobina.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_quantificacao_hemoglobinas')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbQuantificacaoHemoglobina.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_quantificacao_hemoglobinas')
    tb_tipo_hemoglobina = db.relationship('TbTipoHemoglobina', primaryjoin='TbQuantificacaoHemoglobina.co_seq_tp_hb == TbTipoHemoglobina.co_seq_tp_hb', backref='tb_quantificacao_hemoglobinas')



class TbQueryRelatorio(db.Model):
    __tablename__ = 'tb_query_relatorio'

    co_seq_query_relatorio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_relatorio_controle = db.Column(db.ForeignKey('tb_relatorio_controle.co_seq_relatorio_controle', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)
    ds_linha = db.Column(db.String(1000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_relatorio_controle = db.relationship('TbRelatorioControle', primaryjoin='TbQueryRelatorio.co_seq_relatorio_controle == TbRelatorioControle.co_seq_relatorio_controle', backref='tb_query_relatorios')



class TbQuestionarioTesteSuor(db.Model):
    __tablename__ = 'tb_questionario_teste_suor'

    co_seq_questionario_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pergunta_suor = db.Column(db.ForeignKey('tb_pergunta_questionario_suor.co_seq_pergunta_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_item_pergunta_suor = db.Column(db.ForeignKey('tb_item_pergunta_suor.co_seq_item_pergunta_suor', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    ds_outras_resposta = db.Column(db.String(200))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_item_pergunta_suor = db.relationship('TbItemPerguntaSuor', primaryjoin='TbQuestionarioTesteSuor.co_seq_item_pergunta_suor == TbItemPerguntaSuor.co_seq_item_pergunta_suor', backref='tb_questionario_teste_suors')
    tb_pergunta_questionario_suor = db.relationship('TbPerguntaQuestionarioSuor', primaryjoin='TbQuestionarioTesteSuor.co_seq_pergunta_suor == TbPerguntaQuestionarioSuor.co_seq_pergunta_suor', backref='tb_questionario_teste_suors')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbQuestionarioTesteSuor.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_questionario_teste_suors')



t_tb_realizacao_placa = db.Table(
    'tb_realizacao_placa',
    db.Column('co_seq_tp_exame_metodo', db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('nu_seq_placa', db.ForeignKey('tb_placa.nu_seq_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('co_seq_equip_exame', db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
)



class TbRecebimentoAmostraSuor(db.Model):
    __tablename__ = 'tb_recebimento_amostra_suor'

    co_seq_recebimento_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_col_teste_suor = db.Column(db.ForeignKey('tb_coleta_teste_suor.co_seq_col_teste_suor', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_portado = db.Column(db.String(70))
    dt_recebimento_material = db.Column(db.Numeric(8, 0), nullable=False)
    hr_recebimento_material = db.Column(db.String(4), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_coleta_teste_suor = db.relationship('TbColetaTesteSuor', primaryjoin='TbRecebimentoAmostraSuor.co_seq_col_teste_suor == TbColetaTesteSuor.co_seq_col_teste_suor', backref='tb_recebimento_amostra_suors')



class TbRecebimentoMaterial(db.Model):
    __tablename__ = 'tb_recebimento_material'

    co_seq_rec_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_envio_material = db.Column(db.ForeignKey('tb_tipo_envio_material.co_seq_tp_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_portador = db.Column(db.ForeignKey('tb_portador.co_seq_portador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_recebimento_material = db.Column(db.Numeric(8, 0), nullable=False)
    nu_correio = db.Column(db.String(60))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbRecebimentoMaterial.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_recebimento_materials')
    tb_portador = db.relationship('TbPortador', primaryjoin='TbRecebimentoMaterial.co_seq_portador == TbPortador.co_seq_portador', backref='tb_recebimento_materials')
    tb_tipo_envio_material = db.relationship('TbTipoEnvioMaterial', primaryjoin='TbRecebimentoMaterial.co_seq_tp_envio_material == TbTipoEnvioMaterial.co_seq_tp_envio_material', backref='tb_recebimento_materials')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbRecebimentoMaterial.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tb_recebimento_materials')



class TbRecebimentoMaterialImagem(db.Model):
    __tablename__ = 'tb_recebimento_material_imagem'

    co_seq_img_receb_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_receb_material_unidade = db.Column(db.ForeignKey('tb_recebimento_material_unidade.co_seq_receb_material_unidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    img_receb_material = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recebimento_material_unidade = db.relationship('TbRecebimentoMaterialUnidade', primaryjoin='TbRecebimentoMaterialImagem.co_seq_receb_material_unidade == TbRecebimentoMaterialUnidade.co_seq_receb_material_unidade', backref='tb_recebimento_material_imagems')



class TbRecebimentoMaterialRecepcao(db.Model):
    __tablename__ = 'tb_recebimento_material_recepcao'

    co_seq_rec_material_recepcao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_portador = db.Column(db.ForeignKey('tb_portador.co_seq_portador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_envio_material = db.Column(db.ForeignKey('tb_tipo_envio_material.co_seq_tp_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_rec_recep_amostra = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_rec_recep_amostra = db.Column(db.Numeric(14, 0))
    dt_post_recep_amostra = db.Column(db.Numeric(8, 0))
    nu_correio = db.Column(db.String(60))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    hr_rec_recep_amostra = db.Column(db.String(4))
    hr_post_recep_amostra = db.Column(db.String(4))
    dt_hr_recebimento_laboratorio = db.Column(db.Numeric(14, 0))
    aut_recebimento_laboratorio = db.Column(db.String(20))

    tb_portador = db.relationship('TbPortador', primaryjoin='TbRecebimentoMaterialRecepcao.co_seq_portador == TbPortador.co_seq_portador', backref='tb_recebimento_material_recepcaos')
    tb_tipo_envio_material = db.relationship('TbTipoEnvioMaterial', primaryjoin='TbRecebimentoMaterialRecepcao.co_seq_tp_envio_material == TbTipoEnvioMaterial.co_seq_tp_envio_material', backref='tb_recebimento_material_recepcaos')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbRecebimentoMaterialRecepcao.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_recebimento_material_recepcaos')



class TbRecebimentoMaterialUnidade(db.Model):
    __tablename__ = 'tb_recebimento_material_unidade'

    co_seq_receb_material_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_envio_material = db.Column(db.ForeignKey('tb_tipo_envio_material.co_seq_tp_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_correio = db.Column(db.String(60))
    qt_material_receb = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20))
    dt_rec_amostra = db.Column(db.Numeric(8, 0))
    dt_post_amostra = db.Column(db.Numeric(8, 0))
    co_carac_conteudo_materia = db.Column(db.Numeric(2, 0))

    tb_tipo_envio_material = db.relationship('TbTipoEnvioMaterial', primaryjoin='TbRecebimentoMaterialUnidade.co_seq_tp_envio_material == TbTipoEnvioMaterial.co_seq_tp_envio_material', backref='tb_recebimento_material_unidades')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbRecebimentoMaterialUnidade.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_recebimento_material_unidades')



class TbRecebimentoSuorImagem(db.Model):
    __tablename__ = 'tb_recebimento_suor_imagem'

    co_seq_suor_imagem = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recebimento_suor = db.Column(db.ForeignKey('tb_recebimento_amostra_suor.co_seq_recebimento_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_tp_recep_imagem = db.Column(db.ForeignKey('tb_tipo_imagem_recepcao.co_tp_recep_imagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    img_recep_amostra = db.Column(db.LargeBinary, nullable=False)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recebimento_amostra_suor = db.relationship('TbRecebimentoAmostraSuor', primaryjoin='TbRecebimentoSuorImagem.co_seq_recebimento_suor == TbRecebimentoAmostraSuor.co_seq_recebimento_suor', backref='tb_recebimento_suor_imagems')
    tb_tipo_imagem_recepcao = db.relationship('TbTipoImagemRecepcao', primaryjoin='TbRecebimentoSuorImagem.co_tp_recep_imagem == TbTipoImagemRecepcao.co_tp_recep_imagem', backref='tb_recebimento_suor_imagems')



class TbRecepcaoAmostra(db.Model):
    __tablename__ = 'tb_recepcao_amostra'
    __table_args__ = (
        db.Index('in_recamo_idecodbarr_dthrgeretiq', 'ide_codigo_barra', 'dt_hr_geracao_etiqueta'),
        db.Index('in_recamo_coseqtptria_coseqrecp', 'co_seq_tp_triagem', 'co_seq_recep_amostra'),
        db.Index('in_recamo_coentpes_idecoconf', 'co_ent_pessoa', 'ide_co_conflito'),
        db.Index('in_recamo_coentpes_idecoconf_nuamo', 'co_ent_pessoa', 'ide_co_conflito', 'nu_amostra'),
        db.Index('in_recamo_coseqtptria_coseqamo', 'co_seq_tp_triagem', 'co_seq_amostra'),
        db.Index('in_recamo_coentpes_idecoconf_nuamo_coseqtpamo', 'co_ent_pessoa', 'ide_co_conflito', 'nu_amostra', 'co_seq_tp_amostra'),
        db.Index('in_recamo_coseqrecepamo_coseqamo', 'co_seq_recep_amostra', 'co_seq_amostra'),
        db.Index('in_recamo_coseqrecepamo_coseqamo_cosqttptria', 'co_seq_recep_amostra', 'co_seq_amostra', 'co_seq_tp_triagem')
    )

    co_seq_recep_amostra = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ent_pessoa = db.Column(db.ForeignKey('tb_codigo_entrada_pessoa.co_ent_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_amostra_labotatorio = db.Column(db.ForeignKey('tb_codigo_laboratorio.co_amostra_labotatorio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, server_default=db.FetchedValue())
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False, index=True)
    dt_rec_recep_amostra = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_post_recep_amostra = db.Column(db.Numeric(8, 0))
    dt_col_recep_amostra = db.Column(db.Numeric(8, 0))
    ide_co_conflito = db.Column(db.String(1), index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_prioridade_digitacao = db.Column(db.String(1))
    ide_codigo_barra = db.Column(db.String(1), index=True)
    dt_hr_geracao_etiqueta = db.Column(db.Numeric(14, 0), index=True)
    aut_geracao_etiqueta = db.Column(db.String(20))
    hr_rec_recep_amostra = db.Column(db.String(4))
    dt_hr_rec_recep_amostra = db.Column(db.Numeric(14, 0))
    dt_hr_envio_laboratorio = db.Column(db.Numeric(14, 0))
    aut_envio_laboratorio = db.Column(db.String(20))
    ide_letra_ilegivel = db.Column(db.String(1))
    ide_aceitou_participa_projeto = db.Column(db.String(1))
    ide_aceitou_projeto = db.Column(db.String(1))
    ide_erro_impressao_etiqueta = db.Column(db.String(1))
    vr_temperatura = db.Column(db.Numeric(14, 0))

    tb_codigo_laboratorio = db.relationship('TbCodigoLaboratorio', primaryjoin='TbRecepcaoAmostra.co_amostra_labotatorio == TbCodigoLaboratorio.co_amostra_labotatorio', backref='tb_recepcao_amostras')
    tb_codigo_entrada_pessoa = db.relationship('TbCodigoEntradaPessoa', primaryjoin='TbRecepcaoAmostra.co_ent_pessoa == TbCodigoEntradaPessoa.co_ent_pessoa', backref='tb_recepcao_amostras')
    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbRecepcaoAmostra.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_recepcao_amostras')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbRecepcaoAmostra.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_recepcao_amostras')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbRecepcaoAmostra.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_recepcao_amostras')


class TbRecepcaoDigitacaoImagem(TbRecepcaoAmostra):
    __tablename__ = 'tb_recepcao_digitacao_imagem'

    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)


class TbRecepcaoImagemDigitacao(TbRecepcaoAmostra):
    __tablename__ = 'tb_recepcao_imagem_digitacao'

    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbRecepcaoAmostraImagem(db.Model):
    __tablename__ = 'tb_recepcao_amostra_imagem'
    __table_args__ = (
        db.Index('in_recepamoimg_coseqrecepamo_cotprecepimg', 'co_seq_recep_amostra', 'co_tp_recep_imagem'),
    )

    co_seq_recep_amostra_imagem = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_tp_recep_imagem = db.Column(db.ForeignKey('tb_tipo_imagem_recepcao.co_tp_recep_imagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    img_recep_amostra = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbRecepcaoAmostraImagem.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_recepcao_amostra_imagems')
    tb_tipo_imagem_recepcao = db.relationship('TbTipoImagemRecepcao', primaryjoin='TbRecepcaoAmostraImagem.co_tp_recep_imagem == TbTipoImagemRecepcao.co_tp_recep_imagem', backref='tb_recepcao_amostra_imagems')



class TbRecepcaoAmostraImagemSoro(db.Model):
    __tablename__ = 'tb_recepcao_amostra_imagem_soro'

    co_seq_recep_soro_imagem = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_soro = db.Column(db.ForeignKey('tb_recepcao_amostra_soro.co_seq_recep_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_tp_recep_imagem = db.Column(db.ForeignKey('tb_tipo_imagem_recepcao.co_tp_recep_imagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    img_recep_amostra = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recepcao_amostra_soro = db.relationship('TbRecepcaoAmostraSoro', primaryjoin='TbRecepcaoAmostraImagemSoro.co_seq_recep_soro == TbRecepcaoAmostraSoro.co_seq_recep_soro', backref='tb_recepcao_amostra_imagem_soroes')
    tb_tipo_imagem_recepcao = db.relationship('TbTipoImagemRecepcao', primaryjoin='TbRecepcaoAmostraImagemSoro.co_tp_recep_imagem == TbTipoImagemRecepcao.co_tp_recep_imagem', backref='tb_recepcao_amostra_imagem_soroes')



class TbRecepcaoAmostraSoro(db.Model):
    __tablename__ = 'tb_recepcao_amostra_soro'

    co_seq_recep_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_col_recep_amostra = db.Column(db.Numeric(8, 0))
    hr_col_amostra = db.Column(db.String(4))
    dt_rec_recep_amostra = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    vr_volume_rec = db.Column(db.Numeric(8, 0))
    vr_volume_ter = db.Column(db.Numeric(8, 0))
    dt_post_recep_amostra = db.Column(db.Numeric(8, 0))
    hr_post_recep_amostra = db.Column(db.String(4))
    hr_rec_recep_amostra = db.Column(db.String(4))
    vr_temperatura_amostra = db.Column(db.Numeric(3, 1))

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbRecepcaoAmostraSoro.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_recepcao_amostra_soroes')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbRecepcaoAmostraSoro.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_recepcao_amostra_soroes')



class TbRecepcaoClassificacaoImagem(db.Model):
    __tablename__ = 'tb_recepcao_classificacao_imagem'

    co_seq_classificacao_img = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_classificacao_img = db.Column(db.ForeignKey('tb_tipo_classificacao_imagem.co_seq_tp_classificacao_img', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbRecepcaoClassificacaoImagem.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_recepcao_classificacao_imagems')
    tb_tipo_classificacao_imagem = db.relationship('TbTipoClassificacaoImagem', primaryjoin='TbRecepcaoClassificacaoImagem.co_seq_tp_classificacao_img == TbTipoClassificacaoImagem.co_seq_tp_classificacao_img', backref='tb_recepcao_classificacao_imagems')



class TbRecepcaoLembrete(db.Model):
    __tablename__ = 'tb_recepcao_lembrete'

    co_recepcao_lembrete = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_tp_recep_imagem = db.Column(db.ForeignKey('tb_tipo_imagem_recepcao.co_tp_recep_imagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_referencia = db.Column(db.Numeric(8, 0), nullable=False)
    img_lembrete = db.Column(db.LargeBinary, nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbRecepcaoLembrete.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_recepcao_lembretes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbRecepcaoLembrete.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_recepcao_lembretes')
    tb_tipo_imagem_recepcao = db.relationship('TbTipoImagemRecepcao', primaryjoin='TbRecepcaoLembrete.co_tp_recep_imagem == TbTipoImagemRecepcao.co_tp_recep_imagem', backref='tb_recepcao_lembretes')


class TbLembreteDigitacaoImagem(TbRecepcaoLembrete):
    __tablename__ = 'tb_lembrete_digitacao_imagem'

    co_recepcao_lembrete = db.Column(db.ForeignKey('tb_recepcao_lembrete.co_recepcao_lembrete', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)


class TbLembreteImagemDigitacao(TbRecepcaoLembrete):
    __tablename__ = 'tb_lembrete_imagem_digitacao'

    co_recepcao_lembrete = db.Column(db.ForeignKey('tb_recepcao_lembrete.co_recepcao_lembrete', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, unique=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbRecepcaoSoroComunicacao(db.Model):
    __tablename__ = 'tb_recepcao_soro_comunicacao'

    co_seq_recep_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_soro = db.Column(db.ForeignKey('tb_recepcao_amostra_soro.co_seq_recep_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbRecepcaoSoroComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_recepcao_soro_comunicacaos')
    tb_recepcao_amostra_soro = db.relationship('TbRecepcaoAmostraSoro', primaryjoin='TbRecepcaoSoroComunicacao.co_seq_recep_soro == TbRecepcaoAmostraSoro.co_seq_recep_soro', backref='tb_recepcao_soro_comunicacaos')



class TbRecepcaoSoroSolicitacao(db.Model):
    __tablename__ = 'tb_recepcao_soro_solicitacao'

    co_seq_recep_soro_solicitacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_recep_soro = db.Column(db.ForeignKey('tb_recepcao_amostra_soro.co_seq_recep_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_recepcao_amostra_soro = db.relationship('TbRecepcaoAmostraSoro', primaryjoin='TbRecepcaoSoroSolicitacao.co_seq_recep_soro == TbRecepcaoAmostraSoro.co_seq_recep_soro', backref='tb_recepcao_soro_solicitacaos')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbRecepcaoSoroSolicitacao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_recepcao_soro_solicitacaos')



class TbReenvioItemComunicacao(db.Model):
    __tablename__ = 'tb_reenvio_item_comunicacao'

    co_reenvio_item_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao_tp_mot = db.Column(db.ForeignKey('tb_comunicacao_tipo_motivo.co_seq_comunicacao_tp_mot', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    obs_conclusao = db.Column(db.String(2000), nullable=False)
    dt_hr_conclusao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_conclusao = db.Column(db.String(20), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao_tipo_motivo = db.relationship('TbComunicacaoTipoMotivo', primaryjoin='TbReenvioItemComunicacao.co_seq_comunicacao_tp_mot == TbComunicacaoTipoMotivo.co_seq_comunicacao_tp_mot', backref='tb_reenvio_item_comunicacaos')



class TbReferenciaExame(db.Model):
    __tablename__ = 'tb_referencia_exame'

    co_seq_referencia_exame = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_medida = db.Column(db.ForeignKey('tb_unidade_medida.co_seq_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_referencia_exame = db.Column(db.ForeignKey('tb_tipo_referencia_exame.co_seq_tp_referencia_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tex_referencia = db.Column(db.String(30), nullable=False)
    tex_interpretacao = db.Column(db.String(100), nullable=False)
    dt_ini_hist = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter_hist = db.Column(db.Numeric(8, 0))
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbReferenciaExame.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_referencia_exames')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbReferenciaExame.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_referencia_exames')
    tb_tipo_referencia_exame = db.relationship('TbTipoReferenciaExame', primaryjoin='TbReferenciaExame.co_seq_tp_referencia_exame == TbTipoReferenciaExame.co_seq_tp_referencia_exame', backref='tb_referencia_exames')
    tb_unidade_medida = db.relationship('TbUnidadeMedida', primaryjoin='TbReferenciaExame.co_seq_unidade_medida == TbUnidadeMedida.co_seq_unidade_medida', backref='tb_referencia_exames')



class TbReferenciaMunicipio(db.Model):
    __tablename__ = 'tb_referencia_municipio'

    co_seg_ref_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbReferenciaMunicipio.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_referencia_municipios')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbReferenciaMunicipio.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_referencia_municipios')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbReferenciaMunicipio.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_referencia_municipios')



class TbReferenciaResultadoSoroSite(db.Model):
    __tablename__ = 'tb_referencia_resultado_soro_site'

    co_seq_referencia_soro_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_exame_soro_site = db.Column(db.ForeignKey('tb_resultado_exame_soro_site.co_seq_res_exame_soro_site', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)
    tex_referencia = db.Column(db.String(30))
    tex_interpretacao = db.Column(db.String(100))

    tb_resultado_exame_soro_site = db.relationship('TbResultadoExameSoroSite', primaryjoin='TbReferenciaResultadoSoroSite.co_seq_res_exame_soro_site == TbResultadoExameSoroSite.co_seq_res_exame_soro_site', backref='tb_referencia_resultado_soro_sites')



class TbReferenciaUnidade(db.Model):
    __tablename__ = 'tb_referencia_unidade'

    co_seq_ref_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_unidade_saude = db.Column(db.ForeignKey('tb_profissional_unidade.co_seq_prof_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_profissional_unidade = db.relationship('TbProfissionalUnidade', primaryjoin='TbReferenciaUnidade.co_seq_prof_unidade_saude == TbProfissionalUnidade.co_seq_prof_unidade_saude', backref='tb_referencia_unidades')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbReferenciaUnidade.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_referencia_unidades')



class TbRegional(db.Model):
    __tablename__ = 'tb_regional'

    co_seq_regional = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_ext_regional = db.Column(db.String(20), nullable=False)
    no_regional = db.Column(db.String(70), nullable=False)
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(20), nullable=False)
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_fax = db.Column(db.String(35), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbRegional.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_regionals')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbRegional.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_regionals')



class TbRegraAiTipoExameMetodo(db.Model):
    __tablename__ = 'tb_regra_ai_tipo_exame_metodo'

    co_seq_regra_ai_tp_exame_metodo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.Numeric(5, 0))
    nu_dias_nascimento_coleta = db.Column(db.Numeric(5, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_providencia = db.Column(db.Numeric(4, 0))
    ide_menor_que = db.Column(db.String(1))
    co_mot_inadequacao = db.Column(db.Numeric(2, 0))
    obs_comunicacao = db.Column(db.String(2000))



class TbRegraEmissaoHbResultado(db.Model):
    __tablename__ = 'tb_regra_emissao_hb_resultado'

    co_seq_regra_emissao_res = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_regra_emissao_res = db.Column(db.String(200), nullable=False)



class TbReimpressaoResultado(db.Model):
    __tablename__ = 'tb_reimpressao_resultado'

    co_seq_reimpressao_res = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_mot_reimpressao = db.Column(db.ForeignKey('tb_motivo_reimpressao_resultado.co_seq_mot_reimpressao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    obs_reimpressao = db.Column(db.String(2000))
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbReimpressaoResultado.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_reimpressao_resultadoes')
    tb_motivo_reimpressao_resultado = db.relationship('TbMotivoReimpressaoResultado', primaryjoin='TbReimpressaoResultado.co_seq_mot_reimpressao == TbMotivoReimpressaoResultado.co_seq_mot_reimpressao', backref='tb_reimpressao_resultadoes')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbReimpressaoResultado.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_reimpressao_resultadoes')



class TbRelatorioControle(db.Model):
    __tablename__ = 'tb_relatorio_controle'

    co_seq_relatorio_controle = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_filtro_relatorio = db.Column(db.ForeignKey('tb_filtro_relatorio_controle.co_seq_filtro_relatorio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_relatorio = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_banco = db.Column(db.String(1))

    tb_filtro_relatorio_controle = db.relationship('TbFiltroRelatorioControle', primaryjoin='TbRelatorioControle.co_seq_filtro_relatorio == TbFiltroRelatorioControle.co_seq_filtro_relatorio', backref='tb_relatorio_controles')



class TbRelatorioUsuario(db.Model):
    __tablename__ = 'tb_relatorio_usuario'

    co_seq_relatorio_usuario = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_usuario = db.Column(db.ForeignKey('tb_usuario.co_seq_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_relatorio_controle = db.Column(db.ForeignKey('tb_relatorio_controle.co_seq_relatorio_controle', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_relatorio_controle = db.relationship('TbRelatorioControle', primaryjoin='TbRelatorioUsuario.co_seq_relatorio_controle == TbRelatorioControle.co_seq_relatorio_controle', backref='tb_relatorio_usuarios')
    tb_usuario = db.relationship('TbUsuario', primaryjoin='TbRelatorioUsuario.co_seq_usuario == TbUsuario.co_seq_usuario', backref='tb_relatorio_usuarios')



class TbRepeticaoSoroAnalise(db.Model):
    __tablename__ = 'tb_repeticao_soro_analise'

    co_seq_repeticao_soro_analise = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_amostra_repeticao = db.Column(db.Numeric(2, 0), nullable=False)
    ds_liberacao = db.Column(db.String(10), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)

    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbRepeticaoSoroAnalise.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_repeticao_soro_analises')



class TbResComunicacaoGrupoSoro(db.Model):
    __tablename__ = 'tb_res_comunicacao_grupo_soro'

    co_seq_res_com_grupo_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_lab_grupo_soro = db.Column(db.ForeignKey('tb_res_laboratorial_grupo_soro.co_seq_res_lab_grupo_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbResComunicacaoGrupoSoro.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_res_comunicacao_grupo_soroes')
    tb_res_laboratorial_grupo_soro = db.relationship('TbResLaboratorialGrupoSoro', primaryjoin='TbResComunicacaoGrupoSoro.co_seq_res_lab_grupo_soro == TbResLaboratorialGrupoSoro.co_seq_res_lab_grupo_soro', backref='tb_res_comunicacao_grupo_soroes')



class TbResImportadoSoroHpoOnline(db.Model):
    __tablename__ = 'tb_res_importado_soro_hpo_online'

    co_seq_res_soro_hipo_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_conferencia_soro = db.Column(db.ForeignKey('tb_conferencia_soro_controle.co_seq_conferencia_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_conferencia_soro_controle = db.relationship('TbConferenciaSoroControle', primaryjoin='TbResImportadoSoroHpoOnline.co_seq_conferencia_soro == TbConferenciaSoroControle.co_seq_conferencia_soro', backref='tb_res_importado_soro_hpo_onlines')



class TbResImportadoSoroOnline(db.Model):
    __tablename__ = 'tb_res_importado_soro_online'

    co_seq_res_soro_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbResImportadoSoroOnline.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_res_importado_soro_onlines')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbResImportadoSoroOnline.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_res_importado_soro_onlines')



class TbResIndividualGrupoSoro(db.Model):
    __tablename__ = 'tb_res_individual_grupo_soro'

    co_seq_res_indiv_grupo_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_soro = db.Column(db.ForeignKey('tb_resultado_laboratorial_soro.co_seq_res_laboratorial_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_lab_grupo_soro = db.Column(db.ForeignKey('tb_res_laboratorial_grupo_soro.co_seq_res_lab_grupo_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_res_laboratorial_grupo_soro = db.relationship('TbResLaboratorialGrupoSoro', primaryjoin='TbResIndividualGrupoSoro.co_seq_res_lab_grupo_soro == TbResLaboratorialGrupoSoro.co_seq_res_lab_grupo_soro', backref='tb_res_individual_grupo_soroes')
    tb_resultado_laboratorial_soro = db.relationship('TbResultadoLaboratorialSoro', primaryjoin='TbResIndividualGrupoSoro.co_seq_res_laboratorial_soro == TbResultadoLaboratorialSoro.co_seq_res_laboratorial_soro', backref='tb_res_individual_grupo_soroes')



class TbResLaboratorialGrupoSoro(db.Model):
    __tablename__ = 'tb_res_laboratorial_grupo_soro'

    co_seq_res_lab_grupo_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_interpretacao_grupo = db.Column(db.ForeignKey('tb_interpretacao_exame_grupo.co_seq_interpretacao_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_grupo_doenca = db.Column(db.ForeignKey('tb_grupo_resultado_doenca.co_seq_grupo_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    tex_res_familia = db.Column(db.String(2000))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    nu_mes_emissao_comunicacao = db.Column(db.Numeric(2, 0))
    nu_semana_comunicacao_dt_col = db.Column(db.Numeric(4, 0))
    nu_semana_emissao_comunicacao = db.Column(db.Numeric(4, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbResLaboratorialGrupoSoro.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_res_laboratorial_grupo_soroes')
    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbResLaboratorialGrupoSoro.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_res_laboratorial_grupo_soroes')
    tb_grupo_resultado_doenca = db.relationship('TbGrupoResultadoDoenca', primaryjoin='TbResLaboratorialGrupoSoro.co_seq_grupo_doenca == TbGrupoResultadoDoenca.co_seq_grupo_doenca', backref='tb_res_laboratorial_grupo_soroes')
    tb_interpretacao_exame_grupo = db.relationship('TbInterpretacaoExameGrupo', primaryjoin='TbResLaboratorialGrupoSoro.co_seq_interpretacao_grupo == TbInterpretacaoExameGrupo.co_seq_interpretacao_grupo', backref='tb_res_laboratorial_grupo_soroes')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbResLaboratorialGrupoSoro.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_res_laboratorial_grupo_soroes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbResLaboratorialGrupoSoro.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_res_laboratorial_grupo_soroes')



class TbResNaoProcessadoSerial(db.Model):
    __tablename__ = 'tb_res_nao_processado_serial'

    co_seq_res_nao_proc_serial = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_com_porta_serial = db.Column(db.ForeignKey('tb_comunicacao_porta_serial.co_seq_com_porta_serial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbResNaoProcessadoSerial.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_res_nao_processado_serials')
    tb_comunicacao_porta_serial = db.relationship('TbComunicacaoPortaSerial', primaryjoin='TbResNaoProcessadoSerial.co_seq_com_porta_serial == TbComunicacaoPortaSerial.co_seq_com_porta_serial', backref='tb_res_nao_processado_serials')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbResNaoProcessadoSerial.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_res_nao_processado_serials')



class TbResponsavelConsorcio(db.Model):
    __tablename__ = 'tb_responsavel_consorcio'

    co_seq_res_consorcio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_consorcio = db.Column(db.ForeignKey('tb_consorcio.co_seq_consorcio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_cargo = db.Column(db.ForeignKey('tb_cargo.co_seq_cargo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    no_res_consorcio = db.Column(db.String(70), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_celular = db.Column(db.String(20), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_cargo = db.relationship('TbCargo', primaryjoin='TbResponsavelConsorcio.co_seq_cargo == TbCargo.co_seq_cargo', backref='tb_responsavel_consorcios')
    tb_consorcio = db.relationship('TbConsorcio', primaryjoin='TbResponsavelConsorcio.co_seq_consorcio == TbConsorcio.co_seq_consorcio', backref='tb_responsavel_consorcios')



class TbResponsavelRegional(db.Model):
    __tablename__ = 'tb_responsavel_regional'

    co_seq_res_regional = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_cargo = db.Column(db.ForeignKey('tb_cargo.co_seq_cargo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_regional = db.Column(db.ForeignKey('tb_regional.co_seq_regional', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_res_regional = db.Column(db.String(70), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_celular = db.Column(db.String(20), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_cargo = db.relationship('TbCargo', primaryjoin='TbResponsavelRegional.co_seq_cargo == TbCargo.co_seq_cargo', backref='tb_responsavel_regionals')
    tb_regional = db.relationship('TbRegional', primaryjoin='TbResponsavelRegional.co_seq_regional == TbRegional.co_seq_regional', backref='tb_responsavel_regionals')



class TbResultadoBiologiaMolecular(db.Model):
    __tablename__ = 'tb_resultado_biologia_molecular'

    co_seq_res_biologia_molecular = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_intepretacao_genetica = db.Column(db.ForeignKey('tb_interpretacao_resultado_genetica.co_seq_intepretacao_genetica', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_painel_mutacao = db.Column(db.ForeignKey('tb_painel_mutacao.co_seq_painel_mutacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_soliciatacao_bm = db.Column(db.ForeignKey('tb_solicitacao_biologia_molecular.co_seq_soliciatacao_bm', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_biologia_molecular = db.Column(db.ForeignKey('tb_biologia_molecular.co_seq_biologia_molecular', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_resultado = db.Column(db.Numeric(8, 0))
    ds_metodologia = db.Column(db.Text)
    ds_resultado = db.Column(db.Text)
    ds_conclusao_genetica = db.Column(db.Text)
    ds_obs_resultado = db.Column(db.Text)
    ide_liberado_impressao = db.Column(db.String(1), nullable=False)
    ide_sequenciamento = db.Column(db.String(1), nullable=False)
    ide_resultado_manual = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_biologia_molecular = db.relationship('TbBiologiaMolecular', primaryjoin='TbResultadoBiologiaMolecular.co_seq_biologia_molecular == TbBiologiaMolecular.co_seq_biologia_molecular', backref='tb_resultado_biologia_moleculars')
    tb_interpretacao_resultado_genetica = db.relationship('TbInterpretacaoResultadoGenetica', primaryjoin='TbResultadoBiologiaMolecular.co_seq_intepretacao_genetica == TbInterpretacaoResultadoGenetica.co_seq_intepretacao_genetica', backref='tb_resultado_biologia_moleculars')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbResultadoBiologiaMolecular.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_resultado_biologia_moleculars')
    tb_painel_mutacao = db.relationship('TbPainelMutacao', primaryjoin='TbResultadoBiologiaMolecular.co_seq_painel_mutacao == TbPainelMutacao.co_seq_painel_mutacao', backref='tb_resultado_biologia_moleculars')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbResultadoBiologiaMolecular.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_resultado_biologia_moleculars')
    tb_solicitacao_biologia_molecular = db.relationship('TbSolicitacaoBiologiaMolecular', primaryjoin='TbResultadoBiologiaMolecular.co_seq_soliciatacao_bm == TbSolicitacaoBiologiaMolecular.co_seq_soliciatacao_bm', backref='tb_resultado_biologia_moleculars')



class TbResultadoComunicacao(db.Model):
    __tablename__ = 'tb_resultado_comunicacao'

    co_seq_res_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbResultadoComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_resultado_comunicacaos')
    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbResultadoComunicacao.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_resultado_comunicacaos')



class TbResultadoComunicacaoGrupo(db.Model):
    __tablename__ = 'tb_resultado_comunicacao_grupo'

    co_seq_res_comunicacao_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_grupo = db.Column(db.ForeignKey('tb_resultado_laboratorial_grupo.co_seq_res_laboratorial_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbResultadoComunicacaoGrupo.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_resultado_comunicacao_grupoes')
    tb_resultado_laboratorial_grupo = db.relationship('TbResultadoLaboratorialGrupo', primaryjoin='TbResultadoComunicacaoGrupo.co_seq_res_laboratorial_grupo == TbResultadoLaboratorialGrupo.co_seq_res_laboratorial_grupo', backref='tb_resultado_comunicacao_grupoes')



class TbResultadoExameSoroHpoSite(db.Model):
    __tablename__ = 'tb_resultado_exame_soro_hpo_site'

    co_seq_conf_exa_soro_hpo_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_soro_hipo_site = db.Column(db.ForeignKey('tb_resultado_soro_hpo_site.co_seq_res_soro_hipo_site', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_exame = db.Column(db.String(100), nullable=False)
    res_laboratorial = db.Column(db.String(100), nullable=False)
    ds_unidade_medida = db.Column(db.String(50), nullable=False)
    tex_referencia_res = db.Column(db.String(2000), nullable=False)

    tb_resultado_soro_hpo_site = db.relationship('TbResultadoSoroHpoSite', primaryjoin='TbResultadoExameSoroHpoSite.co_seq_res_soro_hipo_site == TbResultadoSoroHpoSite.co_seq_res_soro_hipo_site', backref='tb_resultado_exame_soro_hpo_sites')



class TbResultadoExameSoroSite(db.Model):
    __tablename__ = 'tb_resultado_exame_soro_site'

    co_seq_res_exame_soro_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_soro_site = db.Column(db.ForeignKey('tb_resultado_soro_site.co_seq_res_soro_site', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_site = db.Column(db.Numeric(5, 0), nullable=False)
    co_seq_tp_exame_metodo_site = db.Column(db.Numeric(5, 0), nullable=False)
    co_seq_amostra_soro_site = db.Column(db.Numeric(14, 0))
    ds_tp_exame = db.Column(db.String(100))
    ds_tp_metodo = db.Column(db.String(80))
    ds_unidade_medida = db.Column(db.String(50))
    tex_referencia_res = db.Column(db.String(2000))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    res_impresso = db.Column(db.String(100))
    co_seq_unidade_medida_site = db.Column(db.Numeric(3, 0))
    ds_tp_unidade_medida = db.Column(db.String(50))

    tb_resultado_soro_site = db.relationship('TbResultadoSoroSite', primaryjoin='TbResultadoExameSoroSite.co_seq_res_soro_site == TbResultadoSoroSite.co_seq_res_soro_site', backref='tb_resultado_exame_soro_sites')



class TbResultadoImportadoOnline(db.Model):
    __tablename__ = 'tb_resultado_importado_online'
    __table_args__ = (
        db.Index('in_resimponline_corecepamo_cotpexemet', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo'),
    )

    co_seq_res_importado_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame'), index=True)

    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbResultadoImportadoOnline.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_resultado_importado_onlines')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbResultadoImportadoOnline.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_resultado_importado_onlines')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbResultadoImportadoOnline.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_resultado_importado_onlines')



class TbResultadoIndividualGrupo(db.Model):
    __tablename__ = 'tb_resultado_individual_grupo'

    co_seq_res_individual_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_grupo = db.Column(db.ForeignKey('tb_resultado_laboratorial_grupo.co_seq_res_laboratorial_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbResultadoIndividualGrupo.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_resultado_individual_grupoes')
    tb_resultado_laboratorial_grupo = db.relationship('TbResultadoLaboratorialGrupo', primaryjoin='TbResultadoIndividualGrupo.co_seq_res_laboratorial_grupo == TbResultadoLaboratorialGrupo.co_seq_res_laboratorial_grupo', backref='tb_resultado_individual_grupoes')



class TbResultadoInterfaceado(db.Model):
    __tablename__ = 'tb_resultado_interfaceado'

    co_seq_res_interfaceado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial = db.Column(db.ForeignKey('tb_resultado_laboratorial.co_seq_res_laboratorial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_resultado_laboratorial = db.relationship('TbResultadoLaboratorial', primaryjoin='TbResultadoInterfaceado.co_seq_res_laboratorial == TbResultadoLaboratorial.co_seq_res_laboratorial', backref='tb_resultado_interfaceadoes')



class TbResultadoLaboratorial(db.Model):
    __tablename__ = 'tb_resultado_laboratorial'
    __table_args__ = (
        db.Index('in_reslabl_dtreg_dthrcanc', 'dt_registro', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_coseqreslab_coseqrespamo_coseqtbmet_dtreg', 'co_seq_res_laboratorial', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo', 'dt_registro'),
        db.Index('in_reslabl_co_seqreslab_dtreg', 'co_seq_res_laboratorial', 'dt_registro'),
        db.Index('in_reslabl_coseqrespamo_coseqtbmet', 'co_seq_recep_amostra', 'co_seq_tp_exame_metodo'),
        db.Index('in_reslabl_corecep_dthrcanc_cotpexamet', 'co_seq_recep_amostra', 'dt_hr_cancelamento', 'co_seq_tp_exame_metodo'),
        db.Index('in_reslabl_comotcanc_dthrcanc', 'co_mot_canc_res', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_corecep_dthrcanc_cotpexamet_dt_reg', 'co_seq_recep_amostra', 'dt_hr_cancelamento', 'co_seq_tp_exame_metodo', 'dt_registro'),
        db.Index('in_reslabl_coseqreslab_coseqrecepamo_dt_reg', 'co_seq_res_laboratorial', 'co_seq_recep_amostra', 'dt_registro'),
        db.Index('in_reslabl_dthrcanc_ideai_coseqtpexamet', 'dt_hr_cancelamento', 'ide_amostra_inadequada', 'co_seq_tp_exame_metodo'),
        db.Index('in_reslabl_cotpexa_dthrcanc', 'co_seq_tp_exame', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_coseqrecep_comotcanc_dthrcanc', 'co_seq_recep_amostra', 'co_mot_canc_res', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_cotplibgrpo_dthrcanc', 'co_seq_tp_exame_lib_grupo', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_cotpexa_coseqrecep_dthrcanc', 'co_seq_tp_exame', 'co_seq_recep_amostra', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_coseqrecep_dthrcanc_ideai', 'co_seq_recep_amostra', 'dt_hr_cancelamento', 'ide_amostra_inadequada'),
        db.Index('in_reslabl_dtreg_coseqrecepamo', 'dt_registro', 'co_seq_recep_amostra'),
        db.Index('in_reslabl_dthrcanc_dtreg_ideai', 'dt_hr_cancelamento', 'dt_registro', 'ide_amostra_inadequada'),
        db.Index('in_reslabl_coseqrecepamocanc', 'co_seq_recep_amostra', 'dt_hr_cancelamento'),
        db.Index('in_reslabl_coseqreslab_coseqrecepamo', 'co_seq_res_laboratorial', 'co_seq_recep_amostra'),
        db.Index('in_reslabl_co_seqreslab_coseqtbexamet', 'co_seq_res_laboratorial', 'co_seq_tp_exame_metodo'),
        db.Index('in_reslabl_cotplibgrpo_dthrcanc_coseqrecep', 'co_seq_tp_exame_lib_grupo', 'dt_hr_cancelamento', 'co_seq_recep_amostra')
    )

    co_seq_res_laboratorial = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_medida = db.Column(db.ForeignKey('tb_unidade_medida.co_seq_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_mot_canc_res = db.Column(db.ForeignKey('tb_motivo_cancelamento_resultado.co_mot_canc_res', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra_placa = db.Column(db.ForeignKey('tb_amostra_placa.co_seq_amostra_placa', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    tex_referencia_res = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    nu_mes_emissao_comunicacao = db.Column(db.Numeric(2, 0))
    res_laboratorial = db.Column(db.String(100))
    res_impresso = db.Column(db.String(100), index=True)
    ide_amostra_inadequada = db.Column(db.String(1), index=True)
    vr_utilizado_int = db.Column(db.String(100))
    vr_informado_analise = db.Column(db.String(100))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    co_seq_tp_exame_lib_grupo = db.Column(db.Numeric(5, 0), index=True)
    nu_dia_comunicacao_dt_coleta = db.Column(db.Numeric(8, 0))

    tb_motivo_cancelamento_resultado = db.relationship('TbMotivoCancelamentoResultado', primaryjoin='TbResultadoLaboratorial.co_mot_canc_res == TbMotivoCancelamentoResultado.co_mot_canc_res', backref='tb_resultado_laboratorials')
    tb_amostra_placa = db.relationship('TbAmostraPlaca', primaryjoin='TbResultadoLaboratorial.co_seq_amostra_placa == TbAmostraPlaca.co_seq_amostra_placa', backref='tb_resultado_laboratorials')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbResultadoLaboratorial.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_resultado_laboratorials')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbResultadoLaboratorial.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_resultado_laboratorials')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbResultadoLaboratorial.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_resultado_laboratorials')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbResultadoLaboratorial.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_resultado_laboratorials')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbResultadoLaboratorial.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_resultado_laboratorials')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbResultadoLaboratorial.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_resultado_laboratorials')
    tb_unidade_medida = db.relationship('TbUnidadeMedida', primaryjoin='TbResultadoLaboratorial.co_seq_unidade_medida == TbUnidadeMedida.co_seq_unidade_medida', backref='tb_resultado_laboratorials')



class TbResultadoLaboratorialGrupo(db.Model):
    __tablename__ = 'tb_resultado_laboratorial_grupo'
    __table_args__ = (
        db.Index('in_reslabgrp_coseqreslab_coseqrecepamo', 'co_seq_res_laboratorial_grupo', 'co_seq_recep_amostra'),
        db.Index('in_reslabgrp_dthrcanc_coseqrecepamo', 'dt_hr_cancelamento', 'co_seq_recep_amostra')
    )

    co_seq_res_laboratorial_grupo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_interpretacao_grupo = db.Column(db.ForeignKey('tb_interpretacao_exame_grupo.co_seq_interpretacao_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_recep_amostra = db.Column(db.ForeignKey('tb_recepcao_amostra.co_seq_recep_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_grupo_doenca = db.Column(db.ForeignKey('tb_grupo_resultado_doenca.co_seq_grupo_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    nu_mes_emissao_comunicacao = db.Column(db.Numeric(2, 0))
    nu_semana_comunicacao_dt_col = db.Column(db.Numeric(4, 0))
    nu_semana_emissao_comunicacao = db.Column(db.Numeric(4, 0))
    dt_proxima_col = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbResultadoLaboratorialGrupo.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_resultado_laboratorial_grupoes')
    tb_grupo_resultado_doenca = db.relationship('TbGrupoResultadoDoenca', primaryjoin='TbResultadoLaboratorialGrupo.co_seq_grupo_doenca == TbGrupoResultadoDoenca.co_seq_grupo_doenca', backref='tb_resultado_laboratorial_grupoes')
    tb_interpretacao_exame_grupo = db.relationship('TbInterpretacaoExameGrupo', primaryjoin='TbResultadoLaboratorialGrupo.co_seq_interpretacao_grupo == TbInterpretacaoExameGrupo.co_seq_interpretacao_grupo', backref='tb_resultado_laboratorial_grupoes')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbResultadoLaboratorialGrupo.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_resultado_laboratorial_grupoes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbResultadoLaboratorialGrupo.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_resultado_laboratorial_grupoes')
    tb_recepcao_amostra = db.relationship('TbRecepcaoAmostra', primaryjoin='TbResultadoLaboratorialGrupo.co_seq_recep_amostra == TbRecepcaoAmostra.co_seq_recep_amostra', backref='tb_resultado_laboratorial_grupoes')



class TbResultadoLaboratorialSoro(db.Model):
    __tablename__ = 'tb_resultado_laboratorial_soro'

    co_seq_res_laboratorial_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_analise_soro = db.Column(db.ForeignKey('tb_analise_amostra_soro.co_seq_analise_soro', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra_soro_tp_exame = db.Column(db.ForeignKey('tb_amostra_soro_tipo_exame.co_seq_amostra_soro_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_medida = db.Column(db.ForeignKey('tb_unidade_medida.co_seq_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    res_impresso = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    tex_referencia_res = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_amostra_soro_tipo_exame = db.relationship('TbAmostraSoroTipoExame', primaryjoin='TbResultadoLaboratorialSoro.co_seq_amostra_soro_tp_exame == TbAmostraSoroTipoExame.co_seq_amostra_soro_tp_exame', backref='tb_resultado_laboratorial_soroes')
    tb_analise_amostra_soro = db.relationship('TbAnaliseAmostraSoro', primaryjoin='TbResultadoLaboratorialSoro.co_seq_analise_soro == TbAnaliseAmostraSoro.co_seq_analise_soro', backref='tb_resultado_laboratorial_soroes')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbResultadoLaboratorialSoro.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_resultado_laboratorial_soroes')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbResultadoLaboratorialSoro.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_resultado_laboratorial_soroes')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbResultadoLaboratorialSoro.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_resultado_laboratorial_soroes')
    tb_unidade_medida = db.relationship('TbUnidadeMedida', primaryjoin='TbResultadoLaboratorialSoro.co_seq_unidade_medida == TbUnidadeMedida.co_seq_unidade_medida', backref='tb_resultado_laboratorial_soroes')



class TbResultadoLaboratorialSuor(db.Model):
    __tablename__ = 'tb_resultado_laboratorial_suor'

    co_seq_res_laboratorial_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_medida = db.Column(db.ForeignKey('tb_unidade_medida.co_seq_unidade_medida', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_analise_suor = db.Column(db.ForeignKey('tb_analise_teste_suor.co_seq_analise_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_mot_canc_res = db.Column(db.ForeignKey('tb_motivo_cancelamento_resultado.co_mot_canc_res', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_referencia_res = db.Column(db.String(2000))
    obs_res_impresso = db.Column(db.String(2000))
    res_impresso = db.Column(db.String(100))
    res_laboratorial = db.Column(db.String(100))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    vr_informado_analise = db.Column(db.String(100))

    tb_motivo_cancelamento_resultado = db.relationship('TbMotivoCancelamentoResultado', primaryjoin='TbResultadoLaboratorialSuor.co_mot_canc_res == TbMotivoCancelamentoResultado.co_mot_canc_res', backref='tb_resultado_laboratorial_suors')
    tb_analise_teste_suor = db.relationship('TbAnaliseTesteSuor', primaryjoin='TbResultadoLaboratorialSuor.co_seq_analise_suor == TbAnaliseTesteSuor.co_seq_analise_suor', backref='tb_resultado_laboratorial_suors')
    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbResultadoLaboratorialSuor.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_resultado_laboratorial_suors')
    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbResultadoLaboratorialSuor.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_resultado_laboratorial_suors')
    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbResultadoLaboratorialSuor.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_resultado_laboratorial_suors')
    tb_unidade_medida = db.relationship('TbUnidadeMedida', primaryjoin='TbResultadoLaboratorialSuor.co_seq_unidade_medida == TbUnidadeMedida.co_seq_unidade_medida', backref='tb_resultado_laboratorial_suors')



class TbResultadoOutroLaboratorio(db.Model):
    __tablename__ = 'tb_resultado_outro_laboratorio'

    co_seq_res_outro_laboratorio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_operador = db.Column(db.ForeignKey('tb_operador.co_seq_operador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_resultado = db.Column(db.Numeric(8, 0), nullable=False)
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    ide_res_alterado = db.Column(db.String(1), nullable=False)
    ide_res_quantitativo = db.Column(db.String(1), nullable=False)
    vr_res_outro_laboratorio = db.Column(db.String(30), nullable=False)
    ds_metodo_outro_laboratorio = db.Column(db.String(50), nullable=False)
    vr_ref_ini_outro_laboratorio = db.Column(db.String(30))
    vr_ref_ter_outro_laboratorio = db.Column(db.String(30))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_unidade_saude = db.Column(db.Numeric(8, 0))

    tb_operador = db.relationship('TbOperador', primaryjoin='TbResultadoOutroLaboratorio.co_seq_operador == TbOperador.co_seq_operador', backref='tb_resultado_outro_laboratorios')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbResultadoOutroLaboratorio.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_resultado_outro_laboratorios')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbResultadoOutroLaboratorio.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_resultado_outro_laboratorios')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbResultadoOutroLaboratorio.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_resultado_outro_laboratorios')



class TbResultadoSoroComunicacao(db.Model):
    __tablename__ = 'tb_resultado_soro_comunicacao'

    co_seq_res_soro_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_res_laboratorial_soro = db.Column(db.ForeignKey('tb_resultado_laboratorial_soro.co_seq_res_laboratorial_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbResultadoSoroComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_resultado_soro_comunicacaos')
    tb_resultado_laboratorial_soro = db.relationship('TbResultadoLaboratorialSoro', primaryjoin='TbResultadoSoroComunicacao.co_seq_res_laboratorial_soro == TbResultadoLaboratorialSoro.co_seq_res_laboratorial_soro', backref='tb_resultado_soro_comunicacaos')



class TbResultadoSoroHpoSite(db.Model):
    __tablename__ = 'tb_resultado_soro_hpo_site'

    co_seq_res_soro_hipo_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_conferencia_soro_site = db.Column(db.Numeric(10, 0), nullable=False)
    co_seq_amostra_site = db.Column(db.Numeric(14, 0), nullable=False)
    co_seq_amostra_soro_site = db.Column(db.Numeric(14, 0), nullable=False)
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0), nullable=False)
    co_ent_pessoa_site = db.Column(db.String(20))
    no_municipio = db.Column(db.String(70))
    no_prof_saude = db.Column(db.String(80))
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    dt_rec_amostra = db.Column(db.Numeric(8, 0))
    no_pessoa = db.Column(db.String(80))
    tex_repasse_res = db.Column(db.String(4000))
    nu_fax = db.Column(db.String(35))
    nu_telefone = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    no_prof_responsavel_soro = db.Column(db.String(80))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_impressao_resultado = db.Column(db.Numeric(14, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False)
    dt_referencia = db.Column(db.Numeric(8, 0))



class TbResultadoSoroPortaSerial(db.Model):
    __tablename__ = 'tb_resultado_soro_porta_serial'

    co_seq_res_soro_porta_serial = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_analise_soro = db.Column(db.ForeignKey('tb_analise_amostra_soro.co_seq_analise_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_com_porta_serial = db.Column(db.ForeignKey('tb_comunicacao_porta_serial.co_seq_com_porta_serial', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_proc_controle_int = db.Column(db.Numeric(14, 0), nullable=False)

    tb_analise_amostra_soro = db.relationship('TbAnaliseAmostraSoro', primaryjoin='TbResultadoSoroPortaSerial.co_seq_analise_soro == TbAnaliseAmostraSoro.co_seq_analise_soro', backref='tb_resultado_soro_porta_serials')
    tb_comunicacao_porta_serial = db.relationship('TbComunicacaoPortaSerial', primaryjoin='TbResultadoSoroPortaSerial.co_seq_com_porta_serial == TbComunicacaoPortaSerial.co_seq_com_porta_serial', backref='tb_resultado_soro_porta_serials')



class TbResultadoSoroSite(db.Model):
    __tablename__ = 'tb_resultado_soro_site'
    __table_args__ = (
        db.Index('in_ressorsit_dthrcanc_dthrimpres_cousasausit', 'dt_hr_cancelamento', 'dt_hr_impressao_resultado', 'co_seq_unidade_saude_site'),
        db.Index('in_ressorsit_cotptriasit_cousasit_dthrcanc', 'co_seq_tp_triagem_site', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento'),
        db.Index('in_ressorsit_cotptriasit_cousasit', 'co_seq_tp_triagem_site', 'co_seq_unidade_saude_site'),
        db.Index('in_ressorsit_dthrcanc_cousasausit', 'dt_hr_cancelamento', 'co_seq_unidade_saude_site')
    )

    co_seq_res_soro_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0), nullable=False)
    co_seq_mot_comunicacao_site = db.Column(db.Numeric(4, 0))
    co_seq_providencia_site = db.Column(db.Numeric(4, 0))
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    co_seq_amostra_site = db.Column(db.Numeric(14, 0), nullable=False)
    no_pessoa = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.Numeric(8, 0))
    no_logradouro = db.Column(db.String(100))
    nu_logradouro = db.Column(db.String(20))
    no_municipio = db.Column(db.String(70))
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80))
    nu_telefone = db.Column(db.String(35))
    ds_cid = db.Column(db.String(40))
    ds_procedimento = db.Column(db.String(200))
    nu_cns = db.Column(db.String(15))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    dt_col_amostra = db.Column(db.Numeric(8, 0))
    dt_resultado = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_impressao_resultado = db.Column(db.Numeric(14, 0), index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_endereco_formatado = db.Column(db.String(200))
    ide_assinatura_impressao_soro = db.Column(db.String(1))
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False)
    co_seq_tp_triagem_site = db.Column(db.Numeric(2, 0), index=True)



class TbResultadoSuorComunicacao(db.Model):
    __tablename__ = 'tb_resultado_suor_comunicacao'

    co_seq_res_suor_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_res_laboratorial_suor = db.Column(db.ForeignKey('tb_resultado_laboratorial_suor.co_seq_res_laboratorial_suor', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbResultadoSuorComunicacao.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_resultado_suor_comunicacaos')
    tb_resultado_laboratorial_suor = db.relationship('TbResultadoLaboratorialSuor', primaryjoin='TbResultadoSuorComunicacao.co_seq_res_laboratorial_suor == TbResultadoLaboratorialSuor.co_seq_res_laboratorial_suor', backref='tb_resultado_suor_comunicacaos')



class TbResultadoToxoplasmosePbh(db.Model):
    __tablename__ = 'tb_resultado_toxoplasmose_pbh'

    co_seq_res_toxo_pbh = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_interpretacao = db.Column(db.ForeignKey('tb_interpretacao_exame.co_seq_interpretacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_exame_pbh = db.Column(db.ForeignKey('tb_tipo_exame_pbh.co_seq_tp_exame_pbh', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa_toxo_pbh = db.Column(db.ForeignKey('tb_pessoa_toxoplasmose_pbh.co_seq_pessoa_toxo_pbh', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_nuped_pbh = db.Column(db.String(30))
    dt_pedido_pbh = db.Column(db.String(30), nullable=False)
    ds_unidade_distrito_pbh = db.Column(db.String(80))
    dt_ultimo_mestruacao_pbh = db.Column(db.String(10))
    co_unidade_pbh = db.Column(db.String(20))
    no_unidade_pbh = db.Column(db.String(80), nullable=False)
    co_exame_pbh = db.Column(db.String(10), nullable=False)
    no_exame_pbh = db.Column(db.String(80), nullable=False)
    no_usuario_pbh = db.Column(db.String(80), nullable=False)
    ds_sexo_pbh = db.Column(db.String(1))
    dt_nascimento_pbh = db.Column(db.String(10))
    ds_idade_pbh = db.Column(db.String(10))
    co_tp_exame_pbh = db.Column(db.String(5), nullable=False)
    ds_tp_exame_pbh = db.Column(db.String(80), nullable=False)
    vr_resultado_pbh = db.Column(db.String(100), nullable=False)
    ds_resultado_pbh = db.Column(db.String(100), nullable=False)
    ds_comunicacao_pbh = db.Column(db.String(100))
    dt_resultado_pbh = db.Column(db.String(20), nullable=False)
    no_mae_pbh = db.Column(db.String(80))
    nu_cns_pbh = db.Column(db.String(40))
    dt_resultado = db.Column(db.Numeric(8, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0))
    ide_sus_pbh = db.Column(db.String(1))
    co_unidade_pbh_1 = db.Column(db.String(20))
    ds_interpretacao_res_pbh = db.Column(db.String(100))
    ide_res_divergente = db.Column(db.String(1))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))

    tb_interpretacao_exame = db.relationship('TbInterpretacaoExame', primaryjoin='TbResultadoToxoplasmosePbh.co_seq_interpretacao == TbInterpretacaoExame.co_seq_interpretacao', backref='tb_resultado_toxoplasmose_pbhs')
    tb_pessoa_toxoplasmose_pbh = db.relationship('TbPessoaToxoplasmosePbh', primaryjoin='TbResultadoToxoplasmosePbh.co_seq_pessoa_toxo_pbh == TbPessoaToxoplasmosePbh.co_seq_pessoa_toxo_pbh', backref='tb_resultado_toxoplasmose_pbhs')
    tb_tipo_exame_pbh = db.relationship('TbTipoExamePbh', primaryjoin='TbResultadoToxoplasmosePbh.co_seq_tp_exame_pbh == TbTipoExamePbh.co_seq_tp_exame_pbh', backref='tb_resultado_toxoplasmose_pbhs')



class TbResultadoTriagemNeonatal(db.Model):
    __tablename__ = 'tb_resultado_triagem_neonatal'
    __table_args__ = (
        db.Index('in_resneonat_coseqpes_dthrcanc', 'co_seq_pessoa_site', 'dt_hr_cancelamento'),
        db.Index('in_resneonat_cosequsa_dthrcanc', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento'),
        db.Index('in_resneonat_cosequsa_dthrcanc_cdentpes', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento', 'co_ent_pessoa_site'),
        db.Index('in_resneonat_cosequsa_dthrcanc_dthrimp', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento', 'dt_hr_impressao_resultado'),
        db.Index('in_resneonat_cosequsa_dthrcanc_dtreg', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento', 'dt_registro'),
        db.Index('in_resneonat_cosequsa_dthrcanc_nopes', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento', 'no_pessoa')
    )

    co_seq_res_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False, index=True)
    no_pessoa = db.Column(db.String(80), nullable=False, index=True)
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False, index=True)
    dt_nascimento = db.Column(db.Numeric(8, 0), index=True)
    dt_col_amostra = db.Column(db.Numeric(8, 0), index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    co_seq_res_laboratorial_site = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    co_seq_amostra_placa_site = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    co_seq_recep_amostra_site = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    co_seq_mot_comunicacao_site = db.Column(db.Numeric(4, 0))
    co_seq_providencia_site = db.Column(db.Numeric(4, 0))
    tex_res_controle_tratamento = db.Column(db.String(2000), nullable=False)
    tex_res_familia = db.Column(db.String(2000), nullable=False)
    tex_res_municipio = db.Column(db.String(2000), nullable=False)
    tex_referencia_res = db.Column(db.String(2000), nullable=False)
    obs_res_impresso = db.Column(db.String(2000), nullable=False)
    nu_mes_emissao_comunicacao = db.Column(db.Numeric(2, 0))
    res_laboratorial = db.Column(db.String(100), nullable=False)
    res_impresso = db.Column(db.String(100), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_seq_unidade_medida_site = db.Column(db.Numeric(3, 0), index=True)
    ide_amostra_inadequada = db.Column(db.String(1), nullable=False)
    vr_utilizado_int = db.Column(db.String(100), nullable=False)
    vr_informado_analise = db.Column(db.String(100), nullable=False)
    co_seq_tp_exame_metodo_site = db.Column(db.Numeric(5, 0), nullable=False, index=True)
    no_doenca = db.Column(db.String(50), nullable=False)
    ds_tp_exame = db.Column(db.String(100), nullable=False)
    ds_tp_metodo = db.Column(db.String(80), nullable=False)
    ds_unidade_medida = db.Column(db.String(50), nullable=False)
    no_municipio = db.Column(db.String(70), nullable=False)
    no_unidade_saude = db.Column(db.String(100), nullable=False)
    ds_tp_material_coletado = db.Column(db.String(50), nullable=False)
    ide_controle_medico = db.Column(db.String(1))
    dt_rec_amostra = db.Column(db.Numeric(8, 0), index=True)
    no_logradouro = db.Column(db.String(100))
    nu_logradouro = db.Column(db.String(20))
    cmp_nr_logradouro = db.Column(db.String(20))
    no_bairro = db.Column(db.String(80))
    no_municipio_pessoa = db.Column(db.String(50))
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    dt_hr_impressao_resultado = db.Column(db.Numeric(14, 0), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_impressao = db.Column(db.Numeric(8, 0), index=True)
    ds_endereco_formatado = db.Column(db.String(200))
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0))
    dt_ultimo_resultado = db.Column(db.Numeric(8, 0))
    vr_informado_analise_retificacao = db.Column(db.String(200))
    dt_hr_cancelamento_retificacao = db.Column(db.Numeric(14, 0))
    ide_amostra_inadequada_retificacao = db.Column(db.String(1))
    ds_unidade_medida_retificacao = db.Column(db.String(50))
    ds_mot_canc_res_retificacao = db.Column(db.String(200))
    tex_referencia_res_retificacao = db.Column(db.String(2000))
    tex_res_familia_retificacao = db.Column(db.String(2000))
    ide_laudo_retificacao = db.Column(db.String(1))
    co_seq_tp_exame_site = db.Column(db.Numeric(5, 0), index=True)
    ds_hash = db.Column(db.String(200))



class TbResultadoTriagemPrenatal(db.Model):
    __tablename__ = 'tb_resultado_triagem_prenatal'
    __table_args__ = (
        db.Index('in_restriprenat_cosequsa_dthrcanc', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento'),
        db.Index('in_restriprenat_cosequsa_dthrcanc_dtproxcol', 'co_seq_unidade_saude_site', 'dt_hr_cancelamento', 'dt_proxima_col')
    )

    co_seq_res_site_prenatal = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False, index=True)
    no_pessoa = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.Numeric(8, 0), index=True)
    dt_col_amostra = db.Column(db.Numeric(8, 0), index=True)
    nu_amostra = db.Column(db.Numeric(5, 0), nullable=False)
    dt_resultado = db.Column(db.Numeric(8, 0), index=True)
    co_seq_mot_comunicacao_site = db.Column(db.Numeric(4, 0))
    co_seq_providencia_site = db.Column(db.Numeric(4, 0))
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    ds_tp_metodo_igm = db.Column(db.String(60))
    ds_tp_metodo_igg = db.Column(db.String(60))
    tex_res_controle_tratamento = db.Column(db.String(2000))
    tex_res_familia = db.Column(db.String(2000))
    tex_res_municipio = db.Column(db.String(2000))
    ds_tp_material_coletado = db.Column(db.String(50))
    no_logradouro = db.Column(db.String(100))
    nu_logradouro = db.Column(db.String(20))
    cmp_nr_logradouro = db.Column(db.String(20))
    ds_bairro = db.Column(db.String(80))
    resultado_igm = db.Column(db.String(100), nullable=False)
    resultado_igg = db.Column(db.String(100), nullable=False)
    co_seq_res_laboratorial_igm_1 = db.Column(db.Numeric(14, 0), nullable=False)
    co_seq_res_laboratorial_igm_2 = db.Column(db.Numeric(14, 0), nullable=False)
    dt_resultado_igm_1 = db.Column(db.Numeric(8, 0))
    dt_resultado_igm_2 = db.Column(db.Numeric(8, 0))
    resultado_igm_1 = db.Column(db.String(100))
    resultado_igm_2 = db.Column(db.String(100))
    co_seq_res_laboratorial_igg_1 = db.Column(db.Numeric(14, 0))
    co_seq_res_laboratorial_igg_2 = db.Column(db.Numeric(14, 0))
    dt_resultado_igg_1 = db.Column(db.Numeric(8, 0))
    dt_resultado_igg_2 = db.Column(db.Numeric(8, 0))
    resultado_igg_1 = db.Column(db.String(100))
    resultado_igg_2 = db.Column(db.String(100))
    no_municipio = db.Column(db.String(70))
    dt_proxima_col = db.Column(db.Numeric(8, 0), index=True)
    co_seq_res_laboratorial_igm = db.Column(db.Numeric(14, 0))
    co_seq_res_laboratorial_igg = db.Column(db.Numeric(14, 0))
    co_seq_res_laboratorial_grupo_site = db.Column(db.Numeric(14, 0))
    co_seq_recep_amostra_site = db.Column(db.Numeric(14, 0), nullable=False, index=True)
    co_seq_pessoa_site = db.Column(db.Numeric(10, 0), nullable=False, index=True)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_impressao_resultado = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_rec_amostra = db.Column(db.Numeric(8, 0))
    ds_endereco_formatado = db.Column(db.String(200))
    dt_col_amostra_1 = db.Column(db.Numeric(8, 0))
    dt_col_amostra_2 = db.Column(db.Numeric(8, 0))
    nu_telefone = db.Column(db.String(35))
    co_seq_comunicacao_site = db.Column(db.Numeric(8, 0))
    ida_gestacional_semanas = db.Column(db.Numeric(6, 0))
    dt_hr_cancelamento_retificacao_igm = db.Column(db.Numeric(14, 0))
    ds_mot_canc_res_retificacao_igm = db.Column(db.String(100))
    res_impresso_retificacao_igm = db.Column(db.String(100))
    dt_hr_cancelamento_retificacao_igg = db.Column(db.Numeric(14, 0))
    ds_mot_canc_res_retificacao_igg = db.Column(db.String(100))
    res_impresso_retificacao_igg = db.Column(db.String(100))



class TbResumoAtendimento(db.Model):
    __tablename__ = 'tb_resumo_atendimento'

    co_seq_resulmo_consulta_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_consulta_amb = db.Column(db.ForeignKey('tb_consulta_ambulatorio.co_seq_consulta_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_resulmo_consulta_amb = db.Column(db.Text, nullable=False)
    ds_hma = db.Column(db.Text)
    ds_exame_fisico = db.Column(db.Text)
    nu_peso_paciente = db.Column(db.Numeric(5, 2))
    nu_altura_paciente = db.Column(db.Numeric(5, 2))
    nu_frequencia_cardiaca = db.Column(db.Numeric(8, 3))
    nu_frequencia_respiratoria = db.Column(db.Numeric(8, 3))
    nu_imc = db.Column(db.Numeric(8, 3))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_consulta_ambulatorio = db.relationship('TbConsultaAmbulatorio', primaryjoin='TbResumoAtendimento.co_seq_consulta_amb == TbConsultaAmbulatorio.co_seq_consulta_amb', backref='tb_resumo_atendimentoes')



class TbSecaoFichaAtendimento(db.Model):
    __tablename__ = 'tb_secao_ficha_atendimento'

    co_seq_secao_ficha_amb = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_grupo_ficha_amb = db.Column(db.ForeignKey('tb_grupo_ficha_atendimento.co_seq_grupo_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ficha_amb = db.Column(db.ForeignKey('tb_ficha_ambulatorial.co_seq_ficha_amb', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_secao = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_ordem = db.Column(db.Numeric(8, 0), nullable=False)
    ide_multline = db.Column(db.String(1))
    nu_coluna = db.Column(db.Numeric(2, 0), nullable=False)
    ide_historico_secao = db.Column(db.String(1))

    tb_ficha_ambulatorial = db.relationship('TbFichaAmbulatorial', primaryjoin='TbSecaoFichaAtendimento.co_seq_ficha_amb == TbFichaAmbulatorial.co_seq_ficha_amb', backref='tb_secao_ficha_atendimentoes')
    tb_grupo_ficha_atendimento = db.relationship('TbGrupoFichaAtendimento', primaryjoin='TbSecaoFichaAtendimento.co_seq_grupo_ficha_amb == TbGrupoFichaAtendimento.co_seq_grupo_ficha_amb', backref='tb_secao_ficha_atendimentoes')



class TbSetorEncaminhamento(db.Model):
    __tablename__ = 'tb_setor_encaminhamento'

    co_seq_enc_setor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_enc_setor = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbSistema(db.Model):
    __tablename__ = 'tb_sistema'

    co_seq_sistema = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_sistema = db.Column(db.String(50), nullable=False)



class TbSolicitacaoAtualizacao(db.Model):
    __tablename__ = 'tb_solicitacao_atualizacao'

    co_seq_solicitacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_item_solicitacao = db.Column(db.ForeignKey('tb_item_solicitacao_atualizacao.co_seq_item_solicitacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tex_solicitacao = db.Column(db.String(2000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    aut_conclusao = db.Column(db.String(20))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbSolicitacaoAtualizacao.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_solicitacao_atualizacaos')
    tb_item_solicitacao_atualizacao = db.relationship('TbItemSolicitacaoAtualizacao', primaryjoin='TbSolicitacaoAtualizacao.co_seq_item_solicitacao == TbItemSolicitacaoAtualizacao.co_seq_item_solicitacao', backref='tb_solicitacao_atualizacaos')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbSolicitacaoAtualizacao.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_solicitacao_atualizacaos')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbSolicitacaoAtualizacao.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_solicitacao_atualizacaos')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbSolicitacaoAtualizacao.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_solicitacao_atualizacaos')



class TbSolicitacaoBiologiaMolecular(db.Model):
    __tablename__ = 'tb_solicitacao_biologia_molecular'

    co_seq_soliciatacao_bm = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_painel_mutacao = db.Column(db.ForeignKey('tb_painel_mutacao.co_seq_painel_mutacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_biologia_molecular = db.Column(db.ForeignKey('tb_biologia_molecular.co_seq_biologia_molecular', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_sequenciamento = db.Column(db.String(1), nullable=False)
    dt_solicitacao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_biologia_molecular = db.relationship('TbBiologiaMolecular', primaryjoin='TbSolicitacaoBiologiaMolecular.co_seq_biologia_molecular == TbBiologiaMolecular.co_seq_biologia_molecular', backref='tb_solicitacao_biologia_moleculars')
    tb_painel_mutacao = db.relationship('TbPainelMutacao', primaryjoin='TbSolicitacaoBiologiaMolecular.co_seq_painel_mutacao == TbPainelMutacao.co_seq_painel_mutacao', backref='tb_solicitacao_biologia_moleculars')



class TbSolicitacaoControleExame(db.Model):
    __tablename__ = 'tb_solicitacao_controle_exame'

    co_seq_controle_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbSolicitacaoControleExame.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_solicitacao_controle_exames')



class TbSolicitacaoMaterial(db.Model):
    __tablename__ = 'tb_solicitacao_material'
    __table_args__ = (
        db.Index('in_solmatpes_coseqsol_dtsol', 'co_seq_solicitacao_material', 'dt_solicitacao'),
        db.Index('in_solmatpes_coseqsol_coseqtpmat_dtsol', 'co_seq_solicitacao_material', 'co_seq_tp_material', 'dt_solicitacao'),
        db.Index('in_solmatpes_coseqtpmat_dtsol', 'co_seq_tp_material', 'dt_solicitacao')
    )

    co_seq_solicitacao_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_distrito = db.Column(db.ForeignKey('tb_distrito.co_seq_distrito', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_solicitacao = db.Column(db.Numeric(8, 0), nullable=False, index=True)
    qt_solicitacao = db.Column(db.Numeric(5, 0), nullable=False)
    obs_solicitacao = db.Column(db.String(200), nullable=False)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_distrito = db.relationship('TbDistrito', primaryjoin='TbSolicitacaoMaterial.co_seq_distrito == TbDistrito.co_seq_distrito', backref='tb_solicitacao_materials')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbSolicitacaoMaterial.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tb_solicitacao_materials')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbSolicitacaoMaterial.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_solicitacao_materials')



class TbSolicitacaoMaterialPessoa(db.Model):
    __tablename__ = 'tb_solicitacao_material_pessoa'
    __table_args__ = (
        db.Index('in_solmatpes_coseqagen_dthrcanc', 'co_seq_agendamento', 'dt_hr_cancelamento'),
    )

    co_seq_material_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento = db.Column(db.ForeignKey('tb_agendamento.co_seq_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_solicitacao_material = db.Column(db.ForeignKey('tb_solicitacao_material.co_seq_solicitacao_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_envio_material = db.Column(db.ForeignKey('tb_tipo_envio_material.co_seq_tp_envio_material', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_comunicacao = db.Column(db.ForeignKey('tb_comunicacao.co_seq_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_portador = db.Column(db.ForeignKey('tb_portador.co_seq_portador', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_recebimento_material = db.Column(db.Numeric(14, 0))
    aut_recebimento_material = db.Column(db.String(20))
    nu_correio = db.Column(db.String(60))
    dt_recebimento_material = db.Column(db.Numeric(8, 0))

    tb_agendamento = db.relationship('TbAgendamento', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_agendamento == TbAgendamento.co_seq_agendamento', backref='tb_solicitacao_material_pessoas')
    tb_comunicacao = db.relationship('TbComunicacao', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_comunicacao == TbComunicacao.co_seq_comunicacao', backref='tb_solicitacao_material_pessoas')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_solicitacao_material_pessoas')
    tb_portador = db.relationship('TbPortador', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_portador == TbPortador.co_seq_portador', backref='tb_solicitacao_material_pessoas')
    tb_solicitacao_material = db.relationship('TbSolicitacaoMaterial', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_solicitacao_material == TbSolicitacaoMaterial.co_seq_solicitacao_material', backref='tb_solicitacao_material_pessoas')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_solicitacao_material_pessoas')
    tb_tipo_envio_material = db.relationship('TbTipoEnvioMaterial', primaryjoin='TbSolicitacaoMaterialPessoa.co_seq_tp_envio_material == TbTipoEnvioMaterial.co_seq_tp_envio_material', backref='tb_solicitacao_material_pessoas')



class TbSolicitacaoMaterialUnidade(db.Model):
    __tablename__ = 'tb_solicitacao_material_unidade'

    co_seq_material_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_material_site = db.Column(db.ForeignKey('tb_tipo_material_site.co_seq_tp_material_site', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude_site = db.Column(db.Numeric(8, 0), nullable=False)
    dt_solicitacao = db.Column(db.Numeric(8, 0), nullable=False)
    qt_solicitacao = db.Column(db.Numeric(5, 0), nullable=False)
    qt_fornecida = db.Column(db.Numeric(5, 0))
    dt_liberacao = db.Column(db.Numeric(8, 0))
    dt_hr_liberacao = db.Column(db.Numeric(14, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento_site = db.Column(db.Numeric(14, 0))
    ds_cancelamento = db.Column(db.String(200))

    tb_tipo_material_site = db.relationship('TbTipoMaterialSite', primaryjoin='TbSolicitacaoMaterialUnidade.co_seq_tp_material_site == TbTipoMaterialSite.co_seq_tp_material_site', backref='tb_solicitacao_material_unidades')



class TbSolicitacaoUnidadeControle(db.Model):
    __tablename__ = 'tb_solicitacao_unidade_controle'

    co_seq_solicitacao_unidade_controle = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_solicitacao_material = db.Column(db.ForeignKey('tb_solicitacao_material.co_seq_solicitacao_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_material_unidade_site = db.Column(db.Numeric(14, 0), nullable=False)
    dt_solicitacao = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_solicitacao = db.Column(db.Numeric(14, 0), nullable=False)
    qt_solicitacao = db.Column(db.Numeric(5, 0), nullable=False)
    qt_fornecida = db.Column(db.Numeric(5, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_solicitacao_material = db.relationship('TbSolicitacaoMaterial', primaryjoin='TbSolicitacaoUnidadeControle.co_seq_solicitacao_material == TbSolicitacaoMaterial.co_seq_solicitacao_material', backref='tb_solicitacao_unidade_controles')



class TbSoroMotivoInadequacao(db.Model):
    __tablename__ = 'tb_soro_motivo_inadequacao'

    co_seq_mot_inadequacao_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_mot_inadequacao = db.Column(db.ForeignKey('tb_motivo_inadequacao.co_mot_inadequacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_amostra_soro = db.Column(db.ForeignKey('tb_amostra_soro.co_seq_amostra_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_motivo_inadequacao = db.relationship('TbMotivoInadequacao', primaryjoin='TbSoroMotivoInadequacao.co_mot_inadequacao == TbMotivoInadequacao.co_mot_inadequacao', backref='tb_soro_motivo_inadequacaos')
    tb_amostra_soro = db.relationship('TbAmostraSoro', primaryjoin='TbSoroMotivoInadequacao.co_seq_amostra_soro == TbAmostraSoro.co_seq_amostra_soro', backref='tb_soro_motivo_inadequacaos')



class TbStatusConsultaAmbulatorial(db.Model):
    __tablename__ = 'tb_status_consulta_ambulatorial'

    co_seq_status_consulta_amb = db.Column(db.Numeric(1, 0), primary_key=True, unique=True)
    ds_status_consulta_amb = db.Column(db.String(50), nullable=False)



class TbSubgrupoResultado(db.Model):
    __tablename__ = 'tb_subgrupo_resultado'

    co_seq_res_subgrupo = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_grupo_res = db.Column(db.ForeignKey('tb_grupo_resultado.co_seq_grupo_res', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_res_subgrupo = db.Column(db.String(200), nullable=False)
    nu_seq_grupo = db.Column(db.Numeric(2, 0), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_grupo_resultado = db.relationship('TbGrupoResultado', primaryjoin='TbSubgrupoResultado.co_seq_grupo_res == TbGrupoResultado.co_seq_grupo_res', backref='tb_subgrupo_resultadoes')



class TbSubmenu(db.Model):
    __tablename__ = 'tb_submenu'
    __table_args__ = (
        db.Index('pk_i_submenu', 'co_seq_transacao', 'co_seq_sistema', 'co_seq_tp_categoria'),
    )

    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_sistema = db.Column(db.ForeignKey('tb_sistema.co_seq_sistema', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_tp_categoria = db.Column(db.ForeignKey('tb_categoria_menu.co_seq_tp_categoria', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    nu_seq_submenu = db.Column(db.Numeric(2, 0), nullable=False)

    tb_sistema = db.relationship('TbSistema', primaryjoin='TbSubmenu.co_seq_sistema == TbSistema.co_seq_sistema', backref='tb_submenus')
    tb_categoria_menu = db.relationship('TbCategoriaMenu', primaryjoin='TbSubmenu.co_seq_tp_categoria == TbCategoriaMenu.co_seq_tp_categoria', backref='tb_submenus')
    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbSubmenu.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_submenus')



class TbSuspencaoTratamento(db.Model):
    __tablename__ = 'tb_suspencao_tratamento'

    co_seq_suspencao_tratamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_ini = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter = db.Column(db.Numeric(8, 0))
    obs_suspencao_tratamento = db.Column(db.String(200))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))

    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbSuspencaoTratamento.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_suspencao_tratamentoes')



class TbTabelaSistema(db.Model):
    __tablename__ = 'tb_tabela_sistema'

    co_seq_tabela_sistema = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    no_tabela_sistema = db.Column(db.String(40), nullable=False)



class TbTabelaVirtual(db.Model):
    __tablename__ = 'tb_tabela_virtual'

    co_seq_tabela_virtual = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    no_tabela_virtual = db.Column(db.String(50), nullable=False)



class TbTabelaVirtualAmbulatorio(db.Model):
    __tablename__ = 'tb_tabela_virtual_ambulatorio'

    co_seq_tabela_amb = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    ds_tabela_amb = db.Column(db.String(70), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



t_tb_temp_controle_placa = db.Table(
    'tb_temp_controle_placa',
    db.Column('co_seq_colaborador', db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True),
    db.Column('nu_placa_temp', db.String(20), nullable=False),
    db.Column('ds_tp_exame', db.String(100)),
    db.Column('a1', db.String(20)),
    db.Column('a2', db.String(20)),
    db.Column('b1', db.String(20)),
    db.Column('b2', db.String(20)),
    db.Column('c1', db.String(20)),
    db.Column('c2', db.String(20)),
    db.Column('d1', db.String(20)),
    db.Column('d2', db.String(20)),
    db.Column('e1', db.String(20)),
    db.Column('e2', db.String(20)),
    db.Column('f1', db.String(20)),
    db.Column('f2', db.String(20)),
    db.Column('alto', db.String(20)),
    db.Column('medio', db.String(20)),
    db.Column('baixo', db.String(20)),
    db.Column('controle_1', db.String(20)),
    db.Column('controle_2', db.String(20)),
    db.Column('branco', db.String(20))
)



class TbTerminoWorklist(db.Model):
    __tablename__ = 'tb_termino_worklist'

    co_seq_ter_worklist = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    nu_worklist = db.Column(db.Numeric(14, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbTerminoWorklist.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_termino_worklists')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTerminoWorklist.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_termino_worklists')



class TbTerminoWorklistPlaca(db.Model):
    __tablename__ = 'tb_termino_worklist_placa'

    co_seq_ter_worklist_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    nu_placa = db.Column(db.ForeignKey('tb_numero_placa.nu_placa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_ter_worklist = db.Column(db.ForeignKey('tb_termino_worklist.co_seq_ter_worklist', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_termino_worklist = db.relationship('TbTerminoWorklist', primaryjoin='TbTerminoWorklistPlaca.co_seq_ter_worklist == TbTerminoWorklist.co_seq_ter_worklist', backref='tb_termino_worklist_placas')
    tb_numero_placa = db.relationship('TbNumeroPlaca', primaryjoin='TbTerminoWorklistPlaca.nu_placa == TbNumeroPlaca.nu_placa', backref='tb_termino_worklist_placas')



class TbTesteSuor(db.Model):
    __tablename__ = 'tb_teste_suor'

    co_seq_teste_suor = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_agendamento_coleta = db.Column(db.ForeignKey('tb_agendamento_coleta.co_seq_agendamento_coleta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_registro = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_agendamento_coleta = db.relationship('TbAgendamentoColeta', primaryjoin='TbTesteSuor.co_seq_agendamento_coleta == TbAgendamentoColeta.co_seq_agendamento_coleta', backref='tb_teste_suors')
    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbTesteSuor.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_teste_suors')
    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbTesteSuor.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_teste_suors')



class TbTextoPadrao(db.Model):
    __tablename__ = 'tb_texto_padrao'

    co_seq_txt_padro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_txt_padrao = db.Column(db.ForeignKey('tb_tipo_texto_padrao.co_seq_tp_txt_padrao', ondelete='RESTRICT', onupdate='RESTRICT'), db.ForeignKey('tb_tipo_texto_padrao.co_seq_tp_txt_padrao'), nullable=False, index=True)
    co_origem = db.Column(db.Numeric(14, 0), nullable=False)
    txt_padrao = db.Column(db.Text, nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_texto_padrao = db.relationship('TbTipoTextoPadrao', primaryjoin='TbTextoPadrao.co_seq_tp_txt_padrao == TbTipoTextoPadrao.co_seq_tp_txt_padrao', backref='tbtipotextopadrao_tb_texto_padraos')
    tb_tipo_texto_padrao1 = db.relationship('TbTipoTextoPadrao', primaryjoin='TbTextoPadrao.co_seq_tp_txt_padrao == TbTipoTextoPadrao.co_seq_tp_txt_padrao', backref='tbtipotextopadrao_tb_texto_padraos_0')



class TbTextoRepasseResultadoSoro(db.Model):
    __tablename__ = 'tb_texto_repasse_resultado_soro'

    co_seq_tex_repasse_res = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_tp_conduta_soro = db.Column(db.ForeignKey('tb_tipo_conduta_soro.co_seq_tp_conduta_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tex_repasse_res = db.Column(db.String(4000), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_conduta_soro = db.relationship('TbTipoCondutaSoro', primaryjoin='TbTextoRepasseResultadoSoro.co_seq_tp_conduta_soro == TbTipoCondutaSoro.co_seq_tp_conduta_soro', backref='tb_texto_repasse_resultado_soroes')



class TbTipoAdmMedicamentoAmb(db.Model):
    __tablename__ = 'tb_tipo_adm_medicamento_amb'

    co_seq_adm_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_adm_medicamento = db.Column(db.String(80), nullable=False)
    qt_dia = db.Column(db.Numeric(8, 0))
    nu_dia = db.Column(db.Numeric(8, 0))
    qt_dia_tp_adm = db.Column(db.Numeric(8, 0))
    nu_ordem = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoAgendamento(db.Model):
    __tablename__ = 'tb_tipo_agendamento'

    co_seq_tp_agendamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_tp_agendamento = db.Column(db.String(80), nullable=False)
    ide_envio_material = db.Column(db.String(1), nullable=False)
    ide_controla_comparecimento = db.Column(db.String(1), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1), nullable=False)
    ide_cancelamento_pendencia = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0))
    aut_ultima_alteracao = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(20, 0))
    aut_registro = db.Column(db.String(20))
    nu_dia_realizacao = db.Column(db.Numeric(3, 0))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbTipoAgendamento.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_tipo_agendamentoes')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbTipoAgendamento.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_tipo_agendamentoes')



class TbTipoAgendamentoExameMetodo(db.Model):
    __tablename__ = 'tb_tipo_agendamento_exame_metodo'

    co_seq_tp_agen_exame_metodo = db.Column(db.Integer, primary_key=True, unique=True)
    co_seq_tp_agendamento = db.Column(db.Numeric(2, 0), nullable=False)
    co_seq_tp_exame_metodo = db.Column(db.Numeric(5, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoAgendamentoProvidencia(db.Model):
    __tablename__ = 'tb_tipo_agendamento_providencia'

    co_seq_agenda_providencia = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbTipoAgendamentoProvidencia.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_tipo_agendamento_providencias')
    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbTipoAgendamentoProvidencia.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_tipo_agendamento_providencias')



class TbTipoAlerta(db.Model):
    __tablename__ = 'tb_tipo_alerta'

    co_seq_tp_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_alerta = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoAlertaColaborador(db.Model):
    __tablename__ = 'tb_tipo_alerta_colaborador'

    co_seq_tp_alerta_colaborador = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_colaborador = db.Column(db.ForeignKey('tb_colaborador.co_seq_colaborador', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_alerta = db.Column(db.ForeignKey('tb_tipo_alerta.co_seq_tp_alerta', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_colaborador = db.relationship('TbColaborador', primaryjoin='TbTipoAlertaColaborador.co_seq_colaborador == TbColaborador.co_seq_colaborador', backref='tb_tipo_alerta_colaboradors')
    tb_tipo_alerta = db.relationship('TbTipoAlerta', primaryjoin='TbTipoAlertaColaborador.co_seq_tp_alerta == TbTipoAlerta.co_seq_tp_alerta', backref='tb_tipo_alerta_colaboradors')



class TbTipoAlertaUnidade(db.Model):
    __tablename__ = 'tb_tipo_alerta_unidade'

    co_seq_tp_alerta_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_alerta_unidade = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoAmostra(db.Model):
    __tablename__ = 'tb_tipo_amostra'

    co_seq_tp_amostra = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_tp_amostra = db.Column(db.String(50), nullable=False)
    co_seq_tp_material_coletado = db.Column(db.Numeric(5, 0))



class TbTipoAnaliseSuor(db.Model):
    __tablename__ = 'tb_tipo_analise_suor'

    co_seq_tp_analise_suor = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_seq_tp_analise_suor = db.Column(db.String(50), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoArquivo(db.Model):
    __tablename__ = 'tb_tipo_arquivo'

    co_seq_tp_arq = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_arq = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoCampoModificacao(db.Model):
    __tablename__ = 'tb_tipo_campo_modificacao'

    co_campo_modificacao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_campo_modificacao = db.Column(db.String(50), nullable=False)



class TbTipoClassificacaoImagem(db.Model):
    __tablename__ = 'tb_tipo_classificacao_imagem'

    co_seq_tp_classificacao_img = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_tp_classificacao_imagem = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoCodigoEntradaPessoa(db.Model):
    __tablename__ = 'tb_tipo_codigo_entrada_pessoa'

    co_seq_tp_ent_pessoa = db.Column(db.Numeric(1, 0), primary_key=True, unique=True)
    ds_co_ent_pessoa = db.Column(db.String(40), nullable=False)



class TbTipoColetaMaternidade(db.Model):
    __tablename__ = 'tb_tipo_coleta_maternidade'

    co_seq_tp_coleta_maternidade = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_coleta_maternidade = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoColunaAmostraPlaca(db.Model):
    __tablename__ = 'tb_tipo_coluna_amostra_placa'

    co_seq_tp_col_amostra_placa = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_tp_col_amostra = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_coluna_grafico = db.Column(db.String(1), nullable=False)



class TbTipoColunaPlaca(db.Model):
    __tablename__ = 'tb_tipo_coluna_placa'

    co_seq_tp_col_placa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_col_placa = db.Column(db.String(100), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)



class TbTipoColunaResultado(db.Model):
    __tablename__ = 'tb_tipo_coluna_resultado'

    co_seq_tp_col_resultado = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_col_resultado = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)



class TbTipoComunicacao(db.Model):
    __tablename__ = 'tb_tipo_comunicacao'

    co_seq_tp_comunicacao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_tp_comunicacao = db.Column(db.String(80), nullable=False)



class TbTipoCondutaSoro(db.Model):
    __tablename__ = 'tb_tipo_conduta_soro'

    co_seq_tp_conduta_soro = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_tp_conduta_soro = db.Column(db.String(50), nullable=False)



class TbTipoContato(db.Model):
    __tablename__ = 'tb_tipo_contato'

    co_seq_tp_contato = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_contato = db.Column(db.String(80), nullable=False)
    msc_contato = db.Column(db.String(200), nullable=False)



class TbTipoControleQualidade(db.Model):
    __tablename__ = 'tb_tipo_controle_qualidade'

    co_seq_tp_controle_qualidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_controle_qualidade = db.Column(db.String(50), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)



class TbTipoDietaMaternidade(db.Model):
    __tablename__ = 'tb_tipo_dieta_maternidade'

    co_seq_tp_dieta_maternidade = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_dieta_maternidade = db.Column(db.String(100), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoDiretorio(db.Model):
    __tablename__ = 'tb_tipo_diretorio'

    co_seq_tp_diretorio = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_tp_diretorio = db.Column(db.String(300), nullable=False)



class TbTipoDocumento(db.Model):
    __tablename__ = 'tb_tipo_documento'

    co_seq_tp_documento = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_documento = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)



class TbTipoEndereco(db.Model):
    __tablename__ = 'tb_tipo_endereco'

    co_seq_tp_endereco = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_endereco = db.Column(db.String(30), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoEntradaPadrao(db.Model):
    __tablename__ = 'tb_tipo_entrada_padrao'

    co_seq_tp_ent_padrao = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_ent_padrao = db.Column(db.String(50), nullable=False)



class TbTipoEnvioMaterial(db.Model):
    __tablename__ = 'tb_tipo_envio_material'

    co_seq_tp_envio_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_envio_material = db.Column(db.String(30), nullable=False)



class TbTipoEstadoClinicoColeta(db.Model):
    __tablename__ = 'tb_tipo_estado_clinico_coleta'

    co_tp_estado_clinico = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_estado_clinico = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoEstudoFamiliar(db.Model):
    __tablename__ = 'tb_tipo_estudo_familiar'

    co_seq_tp_estudo_familiar = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    co_seq_exame_padrao = db.Column(db.ForeignKey('tb_exame_padrao.co_seq_exame_padrao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_tp_estudo_familiar = db.Column(db.String(50), nullable=False)

    tb_exame_padrao = db.relationship('TbExamePadrao', primaryjoin='TbTipoEstudoFamiliar.co_seq_exame_padrao == TbExamePadrao.co_seq_exame_padrao', backref='tb_tipo_estudo_familiars')



class TbTipoExame(db.Model):
    __tablename__ = 'tb_tipo_exame'

    co_seq_tp_exame = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    tip_co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_exame = db.Column(db.String(100), nullable=False)
    sg_tp_exame = db.Column(db.String(2), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    no_arquivo_bpa = db.Column(db.String(30))
    sg_geral_tp_exame = db.Column(db.String(25))
    nu_ordem = db.Column(db.Numeric(8, 0))
    ide_edicao_retorno_liberacao = db.Column(db.String(1))
    ide_conferencia_soro = db.Column(db.String(1))
    ide_res_agrupado = db.Column(db.String(1))

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbTipoExame.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_tipo_exames')
    parent = db.relationship('TbTipoExame', remote_side=[co_seq_tp_exame], primaryjoin='TbTipoExame.tip_co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_tipo_exames')



class TbTipoExameAmostra(db.Model):
    __tablename__ = 'tb_tipo_exame_amostra'

    co_seq_tp_exame_amostra = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbTipoExameAmostra.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_tipo_exame_amostras')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTipoExameAmostra.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_tipo_exame_amostras')



class TbTipoExameBloqueado(db.Model):
    __tablename__ = 'tb_tipo_exame_bloqueado'

    co_seq_tp_exame_bloqueado = db.Column(db.Numeric(14, 0), primary_key=True, server_default=db.FetchedValue())
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbTipoExameBloqueado.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_tipo_exame_bloqueadoes')



class TbTipoExameCidDoenca(db.Model):
    __tablename__ = 'tb_tipo_exame_cid_doenca'

    co_seq_tp_exame_cid_doenca = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca_cid = db.Column(db.ForeignKey('tb_doenca_cid.co_seq_doenca_cid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_doenca_cid = db.relationship('TbDoencaCid', primaryjoin='TbTipoExameCidDoenca.co_seq_doenca_cid == TbDoencaCid.co_seq_doenca_cid', backref='tb_tipo_exame_cid_doencas')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbTipoExameCidDoenca.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_tipo_exame_cid_doencas')
    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbTipoExameCidDoenca.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_tipo_exame_cid_doencas')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbTipoExameCidDoenca.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_tipo_exame_cid_doencas')



class TbTipoExameConsulta(db.Model):
    __tablename__ = 'tb_tipo_exame_consulta'

    co_seq_tp_exame_consulta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_exame_consulta = db.Column(db.String(100), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_exame_imagem = db.Column(db.String(1), nullable=False)



class TbTipoExameConsultaAmb(db.Model):
    __tablename__ = 'tb_tipo_exame_consulta_amb'

    co_seq_tp_exame_consulta_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_exame_consulta_amb = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoExameControle(db.Model):
    __tablename__ = 'tb_tipo_exame_controle'

    co_seq_tp_exame_controle = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_exame_controle = db.Column(db.String(200), nullable=False)



class TbTipoExameMesmoProcesso(db.Model):
    __tablename__ = 'tb_tipo_exame_mesmo_processo'

    co_tp_exame_mesmo_proc = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_exame_equip = db.Column(db.String(15))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbTipoExameMesmoProcesso.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_tipo_exame_mesmo_processoes')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTipoExameMesmoProcesso.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_tipo_exame_mesmo_processoes')



class TbTipoExameMetodo(db.Model):
    __tablename__ = 'tb_tipo_exame_metodo'

    co_seq_tp_exame_metodo = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_metodo = db.Column(db.ForeignKey('tb_tipo_metodo.co_seq_tp_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_res_quantitativo = db.Column(db.String(1))
    nu_decimais_res = db.Column(db.Numeric(2, 0))
    nu_repeticao_nova_amostra = db.Column(db.Numeric(2, 0))
    nu_repeticao_controle_medico = db.Column(db.Numeric(2, 0))
    co_ordem_geracao_placa = db.Column(db.Numeric(2, 0))
    ide_1_placa_pagina = db.Column(db.String(1))
    co_seq_tp_col_placa_auxiliar = db.Column(db.Numeric(3, 0))
    ide_assinatura_impressao_soro = db.Column(db.String(1))
    ide_libera_maior_resultado = db.Column(db.String(1))
    ide_seq_placa_equipamento = db.Column(db.String(1))
    ide_arquimo_ms = db.Column(db.String(1))
    ide_libera_maior_menor_valor = db.Column(db.String(1))
    ide_ponto_flutuante = db.Column(db.String(1))
    ide_liberacao_laboratorio = db.Column(db.String(1))

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbTipoExameMetodo.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_tipo_exame_metodoes')
    tb_tipo_metodo = db.relationship('TbTipoMetodo', primaryjoin='TbTipoExameMetodo.co_seq_tp_metodo == TbTipoMetodo.co_seq_tp_metodo', backref='tb_tipo_exame_metodoes')



class TbTipoExamePadrao(db.Model):
    __tablename__ = 'tb_tipo_exame_padrao'

    co_seq_tp_exame_padrao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_tp_amostra = db.Column(db.ForeignKey('tb_tipo_amostra.co_seq_tp_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_exame_padrao = db.Column(db.ForeignKey('tb_exame_padrao.co_seq_exame_padrao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbTipoExamePadrao.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tb_tipo_exame_padraos')
    tb_exame_padrao = db.relationship('TbExamePadrao', primaryjoin='TbTipoExamePadrao.co_seq_exame_padrao == TbExamePadrao.co_seq_exame_padrao', backref='tb_tipo_exame_padraos')
    tb_tipo_amostra = db.relationship('TbTipoAmostra', primaryjoin='TbTipoExamePadrao.co_seq_tp_amostra == TbTipoAmostra.co_seq_tp_amostra', backref='tb_tipo_exame_padraos')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTipoExamePadrao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_tipo_exame_padraos')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbTipoExamePadrao.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_tipo_exame_padraos')



class TbTipoExamePbh(db.Model):
    __tablename__ = 'tb_tipo_exame_pbh'

    co_seq_tp_exame_pbh = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_exame = db.Column(db.String(100), nullable=False)
    co_exame_pbh = db.Column(db.String(10), nullable=False)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbTipoExamePbh.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_tipo_exame_pbhs')



class TbTipoExameProcedimento(db.Model):
    __tablename__ = 'tb_tipo_exame_procedimento'

    co_seq_tp_exame_procedimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame = db.Column(db.ForeignKey('tb_tipo_exame.co_seq_tp_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ide_amostra_menor_30_dias = db.Column(db.String(1), nullable=False)
    ide_primeira_amostra_liberada = db.Column(db.String(1), nullable=False)
    ide_controle_medico = db.Column(db.String(1), nullable=False)
    ide_amostra_familiar = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_dias_nascimento_coleta = db.Column(db.Numeric(5, 0))
    co_seq_tp_amostra = db.Column(db.Numeric)

    tb_tipo_exame = db.relationship('TbTipoExame', primaryjoin='TbTipoExameProcedimento.co_seq_tp_exame == TbTipoExame.co_seq_tp_exame', backref='tb_tipo_exame_procedimentoes')
    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbTipoExameProcedimento.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_tipo_exame_procedimentoes')



class TbTipoExecucaoGuardiao(db.Model):
    __tablename__ = 'tb_tipo_execucao_guardiao'

    co_seq_tp_execucao_guardiao = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_execucao_guardiao = db.Column(db.String(50), nullable=False)



class TbTipoFormaPrescricao(db.Model):
    __tablename__ = 'tb_tipo_forma_prescricao'

    co_seq_tp_forma_prescricao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_forma_prescricao = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoHemoglobina(db.Model):
    __tablename__ = 'tb_tipo_hemoglobina'

    co_seq_tp_hb = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_tp_hb = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoImagemRecepcao(db.Model):
    __tablename__ = 'tb_tipo_imagem_recepcao'

    co_tp_recep_imagem = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_recep_imagem = db.Column(db.String(30), nullable=False)



class TbTipoInterpretacaoExameAmb(db.Model):
    __tablename__ = 'tb_tipo_interpretacao_exame_amb'

    co_seq_tp_int_exame_amb = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_int_exame_amb = db.Column(db.String(40), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoItemAnotacaoPicote(db.Model):
    __tablename__ = 'tb_tipo_item_anotacao_picote'

    co_seq_item_anotacao_picote = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_item_anotacao_picote = db.Column(db.String(80), nullable=False)
    ds_letra_associada = db.Column(db.String(3), nullable=False)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_outro = db.Column(db.String(1), nullable=False)

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbTipoItemAnotacaoPicote.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_tipo_item_anotacao_picotes')



class TbTipoLocalInternacao(db.Model):
    __tablename__ = 'tb_tipo_local_internacao'

    co_seq_tp_local_intenacao = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_local_internacao = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoLogradouro(db.Model):
    __tablename__ = 'tb_tipo_logradouro'

    co_seq_tp_logradouro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_logradouro = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    co_logradouro_bpa = db.Column(db.String(5))



class TbTipoMaterial(db.Model):
    __tablename__ = 'tb_tipo_material'

    co_seq_tp_material = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_material = db.Column(db.String(200), nullable=False)
    ide_lote_tp_material = db.Column(db.String(1), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_cobranca_fechamento_toxo = db.Column(db.String(1), nullable=False)
    ide_opcao_usuario = db.Column(db.String(1), nullable=False)
    co_seq_doenca_emissao_sol = db.Column(db.Numeric(4, 0))
    co_seq_tp_procedimento = db.Column(db.Numeric(4, 0))
    co_seq_tp_procedimento_trasp = db.Column(db.Numeric(4, 0))

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbTipoMaterial.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_tipo_materials')



class TbTipoMaterialColetado(db.Model):
    __tablename__ = 'tb_tipo_material_coletado'

    co_seq_tp_material_coletado = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_material_coletado = db.Column(db.String(50), nullable=False)



class TbTipoMaterialLocalMunicipio(db.Model):
    __tablename__ = 'tb_tipo_material_local_municipio'

    co_seq_tp_material_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_material_site = db.Column(db.ForeignKey('tb_tipo_material_site.co_seq_tp_material_site', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_material_local = db.Column(db.Numeric(5, 0), nullable=False)
    co_seq_municipio_site = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_material_site = db.relationship('TbTipoMaterialSite', primaryjoin='TbTipoMaterialLocalMunicipio.co_seq_tp_material_site == TbTipoMaterialSite.co_seq_tp_material_site', backref='tb_tipo_material_local_municipios')



class TbTipoMaterialSite(db.Model):
    __tablename__ = 'tb_tipo_material_site'

    co_seq_tp_material_site = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_material_local = db.Column(db.Numeric(5, 0), nullable=False)
    co_seq_tp_triagem_site = db.Column(db.Numeric(2, 0), nullable=False)
    ds_tp_material = db.Column(db.String(200), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_maternidade_unidade = db.Column(db.String(1))



class TbTipoMaterialTipoColeta(db.Model):
    __tablename__ = 'tb_tipo_material_tipo_coleta'

    co_seq_tp_material_tp_coleta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_agendamento = db.Column(db.ForeignKey('tb_tipo_agendamento.co_seq_tp_agendamento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_material = db.Column(db.ForeignKey('tb_tipo_material.co_seq_tp_material', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_tipo_agendamento = db.relationship('TbTipoAgendamento', primaryjoin='TbTipoMaterialTipoColeta.co_seq_tp_agendamento == TbTipoAgendamento.co_seq_tp_agendamento', backref='tb_tipo_material_tipo_coletas')
    tb_tipo_material = db.relationship('TbTipoMaterial', primaryjoin='TbTipoMaterialTipoColeta.co_seq_tp_material == TbTipoMaterial.co_seq_tp_material', backref='tb_tipo_material_tipo_coletas')



class TbTipoMetodo(db.Model):
    __tablename__ = 'tb_tipo_metodo'

    co_seq_tp_metodo = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    ds_tp_metodo = db.Column(db.String(80), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoMetodoPadrao(db.Model):
    __tablename__ = 'tb_tipo_metodo_padrao'

    co_seq_tp_metodo_padrao = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    tip_co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    equ_co_seq_equip_exame = db.Column(db.ForeignKey('tb_equipamento_exame.co_seq_equip_exame', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_equipamento_exame = db.relationship('TbEquipamentoExame', primaryjoin='TbTipoMetodoPadrao.co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tbequipamentoexame_tb_tipo_metodo_padraos')
    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTipoMetodoPadrao.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tbtipoexamemetodo_tb_tipo_metodo_padraos')
    tb_equipamento_exame1 = db.relationship('TbEquipamentoExame', primaryjoin='TbTipoMetodoPadrao.equ_co_seq_equip_exame == TbEquipamentoExame.co_seq_equip_exame', backref='tbequipamentoexame_tb_tipo_metodo_padraos_0')
    tb_tipo_exame_metodo1 = db.relationship('TbTipoExameMetodo', primaryjoin='TbTipoMetodoPadrao.tip_co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tbtipoexamemetodo_tb_tipo_metodo_padraos_0')



class TbTipoMotivoComunicacao(db.Model):
    __tablename__ = 'tb_tipo_motivo_comunicacao'

    co_seq_tp_mot_comunicacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_mot_comunicacao = db.Column(db.ForeignKey('tb_motivo_comunicacao.co_seq_mot_comunicacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    ds_tp_mot_comunicacao = db.Column(db.String(60), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_conclusao_laboratorio = db.Column(db.String(1))
    ide_bloqueia_impressao = db.Column(db.String(1))
    ide_cancela_processamento = db.Column(db.String(1))
    ide_bloqueia_impressao_pre = db.Column(db.String(1))
    ide_conclusao_laboratorio_pre = db.Column(db.String(1))

    tb_motivo_comunicacao = db.relationship('TbMotivoComunicacao', primaryjoin='TbTipoMotivoComunicacao.co_seq_mot_comunicacao == TbMotivoComunicacao.co_seq_mot_comunicacao', backref='tb_tipo_motivo_comunicacaos')



class TbTipoOcorrencia(db.Model):
    __tablename__ = 'tb_tipo_ocorrencia'

    co_seq_tp_ocorrencia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_ocorrencia = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoOcorrenciaAlerta(db.Model):
    __tablename__ = 'tb_tipo_ocorrencia_alerta'

    co_seq_tp_controle_alerta = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_controle_alerta = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoOcorrenciaMunicipio(db.Model):
    __tablename__ = 'tb_tipo_ocorrencia_municipio'

    co_tp_ocorrencia_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_ocorrencia = db.Column(db.String(70), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)



class TbTipoParentesco(db.Model):
    __tablename__ = 'tb_tipo_parentesco'

    co_seq_tp_parentesco = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_tp_parentesco = db.Column(db.String(30), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoPeriodicidade(db.Model):
    __tablename__ = 'tb_tipo_periodicidade'

    co_seq_tp_periodicidade = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_periodicidade = db.Column(db.String(40), nullable=False)
    nu_dia = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoPeriodicidadePrescricao(db.Model):
    __tablename__ = 'tb_tipo_periodicidade_prescricao'

    co_seq_tp_periodo_prescricao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_periodo_prescricao = db.Column(db.String(80), nullable=False)
    nu_dia = db.Column(db.Numeric(8, 0))
    nu_ordem = db.Column(db.Numeric(8, 0))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoPosicaoPlaca(db.Model):
    __tablename__ = 'tb_tipo_posicao_placa'

    co_seq_tp_pos_placa = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_seq_tp_pos_placa = db.Column(db.String(40), nullable=False)
    ds_simp_tp_pos_placa = db.Column(db.String(7), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_controle_externo = db.Column(db.String(1), nullable=False)



class TbTipoProcedimento(db.Model):
    __tablename__ = 'tb_tipo_procedimento'

    co_seq_tp_procedimento = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_ext_procedimento = db.Column(db.String(15), nullable=False)
    ds_procedimento = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ida_maxima_cobranca_ano = db.Column(db.Numeric(3, 0))



class TbTipoProtocolo(db.Model):
    __tablename__ = 'tb_tipo_protocolo'

    co_seq_tp_protocolo = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_seq_tp_protocolo = db.Column(db.String(50), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoReferenciaExame(db.Model):
    __tablename__ = 'tb_tipo_referencia_exame'

    co_seq_tp_referencia_exame = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_referencia_exame = db.Column(db.String(400), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoSeparacaoColunaArquivo(db.Model):
    __tablename__ = 'tb_tipo_separacao_coluna_arquivo'

    co_tp_spr_col_arq = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_spr = db.Column(db.String(30), nullable=False)



class TbTipoTempoInicioDieta(db.Model):
    __tablename__ = 'tb_tipo_tempo_inicio_dieta'

    co_tp_tempo_inicio_dieta = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tempo_inicio_dieta = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoTextoPadrao(db.Model):
    __tablename__ = 'tb_tipo_texto_padrao'

    co_seq_tp_txt_padrao = db.Column(db.Numeric(5, 0), primary_key=True, unique=True)
    ds_tp_txt_padrao = db.Column(db.String(100), nullable=False)
    co_help_sistema = db.Column(db.Numeric(6, 0))
    ds_campo = db.Column(db.String(200))
    co_mensagem_1 = db.Column(db.Numeric(6, 0))
    co_mensagem_2 = db.Column(db.Numeric(6, 0))



class TbTipoTransfusao(db.Model):
    __tablename__ = 'tb_tipo_transfusao'

    co_seg_tp_transfusao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_transfusao = db.Column(db.String(40), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoTriagem(db.Model):
    __tablename__ = 'tb_tipo_triagem'

    co_seq_tp_triagem = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_triagem = db.Column(db.String(30), nullable=False)
    msc_co_paciente = db.Column(db.String(20), nullable=False)
    cmp_ref_unidade = db.Column(db.String(2))
    ide_co_gerado_recepcao = db.Column(db.String(1), nullable=False)
    nu_caracter_reg_unidade = db.Column(db.Numeric(1, 0), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_etiqueta_nova_amostra = db.Column(db.String(1))
    ide_analise_soro_laboratorio = db.Column(db.String(1))



class TbTipoTriagemExameMetodo(db.Model):
    __tablename__ = 'tb_tipo_triagem_exame_metodo'

    co_seq_tp_triagem_exame_metodo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTipoTriagemExameMetodo.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_tipo_triagem_exame_metodoes')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbTipoTriagemExameMetodo.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_tipo_triagem_exame_metodoes')



class TbTipoTriagemProvidencia(db.Model):
    __tablename__ = 'tb_tipo_triagem_providencia'

    co_seq_tp_triagem_providencia = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_providencia = db.Column(db.ForeignKey('tb_providencia.co_seq_providencia', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    tb_providencia = db.relationship('TbProvidencia', primaryjoin='TbTipoTriagemProvidencia.co_seq_providencia == TbProvidencia.co_seq_providencia', backref='tb_tipo_triagem_providencias')
    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbTipoTriagemProvidencia.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_tipo_triagem_providencias')



class TbTipoUnidade(db.Model):
    __tablename__ = 'tb_tipo_unidade'

    co_seq_tp_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_unidade = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoUnidadeMedida(db.Model):
    __tablename__ = 'tb_tipo_unidade_medida'

    co_seq_tip_unidade_medida = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_tp_unidade_medida = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTipoUsuario(db.Model):
    __tablename__ = 'tb_tipo_usuario'

    co_seq_tp_usuario = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_usuario = db.Column(db.String(20), nullable=False)



class TbTipoVacina(db.Model):
    __tablename__ = 'tb_tipo_vacina'

    co_seq_tp_vacina = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    ds_tp_vacina = db.Column(db.String(50), nullable=False)



class TbTipoViaMedicamento(db.Model):
    __tablename__ = 'tb_tipo_via_medicamento'

    co_seq_tp_via_medicamento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    ds_tp_via_medicamento = db.Column(db.String(80), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbTraducaoResultadoMetodo(db.Model):
    __tablename__ = 'tb_traducao_resultado_metodo'
    __table_args__ = (
        db.Index('in_tradresmed_cotpexa_vrresmed_dthrcanc', 'co_seq_tp_exame_metodo', 'vr_res_metodo', 'dt_hr_cancelamento'),
        db.Index('in_tradresmed_vrresmed_dthrcanc', 'vr_res_metodo', 'dt_hr_cancelamento')
    )

    co_seq_traducao_res_metodo = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_res_metodo = db.Column(db.String(100), nullable=False, index=True)
    vr_traducao_res = db.Column(db.String(100), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0), index=True)
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbTraducaoResultadoMetodo.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_traducao_resultado_metodoes')



class TbTransacao(db.Model):
    __tablename__ = 'tb_transacao'

    co_seq_transacao = db.Column(db.Numeric(4, 0), primary_key=True, unique=True)
    co_seq_sistema = db.Column(db.ForeignKey('tb_sistema.co_seq_sistema', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_transacao = db.Column(db.String(70), nullable=False)
    ds_transacao = db.Column(db.String(60), nullable=False)
    sg_transacao = db.Column(db.String(30), nullable=False)

    tb_sistema = db.relationship('TbSistema', primaryjoin='TbTransacao.co_seq_sistema == TbSistema.co_seq_sistema', backref='tb_transacaos')



class TbTransacaoAcao(db.Model):
    __tablename__ = 'tb_transacao_acao'
    __table_args__ = (
        db.Index('pk_i_transacao_acao', 'co_seq_acao_transacao', 'co_seq_transacao'),
    )

    co_seq_acao_transacao = db.Column(db.ForeignKey('tb_acao_transacao.co_seq_acao_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_acao_transacao = db.relationship('TbAcaoTransacao', primaryjoin='TbTransacaoAcao.co_seq_acao_transacao == TbAcaoTransacao.co_seq_acao_transacao', backref='tb_transacao_acaos')
    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbTransacaoAcao.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_transacao_acaos')



class TbTransacaoCampoModificacao(db.Model):
    __tablename__ = 'tb_transacao_campo_modificacao'

    co_seq_transacao_campo_mod = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_atualizacao_transacao = db.Column(db.ForeignKey('tb_motivo_alteracao_transacao.co_seq_atualizacao_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_campo_modificacao = db.Column(db.ForeignKey('tb_tipo_campo_modificacao.co_campo_modificacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_atual = db.Column(db.String(2000), nullable=False)
    vr_anterior = db.Column(db.String(2000), nullable=False)

    tb_tipo_campo_modificacao = db.relationship('TbTipoCampoModificacao', primaryjoin='TbTransacaoCampoModificacao.co_campo_modificacao == TbTipoCampoModificacao.co_campo_modificacao', backref='tb_transacao_campo_modificacaos')
    tb_motivo_alteracao_transacao = db.relationship('TbMotivoAlteracaoTransacao', primaryjoin='TbTransacaoCampoModificacao.co_seq_atualizacao_transacao == TbMotivoAlteracaoTransacao.co_seq_atualizacao_transacao', backref='tb_transacao_campo_modificacaos')



class TbTransacaoMonitoramentoOnline(db.Model):
    __tablename__ = 'tb_transacao_monitoramento_online'

    co_seq_trans_monitoramento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_usuario_monitoramento = db.Column(db.ForeignKey('tb_usuario_monitoramento_online.co_seq_usuario_monitoramento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbTransacaoMonitoramentoOnline.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_transacao_monitoramento_onlines')
    tb_usuario_monitoramento_online = db.relationship('TbUsuarioMonitoramentoOnline', primaryjoin='TbTransacaoMonitoramentoOnline.co_seq_usuario_monitoramento == TbUsuarioMonitoramentoOnline.co_seq_usuario_monitoramento', backref='tb_transacao_monitoramento_onlines')



class TbTransacaoPacienteOnline(db.Model):
    __tablename__ = 'tb_transacao_paciente_online'

    co_seq_trans_paciente_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_usuapo_paciente_online = db.Column(db.ForeignKey('tb_usuario_paciente_online.co_seq_usuapo_paciente_online', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    ds_senha_paciente_online = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbTransacaoPacienteOnline.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_transacao_paciente_onlines')
    tb_usuario_paciente_online = db.relationship('TbUsuarioPacienteOnline', primaryjoin='TbTransacaoPacienteOnline.co_seq_usuapo_paciente_online == TbUsuarioPacienteOnline.co_seq_usuapo_paciente_online', backref='tb_transacao_paciente_onlines')



class TbTransacaoTriagemOnline(db.Model):
    __tablename__ = 'tb_transacao_triagem_online'

    co_seq_trans_triagem_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_usuario_triagem_online = db.Column(db.ForeignKey('tb_usuario_triagem_online.co_seq_usuario_triagem_online', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbTransacaoTriagemOnline.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_transacao_triagem_onlines')
    tb_usuario_triagem_online = db.relationship('TbUsuarioTriagemOnline', primaryjoin='TbTransacaoTriagemOnline.co_seq_usuario_triagem_online == TbUsuarioTriagemOnline.co_seq_usuario_triagem_online', backref='tb_transacao_triagem_onlines')



class TbTransacaoUsuario(db.Model):
    __tablename__ = 'tb_transacao_usuario'
    __table_args__ = (
        db.Index('pk_i_transacao_usuario', 'co_seq_acao_transacao', 'co_seq_transacao', 'co_seq_usuario'),
    )

    co_seq_acao_transacao = db.Column(db.ForeignKey('tb_acao_transacao.co_seq_acao_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_usuario = db.Column(db.ForeignKey('tb_usuario.co_seq_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_acao_transacao = db.relationship('TbAcaoTransacao', primaryjoin='TbTransacaoUsuario.co_seq_acao_transacao == TbAcaoTransacao.co_seq_acao_transacao', backref='tb_transacao_usuarios')
    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbTransacaoUsuario.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_transacao_usuarios')
    tb_usuario = db.relationship('TbUsuario', primaryjoin='TbTransacaoUsuario.co_seq_usuario == TbUsuario.co_seq_usuario', backref='tb_transacao_usuarios')



class TbTransferenciaPaciente(db.Model):
    __tablename__ = 'tb_transferencia_paciente'

    co_seq_transferencia_paciente = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_uf = db.Column(db.ForeignKey('tb_uf.co_seq_uf', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_paciente = db.Column(db.ForeignKey('tb_paciente.co_seq_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    obs_transferencia_paciente = db.Column(db.String(200), nullable=False)

    tb_paciente = db.relationship('TbPaciente', primaryjoin='TbTransferenciaPaciente.co_seq_paciente == TbPaciente.co_seq_paciente', backref='tb_transferencia_pacientes')
    tb_uf = db.relationship('TbUf', primaryjoin='TbTransferenciaPaciente.co_seq_uf == TbUf.co_seq_uf', backref='tb_transferencia_pacientes')



class TbTransfusao(db.Model):
    __tablename__ = 'tb_transfusao'

    co_seq_transfusao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seg_tp_transfusao = db.Column(db.ForeignKey('tb_tipo_transfusao.co_seg_tp_transfusao', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_amostra = db.Column(db.ForeignKey('tb_amostra.co_seq_amostra', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    dt_transfusao = db.Column(db.Numeric(8, 0), nullable=False)
    no_hosp = db.Column(db.String(80))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ide_transfusao_antes_col = db.Column(db.String(1), nullable=False)

    tb_tipo_transfusao = db.relationship('TbTipoTransfusao', primaryjoin='TbTransfusao.co_seg_tp_transfusao == TbTipoTransfusao.co_seg_tp_transfusao', backref='tb_transfusaos')
    tb_amostra = db.relationship('TbAmostra', primaryjoin='TbTransfusao.co_seq_amostra == TbAmostra.co_seq_amostra', backref='tb_transfusaos')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbTransfusao.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_transfusaos')
    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbTransfusao.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tb_transfusaos')



class TbTratamentoDescentralizado(db.Model):
    __tablename__ = 'tb_tratamento_descentralizado'

    co_seq_tratamento_municipio = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_doenca_paciente = db.Column(db.ForeignKey('tb_doenca_paciente.co_seq_doenca_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_municipalizacao = db.Column(db.Numeric(8, 0))
    dt_descentralizacao_ampliada = db.Column(db.Numeric(8, 0))
    ds_nao_descentralizacao = db.Column(db.String(100))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca_paciente = db.relationship('TbDoencaPaciente', primaryjoin='TbTratamentoDescentralizado.co_seq_doenca_paciente == TbDoencaPaciente.co_seq_doenca_paciente', backref='tb_tratamento_descentralizadoes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbTratamentoDescentralizado.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_tratamento_descentralizadoes')



class TbUf(db.Model):
    __tablename__ = 'tb_uf'

    co_seq_uf = db.Column(db.Numeric(2, 0), primary_key=True, unique=True)
    no_uf = db.Column(db.String(50), nullable=False)
    sg_uf = db.Column(db.String(2), nullable=False)
    co_ibge_uf = db.Column(db.String(5), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbUnidadeCancelamentoEmail(db.Model):
    __tablename__ = 'tb_unidade_cancelamento_email'

    co_seq_unidade_canc_email = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ref_unidade = db.Column(db.String(10), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbUnidadeMedida(db.Model):
    __tablename__ = 'tb_unidade_medida'

    co_seq_unidade_medida = db.Column(db.Numeric(3, 0), primary_key=True, unique=True)
    ds_unidade_medida = db.Column(db.String(50), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbUnidadeSaude(db.Model):
    __tablename__ = 'tb_unidade_saude'
    __table_args__ = (
        db.Index('in_unidadesaude_cosegmun_cosequsa', 'co_seq_municipio', 'co_seq_unidade_saude'),
    )

    co_seq_unidade_saude = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_distrito = db.Column(db.ForeignKey('tb_distrito.co_seq_distrito', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_logradouro = db.Column(db.ForeignKey('tb_tipo_logradouro.co_seq_tp_logradouro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    no_unidade_saude = db.Column(db.String(100), nullable=False)
    co_ref_unidade = db.Column(db.String(10), nullable=False, index=True)
    nu_cnes = db.Column(db.String(30))
    no_logradouro = db.Column(db.String(100), nullable=False)
    nu_logradouro = db.Column(db.String(20), nullable=False)
    cmp_nr_logradouro = db.Column(db.String(50), nullable=False)
    no_bairro = db.Column(db.String(80), nullable=False)
    nu_cep = db.Column(db.String(8), nullable=False)
    nu_telefone = db.Column(db.String(35), nullable=False)
    nu_fax = db.Column(db.String(35), nullable=False)
    ds_email = db.Column(db.String(200), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    nu_telefone_auxiliar = db.Column(db.String(35), nullable=False)

    tb_distrito = db.relationship('TbDistrito', primaryjoin='TbUnidadeSaude.co_seq_distrito == TbDistrito.co_seq_distrito', backref='tb_unidade_saudes')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbUnidadeSaude.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_unidade_saudes')
    tb_tipo_logradouro = db.relationship('TbTipoLogradouro', primaryjoin='TbUnidadeSaude.co_seq_tp_logradouro == TbTipoLogradouro.co_seq_tp_logradouro', backref='tb_unidade_saudes')



class TbUnidadeSaudeDoenca(db.Model):
    __tablename__ = 'tb_unidade_saude_doenca'

    co_seq_unidade_doenca = db.Column(db.Numeric(8, 0), primary_key=True, unique=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbUnidadeSaudeDoenca.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_unidade_saude_doencas')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbUnidadeSaudeDoenca.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_unidade_saude_doencas')



class TbUnidadeTipo(db.Model):
    __tablename__ = 'tb_unidade_tipo'

    co_seq_tp_unidade_saude = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_unidade = db.Column(db.ForeignKey('tb_tipo_unidade.co_seq_tp_unidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)

    tb_tipo_unidade = db.relationship('TbTipoUnidade', primaryjoin='TbUnidadeTipo.co_seq_tp_unidade == TbTipoUnidade.co_seq_tp_unidade', backref='tb_unidade_tipoes')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbUnidadeTipo.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_unidade_tipoes')



class TbUnidadeTipoTriagem(db.Model):
    __tablename__ = 'tb_unidade_tipo_triagem'

    co_seq_tp_triagem_unidade = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_triagem = db.Column(db.ForeignKey('tb_tipo_triagem.co_seq_tp_triagem', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_triagem = db.relationship('TbTipoTriagem', primaryjoin='TbUnidadeTipoTriagem.co_seq_tp_triagem == TbTipoTriagem.co_seq_tp_triagem', backref='tb_unidade_tipo_triagems')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbUnidadeTipoTriagem.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_unidade_tipo_triagems')



class TbUsuario(db.Model):
    __tablename__ = 'tb_usuario'

    co_seq_usuario = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_usuario = db.Column(db.ForeignKey('tb_tipo_usuario.co_seq_tp_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_acesso_usuario = db.Column(db.String(20), nullable=False, index=True)
    sen_acesso_usuario = db.Column(db.String(20), index=True)
    no_usuario = db.Column(db.String(50), nullable=False)
    ide_usuario_ativo = db.Column(db.String(1), nullable=False)
    ide_senha_inicializada = db.Column(db.String(1), nullable=False)
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_usuario = db.relationship('TbTipoUsuario', primaryjoin='TbUsuario.co_seq_tp_usuario == TbTipoUsuario.co_seq_tp_usuario', backref='tb_usuarios')



class TbUsuarioAmbulatorioOnline(db.Model):
    __tablename__ = 'tb_usuario_ambulatorio_online'

    co_seq_usuario_amb_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_prof_saude = db.Column(db.ForeignKey('tb_profissional_saude.co_seq_prof_saude', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_doenca = db.Column(db.ForeignKey('tb_doenca.co_seq_doenca', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_especialidade = db.Column(db.ForeignKey('tb_especialidade.co_seq_especialidade', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_acesso_usuario = db.Column(db.String(20), nullable=False)
    sen_acesso_usuario = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_ultima_alteracao = db.Column(db.Numeric(14, 0), nullable=False)
    aut_ultima_alteracao = db.Column(db.String(20), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_doenca = db.relationship('TbDoenca', primaryjoin='TbUsuarioAmbulatorioOnline.co_seq_doenca == TbDoenca.co_seq_doenca', backref='tb_usuario_ambulatorio_onlines')
    tb_especialidade = db.relationship('TbEspecialidade', primaryjoin='TbUsuarioAmbulatorioOnline.co_seq_especialidade == TbEspecialidade.co_seq_especialidade', backref='tb_usuario_ambulatorio_onlines')
    tb_profissional_saude = db.relationship('TbProfissionalSaude', primaryjoin='TbUsuarioAmbulatorioOnline.co_seq_prof_saude == TbProfissionalSaude.co_seq_prof_saude', backref='tb_usuario_ambulatorio_onlines')



class TbUsuarioExecucaoTransacao(db.Model):
    __tablename__ = 'tb_usuario_execucao_transacao'

    co_seq_execucao_transacao = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_transacao = db.Column(db.ForeignKey('tb_transacao.co_seq_transacao', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_usuario = db.Column(db.ForeignKey('tb_usuario.co_seq_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_conclusao = db.Column(db.Numeric(14, 0))
    aut_conclusao = db.Column(db.String(20))

    tb_transacao = db.relationship('TbTransacao', primaryjoin='TbUsuarioExecucaoTransacao.co_seq_transacao == TbTransacao.co_seq_transacao', backref='tb_usuario_execucao_transacaos')
    tb_usuario = db.relationship('TbUsuario', primaryjoin='TbUsuarioExecucaoTransacao.co_seq_usuario == TbUsuario.co_seq_usuario', backref='tb_usuario_execucao_transacaos')



class TbUsuarioGrupo(db.Model):
    __tablename__ = 'tb_usuario_grupo'
    __table_args__ = (
        db.Index('pk_i_usuario_grupo', 'co_seq_grupo', 'co_seq_usuario'),
    )

    co_seq_grupo = db.Column(db.ForeignKey('tb_grupo.co_seq_grupo', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    co_seq_usuario = db.Column(db.ForeignKey('tb_usuario.co_seq_usuario', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True, nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_grupo = db.relationship('TbGrupo', primaryjoin='TbUsuarioGrupo.co_seq_grupo == TbGrupo.co_seq_grupo', backref='tb_usuario_grupoes')
    tb_usuario = db.relationship('TbUsuario', primaryjoin='TbUsuarioGrupo.co_seq_usuario == TbUsuario.co_seq_usuario', backref='tb_usuario_grupoes')



class TbUsuarioMonitoramentoOnline(db.Model):
    __tablename__ = 'tb_usuario_monitoramento_online'

    co_seq_usuario_monitoramento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    no_pessoa = db.Column(db.String(80))
    nu_telefone = db.Column(db.String(35))
    ds_email = db.Column(db.String(200))
    no_funcao = db.Column(db.String(200))
    ds_usuario_triagem_online = db.Column(db.String(40), nullable=False)
    ds_senha_triagem_online = db.Column(db.String(40), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbUsuarioPacienteOnline(db.Model):
    __tablename__ = 'tb_usuario_paciente_online'

    co_seq_usuapo_paciente_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_ent_pessoa_site = db.Column(db.String(20), nullable=False)
    ds_senha_paciente_online = db.Column(db.String(20), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    ds_email = db.Column(db.String(200))



class TbUsuarioTriagemOnline(db.Model):
    __tablename__ = 'tb_usuario_triagem_online'

    co_seq_usuario_triagem_online = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_unidade_saude = db.Column(db.ForeignKey('tb_unidade_saude.co_seq_unidade_saude', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_municipio = db.Column(db.ForeignKey('tb_municipio.co_seq_municipio', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_distrito = db.Column(db.ForeignKey('tb_distrito.co_seq_distrito', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ds_usuario_triagem_online = db.Column(db.String(40), nullable=False)
    ds_senha_triagem_online = db.Column(db.String(40), nullable=False)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_distrito = db.relationship('TbDistrito', primaryjoin='TbUsuarioTriagemOnline.co_seq_distrito == TbDistrito.co_seq_distrito', backref='tb_usuario_triagem_onlines')
    tb_municipio = db.relationship('TbMunicipio', primaryjoin='TbUsuarioTriagemOnline.co_seq_municipio == TbMunicipio.co_seq_municipio', backref='tb_usuario_triagem_onlines')
    tb_unidade_saude = db.relationship('TbUnidadeSaude', primaryjoin='TbUsuarioTriagemOnline.co_seq_unidade_saude == TbUnidadeSaude.co_seq_unidade_saude', backref='tb_usuario_triagem_onlines')



class TbVacina(db.Model):
    __tablename__ = 'tb_vacina'
    __table_args__ = (
        db.Index('in_vac_copac_dthrcanc', 'co_seq_paciente', 'dt_hr_cancelamento'),
    )

    co_seq_vacina = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_paciente = db.Column(db.ForeignKey('tb_paciente.co_seq_paciente', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_consulta = db.Column(db.ForeignKey('tb_consulta.co_seq_consulta', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    co_seq_tp_vacina = db.Column(db.ForeignKey('tb_tipo_vacina.co_seq_tp_vacina', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_vacina = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_consulta = db.relationship('TbConsulta', primaryjoin='TbVacina.co_seq_consulta == TbConsulta.co_seq_consulta', backref='tb_vacinas')
    tb_paciente = db.relationship('TbPaciente', primaryjoin='TbVacina.co_seq_paciente == TbPaciente.co_seq_paciente', backref='tb_vacinas')
    tb_tipo_vacina = db.relationship('TbTipoVacina', primaryjoin='TbVacina.co_seq_tp_vacina == TbTipoVacina.co_seq_tp_vacina', backref='tb_vacinas')



class TbValorTipoProcedimento(db.Model):
    __tablename__ = 'tb_valor_tipo_procedimento'

    co_seq_vr_tp_procedimento = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_tp_procedimento = db.Column(db.ForeignKey('tb_tipo_procedimento.co_seq_tp_procedimento', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    vr_procedimento = db.Column(db.Numeric(12, 2), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)
    dt_ini = db.Column(db.Numeric(8, 0), nullable=False)
    dt_ter = db.Column(db.Numeric(8, 0))

    tb_tipo_procedimento = db.relationship('TbTipoProcedimento', primaryjoin='TbValorTipoProcedimento.co_seq_tp_procedimento == TbTipoProcedimento.co_seq_tp_procedimento', backref='tb_valor_tipo_procedimentoes')



class TbVersaoBancoDado(db.Model):
    __tablename__ = 'tb_versao_banco_dados'

    co_seq_versao_banco_dados = db.Column(db.Numeric(6, 0), primary_key=True, unique=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)



class TbVinculoPessoa(db.Model):
    __tablename__ = 'tb_vinculo_pessoa'

    co_seq_vinculo_pessoa = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    pes_co_seq_pessoa = db.Column(db.ForeignKey('tb_pessoa.co_seq_pessoa', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_pessoa = db.relationship('TbPessoa', primaryjoin='TbVinculoPessoa.co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tbpessoa_tb_vinculo_pessoas')
    tb_pessoa1 = db.relationship('TbPessoa', primaryjoin='TbVinculoPessoa.pes_co_seq_pessoa == TbPessoa.co_seq_pessoa', backref='tbpessoa_tb_vinculo_pessoas_0')



class TbVolumeSoro(db.Model):
    __tablename__ = 'tb_volume_soro'

    co_seq_volume_soro = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    vr_volume_minimo = db.Column(db.Numeric(8, 0), nullable=False)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)



class TbVolumeSoroExame(db.Model):
    __tablename__ = 'tb_volume_soro_exame'

    co_seq_volume_soro_exame = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.FetchedValue())
    co_seq_volume_soro = db.Column(db.ForeignKey('tb_volume_soro.co_seq_volume_soro', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    co_seq_tp_exame_metodo = db.Column(db.ForeignKey('tb_tipo_exame_metodo.co_seq_tp_exame_metodo', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    dt_hr_cancelamento = db.Column(db.Numeric(14, 0))
    aut_cancelamento = db.Column(db.String(20))
    dt_hr_registro = db.Column(db.Numeric(14, 0), nullable=False)
    aut_registro = db.Column(db.String(20), nullable=False)

    tb_tipo_exame_metodo = db.relationship('TbTipoExameMetodo', primaryjoin='TbVolumeSoroExame.co_seq_tp_exame_metodo == TbTipoExameMetodo.co_seq_tp_exame_metodo', backref='tb_volume_soro_exames')
    tb_volume_soro = db.relationship('TbVolumeSoro', primaryjoin='TbVolumeSoroExame.co_seq_volume_soro == TbVolumeSoro.co_seq_volume_soro', backref='tb_volume_soro_exames')
