from mongoengine import (Document, StringField, EmailField, IntField)

class User(Document):
    _id = StringField(required=True, primary_key=True)
    firstName = StringField(max_length=40, required=True)
    lastName = StringField(max_length=40, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    userType = IntField(min_value=1, max_value=6, required=True)
    gender = StringField(max_length=40, required=True)
    dateOfBirth = StringField(max_length=40, required=True)
    address = StringField(max_length=40, required=True)
    age = IntField(min_value=0, max_value=200, required=True)

    def get_fullname(self):
        return self.firstName + ' ' + self.lastName

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
    
    


