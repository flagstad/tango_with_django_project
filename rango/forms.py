from django import forms
from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter the category name')
    # likes = forms.IntegerField(help_text='Please enter the amount of likes', initial=0)
    # views = forms.IntegerField(help_text='Please enter the amount of views', initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name', )

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the page title')
    url = forms.URLField(max_length=200, help_text='Please enter the URL of the page')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)

    class Meta:
        model = Page
        exclude = ('category', )