from django.shortcuts import render, get_object_or_404
from .models import * 

# landing page view
def landingPage(request):
    article = Article.objects.all()
    category = Category.objects.all()
    context = {'article':article, 'category':category}
    return render(request, 'magazine/index.html', context)

# about page view
def aboutPage(request):
    context = {}
    return render(request, 'magazine/about.html', context)

# article page view
def articlepage(request):
    context = {}
    return render(request, 'magazine/article.html', context)

# category list page view
def categorylist(request):
    context = {}
    return render(request, 'magazine/category_post_list.html', context)

# price page view
def pricepage(request):
    context = {}
    return render(request, 'magazine/pricing.html', context)

# contact
def contactpage(request):
    context = {}
    return render(request, 'magazine/contact.html', context)

# magazine
def magpage(request):
    context = {}
    return render(request, 'magazine/magazine.html', context)

# registration
def reg(request):
    context = {}
    return render(request, 'accounts/reg.html', context)

# login
def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)