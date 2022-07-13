from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from slugify import slugify
from address.managers import OwnContactQs, AllContactManager


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    old = models.PositiveIntegerField(verbose_name='Возраст')
    is_active = models.BooleanField(default=False, verbose_name='Общедоступный контакт')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(null=False, default='')
    photo = models.ImageField('Фотография', upload_to='address/photos', default='', blank=True)

    objects = models.Manager()
    general_contacts = AllContactManager()
    # для фильтрации
    personal_contacts = OwnContactQs().as_manager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.surname)
        super(Contact, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('info', args=[str(self.slug)])


class Phone(models.Model):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'Phone: {self.phone_number} | Name: {self.contact}'


class Email(models.Model):
    email_address = models.EmailField(max_length=100, verbose_name='Email адрес')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'Email: {self.email_address} | Name: {self.contact}'


class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(null=True, verbose_name='Комментарий')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Для контакта')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')

    class Meta:
        ordering = ('-create_at',)

    def __str__(self):
        return self.title
