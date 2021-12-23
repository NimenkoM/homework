
from django.core.management import BaseCommand


from teacher.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--first_name', type=str)
        parser.add_argument('--last_name', type=str)
        parser.add_argument('--age', type=int)

    def handle(self, *args, **options):
        teacher = Teacher.objects.all()
        if options.get('first_name'):
            teacher = teacher.filter(first_name=options.get('first_name'))
        if options.get('last_name'):
            teacher = teacher.filter(last_name=options.get('last_name'))
        if options.get('age'):
            teacher = teacher.filter(age=options.get('age'))
        print(teacher)
