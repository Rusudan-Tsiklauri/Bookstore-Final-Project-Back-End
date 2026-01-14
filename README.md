 📚 Spellbound — Online Bookstore (Flask Backend Project)

"Spellbound" is a full-featured online bookstore web application built as the final project for my Backend Development course.
The project focuses on **server-side logic, database design, authentication, and clean Flask architecture, demonstrating practical backend skills using Python and Flask.



 🎯 Project Overview

Spellbound allows users to browse books and authors, manage a shopping cart, and complete a checkout process, while admins can manage bookstore content.  
The application was designed with real-world backend patterns in mind, including authentication, form validation, relational databases, and role-based access.

This project emphasizes backend functionality over frontend complexity.



 ✨ Key Features

 👤 User Features
- User registration and login
- Secure authentication using Flask-Login
- Browse books and authors
- View detailed book and author pages
- Add books to a shopping cart
- Checkout process

 🔐 Admin Features
- Admin role management
- Add new books and authors
- Edit and delete bookstore content

⚙️ Backend Features
- SQLAlchemy ORM with relational models
- Flask-WTF form handling and validation
- Role-based access control
- Template rendering with Jinja2
- Organized and scalable Flask structure



 🛠 Technology Stack

- **Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** Flask-Login
- **Forms & Validation:** Flask-WTF
- **Templating Engine:** Jinja2
- **Frontend:** HTML, CSS (basic styling)
- **Environment:** Virtualenv


 🗂 Project Structure


spellbound/
│
├── app.py              # Application entry point
├── routes.py           # All application routes
├── models.py           # Database models
├── forms.py            # Flask-WTF forms
├── ext.py              # Extensions (db, login manager)
├── choices.py          # Choice constants
├── init_db.py          # Database initialization
│
├── templates/          # Jinja2 templates
│   ├── base.html
│   ├── home.html
│   ├── authors.html
│   ├── cart.html
│   ├── checkout.html
│   └── ...
│
├── static/
│   └── images/         # Book & author images
│
└── README.md
