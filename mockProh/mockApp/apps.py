from django.apps import AppConfig


class MockappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mockApp'
