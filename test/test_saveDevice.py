import os
from mongoengine import connect
from src.Models.Device import Device as DeviceModel
import pytest

"""
test saving a device to the database. Connection to live db is unavailable due to IP filtering. Will have to manually enable global IP request for test to pass under GitHub Actions environment.
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

def test_saveDevice(database):
    test_device = {
        "id": "9012374",
        "deviceType": "THERMOMETER",
        "datePurchased": "02/12/2000",
        "assignedUser": "Jon Wick",
        "assigner": "John WIck",
        "firmwareVersion": "12.123",
        "serialNumber": 12345
    }   
    #save device
    device = DeviceModel()
    device.set(test_device)
    device.save()

    #retrieve device
    retrieved_device = DeviceModel.objects(_id=test_device['id']).first()
    return retrieved_device.json() == test_device
    

