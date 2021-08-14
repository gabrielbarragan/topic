"""Posts views"""

#django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

#forms
from posts.forms import PostForm

#models
from posts.models import Post



class PostsFeedView(LoginRequiredMixin, ListView):
    """return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 3
    context_object_name= 'posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    """User detail view."""
	
    template_name='posts/detail_post.html'
    slug_field= 'id'
    slug_url_kwarg='post_id'
    queryset = Post.objects.all()

    context_object_name = 'post'

@login_required
def create_post(request):
    """Create a new post view"""
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
           
           form.save()
           return redirect('posts:feed') 
    else: 
        
        form = PostForm()
    
    return render(
        request=request,
        template_name='posts/new.html',
        context = {
            'form': form,
            'user': request.user,
            'Profile': request.user.profile
        }
        )