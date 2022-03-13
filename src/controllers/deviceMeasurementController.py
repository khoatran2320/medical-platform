from flask import Blueprint
from flask_restx import Resource, Namespace
from ..Response import Response

# Import models
from ..Models.Device import Device as DeviceModel
from ..Models.DeviceMeasurement import DeviceMeasurement as DeviceMeasurementModel
from ..Models.User import User as UserModel


# Import parsers
from ..parsers.device_measurement import _measurement_parser, _measurement_id_parser, _measurement_userId_parser

device_measurement_ns = Namespace('device-measurements', 'Device measurement methods')
# api.add_namespace(device_measurement_ns)

@device_measurement_ns.route('/')
class Measurements(Resource):
    """
    Shows a list of measurements, and lets you POST to add new measurement
    """
    @device_measurement_ns.doc(
        responses={
            200: "Added measurement",
            400: "Unable to add measurement",
        },
        parser=_measurement_parser
    )
    def post(self):
        """Add new measurement"""
        data = _measurement_parser.parse_args()

        # create new measurement
        new_measurement = DeviceMeasurementModel()
        new_measurement.set(data)

        try:
            device = DeviceModel.objects(_id=data['deviceId']).first()
            if not device:
                raise ValueError

            user = UserModel.objects(_id=data['userId']).first()
            if not user:
                raise ValueError

            new_measurement.save()
            return Response("Added measurement", status=200)
        except Exception as e:
            print(e)
            return Response("Unable to add measurement", status=400)

    @device_measurement_ns.doc(
        responses={
            200: "Get measurements successfully",
            400: "Unable to get measurements",
        }
    )
    def get(self):
        """Get all measurements"""
        try:
            data = DeviceMeasurementModel.objects.all()
            # serialize
            measurements = [measurement.json() for measurement in data]
            return Response({"message": "Get measurement successfully", "measurements": measurements}, status=200)
        except Exception as e:
            print(e)
            return Response("Unable to get measurements",status=400)


@device_measurement_ns.route('/detail')
class Measurement(Resource):
    """
    Shows detail about a measurement, and lets you DELETE, PUT a measurement
    """
    @device_measurement_ns.doc(
        parser=_measurement_id_parser,
        responses={
            200: "Get measurement successfully",
            400: "Unable to get measurement",
        }
    )
    def get(self):
        """Get detail about a measurement"""
        data = _measurement_id_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(_id=data['id']).first()
            return Response({"message": "Get measurement successfully", "measurement": measurement.json()}, status=200)
        except:
            return Response("Unable to get measurement", status=400)

    @device_measurement_ns.doc(
        parser=_measurement_id_parser,
        responses={
            200: "Updated measurement",
            400: "Unable to update measurement",
        }
    )
    def put(self):
        """Updates a measurement"""
        data = _measurement_id_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(_id=data['id']).first()
            measurement.update(data)
            measurement.save()
            return Response({"message": "Updated measurement", "measurement": measurement.json()}, status=200)

        except Exception as e:
            print(e)
            return Response("Unable to update measurement", status=400)

    @device_measurement_ns.doc(
        parser=_measurement_id_parser,
        responses={
            200: "Deleted measurement",
            400: "Unable to delete measurement",
        }
    )
    def delete(self):
        """Deletes a measurement"""
        data = _measurement_id_parser.parse_args()
        try:
            measurement = DeviceMeasurementModel.objects(_id=data['id']).first()
            measurement.delete()
            return Response("Deleted measurement", status=200)

        except:
            return Response("Unable to delete measurement", status=400)


@device_measurement_ns.route('/user')
class UserMeasurements(Resource):
    """
    Shows detail about a measurement, and lets you DELETE, PUT a measurement
    """
    @device_measurement_ns.doc(
        parser=_measurement_userId_parser,
        responses={
            200: "Get user measurements successfully",
            400: "Unable to get user measurements",
        }
    )
    def get(self):
        """Get user measurements"""
        data = _measurement_userId_parser.parse_args()
        try:
            data = DeviceMeasurementModel.objects(userId=data['userId']).all()
            measurements = [measurement.json() for measurement in data]
            return Response({"message": "Get user measurements successfully", "measurements": measurements}, status=200)
        except Exception as e:
            print(e)
            return Response("Unable to get user measurements", status=400)

    