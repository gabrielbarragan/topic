"""Posts views"""

#django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

#forms
from posts.forms import PostForm

#models
from posts.models import Post




@login_required
def list_posts(request):
    """ List existing posts"""
    posts= Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html', {'posts':posts})

@login_required
def create_post(request):
    """Create a new post view"""
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
           print('here in here')
           form.save()
           return redirect('posts:feed') 
    else: 
        print('no here')
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