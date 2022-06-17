from django.shortcuts import render, get_object_or_404
from .models import Contact, Phone, Email


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'address/index.html', context)


def contact_view(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    phone_numbers = []
    emails_address = []
    for number in obj.phone_set.all():
        phone_numbers.append(number.phone_number)
    for email in obj.email_set.all():
        emails_address.append(email.email_address)
    context = {
        'contact': obj,
        'phone_numbers': phone_numbers,
        'emails': emails_address,
    }

    return render(request, 'address/info_about_contact.html', context)
