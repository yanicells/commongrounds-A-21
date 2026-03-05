from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('requests', CommissionListView.as_view(), name='list_view'),
    path('request/<int:pk>', CommissionDetailView.as_view(), name='detail_view')
]

app_name = 'commissions'