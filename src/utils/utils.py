import bcrypt
from datetime import datetime

def encrypt_pass(pw):
    pw = pw.encode('utf-8')
    hpw = bcrypt.hashpw(pw, bcrypt.gensalt())
    return hpw
    

def parse_date(date):
    try:
        date_of_birth = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        return False
    return True
