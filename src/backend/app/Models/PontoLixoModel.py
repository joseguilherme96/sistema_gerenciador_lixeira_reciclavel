from Models.ExtensionsModel import db
from sqlalchemy import Date,Time
from datetime import datetime

class PontoLixo(db.Model):

    __tablename__ = 'ponto_lixo'

    id_ponto_lixo = db.Column(db.Integer, primary_key=True, autoincrement = True)
    data = db.Column(Date)
    time = db.Column(Time)

    def insert(PontoLixo):

        try:

            data_hora = datetime.now()

            PontoLixo.data = data_hora.date()
            PontoLixo.time = data_hora.time()

            db.session.add(PontoLixo)
            db.session.flush()

            return {

                "ponto_lixo_id":PontoLixo.id_ponto_lixo,
                "data":str(PontoLixo.data),
                "hora":str(PontoLixo.time)

                
            }
        
        except Exception as e:

            raise
    
    def select(where = []):

        query = db.select(PontoLixo)

        for condicao in where:

            if condicao.get('ponto_lixo_id'):
            
                query = query.where(PontoLixo.id_ponto_lixo == condicao['ponto_lixo_id'])
        
            if condicao.get('data'):
            
                query = query.where(PontoLixo.data == condicao['data'])

            if condicao.get('hora'):
            
                query = query.where(PontoLixo.time == condicao['hora'])
        
        result = db.session.execute(query).all()

        return result

