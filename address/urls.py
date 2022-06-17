from django.urls import path
from address import views


urlpatterns = [
    path('', views.contact_list_view, name='main_menu'),
    path('<int:pk>', views.contact_view, name='info'),
]
