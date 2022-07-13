from django.urls import path, include
from address import views


contact_url = [
    path('', views.ContactDetailView.as_view(), name='info'),
    path('update/', views.UpdateContactView.as_view(), name='update'),
    path('delete/', views.DeleteContactView.as_view(), name='delete'),
    path('comment/', views.CreateComment.as_view(), name='create_comment'),
]


urlpatterns = [
    path('', views.AllContactListView.as_view(), name='main_menu'),
    path('personal_contacts/', views.OwnContactListView.as_view(), name='personal_contacts'),
    path('create/', views.CreateContactView.as_view(), name='create'),
    path('<slug:slug>/', include(contact_url)),
    path('accounts/register', views.RegistrationView.as_view(), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
]
