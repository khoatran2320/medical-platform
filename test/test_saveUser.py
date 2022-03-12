import os
from mongoengine import connect
import pytest
from src.Models.User import User as UserModel

"""
test saving a user to the database. Connection to live db is unavailable due to IP filtering. Will have to manually enable global IP request for test to pass under GitHub Actions environment.
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
    
def test_saveUser(database):
    test_user = {
        "id": "9011232374",
        "firstName": "Jon",
        "lastName": "Wick",
        "email": "jonwick123@gmail.com",
        "password": "password",
        "userType": "doctor",
        "gender": "male",
        "dateOfBirth": "01/01/2000",
        "address": "12345 painword ave",
        "age": 22
        
    }   
    #save device
    user = UserModel()
    user.set(test_user)
    user.save()

    #retrieve device
    retrieved_user = UserModel.objects(_id=test_user['id']).first()
    return retrieved_user.json() == test_user
    

