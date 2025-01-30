from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product

# Utilisation des vues base sur les classes

class ProductCreateView(CreateView):
    model = Product     # Modèle à utiliser
    form_class = ProductForm        # Formulaire à utiliser
    template_name = 'products/product_form.html'        # Template pour afficher le formulaire
    success_url = reverse_lazy('products:product_list')       # URL de redirection après la création


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'      # Template pour afficher la liste
    context_object_name = 'products'        # Nom de la variable dans le template


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'      # Template pour afficher le détail
    context_object_name = 'product'        # Nom de la variable dans le template


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')

    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')
