"""Posts models"""

#django
from django.db import models 

#Para crear modelos con django para diferentes motores de DB
class user(models.Model):#Las tablas son representadas en una clase
    """User model."""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return email"""
        return self.email