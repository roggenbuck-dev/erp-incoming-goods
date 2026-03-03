# ERP – Incoming Goods Module

> ⚠️ This repository contains a module excerpt of a proprietary ERP system.  
> Project-level configuration (settings.py, manage.py, database setup) is intentionally omitted.

A Django web application for managing incoming goods, developed as part 
of a live production ERP system.

This module was built during an apprenticeship at BARNICOM (Bernau bei 
Berlin) and served as the IHK final project for the apprenticeship as 
*Fachinformatiker für Anwendungsentwicklung*.

The existing ERP system covered customers, orders, invoices and leads – 
but had no warehouse management. This module was developed as the first 
step toward a complete warehouse management system, adding the ability to 
record incoming goods and automatically update stock levels.

It was integrated into the running system after review and sign-off by 
the client via GitLab merge request.

---

## Features

- Book incoming goods by EAN, product name or product number
- All three search fields auto-fill each other via AJAX autocomplete
- Barcode scanner integration – auto-Enter suppressed via `event.preventDefault()` to keep autocomplete working
- Stock automatically updated on every create, update and delete
- Update recalculates stock based on quantity difference
- Delete subtracts quantity from stock before removal
- CSRF-protected AJAX delete without page reload
- Login required for all views (`@login_required`)

---

## Technologies

- Python 3
- Django 4.0.1
- Django REST Framework 3.13.1
- jQuery 3.7.1 & jQuery UI 1.12.1
- MariaDB
- HTML5, CSS3, JavaScript, AJAX
- python-dotenv 0.19.2
- Git & GitLab

---

## Technical Focus

- Transaction-safe stock updates across create, update and delete
- Clear separation of concerns (models / CRUD logic / AJAX endpoints)
- Stock recalculation based on quantity delta logic
- Server-side validation and CSRF protection

## Project Structure
```text
erp-incoming-goods/
├── models/
│   ├── incoming_goods.py
│   ├── product.py
│   ├── warehouse.py
│   └── warehouse_stock.py
├── views/
│   ├── crud/
│   │   ├── create.py
│   │   ├── read.py
│   │   ├── update.py
│   │   └── delete.py
│   └── products/
│       ├── products_by_ean.py
│       ├── products_by_name.py
│       └── products_by_number.py
├── templates/
│   ├── incomingGoods.html
│   ├── create.html
│   └── update.html
├── urls.py
└── README.md
```

---

## Key Components

**`models/incoming_goods.py`** – Core model: stores quantity, product, warehouse, user and timestamp per booking. ForeignKey relations to Product, Warehouse and Django's User model.

**`views/crud/create.py`** – Handles new bookings. Creates an `IncomingGoods` entry and updates `WarehouseStock` in the same operation.

**`views/crud/update.py`** – Calculates the quantity difference between old and new value, adjusts stock accordingly.

**`views/crud/delete.py`** – Subtracts quantity from stock before deleting the entry. Returns JSON response, no page reload.

**`views/products/`** – Three AJAX endpoints (by EAN, name, number) that power the autocomplete. Selecting a result auto-fills all three search fields.

**`templates/create.html`** – Booking form with barcode scanner support. Uses `event.preventDefault()` to suppress the scanner's auto-Enter so autocomplete keeps working.

---

## Notes

- This repository contains the incoming goods module as a code excerpt. The full ERP system is proprietary.
- Only code written by the author is included.
- The module was developed, tested and handed over to the client.

---

## Author

Created by Atze Roggenbuck