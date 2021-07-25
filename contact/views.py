from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm

from.models import Contact

def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Contact form saved succesfully! Contact back you soon')
            return redirect('contact')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
def contact_view(request):
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        print("saved")
        messages.info(request,'Contact form saved succesfully')
    return render(request, 'contact.html')
