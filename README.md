# IoTGenie - Open From Anywhere

## Accessing IoTGenie Anywhere

You can view and manage this project from anywhere using:

- **GitHub Web:** Visit [https://github.com/hijbullahx/IoTGenie](https://github.com/hijbullahx/IoTGenie) in any web browser to view code, issues, and documentation.
- **Clone Locally:** Use `git clone https://github.com/hijbullahx/IoTGenie.git` on any device with Git and Python installed.
- **Cloud IDEs:** Open the repo in cloud-based editors like GitHub Codespaces, Gitpod, or VS Code for the Web for instant access and editing.
- **Web Browser:** All documentation and code are accessible via browser—no special software required for viewing.

This project is public and can be accessed from any device with an internet connection.

# IoTGenie - Software Requirements Specification (SRS)

## Table of Contents
1. Introduction
   - 1.1 Purpose
   - 1.2 Document Conventions
   - 1.3 Intended Audience and Reading Suggestions
   - 1.4 Product Scope
   - 1.5 References
2. Overall Description
   - 2.1 Product Perspective
   - 2.2 Product Functions
   - 2.3 User Classes and Characteristics
   - 2.4 Operating Environment
   - 2.5 Design and Implementation Constraints
   - 2.6 User Documentation
   - 2.7 Assumptions and Dependencies
3. External Interface Requirements
   - 3.1 User Interfaces
   - 3.2 Hardware Interfaces
   - 3.3 Software Interfaces
   - 3.4 Communications Interfaces
4. System Features
   - 4.1 Product Browsing & Search
   - 4.2 Cart Management
   - 4.3 Order Placement & Tracking
   - 4.4 User Authentication & Profile Management
   - 4.5 Admin Management Panel
5. Other Nonfunctional Requirements
   - 5.1 Performance Requirements
   - 5.2 Safety Requirements
   - 5.3 Security Requirements
   - 5.4 Software Quality Attributes
   - 5.5 Business Rules
6. Other Requirements
7. Appendices

---

## 1. Introduction

### 1.1 Purpose
This SRS specifies requirements for IoTGenie, a web-based IoT e-commerce platform allowing customers to browse, purchase, and manage IoT products. The system implements a complete e-commerce workflow with Django backend, REST API capabilities, and responsive frontend templates. This document covers customer and admin functionalities for the current production release.

### 1.2 Document Conventions
- "REQ-" prefix for functional requirements
- High/Medium/Low priority tagging for features
- URLs and endpoints in `/endpoint/` format
- Database models referenced in `ModelName` format

### 1.3 Intended Audience and Reading Suggestions
- **Developers**: For implementation details and API specifications
- **Testers**: For functional and nonfunctional validation points
- **Project Managers**: For scope, constraints, and dependencies
- **End-Users & Stakeholders**: For feature expectations and system capabilities

### 1.4 Product Scope
IoTGenie is a complete e-commerce platform enabling:
- IoT product browsing with search and filtering
- Shopping cart management with quantity control
- Order placement with mock payment integration
- User authentication and profile management
- Admin panel for product and order management
- REST API endpoints for future mobile/React integration

### 1.5 References
- Django 4.0+ Documentation
- Django REST Framework Documentation
- Bootstrap 5 Documentation
- PostgreSQL Documentation
- WhiteNoise Documentation

---

## 2. Overall Description

### 2.1 Product Perspective
IoTGenie is a standalone web application built with:
- **Backend**: Django framework with Django REST Framework
- **Frontend**: Django templates with Bootstrap responsive design
- **Database**: SQLite (development) / PostgreSQL (production)
- **Deployment**: Render.com with WhiteNoise for static file serving
- **Authentication**: Django built-in authentication system

### 2.2 Product Functions
**Core E-commerce Functions:**
- Browse IoT products with category filtering and keyword search
- View detailed product information with popularity tracking (view counts)
- Add/remove items from shopping cart with quantity management
- Place orders with mock payment options (Visa, MasterCard, bKash, Nagad)
- Track order history with per-user order numbering
- Cancel individual items from orders

**User Management Functions:**
- User registration and authentication
- Profile management with password change capability
- Session-based cart persistence

**Administrative Functions:**
- Product management (CRUD operations)
- Order and cart monitoring
- User management through Django admin interface

### 2.3 User Classes and Characteristics
- **Customers**: End users with basic technical knowledge who browse and purchase IoT products
- **Administrators**: Technical users who manage products, orders, and system configuration
- **Future Vendors**: Planned user class for multi-vendor marketplace functionality

### 2.4 Operating Environment
- **Client-side**: Modern web browsers (Chrome, Firefox, Edge, Safari)
- **Server-side**: Python 3.9+, Django 4.0+, WhiteNoise
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Render.com cloud platform
- **Static Files**: WhiteNoise with compressed manifest storage

### 2.5 Design and Implementation Constraints
- Must comply with Django security best practices
- Responsive design for mobile and desktop browsers
- RESTful API design for future frontend framework integration
- Production deployment must support Python 3.9+
- Static file serving optimized for cloud deployment

### 2.6 User Documentation
- Inline help and intuitive UI design
- Admin documentation for product management
- API documentation for developers
- Setup instructions in README

### 2.7 Assumptions and Dependencies
- Users have stable internet connection
- Payment gateway integration is mock (real integration planned)
- Future React.js frontend will consume existing API endpoints
- PostgreSQL availability for production deployment

---

## 3. External Interface Requirements

### 3.1 User Interfaces
**Responsive Web Interface:**
- Product listing page with grid layout and filtering options
- Product detail pages with image display and add-to-cart functionality
- Shopping cart interface with quantity controls
- Order history with cancellation options
- User registration and profile management forms
- Mock payment interface with local payment method logos

**Design Specifications:**
- Bootstrap-based responsive design
- Mobile-first approach with breakpoint optimization
- Consistent navigation and branding across all pages

### 3.2 Hardware Interfaces
- Standard web hosting infrastructure
- Minimum server requirements: 2 CPU cores, 4GB RAM
- Image storage for product photos
- Database storage for transactional data

### 3.3 Software Interfaces
**API Endpoints:**
- Django REST Framework ViewSets for Products, Cart, and Orders
- JSON API responses for future frontend integration
- Product search suggestions endpoint
- Authentication endpoints using Django sessions

**Database Integration:**
- Django ORM with PostgreSQL production database
- Models: Product, Cart, CartItem, Order, OrderItem
- Foreign key relationships and data integrity constraints

### 3.4 Communications Interfaces
- HTTP/HTTPS protocol for web communication
- JSON data format for API responses
- RESTful API architecture for external integrations
- Session-based authentication for web interface

---

## 4. System Features

### 4.1 Product Browsing & Search
**Priority**: High  
**REQ-1**: System shall display all IoT products in a responsive grid layout  
**REQ-2**: System shall provide category-based filtering functionality  
**REQ-3**: System shall implement keyword search across product names and descriptions  
**REQ-4**: System shall track and display product view counts for popularity metrics  
**REQ-5**: System shall provide product detail pages with comprehensive information  

**Implementation Details:**
- Product model with fields: name, description, price, category, image, view_count
- Search functionality using Django Q objects for OR queries
- Category filtering with distinct category extraction
- View count increment on product detail access

### 4.2 Cart Management
**Priority**: High  
**REQ-6**: System shall allow authenticated users to add products to cart  
**REQ-7**: System shall support quantity adjustment for cart items  
**REQ-8**: System shall allow removal of individual items from cart  
**REQ-9**: System shall calculate and display total cart value  
**REQ-10**: System shall persist cart data across user sessions  

**Implementation Details:**
- Cart model with one-to-one relationship to User
- CartItem model linking Cart and Product with quantity
- Total price calculation using property methods
- Session-based cart persistence for logged-in users

### 4.3 Order Placement & Tracking
**Priority**: High  
**REQ-11**: System shall allow order placement from cart contents  
**REQ-12**: System shall generate unique per-user order numbers  
**REQ-13**: System shall provide mock payment interface with multiple payment options  
**REQ-14**: System shall maintain order history for each user  
**REQ-15**: System shall allow cancellation of individual order items  
**REQ-16**: System shall recalculate order totals after item cancellation  

**Implementation Details:**
- Order model with user-specific order numbering
- OrderItem model preserving product price at time of purchase
- Mock payment gateway with bKash, Nagad, Visa, MasterCard options
- Order management with cascade deletion when all items removed

### 4.4 User Authentication & Profile Management
**Priority**: Medium  
**REQ-17**: System shall provide user registration functionality  
**REQ-18**: System shall implement secure login/logout  
**REQ-19**: System shall allow profile editing including password changes  
**REQ-20**: System shall maintain session security across requests  

**Implementation Details:**
- Django built-in authentication system
- Custom UserCreationForm for registration
- Profile editing with password change form
- Session authentication with CSRF protection

### 4.5 Admin Management Panel
**Priority**: High  
**REQ-21**: System shall provide Django admin interface for product management  
**REQ-22**: System shall allow admin monitoring of carts and orders  
**REQ-23**: System shall provide user management capabilities  
**REQ-24**: System shall implement role-based access control  

**Implementation Details:**
- Django admin interface with custom model registration
- Admin access restricted to superuser accounts
- CRUD operations for all major models
- Audit trail through Django's built-in logging

---

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
- Page load times under 2 seconds for product listings
- Database queries optimized with select_related and prefetch_related
- Static file compression using WhiteNoise
- Image optimization for product photos

### 5.2 Safety Requirements
- Confirmation dialogs for item deletion actions
- Order cancellation limited to individual items
- Data validation on all user inputs
- Graceful error handling with user-friendly messages

### 5.3 Security Requirements
- HTTPS encryption for all communications
- CSRF protection on all forms
- SQL injection prevention through Django ORM
- User input sanitization and validation
- Session-based authentication with secure cookies

### 5.4 Software Quality Attributes
- **Scalability**: RESTful API design for future expansion
- **Maintainability**: Clean code structure with Django best practices
- **Usability**: Intuitive interface with responsive design
- **Reliability**: Error handling and logging throughout application

### 5.5 Business Rules
- Only authenticated users can access cart and order functionality
- Product view counts increment on each detail page visit
- Order numbers are unique per user but not globally unique
- Cart contents are cleared after successful order placement

---

## 6. Other Requirements
- API endpoints designed to support future mobile applications
- REST API documentation for third-party integrations
- Deployment configuration for cloud platforms (Render.com)
- Environment-based configuration for development/production

---

## 7. Appendices

### Appendix A: Glossary
- **IoT**: Internet of Things - interconnected computing devices
- **API**: Application Programming Interface
- **CRUD**: Create, Read, Update, Delete operations
- **ORM**: Object-Relational Mapping
- **CSRF**: Cross-Site Request Forgery protection

### Appendix B: Database Schema
**Models Implemented:**
- `Product`: Core product information with view tracking
- `Cart`: User-specific shopping cart
- `CartItem`: Individual items in cart with quantity
- `Order`: User orders with sequential numbering
- `OrderItem`: Individual items in orders with historical pricing

### Appendix C: API Endpoints
- `/api/products/` - Product CRUD operations
- `/api/carts/` - Cart management
- `/api/orders/` - Order management
- `/products/search-suggestions/` - Search autocomplete

### Appendix D: Technology Stack
| Component | Technology | Version |
|-----------|------------|---------|
| Backend Framework | Django | 4.0+ |
| API Framework | Django REST Framework | Latest |
| Database | PostgreSQL/SQLite | - |
| Frontend | Bootstrap | 5.x |
| Authentication | Django JWT | Latest |
| Deployment | Render.com | - |
| Static Files | WhiteNoise | Latest |

---

## Project Overview
IoTGenie is a web-based e-commerce platform designed for the Internet of Things (IoT) ecosystem, allowing users to browse, purchase, and manage IoT products. This project is developed as a scalable, feature-complete e-commerce solution with modern web technologies.

## Implementation Status

### Completed Features
✅ **Product Management System**
- Product model with name, description, price, category, image, view_count
- Product listing with responsive grid layout
- Product detail pages with view count tracking
- Category-based filtering and keyword search functionality

✅ **Shopping Cart System**
- User-specific cart with persistent storage
- Add/remove products with quantity control
- Cart total calculation and display
- Session-based cart management for authenticated users

✅ **Order Management System**
- Complete order placement workflow
- User-specific order numbering system
- Order history with detailed item breakdown
- Individual order item cancellation capability
- Order total recalculation after modifications

✅ **User Authentication & Profiles**
- User registration with automatic login
- Secure login/logout functionality
- Profile editing with password change capability
- Session-based authentication with CSRF protection

✅ **Admin Interface**
- Django admin panel for all models
- Product CRUD operations
- Cart and order monitoring
- User management capabilities

✅ **Payment Integration (Mock)**
- Mock payment gateway with multiple options
- Support for Visa, MasterCard, bKash, Nagad
- Payment confirmation workflow
- Integration placeholder for real payment processors

✅ **API Development**
- Django REST Framework implementation
- ViewSets for Product, Cart, and Order models
- JSON API responses for future frontend integration
- Search suggestions endpoint

### Technical Implementation
✅ **Database Design**
- Normalized relational database schema
- Foreign key relationships with proper constraints
- Data integrity through Django ORM
- Migration system for schema evolution

✅ **Security Features**
- CSRF protection on all forms
- User input validation and sanitization
- Role-based access control
- Session security with secure cookies

✅ **Deployment Configuration**
- Render.com deployment setup
- Environment variable configuration
- WhiteNoise for static file serving
- PostgreSQL production database support

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Git for version control
- Virtual environment (recommended)

### Installation Steps

1. **Clone Repository:**
   ```bash
   git clone https://github.com/hijbullahx/IoTGenie.git
   cd IoTGenie
   ```

2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   ```bash
   # Create .env file with necessary environment variables
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Database Setup:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Static Files Collection:**
   ```bash
   python manage.py collectstatic
   ```

7. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

9. **Access Application:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API endpoints: http://127.0.0.1:8000/api/

### Production Deployment
For Render.com deployment:
1. Set environment variables in Render dashboard
2. Connect GitHub repository
3. Configure build and start commands
4. Set up PostgreSQL database
5. Configure domain and SSL

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend Framework** | Django 4.0+ | Core web framework with ORM and admin interface |
| **API Framework** | Django REST Framework | RESTful API development and serialization |
| **Authentication** | Django JWT + Sessions | Token-based and session-based authentication |
| **Database** | SQLite (dev) / PostgreSQL (prod) | Data persistence and relational data management |
| **Frontend** | Django Templates + Bootstrap 5 | Server-side rendering with responsive design |
| **Static Files** | WhiteNoise | Static file serving for production deployment |
| **Image Handling** | Pillow | Image processing and storage for product photos |
| **Deployment** | Render.com | Cloud platform for application hosting |
| **Version Control** | Git & GitHub | Source code management and collaboration |

## API Documentation

### REST API Endpoints

**Product Endpoints:**
- `GET /api/products/` - List all products
- `POST /api/products/` - Create new product (admin only)
- `GET /api/products/{id}/` - Get product details
- `PUT /api/products/{id}/` - Update product (admin only)
- `DELETE /api/products/{id}/` - Delete product (admin only)

**Cart Endpoints:**
- `GET /api/carts/` - List user carts
- `POST /api/carts/` - Create new cart
- `GET /api/carts/{id}/` - Get cart details
- `PUT /api/carts/{id}/` - Update cart
- `DELETE /api/carts/{id}/` - Delete cart

**Order Endpoints:**
- `GET /api/orders/` - List user orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/{id}/` - Get order details
- `PUT /api/orders/{id}/` - Update order
- `DELETE /api/orders/{id}/` - Delete order

**Additional Endpoints:**
- `GET /products/search-suggestions/?q={query}` - Product search autocomplete

### URL Patterns

**Main Application URLs:**
- `/` - Redirects to product list
- `/products/` - Product listing page
- `/products/{id}/` - Product detail page
- `/products/search-suggestions/` - AJAX search suggestions
- `/cart/` - Shopping cart page
- `/cart/add/{product_id}/` - Add product to cart
- `/cart/remove/{item_id}/` - Remove item from cart
- `/orders/` - Order history page
- `/orders/purchase/` - Order placement page
- `/orders/place/` - Process order placement
- `/orders/{order_id}/cancel/{item_id}/` - Cancel order item

**Authentication URLs:**
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - User profile view
- `/profile/edit/` - Edit user profile

**Admin URLs:**
- `/admin/` - Django admin interface

## File Structure

```
IoTGenie/
├── IoTGenie/                 # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings with Render.com config
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── shop/                     # Main application
│   ├── models.py            # Database models (Product, Cart, Order)
│   ├── views.py             # View functions and ViewSets
│   ├── serializers.py       # DRF serializers
│   ├── forms.py             # Django forms
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Admin interface configuration
│   └── migrations/          # Database migrations
├── templates/                # HTML templates
│   ├── base.html            # Base template with Bootstrap
│   ├── product_list.html    # Product listing page
│   ├── product_detail.html  # Product detail page
│   ├── cart_detail.html     # Shopping cart page
│   ├── order_list.html      # Order history page
│   ├── purchase_order.html  # Order placement page
│   ├── profile.html         # User profile page
│   ├── edit_profile.html    # Profile editing page
│   └── registration/        # Authentication templates
├── static/                   # Static files (CSS, JS, images)
├── media/                    # User uploads (product images)
├── requirements.txt          # Python dependencies
├── manage.py                # Django management script
└── README.md                # This documentation
```

## Contributing

### Development Guidelines
1. Follow Django best practices and PEP 8 coding standards
2. Write comprehensive tests for new features
3. Update documentation for any API changes
4. Use meaningful commit messages
5. Create feature branches for new development

### Future Enhancements
- React.js frontend integration
- Real payment gateway integration (Stripe, PayPal)
- Multi-vendor marketplace functionality
- Advanced search with Elasticsearch
- Email notifications for orders
- Product reviews and ratings system
- Wishlist functionality
- Mobile application development

---

*Last updated: August 2025*