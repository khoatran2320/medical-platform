from os import stat
from flask import jsonify
from flask_restx import Resource, Namespace
from Response import Response

# Import models
from Models.Device import Device as DeviceModel

# Import parsers
from parsers.device import _device_parser, _device_id_parser

device_ns = Namespace('device', 'Device methods')


@device_ns.route('/')
class Devices(Resource):
    """
    Shows a list of devices, and lets you POST to add new device
    """
    @device_ns.doc(
        responses={
            200: "Added device",
            400: "Unable to add device",
        },
        parser=_device_parser
    )
    def post(self):
        """Add new device"""
        data = _device_parser.parse_args()

        # create new device
        new_device = DeviceModel()
        new_device.set(data)

        try:
            new_device.save()
            return Response("Added device", status=200)
        except:
            return Response("Unable to add device", status=400)

    @device_ns.doc(
        response={
            200: "Get devices successfully",
            400: "Unable to get devices",
        }
    )
    def get(self):
        """Get all devices"""
        try:
            data = DeviceModel.objects.all()
            # serialize
            devices = [device.json() for device in data]
            return Response({"message": "Get device successfully", "devices": devices}, status=200)
        except:
            return Response("Unable to get devices",status=200)


@device_ns.route('/detail')
class Device(Resource):
    """
    Shows detail about a device, and lets you DELETE, PUT a device
    """
    @device_ns.doc(
        parser=_device_id_parser,
        responses={
            200: "Get device successfully",
            400: "Unable to get device",
        }
    )
    def get(self):
        """Get detail about a device"""
        data = _device_id_parser.parse_args()
        try:
            device = DeviceModel.objects(_id=data['id']).first()
            return Response({"message": "Get device successfully", "device": device.json()}, status=200)
        except:
            return Response("Unable to get device", status=400)

    @device_ns.doc(
        parser=_device_id_parser,
        responses={
            200: "Updated device",
            400: "Unable to update device",
        }
    )
    def put(self):
        """Updates a device"""
        data = _device_id_parser.parse_args()
        try:
            device = DeviceModel.objects(_id=data['id']).first()
            device.update(data)
            device.save()
            return Response({"message": "Updated device", "device": device.json()}, status=200)

        except Exception as e:
            print(e)
            return Response("Unable to update device", status=400)

    @device_ns.doc(
        parser=_device_id_parser,
        responses={
            200: "Deleted device",
            400: "Unable to delete device",
        }
    )
    def delete(self):
        """Deletes a device"""
        data = _device_id_parser.parse_args()
        try:
            device = DeviceModel.objects(_id=data['id']).first()
            device._delete()
            return Response("Deleted device", status=200)

        except:
            return Response("Unable to delete device", status=200)