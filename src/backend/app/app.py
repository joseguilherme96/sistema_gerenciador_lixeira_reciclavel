# Flask

from flask import Flask,request,jsonify
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
from Routes.Socketio import socketio
 
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
from Routes.InformativoLixeira import informativo_lixeira
from Routes.MaterialColetado import material_coletado
from Routes.PontoLixo import ponto_lixo
from Routes.Cor import cor
from Routes.GrupoLixeiraPontoLixoLixeira import grupo_lixeira_ponto_lixo_lixeira
from Routes.Log import log
from Routes.Estado import estado
from Routes.Login import login_blueprint

# Variavel de ambiente
from dotenv import load_dotenv
import os

# JWT Manager
from flask_jwt_extended import JWTManager

load_dotenv()

# Instância do Flask
app = Flask(__name__)

# Configuração SQLALCHEMY/Banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')

CORS(app, origins = os.getenv('ORIGENS_PERMITIDAS').split(',')) # Permite URL que está sendo executada o front-end

socketio.init_app(app)

jwt = JWTManager(app)

db.init_app(app)
migrate = Migrate(app, db)

# Cria esquema das tabelas no banco de dados
with app.app_context():

    db.create_all()

# Registra Rotas das APIs
app.register_blueprint(grupo_lixeira)
app.register_blueprint(lixeira)
app.register_blueprint(informativo_lixeira)
app.register_blueprint(material_coletado)
app.register_blueprint(ponto_lixo)
app.register_blueprint(cor)
app.register_blueprint(grupo_lixeira_ponto_lixo_lixeira)
app.register_blueprint(log)
app.register_blueprint(estado)
app.register_blueprint(login_blueprint)

# Personaliza mensagens de erro para códigos de respostas HTTP 404,405 e 415.
@app.errorhandler(405)
def metodo_nao_permitido(e):

    return jsonify({'message':"Metodo não permitido !"}),405

@app.errorhandler(404)
def pagina_nao_encontrada(e):

    return jsonify({'message':"Página não encontrada !"}),404

@app.errorhandler(415)
def tipo_media(e):

    return jsonify({'message':'O tipo de conteúdo enviado não é suportado pelo servidor !'}),415

@jwt.expired_token_loader
def rota_nao_autorizada(jwt_header,jwt_payload):

    print(jwt_header)

    return jsonify(message="Acesso não autorizado"),401



app.run(debug=False,host='0.0.0.0',port=5000)
socketio.run(app,host='0.0.0.0',port=5000)


