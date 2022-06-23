from django.urls import path, include
from address import views


contact_url = [
    path('', views.contact_view, name='info'),
    path('update/', views.update_contact_modelform_view, name='update'),
]


urlpatterns = [
    path('', views.contact_list_view, name='main_menu'),
    path('<int:pk>/', include(contact_url)),
    path('create/', views.contact_create_inline_view, name='create'),
]
