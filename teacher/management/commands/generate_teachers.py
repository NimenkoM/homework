import random

from django.core.management import BaseCommand

from faker import Faker

from teacher.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100)

    def handle(self, count, **options):
        faker = Faker()

        teachers = [
            Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(20, 55)
            )
            for _ in range(count)

        ]
        Teacher.objects.bulk_create(teachers)
        print('it works')
