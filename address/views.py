from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import CreateContactModelForm
from .models import Contact


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


def create_contact_modelform_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreateContactModelForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return HttpResponseRedirect(reverse('main_menu'))
        else:
            return render(request, 'address/create_contact.html', context={'form': form})
    else:
        form = CreateContactModelForm()
    return render(request, 'address/create_contact.html', context={'form': form})

