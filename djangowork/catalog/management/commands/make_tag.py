import random
import uuid
from django.core.management.base import BaseCommand
from catalog.models import Tag, Good, Category, ItemsDecor
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help_text = 'Tags for each models'

    def handle(self, *args, **options):
        for i in range(5):
            goods = Good.objects.create(
                name=fake.company(),
                description=fake.text(),
                price=fake.uniform(10, 1000),
                active=fake.boolen(),
                category=Category.objects.first(),
            )
            goods.tags.set(Tag.objects.all()[:3])