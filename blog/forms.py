
from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'The title'})
    )
    class Meta:
        model = Article
        fields = [
            'title',
            'tags',
            'summary'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if title == '':
            raise forms.ValidationError('This is not a valid title')
        return title
