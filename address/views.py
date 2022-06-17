from django.shortcuts import render, get_object_or_404
from .models import Contact, Phone, Email


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'index.html', context)


def contact_view(request, pk):
    context = {}
    obj = get_object_or_404(Contact, pk=pk)
    context['contact'] = obj
    qs_phone = Phone.objects.all()
    context['phone'] = qs_phone
    qs_email = Email.objects.all()
    context['email'] = qs_email

    return render(request, 'info_about_contact.html', context)
