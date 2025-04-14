from flask import Flask
from flask_migrate import Migrate
 
from Models.ExtensionsModel import db
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.PontoLixoModel import PontoLixo
from Routes.GrupoLixeira import lixeira


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():

    db.create_all()

app.register_blueprint(lixeira)



