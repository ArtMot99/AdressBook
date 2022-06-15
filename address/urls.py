from django.urls import path
from address import views


urlpatterns = [
    path('', views.index, name='main_menu'),
    path('<int:pk>', views.description_contact, name='primery_key'),
]
