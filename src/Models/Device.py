from email.policy import default
from mongoengine import (Document, StringField, FloatField, ReferenceField, IntField)
from .User import User

class Device(Document):
    _id = StringField(required=True, primary_key=True)
    deviceType = IntField(min_value=1, max_value=6, required=True)
    datePurchased = StringField(required=True)
    assignedUser = StringField(default="")
    assigner = StringField(default="")
    firmwareVersion = FloatField(min_value=0.0, required=True)
    serialNumber = IntField(min_value=0, required=True)

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

