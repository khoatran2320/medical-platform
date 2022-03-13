from os import stat
from flask import Blueprint
from flask_restx import Resource, Namespace, Api
from ..Response import Response
from ..utils.utils import encrypt_pass

# blueprint = Blueprint('api', __name__)
# api = Api(blueprint, doc='/doc/')

# Import models
from ..Models.User import User as UserModel

# Import parsers
from ..parsers.user import _user_parser, _user_id_parser

user_ns = Namespace('user', 'User methods')
# api.add_namespace(user_ns)

@user_ns.route('/')
class Users(Resource):
    """
    Shows a list of users, and lets you POST to add new user
    """
    @user_ns.doc(
        responses={
            200: "Added user",
            400: "Unable to add user",
        },
        parser=_user_parser
    )
    def post(self):
        """Add new user"""
        data = _user_parser.parse_args()
        data["password"] = encrypt_pass(data["password"])
        # create new user
        new_user = UserModel()
        new_user.set(data)
        try:
            new_user.save()
            return Response("Added user", status=200)
        except:
            return Response("Unable to add user", status=400)

    @user_ns.doc(
        responses={
            200: "Get users successfully",
            400: "Unable to get users",
        }
    )
    def get(self):
        """Get all users"""
        try:
            data = UserModel.objects.all()
            # serialize
            users = [user.json() for user in data]
            return Response({"message": "Get users successfully", "users": users}, status=200)
        except:
            return Response("Unable to get users", status=400)


@user_ns.route('/detail')
class User(Resource):
    """
    Shows detail about a user, and lets you DELETE, PUT a user
    """
    @user_ns.doc(
        parser=_user_id_parser,
        responses={
            200: "Get user successfully",
            400: "Unable to get user",
        }
    )
    def get(self):
        """Get detail about a user"""
        data = _user_id_parser.parse_args()
        try:
            user = UserModel.objects(_id=data['id']).first()
            return Response({"message": "Get user successfully", "user": user.json()}, status=200)
        except:
            return Response("Unable to get user", status=400)

    @user_ns.doc(
        parser=_user_id_parser,
        responses={
            200: "Updated user",
            400: "Unable to update user",
        }
    )
    def put(self):
        """Updates a user"""
        data = _user_id_parser.parse_args()
        try:
            user = UserModel.objects(_id=data['id']).first()
            user.update(data)
            user.save()
            return Response({"message": "Updated user", "user": user.json()}, status=200)

        except Exception as e:
            print(e)
            return Response("Unable to update user", status=400)

    @user_ns.doc(
        parser=_user_id_parser,
        responses={
            200: "Deleted user",
            400: "Unable to delete user",
        }
    )
    def delete(self):
        """Deletes a user"""
        data = _user_id_parser.parse_args()
        try:
            user = UserModel.objects(_id=data['id']).first()
            user.delete()
            return Response("Deleted user", status=200)

        except:
            return Response("Unable to delete user", status=400)