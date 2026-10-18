# Django Helpdesk Ticket Management System

## Project Overview
A Django web application designed to manage internal helpdesk tickets. It allows users to create tickets, track their status, and assign tickets to staff members.

## Features
- View all tickets on the dashboard
- Create new helpdesk tickets
- View ticket details
- Update ticket status
- Assign tickets to staff members
- Store ticket data using SQLite
- Manage records through Django Admin

## Technologies Used
- Python
- Django
- HTML
- SQLite
- Git and GitHub

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/dasarileelasaimanohar/django-helpdesk-ticket-management.git
   ```

2. Open the project folder:
   ```bash
   cd django-helpdesk-ticket-management
   ```

3. Install Django:
   ```bash
   py -m pip install django
   ```

4. Apply database migrations:
   ```bash
   py manage.py migrate
   ```

5. Start the development server:
   ```bash
   py manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## Project Purpose
This project demonstrates the basic management of internal helpdesk tickets using Django.
