from mongoengine import (Document, StringField, IntField)
from .User import User

class DeviceMeasurement(Document):
    _id = StringField(required=True, primary_key=True)
    deviceId = StringField(required=True)
    deviceType = StringField(required=True)
    userId = StringField(required=True)
    reading = IntField(required=True)
    unit = StringField(required=True)

    def _validate_fields(self, data):
        deviceType = data["deviceType"]
        readingUnit = data["unit"]
        if deviceType == "THERMOMETER":
            if readingUnit != "celsius" and readingUnit != "fahrenheit":
                raise ValueError
        if deviceType == "SCALE":
            if readingUnit != "pound" and readingUnit != "kilogram":
                raise ValueError
        if deviceType == "PULSE":
            if readingUnit != "bpm" :
                raise ValueError
        if deviceType == "OXIMETER":
            if readingUnit != "percent" :
                raise ValueError
        if deviceType == "GLUCOMETER":
            if readingUnit != "mg/dl" :
                raise ValueError
        if deviceType == "BLOOD_PRESSURE":
            if readingUnit != "mmhg" :
                raise ValueError
        

    """
    set document fields
    """
    def set(self, data):
        self._validate_fields(data)
        self._id = data['id']
        self.deviceId = data['deviceId']
        self.deviceType = data['deviceType']
        self.userId = data["userId"]
        self.reading = data['reading']
        self.unit = data['unit']
        

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
            'deviceId': self.deviceId,
            'deviceType': self.deviceType,
            'reading': self.reading,
            'unit': self.unit,
            'userId': self.userId 
        }

