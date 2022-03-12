import os
from mongoengine import connect
from src.Models.Chat import Chat as ChatModel
import pytest

"""
test saving a message to the database. Connection to live db is unavailable due to IP filtering. Will have to manually enable global IP request for test to pass under GitHub Actions environment.
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

def test_saveMessage(database):
    test_message = {
        "id": "54324526",
        "fromUser": "234254",
        "toUser": "64336",
        "content": "hello. Testing with attachment",
        "attachment": "https://www.google.com",
    }   
    #save device
    message = ChatModel()
    message.set(test_message)
    message.save()

    #retrieve device
    retrieved_message = ChatModel.objects(_id=test_message['id']).first()
    if retrieved_message:
        retrieved_message = retrieved_message.json()
    comp_keys = ['id', 'fromUser', "toUser", "content", "attachment"]
    for key in comp_keys:
        if test_message[key] != retrieved_message[key]:
            return False
    return True

    
    

