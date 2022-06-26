from django.urls import path, include
from address import views


contact_url = [
    path('', views.contact_view, name='info'),
    path('update/', views.contact_update_inline_view, name='update'),
]


urlpatterns = [
    path('', views.contact_list_view, name='main_menu'),
    path('create/', views.contact_create_inline_view, name='create'),
    path('<slug:slug>/', include(contact_url)),
    path('accounts/', include('django.contrib.auth.urls')),
]
