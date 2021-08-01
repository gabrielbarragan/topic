""" Platzigram url's module"""

from django.urls import path

from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hi/', views.hi),
    path('ciao/', views.ciao),
]
