from ..Models.Device import Device
from ..utils.utils import parse_date    

def make_device_obj(request_json):
    if not parse_date(request_json["datePurchased"]):
        return None

    return Device(
        deviceType=request_json["deviceType"],
        datePurchased=request_json["datePurchased"], 
        assignedUser=request_json["assignedUser"],
        assigner=request_json["assigner"],
        firmwareVersion=request_json["firmwareVersion"],      
        serialNumber=request_json["serialNumber"]
    )


