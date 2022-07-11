from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        print('*'*100)
        print(app_name, app_module)
