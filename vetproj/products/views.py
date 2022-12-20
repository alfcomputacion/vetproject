from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from .models import Product, Category
from .forms import ProductForm

# Create your views here.


class ProductCreateView(CreateView):
    model = Product
    # fields = ['prod_name', 'description', 'category',
    #           'stock', 'buy_price', 'sell_price']
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ['prod_name', 'description', 'category',
    #           'stock', 'buy_price', 'sell_price']
    form_class = ProductForm
# Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ['category']


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('products:category-list')


class CategoryDetailView(DetailView):
    model = Category


class CategoryListView(ListView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['category']
