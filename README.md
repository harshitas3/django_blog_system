<<<<<<< HEAD
# django_blog_system
=======
# Django Blog System

## Features
- List all blogs
- View blog details
- Fetch country info via API

## Installation
1. Clone the repository
   ```sh
   git clone <repository_url>
   cd django_blog_system
   ```
2. Create and activate a virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server
   ```sh
   python manage.py runserver
   ```

## API Endpoints
- `GET /blogs/` - Retrieve all blog posts
- `GET /blogs/<id>/` - Retrieve details of a specific blog post
- `GET /country/<country_name>/` - Fetch country information from an external API

## Usage
- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage blog posts.
- Use an API testing tool like Postman or cURL to interact with the endpoints.

## Deployment
1. Set up a production database and configure `settings.py` accordingly.
2. Collect static files:
   ```sh
   python manage.py collectstatic
   ```
3. Use a WSGI server like Gunicorn for deployment:
   ```sh
   gunicorn blog_project.wsgi:application --bind 0.0.0.0:8000
   ```


>>>>>>> 086c43c (Initial commit)
