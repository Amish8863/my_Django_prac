from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method=="post":
        #check if user has entered correct credentials
        user = authenticate(username='UserName', password='Password')
    
    return render(request, 'login.html')

def logout(request):
    return render(request, 'index.html')

#password for test user is Amish$$$0000

