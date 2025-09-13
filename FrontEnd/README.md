# Full Stack Blog Platform – React (Vite) + Django 5.1 + PostgreSQL

This project is a **modern full-stack web application** combining a **React frontend** (powered by Vite) with a **Django 5.1 backend** and **PostgreSQL** database.  
It includes **JWT authentication**, a **custom API**, **rich text editing**, **charts**, **PayPal integration**, and a fully customized **Django admin panel (Jazzmin)**.

---

## 🚀 Tech Stack

### Frontend (React + Vite)

- ⚛️ React 18 with [Vite](https://vitejs.dev/) for blazing fast builds.
- 🔄 Routing with [React Router DOM](https://reactrouter.com/).
- 📊 Charts with [Chart.js](https://www.chartjs.org/) + `react-chartjs-2`.
- 📝 Rich text editing using [CKEditor 5](https://ckeditor.com/ckeditor-5/).
- 💳 Payments via [PayPal React SDK](https://github.com/paypal/react-paypal-js).
- 🗂 State management with [Zustand](https://docs.pmnd.rs/zustand/getting-started/introduction).
- 🎨 UI Enhancements: SweetAlert2, React Icons, React Photo Album, Lightbox.
- 📅 Date utilities: Day.js & Moment.
- 🔐 Authentication helpers: JWT Decode, JS-Cookie.

### Backend (Django 5.1)

- 🌐 Django REST Framework (`drf`) for building APIs.
- 🔑 JWT Authentication with `rest_framework_simplejwt`.
- 📖 API documentation via [drf-yasg](https://drf-yasg.readthedocs.io/).
- 🎛 Admin panel styled with [Jazzmin](https://django-jazzmin.readthedocs.io/).
- 🔄 CORS enabled for frontend-backend communication.
- 🗄 Database: **PostgreSQL**.

---

## 📂 Project Structure

project-root/
│── backend/ (Django project)
│ ├── api/ # Custom Django app
│ ├── BackEnd/ # Django settings and core
│ ├── templates/ # HTML templates
│ ├── media/ # Uploaded files
│ └── manage.py
│
│── frontend/ (React app with Vite)
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── vite.config.js
│
└── README.md

---

## ⚙️ Setup Instructions

### 1. Backend (Django + PostgreSQL)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


### 2. Frontend (React + Vite)

cd frontend
npm install
npm run dev

🔑 Authentication

Uses JWT Authentication via djangorestframework-simplejwt.

Access tokens expire in 5 minutes, refresh tokens last 50 days.

Tokens are rotated and blacklisted after use.

🎛 Custom Admin Panel

The project uses Jazzmin to customize the Django admin:

Brand: Modern Marketplace

Icons for models (User, Post, Category, Comment, Notification, etc.)

Sidebar navigation enabled

Custom theme colors and UI tweaks

📖 API Documentation

Interactive API docs available via Swagger UI (drf-yasg):

http://localhost:8000/swagger/

🔗 Useful Links

React Docs

Vite Docs

Django Docs

Django REST Framework

Simple JWT

PostgreSQL
```
