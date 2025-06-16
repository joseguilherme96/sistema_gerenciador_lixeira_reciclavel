from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token


login_blueprint = Blueprint('login',__name__)

@login_blueprint.route('/login',methods=["POST"])
def login():

    usuario = request.json.get('usuario',None)
    senha = request.json.get('senha',None)

    if usuario != "default" or senha != "default":

        return jsonify({"message","Usuário ou senha incorretos !"}),401
    
    token_acesso = create_access_token(identity=usuario)
    return jsonify(token_acesso=token_acesso)
