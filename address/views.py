from django.shortcuts import render, get_object_or_404
from .models import Contact, Phone, Email


def contact_list_view(request):
    context = {}
    qs_contact = Contact.objects.all()
    context['contact'] = qs_contact
    return render(request, 'address/index.html', context)


def contact_view(request, pk):
    context = {}
    obj = get_object_or_404(Contact, pk=pk)
    context['contact'] = obj

    return render(request, 'address/info_about_contact.html', context)
