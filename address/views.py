from django.shortcuts import render
from .models import Contact, Phone, Email


def index(request):
    context = {}
    qs_contact = Contact.objects.all()
    qs_phone = Phone.objects.all()
    qs_email = Email.objects.all()
    context['contact'] = qs_contact
    context['phone_number'] = qs_phone
    context['email'] = qs_email

    return render(request, 'index.html', context)


def description_contact(request, pk):
    obj = Contact.objects.get(pk=pk)

    return render(request, 'info_about_contact.html', {'contact': obj})
