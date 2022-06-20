from django import forms
from .models import Contact, Phone, Email


class CreateContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'patronymic', 'old']

