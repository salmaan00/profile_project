from django.apps import AppConfig


class BioAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bio_app'


    def ready(self):
        import bio_app.signals


