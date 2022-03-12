from mongoengine import (Document, StringField, FloatField, IntField)
from .User import User

class Device(Document):
    _id = StringField(required=True, primary_key=True)
    deviceType = IntField(min_value=1, max_value=6, required=True)
    datePurchased = StringField(required=True)
    assignedUser = StringField(default="")
    assigner = StringField(default="")
    firmwareVersion = FloatField(min_value=0.0, required=True)
    serialNumber = IntField(min_value=0, required=True)

    """
    set document fields
    """
    def set(self, data):
        self._id = data['id']
        self.deviceType = data['deviceType']
        self.datePurchased = data['datePurchased']
        self.firmwareVersion = data['firmwareVersion']
        self.serialNumber = data['serialNumber']
        
        """
        optional fields
        """
        if data['assignedUser']:
            self.assignedUser = data['assignedUser']
        if data['assigner']:
            self.assigner = data['assigner']

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
            'deviceType': self.deviceType,
            'datePurchased': self.datePurchased,
            'assignedUser': self.assignedUser,
            'assigner': self.assigner,
            'firmwareVersion': self.firmwareVersion,
            'serialNumber': self.serialNumber
        }

