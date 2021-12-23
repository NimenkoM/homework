from django import forms

from group.models import Group


class GroupForm(forms.ModelForm):

    def clean(self):
        group_size = self.cleaned_data['group_size']

        if group_size < 6:
            self.add_error('group_size', 'Too small size of group')
        if group_size > 20:
            self.add_error('group_size', 'Too large size of group')

    class Meta:
        model = Group
        fields = (
            'group_name',
            'group_direction',
            'group_size',
        )
