---
title: "GLOWVERSE API Documentation"
output: github_document
---

# GLOWVERSE API

Welcome to the GLOWVERSE API! This project is the capstone for the Backend Web Development program, showcasing the skills and knowledge acquired throughout the course. The API is designed to manage products, categories, and user accounts for an e-commerce platform.

## Project Overview
The GLOWVERSE API is a backend solution for an e-commerce platform that includes the following features:
- **User Authentication and Authorization:** Secure user login, registration, and role-based access control (admin/user roles).
- **Product Management:** CRUD operations for products, including categories and stock tracking.
- **User Profiles:** Retrieve and update user profiles.
- **Search and Filtering:** Search products by name and filter by category.
- **Deployment:** API hosted and available online.

## Features
### Authentication
- User login with JWT-based authentication.
- Secure password storage using Django's `make_password`.

### User Management
- Register new users.
- Retrieve and update user profiles.
- Support for different user roles (admin and regular users).

### Product Management
- CRUD operations for products and categories.
- Admin-only access for creating, updating, and deleting products.

### Search and Filtering
- Search for products by name.
- Filter products by category.

## Tech Stack
- **Backend Framework:** Django, Django REST Framework
- **Database:** SQLite (development)
- **Authentication:** JWT (JSON Web Tokens)
- **Hosting:** PythonAnywhere
- **Version Control:** Git and GitHub

## Installation and Setup
```bash
# Clone the repository
git clone https://github.com/<username>/GLOWVERSE.git
cd GLOWVERSE

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
