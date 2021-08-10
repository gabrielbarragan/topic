"""users view"""
#django 
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def login_view(request):
    """login view"""

    return render(request, 'users/login.html')
