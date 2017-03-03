"""AppConfig for demo."""

from django.apps import AppConfig


class DemoConfig(AppConfig):
    """App configuration."""

    name = "modoboa_demo"
    verbose_name = "Modoboa demo"

    def ready(self):
        from . import handlers
