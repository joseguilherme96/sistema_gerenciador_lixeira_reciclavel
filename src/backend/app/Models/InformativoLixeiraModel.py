from Models.ExtensionsModel import db

from sqlalchemy import Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import mapped_column

class InformativoLixeira(db.Model):

    id_informativo = mapped_column(Integer,primary_key=True,autoincrement = True)
    ponto_lixo_id = mapped_column(Integer,ForeignKey("ponto_lixo.id_ponto_lixo"))
    informado_por_id = mapped_column(Integer, ForeignKey("informado_por.id_informador"))
    nivel_lixeira = mapped_column(Float)
    observacao = mapped_column(String(50))
    criado_em = mapped_column(DateTime)