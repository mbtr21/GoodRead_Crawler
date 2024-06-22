# Goodreads Data Crawler Project

## Overview

The Goodreads Data Crawler is a Django-based project designed to fetch book information from Goodreads based on user-provided book names and categories. It leverages the Django REST Framework for API endpoints and uses Celery with RabbitMQ to handle asynchronous task processing. Retrieved data is stored in a SQLite database for efficient and lightweight data management.

## Features

- **Book and Category Search**: Fetch book data from Goodreads by submitting a book name and category (group or book).
- **Asynchronous Task Processing**: Improve data retrieval efficiency using Celery with RabbitMQ for asynchronous task handling.
- **API Endpoints**: Utilize Django REST Framework to create endpoints for submitting search tasks and retrieving stored book data.
- **SQLite Database**: Store and manage retrieved book information with a simple setup and integration.
- **Admin Interface**: Manage and view tasks and book information directly from the Django admin interface.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Celery
- RabbitMQ

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mbtr21/GoodRead_Crawler.git
   ```
2.**Install Dependencies**
```bash
     pip install -r requirements.txt
```
3.**Setup RabbitMQ**
```bash
Ensure RabbitMQ is installed and running on your system. Follow the official RabbitMQ documentation for installation instructions.
```
4.**Run Migrations**
```bash
python manage.py migrate
```
5.**Start Celery Worker**

Open a new terminal window and run the following command:
```bash
celery -A goodreads_data_crawler worker --loglevel=info
```
6.**Start the Django Project**
```bash
python manage.py runserver
```
### Django Admin Interface ###
Access the Django admin interface at http://localhost:8000/admin to manage tasks and view stored book data. Use the admin credentials created during the setup to log in.
### Contributing ###
Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

