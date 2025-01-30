from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description']
        widgets = {
            'description':forms.Textarea(attrs={'rows':10,'cols':80})
        }
        labels = {
            'name':'Nom du produit',
            'price':'Prix du produit',
            'description':'Description du produit'
        }
        help_texts = {
            'name':'Nom du produit',
            'price':'Prix du produit',
            'description':'Description du produit'
        }
        error_messages = {
            'name':{
                'required':'Le nom du produit est obligatoire',
                'max_length':'Le nom du produit doit faire moins de 100 caractères'
            },
            'price':{
                'required':'Le prix du produit est obligatoire',
                'max_digits':'Le prix du produit doit faire moins de 10 chiffres après la virgule',
                'decimal_places':'Le prix du produit doit avoir au moins 2 décimales'
            },
            'description':{
                'required':'La description du produit est obligatoire',
                'max_length':'La description du produit doit faire moins de 100 caractères'
            }
        }   
        