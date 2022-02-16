from mongoengine import connect
from device.device_utilities import make_device_obj
from Models.Device import Device


def test_saveDevice():
    test_device = {
        "deviceType": 1,
        "datePurchased": "02/12/2000",
        "assignedUser": "Jon Wick",
        "assigner": "John WIck",
        "firmwareVersion": 1.2,
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
    device = make_device_obj(test_device)
    device.save()

    #retrieve device
    retrieved_device = Device.objects(assignedUser=test_device['assignedUser']).first()
    return retrieved_device.to_json() == test_device
    

