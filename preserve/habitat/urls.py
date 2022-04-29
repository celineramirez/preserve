from django.urls import path
from . import views

urlpatterns = [
    path('ecosystems', views.post_list, name='post_list'),
    path('ecosystems/<int:pk>/', views.post_detail, name='post_detail'),
]