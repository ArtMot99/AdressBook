from django.urls import path
from address import views


urlpatterns = [
    path('', views.all_contacts_view, name='main_menu'),
    path('<int:pk>', views.one_contact_view, name='info'),
]
