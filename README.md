# IoTGenie - A Web-Based IoT Marketplace

IoTGenie is a web-based e-commerce platform designed for the Internet of Things (IoT) ecosystem, allowing users to browse, purchase, and manage IoT products. This project is developed as a prototype for a scalable, multi-vendor marketplace.

## Project Overview
IoTGenie aims to provide a seamless shopping experience for IoT enthusiasts, with features like product browsing, cart management, and order placement. The platform uses Django and Django REST Framework for the backend, with SQLite in development (planned for PostgreSQL in production). The frontend uses Django templates with Bootstrap, with React.js planned for future enhancements.

## Core Features
### Customer Features
- **Browse and Search**: View IoT products with search and category filters (`/products/`).
- **Product Details**: Detailed product pages with descriptions, prices, categories, and popularity indicators (view counts).
- **Cart System**: Add/remove items, adjust quantities (`/cart/`).
- **Order Placement**: Place orders with mock payment methods (Visa, MasterCard, bKash, Nagad) and a modal indicating payment gateway is under development (`/orders/purchase/`).
- **Order Management**: View and cancel orders (`/orders/`).
- **User Authentication**: Register, login, logout, edit profile (`/register/`, `/profile/`).

### E-Commerce Functionalities
- Full cart system with quantity control.
- Mock payment gateway with local bKash/Nagad logos.
- Order history per user.

### Admin Features
- Admin dashboard (`/admin/`) for managing products, carts, cart items, and orders.



## Technology Stack
| Component       | Technology Used                     |
|-----------------|-------------------------------------|
| Frontend        | Django Templates, Bootstrap (React.js planned) |
| Backend         | Django, Django REST Framework       |
| Database        | SQLite (development), PostgreSQL (production) |
| Authentication  | Django Authentication               |
| Version Control | Git & GitHub                        |

## Setup Instructions
1. Clone Repository:
   ```bash
   git clone <your-repo-url>
   cd IoTGenie

2. Create Virtual Environment:
python -m venv venv
venv\Scripts\activate

3. Install Dependencies:
pip install -r requirements.txt

4. Run Migrations:
python manage.py makemigrations
python manage.py migrate

5. Collect Static Files:
python manage.py collectstatic

6. Create Superuser:
python manage.py createsuperuser

7. Run Server:
python manage.py runserver

8. Access at http://127.0.0.1:8000/ and admin at /admin/.