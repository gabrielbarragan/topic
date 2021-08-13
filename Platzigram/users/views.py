"""users view"""
#django 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

#exceptions


#models 
from django.contrib.auth.models import User
from users.models import Profile

#forms 
from users.forms import ProfileForm, signupForm


def login_view(request):
    """login view"""
    
    if request.user.is_authenticated:
        return redirect('feed')

    elif request.method == 'POST':

        username= request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password= password)

        if user:
            login(request,user)
            return redirect('feed')

        else:
            return render(request, 'users/login.html',{ 'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """logout a user"""
    logout(request)
    return redirect('login')


def signup(request):
    """ signup view"""
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= signupForm()
    return render(
        request= request,
        template_name= 'users/signup.html',
        context={
            'form':form
        }
    )


@login_required
def update_profile(request):
    """Update a user´s profile view"""

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website= data['website']
            profile.phone_number= data['phone_number']
            profile.biography= data['biography']
            profile.picture= data['picture']
            profile.save()

            return redirect('feed')
        
    else:
        form = ProfileForm()

    return render(
        request, 
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form,
        })



