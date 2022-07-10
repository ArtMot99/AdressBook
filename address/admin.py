from django.contrib import admin
from address.models import Contact, Phone, Email, Comment

admin.site.register(Contact)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Comment)
