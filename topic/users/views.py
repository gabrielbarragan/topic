"""users view"""
#django 

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import views as auth_views



#models 
from posts.models import Post
from users.models import User, Profile

#forms 
from users.forms import  signupForm

class UserDetailView(LoginRequiredMixin,DetailView):
    """User detail view."""
	
    template_name='users/detail.html'
    slug_field= 'username'
    slug_url_kwarg='username'
    queryset = User.objects.all()

    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context

class LoginView(auth_views.LoginView):
    """Login user view"""
    
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Users Logout view"""
    next_page= 'users:login'


class SignupView(FormView):
    """user signup view"""
    form_class = signupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
    
    def form_valid(self,form):
        """save form data"""
        form.save()

        return super().form_valid(form)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model= Profile
    fields = ['website','biography','phone_number','picture']
    

    def get_object(self):
        """return user´s profile"""
        return self.request.user.profile
    
    def get_success_url(self):
        """return to user's profile"""
        username=self.object.user.username
        return reverse('users:detail', kwargs={'username':username})

