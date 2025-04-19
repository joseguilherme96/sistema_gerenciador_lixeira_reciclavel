from Models.ExtensionsModel import db
from sqlalchemy import Date,Time

class PontoLixo(db.Model):

    __tablename__ = 'ponto_lixo'

    id_ponto_lixo = db.Column(db.Integer, primary_key=True)
    data = db.Column(Date)
    time = db.Column(Time)

    def insert(PontoLixo):

        db.session.add(PontoLixo)
        db.session.commit()
        return True
    
    def select(where = []):

        query = db.select(PontoLixo)

        if where.get('ponto_lixo_id'):
            
            query = query.where(PontoLixo.id_ponto_lixo == where['ponto_lixo_id'])
        
        result = db.session.execute(query).all()

        return result

