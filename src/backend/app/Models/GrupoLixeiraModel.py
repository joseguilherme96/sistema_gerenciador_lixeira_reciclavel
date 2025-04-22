from Models.ExtensionsModel import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer,String

class GrupoLixeira(db.Model):

    __tablename__ = 'grupo_lixeira'

    id_grupo_lixeira = mapped_column(Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = mapped_column(String(128))
    descricao = mapped_column(String(256))
    cep = mapped_column(String(10))
    endereco = mapped_column(String(256))
    cidade = mapped_column(String(128))
    estado = mapped_column(String(128))
    uf = mapped_column(String(2))

    def insert(lixeira):

        db.session.add(lixeira)
        db.session.commit()
        return True
       


    def select(where = []):

        query = db.select(GrupoLixeira)

        for condicao in where:

            if(condicao.get('grupo_lixeira_id')):

                query = query.where(GrupoLixeira.id_grupo_lixeira == condicao['grupo_lixeira_id'])

        stmt = db.session.execute(query).all()

        return stmt

