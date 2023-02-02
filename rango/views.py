from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

# Create your views here.

def index(request):
    context_dict = {}

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict['categories'] = category_list

    most_viewed = Page.objects.order_by('-views').filter(views__gte=1)[:5]
    context_dict['pages'] = most_viewed

    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')