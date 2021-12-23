from django import forms

from teacher.models import Teacher


class TeacherForm(forms.ModelForm):

    def clean(self):
        age = self.cleaned_data['age']

        if age < 18:
            self.add_error('age', 'Too small age for being a teacher')
        if age > 65:
            self.add_error('age', 'Too old for being a teacher')

    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
        )
