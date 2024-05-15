from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='имя', help_text='Введите своё имя')
    age = forms.CharField(label = 'возраст', help_text='Введите свой возраст')