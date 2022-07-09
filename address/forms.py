from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, PasswordInput

from .models import Contact, Phone, Email


class CreateContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'patronymic', 'old']

    def clean_old(self):
        new_old = self.cleaned_data['old']
        if new_old < 18 or new_old > 100:
            raise ValidationError('Old must be > 18 and < 100!')
        return new_old

    def clean_name(self):
        new_name = self.cleaned_data['name']
        if not new_name[0].isupper():
            raise ValidationError('First letter in name must be upper!')
        return new_name

    def clean_surname(self):
        new_surname = self.cleaned_data['surname']
        if not new_surname[0].isupper():
            raise ValidationError('First letter in surname must be upper!')
        return new_surname

    def clean_patronymic(self):
        new_patro = self.cleaned_data['patronymic']
        if not new_patro[0].isupper():
            raise ValidationError('First letter in patronymic must be upper!')
        return new_patro


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_number']

    def clean_phone_number(self):
        phone_num = self.cleaned_data['phone_number']
        if not phone_num.isdigit() or len(phone_num) != 12:
            raise ValidationError('Phone number must have only digits and must have 12 symbols')
        return phone_num


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
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Passwords don\'t match')
        return cd['password2']

