from Models.ExtensionsModel import db
from sqlalchemy import Date,Time

class PontoLixo(db.Model):

    __tablename__ = 'ponto_lixo'

    id_ponto_lixo = db.Column(db.Integer, primary_key=True)
    data = db.Column(Date)
    time = db.Column(Time)
