from django import forms
from django.forms import inlineformset_factory

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


ContactPhoneFormSet = inlineformset_factory(Contact, Phone,
                                            form=PhoneForm,
                                            can_delete=False,
                                            extra=2)
ContactEmailFormSet = inlineformset_factory(Contact, Email,
                                            form=EmailForm,
                                            can_delete=False,
                                            extra=2,)
ContactPhoneForUpdate = inlineformset_factory(Contact, Phone,
                                              form=PhoneForm,
                                              can_delete=True,
                                              extra=2)
ContactEmailForUpdate = inlineformset_factory(Contact, Email,
                                              form=EmailForm,
                                              can_delete=True,
                                              extra=2)
