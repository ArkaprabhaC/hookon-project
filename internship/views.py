from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    internships=Internship.objects.all()
    return render(request, 'public/home.html', {'internships':internships})
