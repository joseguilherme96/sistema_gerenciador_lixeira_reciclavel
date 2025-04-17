# Flask

from flask import Flask
from flask_migrate import Migrate
 
# Models(Modelos)
from Models.ExtensionsModel import db
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.PontoLixoModel import PontoLixo
from Models.MaterialColetadoModel import MaterialColetado
from Models.CorModel import Cor
from Models.LixeiraModel import Lixeira

# Routes(Rotas)
from Routes.GrupoLixeira import lixeira

# Instância do Flask
app = Flask(__name__)

# Configuração SQLALCHEMY/Banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)
migrate = Migrate(app, db)

# Cria esquema das tabelas no banco de dados
with app.app_context():

    db.create_all()

# Registra Rotas das APIs
app.register_blueprint(lixeira)



