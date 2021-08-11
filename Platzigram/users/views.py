"""users view"""
#django 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

#exceptions
from django.db.utils import IntegrityError

#models 
from django.contrib.auth.models import User
from users.models import Profile


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
      username = request.POST['username']
      password = request.POST['password']
      confirm_password = request.POST['confirm_password']
      email = request.POST['email']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']

      if password != confirm_password:
          return render(request, 'users/signup.html',{'error': 'password confirmation does not match'})
      try:
          user = User.objects.create_user(username=username, password=password)

      except IntegrityError:
          return render(request, 'users/signup.html', {'error': f'User {username} already in use'})
      
      user.first_name = first_name
      user.last_name = last_name
      user.email = email
      
      user.save()

      profile = Profile(user=user)
      profile.save()
      return redirect('login')

    return render(request, 'users/signup.html')



