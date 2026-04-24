from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.admin_logout, name='logout'),
    path('add/', views.add_employee),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('view/', views.view_employees, name='view_employees'),
    path('delete/<int:id>/', views.delete_employee),
]