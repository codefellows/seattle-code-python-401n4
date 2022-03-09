from django.urls import path
from .views import ThingsListView, ThingsDetailView, ThingsCreateView, ThingsUpdateView, ThingsDeleteView

urlpatterns = [
    path('', ThingsListView.as_view(), name='things_list'),
    path('<int:pk>/', ThingsDetailView.as_view(), name='things_detail'),
    path('create/', ThingsCreateView.as_view(), name='things_create'),
    path('<int:pk>/update/', ThingsUpdateView.as_view(), name='things_update'),
    path('<int:pk>/delete/', ThingsDeleteView.as_view(), name='things_delete'),
]