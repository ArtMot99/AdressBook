from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    obj = get_object_or_404(Contact, pk=pk)

    return render(request, 'info_about_contact.html', {'contact': obj})
