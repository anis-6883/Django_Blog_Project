from django.apps import AppConfig


class AppLoginConfig(AppConfig):
    name = 'App_Login'

    def ready(self):
        import App_Login.signals
