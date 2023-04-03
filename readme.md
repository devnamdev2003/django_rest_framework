# Django REST API for CRUD Operations
This is a Django REST API for performing CRUD (Create, Read, Delete) operations on data. The API allows users to interact with the database through HTTP requests and responses. The target users for this project are developers who need to build web applications that require a backend API.

## Features
- Create: Users can create new records in the database by sending a POST request to the API endpoint.
- Read: Users can retrieve records from the database by sending a GET request to the API endpoint.
- Delete: Users can delete records from the database by sending a DELETE request to the API endpoint.

## Technology stack
- Django REST Framework 
- Python

## Getting started

### Prerequisites
Before running this project, you will need to have the following installed on your machine:

- Python 3.10.5
- Django 4.1.7
- Django REST Framework 3.14.0

### Installation and setup

- Clone this repository to your local machine using `git clone https://github.com/devnamdev2003/Rgpv_result_checker_application.git`.
- Install the required packages by running `pip install -r requirements.txt`.
- Create a new database by running `python manage.py migrate`.
Run the server by running `python manage.py runserver`.
Usage
- To create a new record, send a POST request to `/api/insert/` with the record data in the request body.
- To retrieve a record, send a GET request to `/api/{id}/`, where `{id}` is the ID of the record you want to retrieve.
- To delete a record, send a DELETE request to `/api/remove/{id}/`.

## Contributing
If you find any issues or bugs in this project, please feel free to submit an issue or pull request. Contributions are welcome and appreciated!

## License
This project is licensed under the [**__MIT License__**](https://github.com/devnamdev2003/django_rest_framework/blob/main/LICENSE)