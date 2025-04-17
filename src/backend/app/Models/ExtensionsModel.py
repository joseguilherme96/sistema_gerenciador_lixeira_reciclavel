from flask_sqlalchemy import SQLAlchemy

# Poderia passar a instancia do Flask aqui como parâmetro...porém como db tem multiplas instâncias.....
# A intância do Flask será passada posteriormente no arquivo principal app.py
db = SQLAlchemy()