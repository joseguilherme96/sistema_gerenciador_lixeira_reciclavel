from flask import Blueprint
from flask import jsonify
from flask import request
import datetime
import os
import jwt

from flask_jwt_extended import create_access_token


login_blueprint = Blueprint('login',__name__)

## Está função é uma validação temporaria apenas para finalizar o frontend com autenticação com JWT, mas posteriormente será feito consulta valida do usuário no banco de dados 
@login_blueprint.route('/login',methods=["POST"])
def login():

    usuario = request.json.get('usuario')
    senha = request.json.get('senha')

    if usuario != "default" or senha != "default":

        return jsonify({"message","Usuário ou senha incorretos !"}),401
    
    token_acesso = create_access_token(identity=usuario,expires_delta=datetime.timedelta(minutes=1))
    return jsonify(token_acesso=token_acesso,usuario=usuario)

@login_blueprint.route('/validar_token',methods=["POST"])
def validar_token():

    try:

        token = request.json.get('token')
        usuario = request.json.get('usuario')
        jwt.decode(token,os.getenv('JWT_SECRET_KEY'), algorithms=["HS256"])
        
        return jsonify({"message":"Token válido !",'usuario':usuario,'token_acesso':token,'token':True}),200

    except jwt.ExpiredSignatureError:

        return jsonify({"message":"Token expirado !","token":False})

    except jwt.InvalidTokenError:

        return jsonify({"message":"Token inválido !","token":False})
    
    except:

        return jsonify({'message':' Falha ao analisar token !',"token":False})





