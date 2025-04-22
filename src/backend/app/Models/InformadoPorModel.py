from Models.ExtensionsModel import db

from sqlalchemy import Integer, Enum
from sqlalchemy.orm import mapped_column

class InformadoPor(db.Model):

    __tablename__ = "informado_por"

    id_informador = mapped_column(Integer, primary_key= True, autoincrement = True)
    informador = mapped_column(Enum("Usuário","Microcontrolador ESP32"))