from Models.ExtensionsModel import db
from sqlalchemy import DateTime,Integer,String,Float,ForeignKey
from sqlalchemy.orm import mapped_column

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
    observacao = mapped_column(String(50))
    criado_em = mapped_column(DateTime)
    editado_em = mapped_column(DateTime)

    def insert(Lixeira):

        db.session.add(Lixeira)
        db.session.commit()
        return True
    
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
                "observacao" : result.observacao,
                "criado_em" : result.criado_em,
                "editado_em" : result.editado_em
            }]
        
        except Exception as e:

            db.session.rollback()
            raise

