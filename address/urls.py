from django.urls import path
from address import views


urlpatterns = [
    path('', views.contact_list_view, name='main_menu'),
    path('<int:pk>/', views.contact_view, name='info'),
    path('<int:pk>/update/', views.update_contact_modelform_view, name='update'),
    path('create/', views.create_contact_modelform_view, name='create'),

]
