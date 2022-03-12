from mongoengine import (Document, StringField, DateTimeField)
from datetime import datetime
from json import dumps

class Chat(Document):
    _id = StringField(required=True, primary_key=True)
    timestamp = DateTimeField(default=datetime.now)
    fromUser = StringField(required=True)
    toUser = StringField(required=True)
    content = StringField(required=True)
    attachment = StringField(default="")

    """
    set document fields
    """
    def set(self, data):
        self._id = data['id']
        self.fromUser = data['fromUser']
        self.toUser = data['toUser']
        self.content = data['content']
        self.attachment = data['attachment']
        
        """
        optional fields
        """
        if data['attachment']:
            self.attachment = data['attachment']

    """
    update document fields
    """
    def update(self, data):
        for key, val in data.items():
            if val is not None and key != 'id':
                self[key] = val

    """
    delete document
    """
    def delete(self):
        self.delete()

    """
    returns json of fields
    """
    def json(self):
        return {
            'id': self._id,
            'timestamp': self.timestamp.strftime("%m/%d/%Y, %H:%M:%S.%f"),
            'fromUser': self.fromUser,
            'toUser': self.toUser,
            'content': self.content,
            'attachment': self.attachment,
        }
