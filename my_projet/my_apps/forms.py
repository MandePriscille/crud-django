from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['titre','contenu']
        widgets={
            'contenu':forms.Textarea(attrs={'rows':10,'cols':80})
        }
        labels={
            'titre':'Titre de l\'article',
            'contenu':'Contenu de l\'article'
        }

