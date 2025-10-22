````markdown
# 🧠 Backend Wizards — Stage 0 Task  
### 🚀 Dynamic Profile API (Python/Django)

This project is my submission for **Backend Wizards — Stage 0 Task**.  
It’s a simple but dynamic REST API built with **Django REST Framework**, designed to return my profile information along with a **random cat fact** fetched live from the **Cat Facts API**.

---

## 📋 Task Overview

**Goal:**  
Create a RESTful GET endpoint `/me` that returns:
- Your name, email, and backend stack.
- The current UTC timestamp.
- A random cat fact from the Cat Facts API (`https://catfact.ninja/fact`).

### ✅ Expected Response Format

```json
{
  "status": "success",
  "user": {
    "email": "okonkwoemmanuel348@gmail.com",
    "name": "Okonkwo Emmanuel",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "Cats sleep for around 70% of their lives."
}
````

---

## 🧑‍💻 Tech Stack

* **Language:** Python 3.11+
* **Framework:** Django 5.2.1
* **REST Toolkit:** Django REST Framework
* **HTTP Client:** Requests
* **Deployment:** Koyeb (PaaS)
* **Server:** Gunicorn
* **Static Files:** WhiteNoise

---

## ⚙️ Project Structure

```
backendwiszard/
│
├── backendwiszard/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── profileapp/
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🌐 API Endpoint

| Method | Endpoint | Description                             |
| ------ | -------- | --------------------------------------- |
| GET    | `/me`    | Returns profile info + dynamic cat fact |

### Example Request

```bash
GET https://your-koyeb-app-name.koyeb.app/me/
```

### Example Response

```json
{
  "status": "success",
  "user": {
    "email": "okonkwoemmanuel348@gmail.com",
    "name": "Okonkwo Emmanuel",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "Cats have five toes on their front paws, but only four toes on their back paws."
}
```

---

## 🧩 Key Features

✅ Returns **live data** from an external API (Cat Facts API)
✅ Includes **dynamic UTC timestamps** in ISO 8601 format
✅ Proper **error handling** for network failures and timeouts
✅ Uses **Django REST Framework** for clean, maintainable API structure
✅ Ready for **deployment on Koyeb** or other PaaS platforms

---

## 🛠️ Local Development Setup

Follow these steps to run the project locally 👇

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/okonkwo348/backendwiszard-stage0.git
cd backendwiszard-stage0
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Then visit:
👉 **[http://127.0.0.1:8000/me/](http://127.0.0.1:8000/me/)**

---

## 🌐 Deployment (Koyeb)

This app is deployed on **[Koyeb](https://www.koyeb.com)** using the following configuration:

### ⚙️ Procfile

```
web: gunicorn backendwiszard.wsgi --log-file -
```

### ⚙️ Build Command

```
pip install -r requirements.txt
python manage.py collectstatic --noinput
```

### ⚙️ Run Command

```
gunicorn backendwiszard.wsgi
```

### ✅ Settings Adjustments

In `backendwiszard/settings.py`:

```python
import os

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise for static file serving
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

---

## 🧾 Requirements

Here are the core dependencies used in this project:

```
Django==5.2.1
djangorestframework==3.16.0
django-cors-headers==4.7.0
gunicorn==23.0.0
whitenoise==6.9.0
requests==2.32.5
python-dotenv==1.1.0
```

---

## 🧠 Lessons Learned

Through this task, I learned how to:

* Consume external APIs dynamically within Django.
* Format JSON responses using Django REST Framework.
* Handle network errors gracefully.
* Deploy Django apps on modern cloud platforms (Koyeb).
* Write clean, production-ready backend code.

---

## 📫 Contact

**👤 Name:** Okonkwo Emmanuel
**📧 Email:** [okonkwoemmanuel348@gmail.com](mailto:okonkwoemmanuel348@gmail.com)
**💻 Stack:** Python / Django

---

## 🏁 Final Notes

This project fulfills all the **Backend Wizards Stage 0** requirements:

* ✅ Working `/me` endpoint
* ✅ Dynamic cat fact integration
* ✅ Real-time UTC timestamp
* ✅ JSON response structure compliance
* ✅ Hosted on a valid platform (Koyeb)
* ✅ Well-documented repository

---

> “Backend development is not just about writing APIs — it’s about building reliable, predictable, and elegant systems.” 🧱✨
> — *Okonkwo Emmanuel*

```

