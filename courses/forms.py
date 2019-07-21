
from django import forms

from .models import Course


class CourseModelForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
    )
    class Meta:
        model = Course
        fields = [
            'title',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if title == '':
            raise forms.ValidationError('This is not a valid title')
        return title
