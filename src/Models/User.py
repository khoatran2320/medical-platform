from mongoengine import (Document, StringField, EmailField, IntField)

class User(Document):
    _id = StringField(required=True, primary_key=True)
    firstName = StringField(max_length=40, required=True)
    lastName = StringField(max_length=40, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    userType = StringField(min_value=1, max_value=6, required=True)
    gender = StringField(max_length=40, required=True)
    dateOfBirth = StringField(max_length=40, required=True)
    address = StringField(max_length=40, required=True)
    age = IntField(min_value=0, max_value=200, required=True)

    """
    set document fields
    """
    def set(self, data):
        self._id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.userType = data['userType']
        self.gender = data['gender']
        self.dateOfBirth = data['dateOfBirth']
        self.address = data['address']
        self.age = data['age']
        

    """
    update document fields
    """
    def update(self, data):
        for key, val in data.items():
            if val is not None and key != 'id':
                self[key] = val

    """
    delete document
    """
    def delete(self):
        self.delete()

    """
    get full name of user
    """
    def get_fullname(self):
        return self.firstName + ' ' + self.lastName

    """
    returns json of fields
    """
    def json(self):
        return {
            'id': self._id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'userType': self.userType,
            'gender': self.gender,
            'dateOfBirth': self.dateOfBirth,
            'address': self.address,
            'age': self.age
        }
    
    


