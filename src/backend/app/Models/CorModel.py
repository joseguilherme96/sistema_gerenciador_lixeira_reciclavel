from Models.ExtensionsModel import db

from sqlalchemy import Integer, String,Enum
from sqlalchemy.orm import mapped_column


class Cor(db.Model):

    __tablename__ = 'cor'
    
    id_cor = mapped_column(Integer,primary_key=True)
    nome = mapped_column(Enum("Roxo","Azul","Verde","Amarelo","Laranja","Vermelho","Marrom",
                              "Preto","Cinza","Branco"))
    