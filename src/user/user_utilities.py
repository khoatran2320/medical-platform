from ..Models.User import User
from ..utils.utils import encrypt_pass, parse_date

def make_user_obj(request_json):
    if not parse_date(request_json["dateOfBirth"]):
        return None

    if not parse_gender(request_json["gender"]):
        return None

    hpw = encrypt_pass(request_json["password"])
    
    return User(
        firstName=request_json["firstName"],
        lastName=request_json["lastName"], 
        email=request_json["email"],
        password = hpw,
        userType=request_json["userType"],      
        gender=request_json["gender"],
        dateOfBirth=request_json["dateOfBirth"],
        address=request_json["address"],
        age=request_json["age"]
    )

def parse_gender(gn):
    if gn != 'male' or gn != 'female' or gn != 'nonBinary':
        return False
    return True
