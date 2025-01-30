from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('',ProductListView.as_view(),name='product_list'),
    path('detail/<str:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('create/',ProductCreateView.as_view(),name='product_create'),    
    path('<str:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
    path('<str:pk>/delete/',ProductDeleteView.as_view(),name='product_delete'),
]