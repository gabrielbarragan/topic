"""Posts URLs"""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

        # Posts
    
    path(
        route='posts/<str:post_id>/',
        view=views.PostDetailView.as_view(),
        name='post_detail'
    ),

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed',
    ),

    path(
        route='post/new/',
        view=views.CreatePostView.as_view(),
        name='create',
    )
]

