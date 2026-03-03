from django.urls import path

from . import views

app_name = 'merchstore'

urlpatterns = [
    path('items', views.item_list, name='item-list'),
    path('item/<int:pk>', views.item_detail, name='item-detail'),
]
