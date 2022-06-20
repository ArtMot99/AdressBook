from django import forms
from .models import Contact, Phone, Email


class CreateContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'patronymic', 'old']


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_number']


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_address']