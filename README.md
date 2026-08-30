
#  Python & Django Practice Journey

A structured repository tracking hands-on practice, concept implementations, and full-stack web development progress with **Python** and **Django**.

---

## 📂 Repository Architecture

```text
Python_Practice/
├── 📁 Basic Python/
│   ├── 📁 Fundamentals/              # Syntax, Variables, Control Flow & Logic
│   ├── 📁 Strings/                   # String operations & manipulation
│   ├── 📁 Comprehensions/            # List, Dict & Set comprehensions
│   ├── 📁 Methods/                   # Functions, Arguments & Scope
│   ├── 📁 File Handling/             # I/O operations & text processing
│   ├── 📁 Exceptions/                # Try-except, custom exceptions & error handling
│   ├── 📁 OOPS/                      # Classes, Inheritance, Polymorphism & Encapsulation
│   ├── 📁 MultiThreading/            # Concurrent execution, Threads & Locks
│   └── 📁 Python Database(SQLite3)/  # Direct DB integration via SQLite3
│
└── 📁 Django/
    ├── 📁 Django_Project_Prac/       # Standalone practice modules & configs
    └── 📁 myproject/                 # Main full-stack application
        ├── 📁 myproject/             # Project settings, routing & ASGI/WSGI
        └── 📁 students/              # Full-featured Student Management App
            ├── 📁 migrations/        # Schema migrations & relational models
            ├── 📁 static/            # Custom CSS, JS scripts & media
            └── 📁 templates/         # Rendered HTML views & forms

```

---

## 🎯 Django Learning Roadmap & Status Tracker

| SN | Topic | Description & Modules | Status |
| --- | --- | --- | --- |
| **01** | **Django Basics & Request/Response** | Architecture overview, HTTP lifecycle, `HttpResponse` | ✅ **Completed** |
| **02** | **Project Creation** | `django-admin startproject`, project structure configuration | ✅ **Completed** |
| **03** | **Apps, URLs & Views** | `startapp`, URL routing, path converters, view handlers | ✅ **Completed** |
| **04** | **Templates** | Dynamic rendering, context passing, DTL basics | ✅ **Completed** |
| **05** | **Static Files** | Static directory configuration, linking CSS, JS, and assets | ✅ **Completed** |
| **06** | **Models & Migrations** | Model schema design, `makemigrations`, `migrate` lifecycle | ✅ **Completed** |
| **07** | **Django Admin** | `admin.site.register`, superuser creation, admin customization | ✅ **Completed** |
| **08** | **ORM & CRUD Operations** | QuerySets, filtering, object creation, updates & deletions | ✅ **Completed** |
| **09** | **Model Relationships** | ForeignKey, OneToOne, and ManyToMany data relationships | ✅ **Completed** |
| **10** | **Django Forms** | Form classes, `forms.ModelForm`, HTML form rendering | ✅ **Completed** |
| **11** | **Form Validation & CSRF** | Field validation, clean methods, `{% csrf_token %}` security | ✅ **Completed** |
| **12** | **Authentication System** | User login, registration, session management, logout views | ✅ **Completed** |
| **13** | **Users, Permissions & Groups** | Access control, decorators (`@login_required`), user levels | ✅ **Completed** |
| **14** | **Class-Based Views (CBVs)** | Generic views (`ListView`, `DetailView`, `CreateView`) | ⏳ *In Progress* |
| **15** | **Template Inheritance** | Master layouts (`base.html`), blocks, inclusion tags | ⏳ *In Progress* |
| **16** | **Middleware** | Custom middleware pipelines, request/response intercepts | ⏳ *Pending* |
| **17** | **Pagination & Query Optimization** | `Paginator`, `select_related`, `prefetch_related` performance | ⏳ *Pending* |
| **18** | **File / Image Uploads** | `FileField`, `ImageField`, `MEDIA_URL`, storage pipelines | ⏳ *Pending* |
| **19** | **Production & Deployment Basics** | `DEBUG=False`, environment variables, WSGI/Gunicorn, Nginx | ⏳ *Pending* |
| **20** | **Django REST Framework (DRF)** | REST APIs, Serializers, APIViews, ViewSets, Token Auth | ⏳ *Pending* |

---

## 🚀 How to Run the Django Project Locally

1. **Clone the repository:**
```bash
git clone https://github.com/sujith52/Python_Practice.git
cd Python_Practice/Django/myproject

```


2. **Apply migrations:**
```bash
python manage.py migrate

```


3. **Start the local development server:**
```bash
python manage.py runserver

```


4. **Access the application:**
* **App:** `http://127.0.0.1:8000/students/`
* **Admin Panel:** `http://127.0.0.1:8000/admin/`
