import bcrypt

def encrypt_pass(pw):
    # pw = pw.encode('utf-8')
    hpw = bcrypt.hashpw(pw, bcrypt.gensalt())
    return hpw
    
