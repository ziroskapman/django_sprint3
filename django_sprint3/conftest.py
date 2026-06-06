import pytest
from django.core.management import call_command


@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    """Принудительно применить миграции перед тестами"""
    with django_db_blocker.unblock():
        call_command('makemigrations', 'blog')
        call_command('migrate')
