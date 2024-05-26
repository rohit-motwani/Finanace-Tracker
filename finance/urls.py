# finance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_transaction, name='add-transaction'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit-transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('report/', views.report, name='report'),
     path('monthly_report/', views.monthly_report, name='monthly_report'),
]
