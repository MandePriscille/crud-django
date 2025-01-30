from django.shortcuts import get_object_or_404, redirect, render

from my_apps.models import Article
from .forms import ArticleForm


# a. Créer (Create)
def article_create(request):
    form = ArticleForm()
    if request.method == 'POST':
         form = ArticleForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('article_list')
         else:
            form = ArticleForm()
    return render(request,'article/article_create.html',{'form':form})


def article_list(request):
    articles = Article.objects.all()
    return render(request,'article/article_list.html',{'article':articles})


def article_detail(request,pk): 
    article = get_object_or_404(Article,pk=pk)
    return render(request,'article/article_detail.html',{'article':article})


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
        else:
            form = ArticleForm(instance=article)
    return render(request,'article/article_create.html',{'form':form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'article/confirmation.html', {'article': article})