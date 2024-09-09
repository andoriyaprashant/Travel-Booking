# Travel Booking App

This is a Django-based Travel Booking application that allows users to register, log in, and book travel options. Users can view their bookings, cancel bookings, and manage their profiles.

## Features

- User registration and login
- Travel booking functionality
- View, cancel, and manage bookings
- Responsive UI with a modern look
- MySQL database integration


## Installation

To set up and run this project on your local machine, follow the instructions below:

### 1. Clone the Repository

```bash
git clone https://github.com/username/Travel-Booking.git
cd Travel-Booking
```
### Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Install Required Dependencies

```bash
pip install -r requirements.txt
```


### Set Up MySQL Database

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'INTERN',
        'USER': 'root',
        'PASSWORD': 'prashant',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
***You can create the database using MySQL:***

```bash
mysql -u root -p
CREATE DATABASE INTERN;
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the Application

```bash
python manage.py runserver
```
