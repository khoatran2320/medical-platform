from mongoengine import (Document, StringField, DateTimeField, EmbeddedDocument, ListField, EmbeddedDocumentField)
from datetime import datetime
from json import dumps

class Chat(EmbeddedDocument):
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

class ChatRoom(Document):
    _id = StringField(required=True, primary_key=True)
    users = ListField(StringField(), required=True)
    chats = ListField(EmbeddedDocumentField(Chat))

    def set(self, data):
        self._id = data['id']
        self.users = data['users']

    def get_id(self):
        return self._id

    def add_chat(self, chat):
        try:
            self.chats.append(chat)
            self.save()
        except:
            raise Exception('Unable to add chat')