from Models.Device import Device

def make_device_obj(request_json):
    print(request_json)
    return Device(
        deviceType=request_json["deviceType"],
        datePurchased=request_json["datePurchased"], 
        assignedUser=request_json["assignedUser"],
        assigner=request_json["assigner"],
        firmwareVersion=request_json["firmwareVersion"],      
        serialNumber=request_json["serialNumber"]
    )
