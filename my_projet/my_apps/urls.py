from django.urls import path
from my_apps import views

urlpatterns = [
    path('', views.article_create, name='article_create'),
    path('list', views.article_list, name='article_list'),
    path('detail/<str:pk>/', views.article_detail, name='article_detail'),
    path('update/<str:pk>/', views.article_update, name='article_update'),
    path('delete/<str:pk>/', views.article_delete, name='article_delete'),
]