# IoT_Ass3

## Directory Structure

The Light Control IoT Project is structured in the following manner:

    ├── 
    ├── lightController                     # Django Project Root
    │   ├── api                             # API interface, handles all data related functions of project
    │   |    ├── management/commands               # Used for initializing data in models
    |   |    ├── migrations                        # Migrations created for database creation
    │   |    ├── __init__.py                       # Used for Construction of object
    │   |    ├── apps.py                           # Definition of app for Django Project
    │   |    ├── models.py                         # Definition of data tables used in application
    │   |    ├── serializers.py                    # Provide definition for serialization
    │   |    ├── urls.py                           # Map API models to URLS, uses routers
    │   |    ├── views.py                          # Creates viewset API interfaces for models, utilizes serializers
    │   ├── dashboard                       # Dashboard, provides front end GUI and mapping of requests through API
    │   |    ├── migrations                        # Migrations created for database creation
    |   |    ├── templates                         # Stores the HTML template for web UI                         
    │   |    ├── __init__.py                       # Used for Construction of object
    │   |    ├── apps.py                           # Definition of app for Django Project
    │   |    ├── gpio.py                           # Controls GPIO functions of project
    │   |    ├── models.py                         # Stores models for application | not used
    │   |    ├── urls.py                           # Maps light control to front facing URL
    │   |    ├── views.py                          # Handles request logic and displaying of template

    │   ├── dashboard                       # End-to-end, integration tests (alternatively `e2e`)
    │   └── lightController                 # Django Project Settings
    └── ...



## How to run

### Build Circuit

In order to run the light controller application, the circuit must be built as shown in below image:

![image](https://github.com/Abbas-Rizvi/IoT_Ass3/assets/73917749/8f82a08a-b729-4ddd-add0-f00f0c107b92)



### Install dependencies 

Install python dependencies for project. (Suggest running in virtual environment).

`pip install -r requirements.txt`

### Create Databases

From Django Project directory, run the following commands to create the tables required
```
python manage.py makemigrations
python manage.py migrate
```

Once tables have been created instantiate data for initial mode and state. 

*Note these values can be changed via UI within application

```
python manage.py initalize_data
```

### Run Server

Prior to running server, update the IP address of device in dashboard/views.py with IP address of local device.
This allows accessibility from all devices on network.

To run Django server on port 8000, execute command:

```
python manage.py runserver 0.0.0.0:8000
```


## Demo

