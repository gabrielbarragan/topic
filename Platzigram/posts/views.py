"""Posts views"""

#django
from django.http import HttpResponse

#utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont blanc',
        'user': 'Yoleisy Orduz',
        'timestamp': datetime.now(),
        'time': datetime.now().strftime('%b %dth, %Y - %H-%M hrs'),
        'picture':'https://picsum.photos/id/784/200/200'

    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now(),
        'time': datetime.now().strftime('%b %dth, %Y - %H-%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now(),
        'time': datetime.now().strftime('%b %dth, %Y - %H-%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
]

def list_posts(request):
    """ List existing posts"""
    content = []
    for post in posts:
        content.append(f""" 
        <p><strong>{post['name']}</strong></p>
        <p><small>{post['user']} - <i> {post['timestamp']} </i> </small></p>
        <figure><img src="{post['picture']}"/></figure>
        """)
    return HttpResponse('<br>'.join(content))