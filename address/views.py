from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import CreateContactModelForm, ContactEmailFormSet, \
    ContactPhoneFormSet, ContactPhoneForUpdate, ContactEmailForUpdate
from .models import Contact


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'address/index.html', context)


def contact_view(request, slug):
    obj = get_object_or_404(Contact, slug=slug)
    context = {
        'contact': obj,
    }
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('main_menu'))
    else:
        return render(request, 'address/info_about_contact.html', context)


def contact_update_inline_view(request, slug):
    obj = get_object_or_404(Contact, slug=slug)
    if request.method == 'POST':
        form = CreateContactModelForm(data=request.POST, instance=obj)
        phone_form = ContactPhoneForUpdate(data=request.POST, instance=obj)
        email_form = ContactEmailForUpdate(data=request.POST, instance=obj)
        if form.is_valid() and phone_form.is_valid() and email_form:
            form.save()
            phone_form.save()
            email_form.save()
            return HttpResponseRedirect(reverse('info', kwargs={'slug': slug}))
        else:
            return render(request, 'address/update_contact.html', context={'form': form,
                                                                           'phone_form': phone_form,
                                                                           'email_form': email_form})
    else:
        form = CreateContactModelForm(instance=obj)
        phone_form = ContactPhoneForUpdate(instance=obj)
        email_form = ContactEmailForUpdate(instance=obj)
    return render(request, 'address/update_contact.html', context={'form': form,
                                                                   'phone_form': phone_form,
                                                                   'email_form': email_form})


def contact_create_inline_view(request):
    if request.method == 'POST':
        form = CreateContactModelForm(request.POST)
        contact_phone = ContactPhoneFormSet(request.POST)
        contact_email = ContactEmailFormSet(request.POST)
        if form.is_valid() and contact_phone.is_valid() and contact_email.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            contact_phone.instance = contact
            contact_phone.save()
            contact_email.instance = contact
            contact_email.save()
            return HttpResponseRedirect(reverse('main_menu'))
        else:
            return render(request, 'address/create_contact.html', {'form': form,
                                                                   'inlineformset': contact_phone,
                                                                   'inline': contact_email})
    else:
        form = CreateContactModelForm()
        contact_phone = ContactPhoneFormSet()
        contact_email = ContactEmailFormSet()
        return render(request, 'address/create_contact.html', {'form': form,
                                                               'inlineformset': contact_phone,
                                                               'inline': contact_email})
