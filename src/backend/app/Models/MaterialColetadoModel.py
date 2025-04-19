# Usando modelo de Mapeamento Declarativo

from Models.ExtensionsModel import db

from sqlalchemy import Integer,Enum,DateTime
from sqlalchemy.orm import mapped_column   

class MaterialColetado(db.Model):

    __tablename__= "material_coletado"
    
    id_mat_colet = mapped_column(Integer, primary_key=True  )
    nome = mapped_column(Enum("Plástico",'Papel','Metal','Orgânico','Vidro',
                              'Outros','Não Reciclável',name="nome_enum"),nullable=False)
    criado_em = mapped_column(DateTime)

    def insert(MaterialColetado):

        db.session.add(MaterialColetado)
        db.session.commit()
        return True

    def select(where = []):
         
        query =  db.select(MaterialColetado)

        for condicao in where:

            if condicao.get('mat_colet_id'):
            
                query = query.where(MaterialColetado.id_mat_colet == condicao['mat_colet_id'])

        result = db.session.execute(query).all()

        return result