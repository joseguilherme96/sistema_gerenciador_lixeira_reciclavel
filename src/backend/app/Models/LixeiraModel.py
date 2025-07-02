from Models.ExtensionsModel import db
from sqlalchemy import DateTime,Integer,String,Float,ForeignKey,Boolean
from sqlalchemy.orm import mapped_column
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.MaterialColetadoModel import MaterialColetado

class Lixeira(db.Model):

    __tablename__ = 'lixeira'
    
    id_lixeira = mapped_column(Integer, primary_key=True,autoincrement = True)
    descricao = mapped_column(String(30))
    mat_colet_id = mapped_column(Integer,ForeignKey("material_coletado.id_mat_colet"))
    grupo_lixeira_id = mapped_column(Integer,ForeignKey("grupo_lixeira.id_grupo_lixeira"))
    ponto_lixo_id = mapped_column(Integer,ForeignKey("ponto_lixo.id_ponto_lixo"))
    cor_id = mapped_column(Integer,ForeignKey("cor.id_cor"))
    capacidade = mapped_column(Float)
    nivel_lixeira = mapped_column(Float)
    esta_aberta = mapped_column(Boolean)
    observacao = mapped_column(String(50))
    criado_em = mapped_column(DateTime)
    editado_em = mapped_column(DateTime)

    def insert(Lixeira):
        try:    
            db.session.add_all(Lixeira)
            db.session.flush()

            return Lixeira

        except Exception as e:
            raise
    
    def select(where = []):
         
        query =  db.select(Lixeira)

        for condicao in where:

            if condicao.get('cor_id'):
            
                query = query.where(Lixeira.id_lixeira == condicao['id_lixeira'])

            if condicao.get('grupo_lixeira_id'):
            
                query = query.where(Lixeira.grupo_lixeira_id == condicao['grupo_lixeira_id'])

            if condicao.get('lixeira_id'):
            
                query = query.where(Lixeira.id_lixeira == condicao['lixeira_id'])

        result = db.session.execute(query).all()

        return result
    
    def update(lixeira):

        db.session.begin()

        try:

            stmt = db.select(Lixeira).where(Lixeira.id_lixeira == lixeira.id_lixeira)
            result = db.session.scalars(stmt).one()

            result.nivel_lixeira = lixeira.nivel_lixeira
            result.esta_aberta = lixeira.esta_aberta
            db.session.commit()

            return [{
                
                "id_lixeira": result.id_lixeira,
                "descricao" : result.descricao,
                "grupo_lixeira_id" : result.grupo_lixeira_id,
                "ponto_lixo_id" : result.ponto_lixo_id,
                "cor_id" : result.cor_id,
                "capacidade" : result.capacidade,
                "mat_colet_id" : result.mat_colet_id,
                "nivel_lixeira" : result.nivel_lixeira,
                'esta_aberta': "Aberta" if result.esta_aberta else "Fechada",
                "observacao" : result.observacao,
                "criado_em" : result.criado_em,
                "editado_em" : result.editado_em
            }]
        
        except Exception as e:

            db.session.rollback()
            raise

    def calcular_media_nivel_lixo_por_grupo(where = []):

        query = db.select(Lixeira.grupo_lixeira_id, db.func.avg(Lixeira.nivel_lixeira).label('media_nivel_lixeira'))

        try:

            for condicao in where:

                if condicao.get('grupo_lixeira_id'):

                    query = query.where(Lixeira.grupo_lixeira_id == condicao['grupo_lixeira_id'])

            result = db.session.execute(query).all()
        
        except:

            raise


        result = db.session.execute(query).all()

        return result

    def calcular_soma_capacidade_total_armazenamento_de_lixo_por_grupo(where = []):

        query = db.select(Lixeira.grupo_lixeira_id, db.func.sum(Lixeira.capacidade).label('capacidade_total'))

        try:

            for condicao in where:

                if condicao.get('grupo_lixeira_id'):

                    query = query.where(Lixeira.grupo_lixeira_id == condicao['grupo_lixeira_id'])

            result = db.session.execute(query).all()
        
        except:

            raise


        result = db.session.execute(query).all()

        return result
    
    def join_lixeira_grupo_lixeira(where = []):

        query = db.select(Lixeira, GrupoLixeira,MaterialColetado).join(GrupoLixeira, Lixeira.grupo_lixeira_id == GrupoLixeira.id_grupo_lixeira).join(MaterialColetado,Lixeira.mat_colet_id == MaterialColetado.id_mat_colet)

        try:

            for condicao in where:

                if condicao.get('lixeira_id'):

                    query = query.where(Lixeira.id_lixeira == condicao['lixeira_id'])

                if condicao.get('grupo_lixeira_id'):

                    query = query.where(Lixeira.grupo_lixeira_id == condicao['grupo_lixeira_id'])

                
                if condicao.get('mat_colet_id'):

                    query = query.where(MaterialColetado.id_mat_colet == condicao['mat_colet_id'])

                if condicao.get('material_coletado'):

                    query = query.where(MaterialColetado.nome == str(condicao['material_coletado']))

                if condicao.get('capacidade'):

                    query = query.where(Lixeira.capacidade == condicao['capacidade'])

                if condicao.get('nivel_lixeira_menor_igual_que'):

                    query = query.where(Lixeira.nivel_lixeira < condicao['nivel_lixeira_menor_igual_que'])

                if condicao.get('nivel_lixeira_igual_que'):

                    query = query.where(Lixeira.nivel_lixeira == condicao['nivel_lixeira_igual_que'])

                if condicao.get('nivel_lixeira_maior_que'):

                    query = query.where(Lixeira.nivel_lixeira > condicao['nivel_lixeira_maior_que'])

                if condicao.get('endereco'):

                    query = query.where(GrupoLixeira.endereco == condicao['endereco'])

                if condicao.get('bairro'):

                    query = query.where(GrupoLixeira.bairro == condicao['bairro'])

                if condicao.get('cidade'):

                    query = query.where(GrupoLixeira.cidade == condicao['cidade'])

                if condicao.get('estado'):

                    query = query.where(GrupoLixeira.estado == condicao['estado'])

            result = db.session.execute(query).all()

        except:

            raise

        return result
