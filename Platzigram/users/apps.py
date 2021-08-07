"""user app configuration"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """user app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Users'
