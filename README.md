# MaxWay - Food Ordering System

A Django-based food ordering and management system with a customer-facing frontend and an admin dashboard.

## Features

- 🍕 Food product catalog with categories
- 🛒 Shopping cart functionality
- 📱 Responsive design
- 👨‍💼 Admin dashboard for managing products, orders, and customers
- 📊 Order management system
- 🖼️ Image upload support for products

## Tech Stack

- **Backend**: Django 4.2.3
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker & Docker Compose

## Prerequisites

- Python 3.12+
- PostgreSQL (or use Docker)
- Docker & Docker Compose (for containerized deployment)

## Quick Start with Docker

### 1. Clone the repository

```bash
git clone <repository-url>
cd MaxWay
```

### 2. Set up environment variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and update the values, especially:
- `SECRET_KEY`: Generate a new secret key for production
- `DEBUG`: Set to `False` in production
- Database credentials

### 3. Build and run with Docker

```bash
docker-compose up --build -d
```

This will:
- Build the Docker image
- Start PostgreSQL database
- Run migrations automatically
- Collect static files
- Start the application on port 8002

### 4. Access the application

- **Main Application**: http://localhost:8002
- **Admin Panel**: http://localhost:8002/admin

### 5. Create a superuser (optional)

```bash
docker-compose exec web python manage.py createsuperuser
```

## Local Development Setup

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Update `MaxWay/settings.py` with your PostgreSQL credentials, then:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Collect static files

```bash
python manage.py collectstatic
```

### 5. Run the development server

```bash
python manage.py runserver
```

The application will be available at http://localhost:8000

## Project Structure

```
MaxWay/
├── dashboard/          # Admin dashboard app
├── food/              # Customer-facing food app
├── MaxWay/            # Project settings
├── media/             # User-uploaded files
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── Dockerfile         # Docker image configuration
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt   # Python dependencies
└── manage.py          # Django management script
```

## Docker Commands

### Start containers
```bash
docker-compose up -d
```

### Stop containers
```bash
docker-compose down
```

### View logs
```bash
docker-compose logs -f web
docker-compose logs -f db
```

### Run Django commands
```bash
# Create superuser
docker-compose exec web python manage.py createsuperuser

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic

# Access Django shell
docker-compose exec web python manage.py shell
```

### Rebuild after changes
```bash
docker-compose up --build -d
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | (required) |
| `DEBUG` | Debug mode | `True` |
| `DATABASE_NAME` | PostgreSQL database name | `maxway_db` |
| `DATABASE_USER` | PostgreSQL username | `maxway_admin` |
| `DATABASE_PASSWORD` | PostgreSQL password | `root` |
| `DATABASE_HOST` | Database host | `db` (Docker) or `localhost` (local) |
| `DATABASE_PORT` | Database port | `5432` |

## Production Deployment

⚠️ **Important**: Before deploying to production:

1. Set `DEBUG=False` in your `.env` file
2. Generate a strong `SECRET_KEY`:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
3. Change database credentials to strong passwords
4. Update `ALLOWED_HOSTS` in `settings.py` with your domain
5. Set up a reverse proxy (Nginx) for better security
6. Configure SSL/TLS certificates for HTTPS
7. Set up database backups

For detailed deployment instructions, see [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

See [LICENSE](LICENSE) file for details.

## Support

For issues and questions, please open an issue on GitHub.
