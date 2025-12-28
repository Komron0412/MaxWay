# Docker Deployment Guide for MaxWay

This guide will help you deploy the MaxWay Django project using Docker and Docker Compose.

## Prerequisites

- Docker installed on your system ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed (usually comes with Docker Desktop)

## Quick Start

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/MaxWay
   ```

2. **Create a `.env` file (optional, but recommended):**
   ```bash
   # Copy the example and edit as needed
   # SECRET_KEY=your-secret-key-here
   # DEBUG=False
   # DATABASE_NAME=maxway_db
   # DATABASE_USER=maxway_admin
   # DATABASE_PASSWORD=root
   # DATABASE_HOST=db
   # DATABASE_PORT=5432
   ```
   
   Note: If you don't create a `.env` file, the default values from `docker-compose.yml` will be used.

3. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```
   
   This will:
   - Build the Docker image for the Django application
   - Start the PostgreSQL database container
   - Run database migrations
   - Collect static files
   - Start the Gunicorn server

4. **Access the application:**
   - Open your browser and navigate to: `http://localhost:8002`
   - Admin panel: `http://localhost:8002/admin`

## Common Commands

### Start containers in detached mode (background):
```bash
docker-compose up -d
```

### Stop containers:
```bash
docker-compose down
```

### Stop containers and remove volumes (⚠️ This will delete your database):
```bash
docker-compose down -v
```

### View logs:
```bash
docker-compose logs -f
```

### View logs for a specific service:
```bash
docker-compose logs -f web
docker-compose logs -f db
```

### Run Django management commands:
```bash
# Create a superuser
docker-compose exec web python manage.py createsuperuser

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic

# Access Django shell
docker-compose exec web python manage.py shell
```

### Rebuild after code changes:
```bash
docker-compose up --build
```

## Project Structure

```
MaxWay/
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── .dockerignore          # Files to ignore in Docker build
├── manage.py              # Django management script
├── MaxWay/                # Django project settings
├── dashboard/             # Dashboard app
├── food/                  # Food app
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded media files
└── templates/             # HTML templates
```

## Services

### Web Service
- **Image**: Built from `Dockerfile`
- **Port**: 8002 (mapped from container port 8000)
- **Command**: Runs migrations, collects static files, and starts Gunicorn
- **Volumes**: 
  - Project code (for development)
  - Static files volume
  - Media files volume

### Database Service
- **Image**: `postgres:15-alpine`
- **Port**: 5432
- **Database**: `maxway_db`
- **User**: `maxway_admin`
- **Password**: `root` (⚠️ Change this in production!)
- **Volume**: Persistent PostgreSQL data storage

## Environment Variables

You can configure the application using environment variables in a `.env` file or directly in `docker-compose.yml`:

- `SECRET_KEY`: Django secret key (required for production)
- `DEBUG`: Set to `False` in production
- `DATABASE_NAME`: PostgreSQL database name
- `DATABASE_USER`: PostgreSQL username
- `DATABASE_PASSWORD`: PostgreSQL password
- `DATABASE_HOST`: Database host (use `db` for Docker Compose)
- `DATABASE_PORT`: Database port (default: 5432)

## Production Deployment

⚠️ **Important**: Before deploying to production, make sure to:

1. **Set `DEBUG=False`** in your `.env` file or environment variables
2. **Generate a strong `SECRET_KEY`**:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
3. **Change database credentials** to strong passwords
4. **Set `ALLOWED_HOSTS`** in `settings.py` to your domain
5. **Use a reverse proxy** (like Nginx) for better security and performance
6. **Set up SSL/TLS certificates** for HTTPS
7. **Configure proper backup strategy** for the database

## Troubleshooting

### Database connection errors:
- Make sure the database service is healthy: `docker-compose ps`
- Check database logs: `docker-compose logs db`
- Verify environment variables are set correctly

### Static files not loading:
- Run: `docker-compose exec web python manage.py collectstatic --noinput`
- Check that `STATIC_ROOT` is set correctly in `settings.py`

### Port already in use:
- Change the port mapping in `docker-compose.yml`:
  ```yaml
  ports:
    - "8003:8000"  # Use port 8003 instead of 8002
  ```

### Permission errors:
- On Linux, you may need to fix file permissions:
  ```bash
  sudo chown -R $USER:$USER .
  ```

## Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

