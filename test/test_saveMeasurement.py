import os
from mongoengine import connect
from src.Models.DeviceMeasurement import DeviceMeasurement as DeviceMeasurementModel
import pytest

"""
test saving a device measurement to the database. Connection to live db is unavailable due to IP filtering. Will have to manually enable global IP request for test to pass under GitHub Actions environment.
"""
@pytest.fixture()
def database():
    #db name
    db_name = "patient-monitor"

    #obtain user password stored in environment
    db_pass = os.environ["db_pass"]

    #databse URI
    URI = "mongodb+srv://khoa:{}@cluster0.bfh4g.mongodb.net/{}?retryWrites=true&w=majority".format(db_pass, db_name)
    db = connect(host=URI)

def test_saveDeviceMeasurement(database):
    test_deviceMeasurement = {
        "id": "2343651",
        "deviceType": "THERMOMETER",
        "deviceId": "9012374",
        "userId": "9011232374",
        "reading": "94",
        "unit": "fahrenheit"
    }   
    #save measurement
    measurement = DeviceMeasurementModel()
    measurement.set(test_deviceMeasurement)
    measurement.save()
    comp_keys = ['id', 'deviceType', "deviceId", "userId", "reading","unit"]
    retrieved_deviceMeasurement = DeviceMeasurementModel.objects(_id=test_deviceMeasurement['id']).first()
    retrieved_deviceMeasurement = retrieved_deviceMeasurement.json()
    for key in comp_keys:
        if test_deviceMeasurement[key] != retrieved_deviceMeasurement[key]:
            return False
    return True

def test_invalid_userId(database):
    test_deviceMeasurement = {
        "id": "2343651",
        "deviceType": "THERMOMETER",
        "deviceId": "9012374",
        "userId": "does not exist",
        "reading": "94",
        "unit": "fahrenheit"
    }   

    try:
        measurement = DeviceMeasurementModel()
        measurement.set(test_deviceMeasurement)
        measurement.save()
        return False
    except:
        return True

def test_invalid_deviceId(database):
    test_deviceMeasurement = {
        "id": "2343651",
        "deviceType": "THERMOMETER",
        "deviceId": "does not exist",
        "userId": "9011232374",
        "reading": "94",
        "unit": "fahrenheit"
    }   

    try:
        measurement = DeviceMeasurementModel()
        measurement.set(test_deviceMeasurement)
        measurement.save()
        return False
    except:
        return True

def test_invalid_unit(database):
    test_deviceMeasurement = {
        "id": "2343651",
        "deviceType": "THERMOMETER",
        "deviceId": "9012374",
        "userId": "9011232374",
        "reading": "94",
        "unit": "pound"
    }   

    try:
        measurement = DeviceMeasurementModel()
        measurement.set(test_deviceMeasurement)
        measurement.save()
        return False
    except:
        return True