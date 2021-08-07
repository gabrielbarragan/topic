"""user admin classes"""
#django
from django.contrib import admin

#models
from users.models import Profile

# Register your models here.
admin.site.register(Profile)