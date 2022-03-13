# Medical Platform Project
<!-- PROJECT LOGO -->
## About the Project
<div id="top"></div>
<br />
<div>
<h2>Purpose</h2>
<p>
The purpose of this project is to build a platform that will allow medical professionals to monitor patients at home or at the hospital. Additionally, patients and family members, as well as other relevant parties can interact with the platform. 
<br />
</p>
<h2>Concept</h2>
<p >
The platform allows for multiple user roles such as doctors, patients, nurses, admis, family members, and developers. A user can have multiple roles. The platform interaction with many modules to provide users with an overall smooth experience in terms of health monitoring. These modules include device interaction, calendar scheduling, alerts, chatting, voice transriber, data management, and application interfaces. 
<br />
</p>
</div>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#user-stories">User Stories</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites-installation">Prerequisites Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li>
      <a href="#documentation">Documentation</a>
    </li>
    <li>
      <a href="#tests">Tests</a>
    </li>
  </ol>
</details>
<p align="right">(<a href="#top">back to top</a>)</p>


## User Stories
### Administrator User Stories
1. Add users to the system
2. Assign and change roles to users
    - Patient
    - Nurse
    - Doctor
    - Admin
    - Family member
3. A user can have many different roles, e.g.
    - A user can be a patient and/or a doctor
    - A user can be a family member and/or a patient
4. Provide interfaces to third party medical device makers to have their devices feed data to the system
5. Provide ability to disable or enable any device maker or application developer

### Medical Professional User Stories
1. Browse Patients
2. Assign a medical device to a Patient
3. Assign Alert and scheduling for medical measurement, e.g., Patient to measure blood pressure daily. MP will receive an alert if it not done. Temperature is higher or lower than a value. MP will get an alert if the measurement is outside acceptable range.
4. MP can input data for any patient
5. MP can chat with patients using text, voice or videos.
6. MP can read transcripts of Patient uploaded videos and messages
7. MP can search for keywords in messages and chats
8. MP have a calendar where they can show open time slots for appointments
9. MP can see all appointments booked at any time


### Patient Use Cases
1. Patient can enter measurement at any time
2. Patient can write a text or upload video or voice message to the MP
3. Patient can book an appointment with the MP
4. Patient can view their medical measurements

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Branch Strategy -->
## Branch Strategy
Branch from `main` when developing a new feature/module. For example, if developing a `chat` module, then the newly created branch should be named as `chat/<feature>` branch. The feature branch will be merged to main/master branch upon completion of development, implementation, and unit test.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This repository uses python3.8.9

It is recommended that you install requirements and run everything in a virtual environment to avoid conflicts between different projects. Start a new virtual environment by running:

```
python -m virtualenv venv
```

To activate the virtual environment:

```
source venv/bin/activate (macOS/*nix)
venv/bin/activate.cmd (Windows)
```

To allow run script execution:
```
chmod +x run.sh
```
### Prerequisites Installation
To install the requirements of this repository:

```
pip install -r requirements.txt
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
### Usage  
1. Run Flask App
```
./run.sh
```
OR

2. Run Flask App via Docker Container (docker installed)
  ```
  docker-compose up --build
  ```
Flask app runs on http://localhost:5000/
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DOCUMENTATION  -->
## Documentation  

API documentation can be found at the url http://localhost:5000/api/1/doc/ once the app has started.
<p align="right">(<a href="#top">back to top</a>)</p>

## Tests  
This module uses pytest to perform unit tests. The tests currently has a 93% coverage. 

To install pytest:

```
pip install pytest
```

To run pytest:
```
pytest
```
<p align="right">(<a href="#top">back to top</a>)</p>