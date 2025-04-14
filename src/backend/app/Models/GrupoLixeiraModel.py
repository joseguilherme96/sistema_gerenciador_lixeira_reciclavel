from Models.ExtensionsModel import db

class GrupoLixeira(db.Model):

    __tablename__ = 'grupo_lixeira'

    id_lixeira = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    descricao = db.Column(db.String(256))
    cep = db.Column(db.String(10))
    endereco = db.Column(db.String(256))
    cidade = db.Column(db.String(128))
    estado = db.Column(db.String(128))
    uf = db.Column(db.String(2))

    def insert(lixeira):

        db.session.add(lixeira)
        db.session.commit()
        return True
       


    def select():

        users = db.session.execute(db.select(GrupoLixeira)).all()

        return users

