# Django Project Setup

This project is a Django application that manages categories, subcategories, and products. Follow the instructions below to set up the project on your local machine.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- visual studio code
- extention for python

## Installation Steps

### 1. clone repository from github

```
git clone https://github.com/mahmoudmohamed57/Backend-Task-Junior.git
```

### 2. Create and Activate a Virtual Environment

#### On Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Libraries

```
pip install -r requirements.txt
```

### 4. Set Up the Database

```
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
```

### 5. Start the Development Server

```
python manage.py runserver
```

### 6. View All Products

```
http://127.0.0.1:8000/api/products/
```

### 7. View a Specific Product

```
http://127.0.0.1:8000/api/products/<product_id>/
```

### 8. Search Products by Name

```
http://127.0.0.1:8000/api/products/?search=<search_term>
```