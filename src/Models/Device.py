from mongoengine import (Document, StringField, FloatField, ReferenceField, IntField)
from .User import User

class Device(Document):
    deviceType = IntField(min_value=1, max_value=6)
    datePurchased = StringField()
    assignedUser = ReferenceField('User')
    assigner = ReferenceField('User')
    firmwareVersion = FloatField(min_value=0.0)
    serialNumber = IntField(min_value=0)

    def to_json(self):
        return {
            'deviceType': self.deviceType,
            'datePurchased': self.datePurchased,
            'assignedUser': self.assignedUser,
            'assigner': self.assigner,
            'firmwareVersion': self.firmwareVersion,
            'serialNumber': self.serialNumber
        }

