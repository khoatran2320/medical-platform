import os
from mongoengine import connect
from src.Models.Device import Device as DeviceModel
def test_saveDevice():
    test_device = {
        "_id": "9012374",
        "deviceType": "THERMOMETER",
        "datePurchased": "02/12/2000",
        "assignedUser": "Jon Wick",
        "assigner": "John WIck",
        "firmwareVersion": "12.123",
        "serialNumber": 12345
    }   
    #db name
    db_name = "patient-monitor"

    #obtain user password stored in environment
    db_pass = os.environ["db_pass"]

    #databse URI
    URI = "mongodb+srv://khoa:{}@cluster0.bfh4g.mongodb.net/{}?retryWrites=true&w=majority".format(db_pass, db_name)
    db = connect(host=URI)
    #save device
    device = DeviceModel()
    device.set(test_device)
    device.save()

    #retrieve device
    retrieved_device = DeviceModel.objects(assignedUser=test_device['_id']).first()
    return retrieved_device.to_json() == test_device
    

