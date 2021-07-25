from django.shortcuts import render
from .models import Banner
# Create your views here.
def banners(request):
    banner=Banner.objects.all()[:4]
    return render(request,'index.html',{'banner':banner})