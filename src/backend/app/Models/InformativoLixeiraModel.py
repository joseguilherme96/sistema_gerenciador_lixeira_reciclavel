from Models.ExtensionsModel import db

from sqlalchemy import Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import mapped_column

from datetime import datetime

class InformativoLixeira(db.Model):

    id_informativo = mapped_column(Integer,primary_key=True,autoincrement = True)
    ponto_lixo_id = mapped_column(Integer,ForeignKey("ponto_lixo.id_ponto_lixo"))
    informado_por_id = mapped_column(Integer, ForeignKey("informado_por.id_informador"))
    nivel_lixeira = mapped_column(Float)
    observacao = mapped_column(String(50))
    criado_em = mapped_column(DateTime)

    def select(where = []):

        query = db.select(InformativoLixeira)

        for condicao in where:

            if condicao.get('id_informativo'):

                query = query.where(InformativoLixeira.id_informativo == condicao['id_informativo'])

            if condicao.get('ponto_lixo_id'):

                query = query.where(InformativoLixeira.ponto_lixo_id == condicao['ponto_lixo_id'])
            
            if condicao.get('informado_por_id'):

                query = query.where(InformativoLixeira.informado_por_id == condicao['informado_por_id'])

            if condicao.get('nivel_lixeira'):
                
                query = query.where(InformativoLixeira.nivel_lixeira == condicao['nivel_lixeira'])
            
            if condicao.get('criado_em'):
                
                query = query.where(InformativoLixeira.criado_em == condicao['criado_em'])

        
        result = db.session.execute(query)

        return result
    
    def insert(informativo_lixeira):

        informativo_lixeira.criado_em = datetime.now()

        try:
            db.session.add(informativo_lixeira)
            db.session.commit()
            return informativo_lixeira

        except Exception as e:
            print(str(e))
            return False