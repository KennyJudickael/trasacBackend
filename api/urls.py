from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('transactions/', views.TransactionListCreateView().as_view()),
    path('transactions/<uuid:id>/', views.TransactionRetrieveUpdateDestroyView().as_view()),
]
