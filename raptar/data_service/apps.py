from django.apps import AppConfig


class DataServiceConfig(AppConfig):
    name = 'raptar.data_service'

    def ready(self):
        import raptar.data_service.signals
