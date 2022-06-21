from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import CreateContactModelForm, PhoneForm
from .models import Contact


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'address/index.html', context)


def contact_view(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    # phone_numbers = [number.phone_number for number in obj.phone_set.all()]
    # emails_address = [email.email_address for email in obj.email_set.all()]
    context = {
        'contact': obj,
        # 'phone_numbers': phone_numbers,
        # 'emails': emails_address,
    }

    return render(request, 'address/info_about_contact.html', context)


def create_contact_modelform_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreateContactModelForm(request.POST)
        phone_form = PhoneForm(request.POST)
        if form.is_valid() and phone_form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            phone = phone_form.save(commit=False)
            phone.contact = contact
            phone.save()
            return HttpResponseRedirect(reverse('main_menu'))
        else:
            return render(request, 'address/create_contact.html', context={'form': form,
                                                                           'phone_form': phone_form})
    else:
        form = CreateContactModelForm()
        phone_form = PhoneForm()
    return render(request, 'address/create_contact.html', context={'form': form,
                                                                   'phone_form': phone_form})


def update_contact_modelform_view(request, pk, *args, **kwargs):
    obj = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = CreateContactModelForm(data=request.POST, instance=obj)
        phone_form = PhoneForm(data=request.POST, instance=obj.phone_set.first())
        if form.is_valid() and phone_form.is_valid():
            contact = form.save()
            phone = phone_form.save()
            return HttpResponseRedirect(reverse('info', kwargs={'pk': pk}))
        else:
            return render(request, 'address/create_contact.html', context={'form': form,
                                                                           'phone_form': phone_form})
    else:
        form = CreateContactModelForm(instance=obj)
        phone_form = PhoneForm(instance=obj.phone_set.first())
    return render(request, 'address/create_contact.html', context={'form': form,
                                                                   'phone_form': phone_form})


