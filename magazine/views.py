from django.shortcuts import render

# landing page view
def landingPage(request):
    context = {}
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

# registration
def reg(request):
    context = {}
    return render(request, 'accounts/reg.html', context)

# login
def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)