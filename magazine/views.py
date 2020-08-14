from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Issue, Magazine, Category, Article

# landing page view
def landingPage(request):
    article_list = Article.objects.filter()
    context = {}
    return render(request, 'magazine/index.html', {'article_list': article_list})

# about page view
def aboutPage(request):
    context = {}
    return render(request, 'magazine/about.html', context)

# Article View

