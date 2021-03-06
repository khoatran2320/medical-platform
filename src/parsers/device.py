from datetime import datetime
from flask_restx import reqparse


def date_type(date):
    """Parse date type"""
    try:
        date_time = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        raise ValueError('This is not date type')
    return date

# Swagger documentation
date_type.__schema__ = {'type': 'string', 'format': 'mm/dd/yyyy'}
_device_parser = reqparse.RequestParser()
_device_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")
_device_parser.add_argument('deviceType',
                             type=str,
                             choices=('THERMOMETER', 'SCALE', 'PULSE',
                                      'OXIMETER', 'GLUCOMETER', 'BLOOD_PRESSURE'),
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_device_parser.add_argument('datePurchased',
                             type=date_type,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_device_parser.add_argument('assignedUser',
                             type=str,
                             required=False,
                             location=('args','json'))
_device_parser.add_argument('assigner',
                             type=str,
                             required=False,
                             location=('args','json'))
_device_parser.add_argument('firmwareVersion',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_device_parser.add_argument('serialNumber',
                             type=int,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )


_device_put_parser = reqparse.RequestParser()
_device_put_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")
_device_put_parser.add_argument('deviceType',
                             type=str,
                             choices=('THERMOMETER', 'SCALE', 'PULSE',
                                      'OXIMETER', 'GLUCOMETER', 'BLOOD_PRESSURE'),
                             required=False,
                             location=('args','json'))
_device_put_parser.add_argument('datePurchased',
                             type=date_type,
                             required=False,
                             location=('args','json'))
_device_put_parser.add_argument('assignedUser',
                             type=str,
                             required=False,
                             location=('args','json'))
_device_put_parser.add_argument('assigner',
                             type=str,
                             required=False,
                             location=('args','json'))
_device_put_parser.add_argument('firmwareVersion',
                             type=str,
                             required=False,
                             location=('args','json')
                             )
_device_put_parser.add_argument('serialNumber',
                             type=int,
                             required=False,
                             location=('args','json')
                             )

_device_id_parser = reqparse.RequestParser()
_device_id_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")