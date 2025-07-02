# BrewOps API

BrewOps API is a scalable backend solution for managing operations in a Fast-Moving Consumer Goods (FMCG) supply chain, specifically tailored for an alcoholic beverage company (company name anonymized). It includes robust modules for managing accounts, brands, products, stock, sales, and reporting.

🚀 **Live API**:  
Hosted on [Railway](https://railway.app/) → **[https://brewopsapi-production.up.railway.app](https://brewopsapi-production.up.railway.app/)**

---

## 🧱 Project Structure

```
chibuezeonejeme-brewopsapi/
├── apps/
│   ├── accounts/     # User authentication and token management
│   ├── brands/       # Alcoholic beverage brands
│   ├── products/     # Product SKUs and metadata
│   ├── stock/        # Inventory tracking
│   ├── sales/        # Sales recording and pricing
│   └── reporting/    # Analytics endpoints
├── src/              # Project settings and entry points
├── faker_createbrand_product.py
├── faker_create_stock_qty.py
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
└── staticfiles/      # Collected static and Swagger docs
```

## 🛠 Tech Stack

- **Framework**: Django 4+, Django REST Framework
- **Database**: PostgreSQL (prod), SQLite (dev)
- **Auth**: JWT via custom token logic
- **Docs**: Swagger & ReDoc (via `drf-yasg`)
- **Deployment**: [Railway](https://railway.app/)
- **Data Gen**: Faker

## 🔐 Authentication

JWT-based authentication is implemented. You can log in using:

```
POST /api/accounts/login/
```

Payload:
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

Returns access and refresh tokens.

## 🔄 API Endpoints

Base route: `/api/`

Each app exposes endpoints:

- `/accounts/`
- `/brands/`
- `/products/`
- `/stock/`
- `/sales/`
- `/reporting/`

All standard CRUD operations are supported.

## 📊 Reporting

Includes endpoints for:

- Top-selling products
- Brand-wise performance
- Stock availability

## 🧪 Sample Data

Run the scripts below to populate dummy data using [Faker](https://faker.readthedocs.io/):

```bash
python faker_createbrand_product.py
python faker_create_stock_qty.py
```

## 🌐 Deployment Notes

Use `.env` for secrets. Example settings in `src/settings.py`:

```python
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"))
}
```

## 🧭 Run the Server

```bash
# Install packages
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run dev server
python manage.py runserver
```

## 📄 API Documentation

Access interactive API documentation at:

- Swagger: `/swagger/`
- ReDoc: `/redoc/`

## 🛡 CORS Config

Add frontend URLs in `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://yourfrontend.com"
]
```

Or allow all for testing:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

## 🤝 Contributing

This project was built solo to demonstrate robust architecture for FMCG logistics. Contributions and suggestions are welcome.

## 📜 License

MIT License – See `LICENSE` file.
