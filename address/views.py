from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .forms import CreateContactModelForm, ContactEmailFormSet, \
    ContactPhoneFormSet, ContactPhoneForUpdate, ContactEmailForUpdate, UserRegistrationForm, CommentForm
from .models import Contact, Comment


# def contact_list_view(request):
#     context = {}
#     qs_contact = Contact.objects.all()
#     context['contact'] = qs_contact
#     return render(request, 'address/index.html', context)
# def contact_view(request, slug):
#     obj = get_object_or_404(Contact, slug=slug)
#     context = {
#         'contact': obj,
#     }
#     if request.method == 'POST':
#         obj.delete()
#         return HttpResponseRedirect(reverse('main_menu'))
#     else:
#         return render(request, 'address/info_about_contact.html', context)


# def contact_update_inline_view(request, slug):
#     obj = get_object_or_404(Contact, slug=slug)
#     if request.method == 'POST':
#         form = CreateContactModelForm(data=request.POST, instance=obj)
#         phone_form = ContactPhoneForUpdate(data=request.POST, instance=obj)
#         email_form = ContactEmailForUpdate(data=request.POST, instance=obj)
#         if form.is_valid() and phone_form.is_valid() and email_form:
#             form.save()
#             phone_form.save()
#             email_form.save()
#             return HttpResponseRedirect(reverse('info', kwargs={'slug': slug}))
#         else:
#             return render(request, 'address/update_contact.html', context={'form': form,
#                                                                            'phone_form': phone_form,
#                                                                            'email_form': email_form})
#     else:
#         form = CreateContactModelForm(instance=obj)
#         phone_form = ContactPhoneForUpdate(instance=obj)
#         email_form = ContactEmailForUpdate(instance=obj)
#     return render(request, 'address/update_contact.html', context={'form': form,
#                                                                    'phone_form': phone_form,
#                                                                    'email_form': email_form})


# def contact_create_inline_view(request):
#     if request.method == 'POST':
#         form = CreateContactModelForm(request.POST)
#         contact_phone = ContactPhoneFormSet(request.POST)
#         contact_email = ContactEmailFormSet(request.POST)
#         if form.is_valid() and contact_phone.is_valid() and contact_email.is_valid():
#             contact = form.save(commit=False)
#             contact.user = request.user
#             contact.save()
#             contact_phone.instance = contact
#             contact_phone.save()
#             contact_email.instance = contact
#             contact_email.save()
#             return HttpResponseRedirect(reverse('main_menu'))
#         else:
#             return render(request, 'address/create_contact.html', {'form': form,
#                                                                    'inlineformset': contact_phone,
#                                                                    'inline': contact_email})
#     else:
#         form = CreateContactModelForm()
#         contact_phone = ContactPhoneFormSet()
#         contact_email = ContactEmailFormSet()
#         return render(request, 'address/create_contact.html', {'form': form,
#                                                                'inlineformset': contact_phone,
#                                                                'inline': contact_email})

# FromView
# def registration_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             return HttpResponseRedirect(reverse('main_menu'))
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {'form': form})


class ContactListView(ListView):
    # Указываем модель
    model = Contact
    # Указываем используемый шаблон
    template_name = 'address/index.html'
    # Имя при генерации шаблона, вместо object_list(общее имя для всех обьектов)
    context_object_name = 'contact'
    paginate_by = 10


class ContactDetailView(SingleObjectMixin, ListView):
    model = Comment
    template_name = 'address/info_about_contact.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Contact.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = self.object
        return context

    def get_queryset(self):
        return self.object.comment_set.all()


class CreateContactView(CreateView):
    model = Contact
    template_name = 'address/create_contact.html'
    form_class = CreateContactModelForm
    success_url = reverse_lazy('main_menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            contact_phone = ContactPhoneFormSet(self.request.POST)
            contact_email = ContactEmailFormSet(self.request.POST)
        else:
            contact_phone = ContactPhoneFormSet()
            contact_email = ContactEmailFormSet()
        context.update(
            {
                'inlineformset': contact_phone,
                'inline': contact_email
            }
        )
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        contact_phone = ContactPhoneFormSet(self.request.POST)
        contact_email = ContactEmailFormSet(self.request.POST)
        if contact_email.is_valid() and contact_phone.is_valid():
            self.obj = form.save()
            contact_email.instance = self.obj
            contact_phone.instance = self.obj
            contact_email.save()
            contact_phone.save()
        else:
            return self.form_invalid(form)

        return super().form_valid(form)


# todo [ UserPassesTestMixin ] можно дать права доступа с помощью миксина и метода (test_func)
class UpdateContactView(UpdateView):
    template_name = 'address/update_contact.html'
    model = Contact
    form_class = CreateContactModelForm
    success_url = reverse_lazy('main_menu')

    # def test_func(self):
    #     return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            contact_phone = ContactPhoneForUpdate(self.request.POST, instance=self.object)
            contact_email = ContactEmailForUpdate(self.request.POST, instance=self.object)
        else:
            contact_phone = ContactPhoneForUpdate(instance=self.object)
            contact_email = ContactEmailForUpdate(instance=self.object)
        context.update(
            {
                'inlineformset': contact_phone,
                'inline': contact_email
            }
        )
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        contact_phone = ContactPhoneForUpdate(self.request.POST, instance=self.object)
        contact_email = ContactEmailForUpdate(self.request.POST, instance=self.object)
        if contact_email.is_valid() and contact_phone.is_valid():
            form.save()
            contact_email.save()
            contact_phone.save()
        else:
            return self.form_invalid(form)

        return super().form_valid(form)


class DeleteContactView(DeleteView):
    model = Contact
    success_url = reverse_lazy('main_menu')
    template_name = 'address/contact_delete.html'


class RegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = '../templates/registration/register.html'

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('main_menu'))
        else:
            return self.form_invalid(form)


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'address/form_for_comment.html'

    def get_success_url(self):
        return reverse_lazy('info', kwargs={'slug': self.kwargs['slug']})

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        contact = get_object_or_404(Contact, slug=self.kwargs['slug'])
        f.contact = contact
        f.save()
        return super().form_valid(form)
