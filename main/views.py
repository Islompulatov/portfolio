from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def home(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("<h1>Thank you for contacting me</h1>")
    return render(request, 'index.html')
