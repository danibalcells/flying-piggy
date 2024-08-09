from django.apps import AppConfig

class FlyingPiggyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flying_piggy_app'

    def ready(self):
        import flying_piggy_app.signals  # Import the signals