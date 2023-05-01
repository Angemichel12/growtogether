# Growtogether API Project

This is a Growtogether API Project based on Django REST Framework. This API features five types of users - Doctor, woman and Admin, Receptionist and Consultator.
For authenticating user, Django REST Framework custom token authentication is used. Installation guide, API endpoints and sample request/response are given below.

## Please follow the below steps to install this application-

1. Install python 3.8 above and virtualenv.
2. Clone this repository- https://github.com/Angemichel12/growtogether.git
3. Then go to the growtogether directory: cd backend
4. Create virtualenv: virtualenv venv(on window), python3.9 -m venv venv(on mac) (This will create a virtual environment and install all depedencies).
5. Activate the virtual environment: venv/Scripts/actavate(on window), source venv/bin/activate(on mack)
6. Run the app: python manage.py runserver
7. Then create a superuser: python manage.py createsuperuser
8. Then go to Django admin- http://localhost:8000/admin/ and create some patients,doctors, admins and appointments to test the API.

## Endpoints

### 1. Doctor:

- api/doctor/registration/

## Sample API Request and Response

**POST api/doctor/registration/**

Details: API endpoint for creating new doctor account.

request body:

```json
{
  "user_data": {
    "username": "doctor5",
    "email": "doctor@gmail.com",
    "first_name": "Dr. Deal",
    "last_name": "Walker",
    "password": "doctoraccess1234",
    "password2": "doctoraccess1234",
    "phone": "12312343424"
  },
  "profile_data": {
    "department": "OB"
  }
}
```

response body:

```json
{
  "user_data": {
    "username": "doctor5",
    "email": "doctor@gmail.com",
    "first_name": "Dr. Deal",
    "last_name": "Walker",
    "phone": "12312343424"
  },
  "profile_data": {
    "department": "OB"
  }
}
```

**POST api/doctor/login/**

Details: API endpoint for doctor login. Admin needs to approve account otherwise login will not be successful.

request body:

```json
{
  "username": "doctor5",
  "password": "doctoraccess1234"
}
```

response body:

```json
{
  "Message": "You are login successful",
  "token": "c8dabcf01492f84f4db5cafc9003388cdc486cb8"
}
```

# How to run celery worker

celery -A growtogether.celery worker --pool=solo -l info

# how to run celery beat

celery -A growtogether.celery beat -l info
