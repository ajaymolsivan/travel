from django.shortcuts import render
from banners.models import Banner

# Create your views here.
def home(request):
    banner = Banner.objects.all().order_by('-date')[:4]
    return render(request, 'index.html',{'banner':banner})


def about(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact.html')


def packages(request):
    return render(request, 'packages.html')


def blog(request):
    return render(request, 'blog.html')


def services(request):
    return render(request, 'services.html')

def terms(request):
    return render(request, 'terms.html')