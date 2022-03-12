from datetime import datetime
from flask_restx import reqparse


def date_type(date):
    """Parse date type"""
    try:
        date_time = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        raise ValueError('This is not date type')
    return parse(date)

# Swagger documentation
date_type.__schema__ = {'type': 'string', 'format': 'mm/dd/yyyy'}
_device_parser = reqparse.RequestParser()
_device_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=['args', 'json'],
                            help="This field cannot be blank.")
_device_parser.add_argument('deviceType',
                             type=str,
                             choices=('temp', 'blood_pressure', 'glucometer',
                                      'pulse', 'weight', 'blood_saturation'),
                             required=True,
                             location=['args', 'json'],
                             help="This field cannot be blank.")
_device_parser.add_argument('datePurchased',
                             type=date_type,
                             required=True,
                             location=['args', 'json'],
                             help="This field cannot be blank.")
_device_parser.add_argument('assignedUser',
                             type=str,
                             required=False,
                             location=['args', 'json'])
_device_parser.add_argument('assigner',
                             type=str,
                             required=False,
                             location=['args', 'json'])
_device_parser.add_argument('firmwareVersion',
                             type=str,
                             required=True,
                             location=['args', 'json'],
                             help="This field cannot be blank."
                             )
_device_parser.add_argument('serialNumber',
                             type=str,
                             required=True,
                             location=['args', 'json'],
                             help="This field cannot be blank."
                             )


_device_id_parser = reqparse.RequestParser()
_device_id_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=['args', 'json'],
                            help="This field cannot be blank.")