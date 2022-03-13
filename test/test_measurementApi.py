import pytest 

BASE_URL = '/api/1/device-measurements'


def test_add_valid_measurement(app, client):
    """Test adding a valid measurement"""
    # add a measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "7563452",
        "deviceType": "THERMOMETER",
        "deviceId": "4325323",
        "reading": "98",
        "unit": "fahrenheit", 
        "userId": "9011232374"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added measurement'

def test_add_invalid_measurement(app, client):
    """Test adding an invalid measurement"""
    # add an invalid measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "7563452",
        "deviceType": "THERMOMETER",
        "deviceId": "does not exist",
        "reading": "98",
        "unit": "fahrenheit", 
        "userId": "9011232374"
    }
    response = client.post(url, json=data)
    assert response.status_code == 400

def test_get_allMeasurements(app, client):
    """Test getting all measurements"""
    # get all measurements
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get measurements successfully'

def test_add_get_measurement(app, client):
    url = f'{BASE_URL}/'
    data = {
        "id": "3425342",
        "deviceType": "SCALE",
        "deviceId": "4325323",
        "reading": "98",
        "unit": "kilogram", 
        "userId": "9011232374"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added measurement'

    # get measurement detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "3425342"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get measurement successfully'
    assert response.json['measurement']['id'] == '3425342'


def test_update_measurement(app, client):
    # add a measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "53422",
        "deviceType": "OXIMETER",
        "deviceId": "4325323",
        "reading": "98",
        "unit": "percent", 
        "userId": "9011232374"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added measurement'

    # update the measurement
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "53422", 
        "reading": "98"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Updated measurement'
    assert response.json['measurement']['id'] == '53422'
    assert response.json['measurement']['reading'] == '98'

def test_invalid_update(app, client):
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "does not exist", 
        "reading": "92"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to update measurement'

def test_delete_device(app, client):
    # add a measurement
    url = f'{BASE_URL}/'
    data = {
        "id": "6342287",
        "deviceType": "SCALE",
        "deviceId": "4325323",
        "reading": "98",
        "unit": "pound", 
        "userId": "9011232374"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added measurement'

    # delete the measurement
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "6342287",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Deleted measurement'

    # get the same measurement, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "6342287"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to get measurement'

def test_query_user_measurements(app, client):
    url = f'{BASE_URL}/user'
    data = {
        "userId": "9011232374"
    }
    response = client.get(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Get user measurements successfully'
    
