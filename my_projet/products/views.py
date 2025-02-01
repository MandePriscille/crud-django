import logging
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.views import View
from django.contrib import messages

from .forms import ProductForm, AchatForm
from .models import Achat, Product 

logger = logging.getLogger(__name__)
# Utilisation des vues base sur les classes

class ProductCreateView(CreateView):
    model = Product     # Modèle à utiliser
    form_class = ProductForm        # Formulaire à utiliser
    template_name = 'products/product_form.html'        # Template pour afficher le formulaire
    success_url = reverse_lazy('product_list')       # URL de redirection après la création


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
    success_url = reverse_lazy('product_list')

    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


# Implementation des mail lors de l'achat d'un produit

class AcheterProductView(View):
    template_name = 'products/acheter_product.html'
    confirmation_template_name = 'products/acheter_product_confirmation.html'

    def get(self, request, product_id):
        # Afficher le formulaire d'achat
        product = get_object_or_404(Product, id=product_id)
        return render(request, self.template_name, {'product':product})
    

    def post(self, request, product_id):
         # Traiter l'achat
        product = get_object_or_404(Product, id=product_id)
        utilisateur = request.user

        achat = Achat(user=utilisateur, product=product)
        achat.save()

     # Envoyer un e-mail de confirmation

        subject = f"Confirmation d'achat de {product.name}"
        message = f" Bonjour {utilisateur.first_name}, votre achat de {product.name} a bien été effectué."
        from_email = 'settings.EMAIL_HOST_USER'
        recipient_list = [utilisateur.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            logger.info(f"Email de confirmation envoye a l'utilisateur {utilisateur.first_name} pour le produit {product.name}")
        except Exception as e:
            logger.error(f"erreur lors de l'envoie des email a l'utilisateur {utilisateur.email: {e}}")

        return render(request, self.confirmation_template_name, {'product':product})



# utilisation des signaux pour envoyer les mails

class AchatView(TemplateView):
    template_name ='achat/achat.html'
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)

       try:
           # Récupération de tous les produits
           products = Product.objects.all()
           context['products'] = products

           # Initialisation du formulaire d'achat
           context['form'] = AchatForm()

       except Exception as e:
           logger.error(f"Erreur lors de la récupération des données: {e}")
           messages.error(self.request, "Une erreur est survenue lors du chargement des achats.")

       return context

    def post(self, request, *args, **kwargs):
        """ Traite la soumission du formulaire d'achat """
        form = AchatForm(request.POST)

        if form.is_valid():
            try:
                # Créer l'achat sans l'enregistrer immédiatement
                achat = form.save(commit=False)

                # Vérifier si l'utilisateur est authentifié
                if request.user.is_authenticated:
                    achat.user = request.user
                    achat.save()

                    # Envoyer l'e-mail de confirmation
                    self.envoyer_email_confirmation(achat)

                    messages.success(request, "Achat effectué avec succès !")
                else:
                    messages.error(request, "Vous devez être connecté pour effectuer un achat.")

            except Exception as e:
                logger.error(f"Erreur lors de l'achat: {e}")
                messages.error(request, "Une erreur est survenue lors de l'achat.")
        
        else:
            messages.error(request, "Le formulaire contient des erreurs.")

        return redirect('achat')
