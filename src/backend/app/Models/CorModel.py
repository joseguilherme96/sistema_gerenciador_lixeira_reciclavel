from Models.ExtensionsModel import db

from sqlalchemy import Integer, String,Enum
from sqlalchemy.orm import mapped_column


class Cor(db.Model):

    __tablename__ = 'cor'
    
    id_cor = mapped_column(Integer,primary_key=True,autoincrement=True)
    nome = mapped_column(Enum("Roxo","Azul","Verde","Amarelo","Laranja","Vermelho","Marrom",
                              "Preto","Cinza","Branco"))
    
    def insert(Cor):

        db.session.add(Cor)
        db.session.commit()
        return True
    
    def select(where = []):
         
        query =  db.select(Cor)

        for condicao in where:

            if condicao.get('cor_id'):
            
                query = query.where(Cor.id_cor == condicao['cor_id'])

        result = db.session.execute(query).all()

        return result