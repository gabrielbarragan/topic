""" Platzigram url's module"""

from django.urls import path

from platzigram import views as local_view #se renombra para que no entre en conflicto con las de las apps

from posts import views as post_views


urlpatterns = [
    path('hello-world/', local_view.hello_world),
    path('challenge/', local_view.challenge_sol_teacher),
    path('hi/<str:name>/<int:age>/', local_view.say_hi),
    
    path('posts/', post_views.list_posts),
]
