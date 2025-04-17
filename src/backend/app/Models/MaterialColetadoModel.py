# Usando modelo de Mapeamento Declarativo

from Models.ExtensionsModel import db

from sqlalchemy import Integer,Enum,DateTime
from sqlalchemy.orm import mapped_column


class MaterialColetado(db.Model):

    __tablename__= "material_coletado"
    
    id_mat_colet = mapped_column(Integer, primary_key=True)
    nome = mapped_column(Enum("Plástico",'Papel','Metal','Orgânico','Vidro',
                              'Outros','Não Reciclável',name="nome_enum"),nullable=False)
    criado_em = mapped_column(DateTime)