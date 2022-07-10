# Generated by Django 4.0.5 on 2022-07-10 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0003_alter_email_email_address_alter_phone_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.contact', verbose_name='Для контакта'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
