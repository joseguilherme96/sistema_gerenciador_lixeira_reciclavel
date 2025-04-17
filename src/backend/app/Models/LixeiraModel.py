from Models.ExtensionsModel import db
from sqlalchemy import DateTime,Integer,String,Float,ForeignKey
from sqlalchemy.orm import mapped_column

class Lixeira(db.Model):

    __tablename__ = 'lixeira'
    
    id_lixeira = mapped_column(Integer, primary_key=True)
    descricao = mapped_column(String(30))
    mat_colet_id = mapped_column(Integer,ForeignKey("material_coletado.id_mat_colet"))
    grupo_lixeira_id = mapped_column(Integer,ForeignKey("grupo_lixeira.id_lixeira"))
    ponto_lixo_id = mapped_column(Integer,ForeignKey("ponto_lixo.id_ponto_lixo"))
    cor_id = mapped_column(Integer,ForeignKey("cor.id_cor"))
    capacidade = mapped_column(Float)
    nivel_lixeira = mapped_column(Float)
    observacao = mapped_column(String(50))
    criado_em = mapped_column(DateTime)
    editado_em = mapped_column(DateTime)