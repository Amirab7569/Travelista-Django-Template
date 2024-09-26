from django.shortcuts import render
from .forms import ContactForm, NewsletterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your ticket submited successfull',extra_tags='success')
        else:
            messages.error(request,'your ticket didnt submited successfull',extra_tags='error')
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def about_view(request):
    return render(request,'website/about.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    