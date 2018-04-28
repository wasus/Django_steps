from django.shortcuts import render

def home(request):

    return render(request, 'home/home.html', locals())

def about(request):

    return render(request, 'about/about.html', locals())
