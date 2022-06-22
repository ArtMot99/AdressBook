from django.contrib.auth import get_user_model
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    old = models.PositiveIntegerField(verbose_name='Возраст')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(null=False, default='')

    class Meta:
        pass

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_number = models.CharField(max_length=12)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'Phone: {self.phone_number} | Name: {self.contact}'


class Email(models.Model):
    email_address = models.EmailField(max_length=100)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'Email: {self.email_address} | Name: {self.contact}'
