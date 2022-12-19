from django.urls import path
from .views import (ProductCreateView, ProductDeleteView,
                    ProductDetailView, ProductListView, ProductUpdateView, CategoryCreateView, CategoryDetailView, CategoryDeleteView, CategoryListView, CategoryUpdateView)

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/<slug>/detail/', ProductDetailView.as_view(), name='detail'),
    path('product/<slug>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('product/<slug>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/category/create/',
         CategoryCreateView.as_view(), name='category'),
    path('product/category/<slug>/detail/',
         CategoryDetailView.as_view(), name='category-detail'),
    path('product/category/<slug>/delete/',
         CategoryDeleteView.as_view(), name='category-delete'),
    path('product/category/', CategoryListView.as_view(), name='category-list'),
    path('product/category/<slug>/update/',
         CategoryUpdateView.as_view(), name='category-update'),



]
