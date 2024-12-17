# Book Lending API

A Django REST Framework-based API for managing book lending operations. It includes user management, book tracking, and
lending requests.

---

## Installation

### **1. Set up the virtual environment**

```bash
  python -m venv .venv
```

```bash
  .venv\Scripts\activate
```

### **2. Navigate to src directory**

```bash
  cd src
```

### **3. Install dependencies**

```bash
  pip install -r requirements.txt
```

---

## Running the Project

Run this command in terminal, via **src** folder:

```cmd
  python manage.py runserver
```

Access the API documentation at:

- [Swagger UI `http://127.0.0.1:8000/swagger/`](http://127.0.0.1:8000/swagger/)
---

## Authentication

The API uses **Basic Authentication** for secured endpoints.

1. Use your credentials (username and password) to authenticate.

### You can use default test user for testing, click **Authorize** button on Swagger UI

### email: test@test.com

### password: test

---