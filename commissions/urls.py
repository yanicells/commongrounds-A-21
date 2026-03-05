from django.urls import path

from . import views

app_name = 'commissions'

urlpatterns = [
    path('requests', views.request_list, name='request-list'),
    path('request/<int:pk>', views.request_detail, name='request-detail'),
]
