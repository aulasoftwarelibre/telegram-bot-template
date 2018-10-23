# coding=utf-8
from datetime import datetime
from model import db

class Chat(db.Model):
    """Almacén clave/valor para un chat concreto

    Note:
        Si se quiere guardar un valor para todos los chats, usar el valor Id=0

    El objetivo es poder guardar variables de estado de un chat (privado o grupo).Se almacena
    también la fecha de guardado o actualización.
    """
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    chat = db.Column(db.BigInteger, nullable=False)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def set_config(chat, key, value):
        """Guarda un valor

        Args:
            :param chat: Id. del chat
            :param key: Clave del dato
            :param value: Valor del dato

        Returns:
            :return: Instancia de Chat con el valor almacenado
        """
        record = db.session.query(Chat).filter_by(chat=chat, key=key).first()

        if record is None:
            record = Chat(chat=chat, key=key, value=value, created_at=datetime.now())
            db.session.add(record)
        else:
            record.value = value
            record.created_at = datetime.now()

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def get_config(chat, key):
        """ Recupera un valor

        Args:
            :param chat: Id. del chat
            :param key: Clave del valor a recuperar

        Returns:
            :return: Instancia de Chat que coincide con la clave o None si no existe
        """
        record = db.session.query(Chat).filter_by(chat=chat, key=key).first()
        db.session.close()

        return record


