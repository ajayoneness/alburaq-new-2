from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pages'
    verbose_name = 'Pages'

    def ready(self):
        from .bootstrap import sync_default_services_safe

        post_migrate.connect(sync_default_services_safe, sender=self)
        # Also attempt on startup so existing projects get defaults without extra steps.
        sync_default_services_safe()
