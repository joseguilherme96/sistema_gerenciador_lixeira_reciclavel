from Models.ExtensionsModel import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer,String,Date,Time
from datetime import datetime

class GrupoLixeira(db.Model):

    __tablename__ = 'grupo_lixeira'

    id_grupo_lixeira = mapped_column(Integer, primary_key=True,nullable=False,autoincrement=True)
    nome = mapped_column(String(128))
    descricao = mapped_column(String(256))
    cep = mapped_column(String(10))
    endereco = mapped_column(String(256))
    bairro = mapped_column(String(128))
    cidade = mapped_column(String(128))
    estado = mapped_column(String(128))
    uf = mapped_column(String(2))
    data = mapped_column(Date)
    hora = mapped_column(Time)

    def insert(GrupoLixeira):

        try:

            data_hora = datetime.now()

            GrupoLixeira.data = data_hora.date()
            GrupoLixeira.hora = data_hora.time()

            db.session.add(GrupoLixeira)
            db.session.flush()

            return [{
                "id_grupo_lixeira":GrupoLixeira.id_grupo_lixeira,
                "nome":GrupoLixeira.nome,
                "descricao":GrupoLixeira.descricao,
                "cep":GrupoLixeira.cep,
                "endereco":GrupoLixeira.endereco,
                "bairro":GrupoLixeira.bairro,
                "cidade":GrupoLixeira.cidade,
                "estado":GrupoLixeira.estado,
                "uf":GrupoLixeira.uf,
                "data":str(GrupoLixeira.data),
                "hora":str(GrupoLixeira.hora)

            }]
        
        except Exception as e:
            
            raise # Raise levanta uma exceção
       


    def select(where = []):

        query = db.select(GrupoLixeira)

        for condicao in where:

            if(condicao.get('grupo_lixeira_id')):

                query = query.where(GrupoLixeira.id_grupo_lixeira == condicao['grupo_lixeira_id'])

            if(condicao.get('nome')):

                query = query.where(GrupoLixeira.nome == condicao['nome'])

            if(condicao.get('descricao')):

                query = query.where(GrupoLixeira.nome == condicao['descricao'])

            if(condicao.get('logradouro')):

                query = query.where(GrupoLixeira.endereco == condicao['logradouro'])

            if(condicao.get('bairro')):

                query = query.where(GrupoLixeira.bairro == condicao['bairro'])

            if(condicao.get('cidade')):

                query = query.where(GrupoLixeira.cidade == condicao['cidade'])

            if(condicao.get('estado')):

                query = query.where(GrupoLixeira.estado == condicao['estado'])

            if(condicao.get('uf')):

                query = query.where(GrupoLixeira.uf == condicao['uf'])

            if(condicao.get('data')):

                query = query.where(GrupoLixeira.data == condicao['data'])

            if(condicao.get('hora')):

                query = query.where(GrupoLixeira.hora == condicao['hora'])

        stmt = db.session.execute(query).all()

        return stmt

