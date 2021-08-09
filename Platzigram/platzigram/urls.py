""" Platzigram url's module"""

#django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from platzigram import views as local_view #se renombra para que no entre en conflicto con las de las apps

from posts import views as post_views



urlpatterns = [
    path('admin/',admin.site.urls),

    path('hello-world/', local_view.hello_world),
    path('challenge/', local_view.challenge_sol_teacher),
    path('hi/<str:name>/<int:age>/', local_view.say_hi),
    
    path('posts/', post_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
