""" Platzigram url's module"""

#django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from platzigram import views as local_view #se renombra para que no entre en conflicto con las de las apps

from posts import views as post_views
from users import views as users_views



urlpatterns = [
    path('admin/',admin.site.urls),

    path('hello-world/', local_view.hello_world, name='hello_world'),
    path('challenge/', local_view.challenge_sol_teacher, name='sort'),
    path('hi/<str:name>/<int:age>/', local_view.say_hi, name='hi'),
    
    path('posts/', post_views.list_posts, name='feed'),
    path('users/login/',users_views.login_view, name='login'),
    path('users/logout/',users_views.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
