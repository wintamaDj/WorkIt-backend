# WorkIt-backend
Backend for Software Engineering project "WorkIt"

# Dev Setup
Originally devoleped with Django with .venv
Recommend using .env for secrets
Generate your own secrets with this command:
> python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'