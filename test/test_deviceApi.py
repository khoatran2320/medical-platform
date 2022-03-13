import pytest 

BASE_URL = '/api/1/device'


def test_add_valid_device(app, client):
    """Test adding a valid device"""
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "123252",
        "deviceType": "THERMOMETER",
        "datePurchased": "03/10/2022",
        "firmwareVersion": "123.123",
        "serialNumber": "3243643"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added device'

def test_add_invalid_device(app, client):
    """Test adding a invalid device"""
    # add an invalid device
    url = f'{BASE_URL}/'
    data = {
        "id": "123252",
        "deviceType": "sd",
        "datePurchased": "03/10/2022",
        "firmwareVersion": "123.123"
    }
    response = client.post(url, json=data)
    assert response.status_code == 400

def test_get_alldevice(app, client):
    """Test getting all devices"""
    # get all devices
    url = f'{BASE_URL}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['message'] == 'Get devices successfully'

def test_add_get_device(app, client):
    url = f'{BASE_URL}/'
    data = {
        "id": "12325432",
        "deviceType": "THERMOMETER",
        "datePurchased": "03/10/2022",
        "firmwareVersion": "1.123",
        "serialNumber": "323643"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added device'

    # get device detail
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "12325432"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Get device successfully'
    assert response.json['device']['id'] == '12325432'


def test_update_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "4325323",
        "deviceType": "SCALE",
        "datePurchased": "03/02/2002",
        "firmwareVersion": "23.43",
        "serialNumber": "52345234"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added device'

    # update the device
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "4325323", 
        "deviceType": "OXIMETER"
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Updated device'
    assert response.json['device']['id'] == '4325323'
    assert response.json['device']['deviceType'] == 'OXIMETER'

def test_invalid_update(app, client):
    url = f'{BASE_URL}/detail'
    response = client.put(url, query_string={
        "id": "does not exist", 
        "deviceType": "OXIMETER"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to update device'

def test_delete_device(app, client):
    # add a device
    url = f'{BASE_URL}/'
    data = {
        "id": "5433",
        "deviceType": "SCALE",
        "datePurchased": "03/10/2012",
        "firmwareVersion": "12324",
        "serialNumber": "63452"
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Added device'

    # delete the device
    url = f'{BASE_URL}/detail'
    response = client.delete(url, query_string={
        "id": "5433",
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Deleted device'

    # get the same device, should be 400 status code
    url = f'{BASE_URL}/detail'
    response = client.get(url, query_string={
        "id": "5433"
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Unable to get device'
