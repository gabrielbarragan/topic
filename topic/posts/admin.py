"""Posts admin classes"""
#django
from django.contrib import admin

#models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """posts admin."""
    
    list_display = ('user','Profile','title','created','modified')
    list_display_links = ( 'title',)
    list_editable = ( 'Profile',)

    list_filter = (
        'created',
        'modified',
        )

    fieldsets = (
        ('Post',{
            'fields':(
                'title','photo','Profile','user'
        )
        }),
        ('Metadata',{
            'fields':(
                'created',
                'modified',
            )
            }),
        )


    readonly_fields = ('created', 'modified',)