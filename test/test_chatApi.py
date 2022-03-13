import pytest 

BASE_URL = '/api/1/chat'


def test_add_valid_message(app, client):
    """Test adding a valid message"""
    # add a message
    url = f'{BASE_URL}/'
    data = {
        "id": "5431234",
        "fromUser": "12332252",
        "toUser": "123252",
        "content": "testing testing testing"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added message'

def test_add_invalid_message(app, client):
    """Test adding an invalid message"""
    # add an invalid message
    url = f'{BASE_URL}/'
    data = {
        "id": "6432453",
        "fromUser": "does not exist",
        "toUser": "123252",
        "content": "testing testing testing"
    }
    response = client.post(url, json=data)
    assert response.status_code == 400

def test_get_allMessages(app, client):
    """Test getting all messages"""
    # get all messages
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get messages successfully'

def test_add_get_message(app, client):
    url = f'{BASE_URL}/'
    data = {
        "id": "982734",
        "fromUser": "12332252",
        "toUser": "123252",
        "content": "testing testing testing"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added message'

    # get message detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "982734"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get message successfully'
    assert response.json['chat']['id'] == '982734'

def test_delete_message(app, client):
    # add a message
    url = f'{BASE_URL}/'
    data = {
        "id": "1238472",
        "fromUser": "12332252",
        "toUser": "123252",
        "content": "testing testing testing"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added message'

    # delete the message
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "1238472",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Deleted message'

    # get the same message, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "1238472"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to get message'

def test_query_recent_messages(app, client):
    url = f'{BASE_URL}/recent-messages'
    data = {
        "amount": "10",
    }
    response = client.get(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Get messages successfully'
    assert len(response.json['chats']) > 0 and len(response.json['chats']) <= 10

def test_query_received_messages(app, client):
    url = f'{BASE_URL}/user-received-messages'
    data = {
        "userId": "123252",
    }
    response = client.get(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Get user messages successfully'
    assert len(response.json['chats']) > 0
    assert response.json['chats'][0]['toUser'] == "123252"

def test_query_sent_messages(app, client):
    url = f'{BASE_URL}/user-sent-messages'
    data = {
        "userId": "12332252",
    }
    response = client.get(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Get user messages successfully'
    assert len(response.json['chats']) > 0
    assert response.json['chats'][0]['fromUser'] == "12332252"