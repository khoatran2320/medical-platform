from datetime import datetime
from secrets import choice
from flask_restx import reqparse, inputs


def date_type(date):
    """Parse date type"""
    try:
        date_time = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        raise ValueError('This is not date type')
    return date

# Swagger documentation
date_type.__schema__ = {'type': 'string', 'format': 'mm/dd/yyyy'}

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")
_user_parser.add_argument('firstName',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_user_parser.add_argument('lastName',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_user_parser.add_argument('email',
                             type=inputs.email(check=True),
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_user_parser.add_argument('password',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_user_parser.add_argument('userType',
                             type=str,
                             required=True,
                             choices=("PATIENT", "FAMILY", "NURSE", "ADMIN", "DEVELOPER", "DOCTOR"),
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_user_parser.add_argument('gender',
                             type=str,
                             required=True,
                             choices=("male", "female", "none_binary"),
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_user_parser.add_argument('dateOfBirth',
                             type=date_type,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_user_parser.add_argument('address',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )     
_user_parser.add_argument('age',
                             type=int,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )   

_user_id_parser = reqparse.RequestParser()
_user_id_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")