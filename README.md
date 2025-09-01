# Blog API

A RESTful Blog API built with Django & Django REST Framework (DRF), featuring user signup, account management, and secure login with JWT authentication, as well as managing blog posts, categories, and comments with role-based permissions, filtering support, pagination and enforced auto image deletion for optimized storage.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** MySQL
- **Auth:** JWT Authentication (SimpleJWT)
- **Other:** Django-Filter, Pagination, Swagger (drf-spectacular)

## Modules

- Users
- Categories
- Posts 
- Comments

## ER Diagram

![img](https://github.com/raghav-patidar1/django-blog-api/blob/main/assets/blog-ER-diagram.png)

## Users Module
- New user can signup
- User can retrieve, update and delete his account
- Existing user can login with JWT tokens
- Admin can list all users
  
![img](https://github.com/raghav-patidar1/django-blog-api/blob/main/assets/users-module.PNG)

## Categories Module
- Admin can create, update and delete category
- User can retrieve a specific category or list of categories
- User can fetch all posts under a specific category
  
![img](https://github.com/raghav-patidar1/django-blog-api/blob/main/assets/categories-module.PNG)

## Posts Module
- User can fetch all posts
- User can fetch all his posts by user id
- User can create new posts
- User can retreive specific posts by id
- User can update and delete his posts (Owner only)
- Admin can delete specific post by id
- Posts API includes pagination, filtering, and ordering
- User can search posts using title, content, author, year and month
- Each post includes an image
- User can fetch all his posts by userid
  
![img](https://github.com/raghav-patidar1/django-blog-api/blob/main/assets/posts-module.PNG)

## Comments Module
- User can add comments on a post
- User can list all comments on a specific post by post id
- User can retreive specific comment by post id and comment id
- User can update and delete his comment on a specific post by post id and comment id (Owner only)
- Comments API includes pagination
  
![img](https://github.com/raghav-patidar1/django-blog-api/blob/main/assets/comments-module.PNG)

## Prerequisites

To run this project successfully, ensure you have the following:

- Python 3.12+

## Installation

### Clone Repository
    
  ```bash
  https://github.com/raghav-patidar1/django-blog-api.git
  cd django-blog-api
  ```

### Create and Activate Virtual Environment
  ```bash
  python -m venv venv

  source venv/bin/activate   # On Linux/Mac
  venv\Scripts\activate      # On Windows
  ```

### Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```

### Setup Environment Variables
  1. Copy `.env.example` → `.env`:
     
      ```bash
      cp .env.example .env
      ```
  2. Fill in your credentials (Django and MySQL settings).

     Example `.env`configuration file for a live server. 
      ```bash
      SECRET_KEY="your django secret key"
      DEBUG=True
      MYSQL_DB_NAME="mysql database name"
      MYSQL_USER="mysql username"
      MYSQL_PASSWORD="mysql password"
      MYSQL_HOST="mysql host"
      MYSQL_PORT="3306"
      
      ```

      To generate a Django secret key:
      ```bash
      python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
      ```

### Apply Migrations

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### Run Development Server

  ```bash
  python manage.py runserver
  ```

### Access API Docs

API Base URL: `http://localhost:8000/`

👉 [Click here](http://localhost:8000/api/schema/swagger-ui/) to go through Swagger-UI API documentation after running server.


## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Acknowledgements  
- [Django Documentation](https://docs.djangoproject.com/)  
- [Django REST Framework](https://www.django-rest-framework.org/) 
- [DRF SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) 
- [Django-filter](https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html) 
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) 



