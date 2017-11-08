from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def book(request):
    return render(request, 'book.html')

def ideas(request):
    return render(request, 'ideas.html')

def contact(request):
    return render(request, 'contact.html')
