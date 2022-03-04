from mongoengine import (Document, StringField, EmailField, IntField)

class User(Document):
    firstName = StringField(max_length=40, required=True)
    lastName = StringField(max_length=40, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    userType = IntField(min_value=1, max_value=6)
    gender = StringField(max_length=40, required=True)
    dateOfBirth = StringField(max_length=40, required=True)
    address = StringField(max_length=40, required=True)
    age = IntField(min_value=0, max_value=200)

    def get_fullname(self):
        return self.firstName + ' ' + self.lastName
    
    


