from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CreateContact
from .models import Contact, Phone, Email


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'address/index.html', context)


def contact_view(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    phone_numbers = [number.phone_number for number in obj.phone_set.all()]
    emails_address = [email.email_address for email in obj.email_set.all()]
    context = {
        'contact': obj,
        'phone_numbers': phone_numbers,
        'emails': emails_address,
    }

    return render(request, 'address/info_about_contact.html', context)


def create_contact_view(request):
    if request.method == 'POST':
        form = CreateContact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            old = form.cleaned_data['old']
            contact = Contact(name=name, surname=surname, patronymic=patronymic, old=old)
            contact.user = request.user
            contact.save()
            return HttpResponseRedirect(reverse('main_menu'))
        else:
            return render(request, 'address/create_contact.html', context={'form': form})
    else:
        form = CreateContact()
    return render(request, 'address/create_contact.html', context={'form': form})
