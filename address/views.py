from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import CreateContactModelForm, PhoneForm, EmailForm, ContactEmailFormSet, ContactPhoneFormSet
from .models import Contact


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'address/index.html', context)


def contact_view(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    context = {
        'contact': obj,
    }
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('main_menu'))
    else:
        return render(request, 'address/info_about_contact.html', context)


def update_contact_modelform_view(request, pk, *args, **kwargs):
    obj = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = CreateContactModelForm(data=request.POST, instance=obj)
        phone_form = PhoneForm(data=request.POST, instance=obj.phone_set.first())
        email_form = EmailForm(data=request.POST, instance=obj.email_set.first())
        if form.is_valid() and phone_form.is_valid() and email_form:
            form.save()
            phone_form.save()
            email_form.save()
            return HttpResponseRedirect(reverse('info', kwargs={'pk': pk}))
        else:
            return render(request, 'address/update_contact.html', context={'form': form,
                                                                           'phone_form': phone_form,
                                                                           'email_form': email_form})
    else:
        form = CreateContactModelForm(instance=obj)
        phone_form = PhoneForm(instance=obj.phone_set.first())
        email_form = EmailForm(instance=obj.email_set.first())
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
