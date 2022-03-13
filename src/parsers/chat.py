from datetime import datetime
from operator import truediv
from flask_restx import reqparse, inputs



_chat_parser = reqparse.RequestParser()
_chat_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank."
                            )
_chat_parser.add_argument('fromUser',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_chat_parser.add_argument('toUser',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_chat_parser.add_argument('content',
                             type=str,
                             required=True,
                             location=('args','json'),
                             help="This field cannot be blank."
                             )
_chat_parser.add_argument('attachment',
                             type=inputs.URL(check=True),
                             required=False,
                             location=('args','json')
                             )

_chat_id_parser = reqparse.RequestParser()
_chat_id_parser.add_argument('id',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")

_chat_user_parser = reqparse.RequestParser()
_chat_user_parser.add_argument('userId',
                            type=str,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")

_chat_number_parser = reqparse.RequestParser()
_chat_number_parser.add_argument('amount',
                            type=int,
                            required=True,
                            location=('args','json'),
                            help="This field cannot be blank.")