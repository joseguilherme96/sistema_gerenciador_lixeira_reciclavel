# Usando modelo de Mapeamento Declarativo

from Models.ExtensionsModel import db

from sqlalchemy import Integer,Enum,DateTime
from sqlalchemy.orm import mapped_column

class MaterialColetado(db.Model):

    __tablename__= "material_coletado"
    
    id_mat_colet = mapped_column(Integer, primary_key=True,autoincrement = True)
    nome = mapped_column(Enum("Plástico",'Papel','Metal','Orgânico','Vidro',
                              'Outros','Não Reciclável',name="nome_enum"),nullable=True)
    criado_em = mapped_column(DateTime)

    def insert(MaterialColetado):

        db.session.begin()

        try:

            db.session.add(MaterialColetado)
            db.session.commit()

            return {
                "id_mat_colet":MaterialColetado.id_mat_colet,
                "nome":MaterialColetado.nome,
                "criado_em":MaterialColetado.criado_em
            }
        
        except Exception as e:
            
            db.session.rollback()
            raise # Raise levanta uma exceção

    def select(where = []):
         
        query =  db.select(MaterialColetado)
        
        # Será considerado está query para nome caso nome não esteja definido para consulta, pois a consulta não está permitindo não 
        # filtrar nome devido ao Enum(....) que permite valores predefinidos, a solução para contornar este problema foi criar uma condição 
        # "default" para nome. Caso nome não venha com valor predefinido a ser buscado.
        query = query.where(MaterialColetado.nome.in_(["Plástico",'Papel','Metal','Orgânico','Vidro',
                              'Outros','Não Reciclável']))

        for condicao in where:

            if condicao.get('mat_colet_id'):
            
                query = query.where(MaterialColetado.id_mat_colet == condicao['mat_colet_id'])

            if condicao.get('nome'):
            
                query = query.where(MaterialColetado.nome == condicao['nome'])
            
            if condicao.get('criado_em'):
            
                query = query.where(MaterialColetado.criado_em == condicao['criado_em'])
        
        result = db.session.execute(query).all()

        return result