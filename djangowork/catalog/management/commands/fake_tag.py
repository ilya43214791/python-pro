from django.core.management.base import BaseCommand
from catalog.models import Tag
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help_text = 'fill db for Tags'

    def handle(self, *args, **options):
        for i in range(10):
            Tag.objects.create(name=fake.name())

    print("Tags is create")