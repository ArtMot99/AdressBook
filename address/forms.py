from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, PasswordInput

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


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords don\'t match')
        return cd['password2']

