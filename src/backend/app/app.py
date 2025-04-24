# Flask

from flask import Flask,request,jsonify
from flask_migrate import Migrate
 
# Models(Modelos)
from Models.ExtensionsModel import db
from Models.GrupoLixeiraModel import GrupoLixeira
from Models.PontoLixoModel import PontoLixo
from Models.MaterialColetadoModel import MaterialColetado
from Models.CorModel import Cor
from Models.LixeiraModel import Lixeira
from Models.InformadoPorModel import InformadoPor
from Models.InformativoLixeiraModel import InformativoLixeira

# Routes(Rotas)
from Routes.GrupoLixeira import grupo_lixeira
from Routes.Lixeira import lixeira

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
app.register_blueprint(grupo_lixeira)
app.register_blueprint(lixeira)


# Personaliza mensagens de erro para códigos de respostas HTTP 404/405
@app.errorhandler(405)
def metodo_nao_permitido(e):

    return jsonify({'message':"Metodo não permitido !"}),405

@app.errorhandler(404)
def pagina_nao_encontrada(e):

    return jsonify({'message':"Página não encontrada !"}),404
