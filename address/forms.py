from django import forms


class CreateContact(forms.Form):
    name = forms.CharField(required=True, max_length=15, min_length=3, label='Имя')
    surname = forms.CharField(required=True, max_length=15, min_length=3, label='Фамилия')
    patronymic = forms.CharField(required=True, max_length=15, min_length=3, label='Отчество')
    old = forms.IntegerField(required=True, label='Возраст')
    phone = forms.IntegerField(label='Номер телефона')
    email = forms.EmailField(max_length=30)