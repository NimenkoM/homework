from django.db import models
# flake8: noqa

class Student(models.Model):
    id = models.BigAutoField
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_info(self):
        return f'{self.id}{self.first_name} {self.last_name}, age={self.age}'
