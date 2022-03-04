# Medical Platform Project

## Purpose

The purpose of this project is to build a platform that will allow medical professionals to monitor patients at home or at the hospital. Additionally, patients and family members, as well as other relevant parties can interact with the platform. 

## Concept

The platform allows for multiple user roles such as doctors, patients, nurses, admis, family members, and developers. A user can have multiple roles. The platform interaction with many modules to provide users with an overall smooth experience in terms of health monitoring. These modules include device interaction, calendar scheduling, alerts, chatting, voice transriber, data management, and application interfaces. 

## Patient use cases
1. Patient can enter measurement at any time
2. Patient can write a text or upload video or voice message to the MP
3. Patient can book an appointment with the MP
4. Patient can view their medical measurements

## API
- `/add-device` [`POST`]: This route expects device details to save to database. In the body, there should be these keys:
    - `deviceType: Integer` -- the device type
        - 1: thermometer
        - 2: scale
        - 3: pulse
        - 4: oximeter
        - 5: glucometer
        - 6: blood pressure
    - `datePurchased: String` -- the date of purchase for device. The format is `mm/dd/yyyy`
    - `assignedUser: String` -- the name of the user to which the deviced is assigned
    - `assigner: String` -- the name of the user that assigned the device
    - `firmwareVersion: Float` -- the firmware version of the device
    - `serialNumber: Integer` -- the serial number of the device

- `/add-user` [`POST`]: This route expects user details to save to database. In the boody, there should be these keys:
    - `firstName: String` -- first name
    - `lastName: String` -- last name
    - `email: String` -- email
    - `password: String` -- password
    - `userType: Integer` -- the account user type 
        - 1: doctor
        - 2: patient
        - 3: family
        - 4: nurse
        - 5: admin
        - 6: developer
    - `gender: String` -- gender
        - `male`
        - `female`
        - `nonBinary`
    - `dateOfBirth: String` -- date of birth. The date format is `mm/dd/yyyy` 
    - `address: String` -- user address
    - `age: Integer` -- user age 
