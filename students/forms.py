from django import forms

from students.models import Student


class StudentForm(forms.ModelForm):

    def clean(self):
        age = self.cleaned_data['age']

        if age < 5:
            self.add_error('age', 'Too small age for being a student')
        if age > 18:
            self.add_error('age', 'Too old for being a student')

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
        )
