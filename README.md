# Django User Registration API

## Setting Up Django

1. Clone this repository to your local machine:

   git clone https://github.com/paras1244/Test-signup-fan-talent.git


# Navigate to the project directory:
cd django-user-registration-api

# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install project dependencies:
pip install -r requirements.txt

# Apply database migrations:
python manage.py migrate


# Create a superuser for admin access (optional):
python manage.py createsuperuser

# Start the development server:
python manage.py runserver

# Endpoints
Method: POST
http://127.0.0.1:8000/api/sign-up/fan/
http://127.0.0.1:8000/api/sign-up/talent/

# Postman Collection Link
https://documenter.getpostman.com/view/28334318/2s9YC8wBUj

- Required Fields:
    first_name: First name of the user
    last_name: Last name of the user
    username: Username for the user
    email: Email address of the user
    password: Password for the user
    user_type: Set to "Talent"

