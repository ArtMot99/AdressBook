from django import forms


class CreateContact(forms.Form):
    name = forms.CharField(max_length=15, min_length=3, label='Имя')
    surname = forms.CharField(max_length=15, min_length=3, label='Фамилия')
    patronymic = forms.CharField(max_length=15, min_length=3, label='Отчество')
    old = forms.IntegerField(max_length=15, min_length=3, label='Возраст')
