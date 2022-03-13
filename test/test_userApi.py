import pytest 

BASE_URL = '/api/1/user'


def test_add_valid_user(app, client):
    """Test adding a valid user"""
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "123252",
        "address": "123 east meadow lane",
        "age": "22",
        "dateOfBirth": "10/22/2002",
        "email": "jonwick123@gmail.com", 
        "firstName": "Jon",
        "lastName": "Wick", 
        "gender": "male",
        "password":"password", 
        "userType": "DOCTOR"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added user'

def test_add_invalid_user(app, client):
    """Test adding an invalid user"""
    # add an invalid user
    url = f'{BASE_URL}/'
    data = {
        "id": "123252",
        "address": "123 east meadow lane",
        "age": "22",
        "dateOfBirth": "10/22/2002",
        "email": "jonwick123@gmail.com", 
        "firstName": "Jon",
        "lastName": "Wick", 
        "gender": "male",
        "password":"password", 
        "userType": "assassin"
    }
    response = client.post(url, json=data)
    assert response.status_code == 400

def test_get_allUser(app, client):
    """Test getting all users"""
    # get all users
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get users successfully'

def test_add_get_user(app, client):
    url = f'{BASE_URL}/'
    data = {
        "id": "12332252",
        "address": "123 east meadow lane",
        "age": "22",
        "dateOfBirth": "10/22/2002",
        "email": "jonwick123@gmail.com", 
        "firstName": "Jon",
        "lastName": "Wick", 
        "gender": "male",
        "password":"password", 
        "userType": "DOCTOR"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added user'

    # get user detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "12332252"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get user successfully'
    assert response.json['user']['id'] == '12332252'


def test_update_user(app, client):
    # add a user
    url = f'{BASE_URL}/'
    data = {
        "id": "12224552",
        "address": "123 east meadow lane",
        "age": "22",
        "dateOfBirth": "10/22/2002",
        "email": "jonwick123@gmail.com", 
        "firstName": "Jon",
        "lastName": "Wick", 
        "gender": "male",
        "password":"password", 
        "userType": "PATIENT"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added user'

    # update the user
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "12224552", 
        "userType": "FAMILY"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Updated user'
    assert response.json['user']['id'] == '12224552'
    assert response.json['user']['userType'] == 'FAMILY'

def test_invalid_update(app, client):
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "does not exist", 
        "userType": "FAMILY"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to update user'

def test_delete_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "5435432",
        "address": "123 east meadow lane",
        "age": "22",
        "dateOfBirth": "10/22/2002",
        "email": "jonwick123@gmail.com", 
        "firstName": "Jon",
        "lastName": "Wick", 
        "gender": "male",
        "password":"password", 
        "userType": "PATIENT"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added user'

    # delete the device
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "5435432",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Deleted user'

    # get the same device, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "5435432"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to get user'
