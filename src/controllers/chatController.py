from flask_restx import Resource, Namespace
from Response import Response


# Import models
from Models.Chat import Chat as ChatModel

# Import parsers
from parsers.chat import _chat_parser, _chat_id_parser

chat_ns = Namespace('chat', 'Chat methods')

@chat_ns.route('/')
class Messages(Resource):
    """
    Shows a list of messages, and lets you POST to add new message
    """
    @chat_ns.doc(
        responses={
            200: "Added message",
            400: "Unable to add message",
        },
        parser=_chat_parser
    )
    def post(self):
        """Add new message"""
        data = _chat_parser.parse_args()

        # create new message
        new_message = ChatModel()
        new_message.set(data)

        try:
            new_message.save()
            return Response("Added message", status=200)
        except:
            return Response("Unable to add message", status=400)

    @chat_ns.doc(
        response={
            200: "Get messages successfully",
            400: "Unable to get messages",
        }
    )
    def get(self):
        """Get all messages"""
        try:
            data = ChatModel.objects.all()
            # serialize
            messages = [message.json() for message in data]
            return Response({"message": "Get message successfully", "chats": messages}, status=200)
        except Exception as e:
            print(e)
            return Response("Unable to get messages",status=400)


@chat_ns.route('/detail')
class Message(Resource):
    """
    Shows detail about a message, and lets you DELETE, PUT a message
    """
    @chat_ns.doc(
        parser=_chat_id_parser,
        responses={
            200: "Get message successfully",
            400: "Unable to get message",
        }
    )
    def get(self):
        """Get detail about a message"""
        data = _chat_id_parser.parse_args()
        try:
            message = ChatModel.objects(_id=data['id']).first()
            return Response({"message": "Get message successfully", "chat": message.json()}, status=200)
        except:
            return Response("Unable to get message", status=400)

    @chat_ns.doc(
        parser=_chat_id_parser,
        responses={
            200: "Updated message",
            400: "Unable to update message",
        }
    )
    def put(self):
        """Updates a message"""
        data = _chat_id_parser.parse_args()
        try:
            message = ChatModel.objects(_id=data['id']).first()
            message.update(data)
            message.save()
            return Response({"message": "Updated message", "message": message.json()}, status=200)

        except Exception as e:
            print(e)
            return Response("Unable to update message", status=400)

    @chat_ns.doc(
        parser=_chat_id_parser,
        responses={
            200: "Deleted message",
            400: "Unable to delete message",
        }
    )
    def delete(self):
        """Deletes a chat"""
        data = _chat_id_parser.parse_args()
        try:
            message = ChatModel.objects(_id=data['id']).first()
            message._delete()
            return Response("Deleted message", status=200)

        except:
            return Response("Unable to delete message", status=400)