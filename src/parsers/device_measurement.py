from datetime import datetime
from flask_restx import reqparse


_measurement_parser = reqparse.RequestParser()
_measurement_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")
_measurement_parser.add_argument('deviceType',
                             type=str,
                             choices=('THERMOMETER', 'SCALE', 'PULSE',
                                      'OXIMETER', 'GLUCOMETER', 'BLOOD_PRESSURE'),
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_measurement_parser.add_argument('deviceId',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_measurement_parser.add_argument('reading',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_measurement_parser.add_argument('unit',
                             type=str, 
                             choices=('celsius', 'fahrenheit', 'pound', 'kilogram', 'bpm', 'percent',
                                      'mg/dl', 'mmhg'),
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")
_measurement_parser.add_argument('userId',
                             type=str, 
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank.")


_measurement_put_parser = reqparse.RequestParser()
_measurement_put_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")
_measurement_put_parser.add_argument('deviceType',
                             type=str,
                             choices=('THERMOMETER', 'SCALE', 'PULSE',
                                      'OXIMETER', 'GLUCOMETER', 'BLOOD_PRESSURE'),
                             required=False,
                             location=('args','json'))
_measurement_put_parser.add_argument('deviceId',
                             type=str,
                             required=False,
                             location=('args','json'))
_measurement_put_parser.add_argument('reading',
                             type=str,
                             required=False,
                             location=('args','json'))
_measurement_put_parser.add_argument('unit',
                             type=str, 
                             choices=('celsius', 'fahrenheit', 'pound', 'kilogram', 'bpm', 'percent',
                                      'mg/dl', 'mmhg'),
                             required=False,
                             location=('args','json'))
_measurement_put_parser.add_argument('userId',
                             type=str, 
                             required=False,
                             location=('args','json'))

_measurement_id_parser = reqparse.RequestParser()
_measurement_id_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")

_measurement_userId_parser = reqparse.RequestParser()
_measurement_userId_parser.add_argument('userId',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")