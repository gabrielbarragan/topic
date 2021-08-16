"""Posts views"""

#django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

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

class CreatePostView(LoginRequiredMixin,CreateView):
    """Create a new post"""
    template_name= 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    


    def get_context_data (self, **kwargs):
        """Add user and profile to context"""

        context= super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['Profile']= self.request.user.profile

        return context

