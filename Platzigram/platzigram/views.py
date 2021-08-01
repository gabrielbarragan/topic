""" Platzigram views"""

from django.http import HttpResponse
from django.http import JsonResponse

#utilities
from datetime import datetime

def hello_world(request):
    """ Return a time of server"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs',)

    return HttpResponse(f'Oh, hi! Current server time is {now}')


def hi(request):
    """Hi."""
    numbers_list_sorted = sorted([int(number) for number in request.GET['numbers'].split(',')])
        
    response = JsonResponse({'"numbers"': numbers_list_sorted})

    return HttpResponse(response)

def ciao(request):
    """ciao."""

    dict_numbers = { 
        keys: sorted([int(number) if number.isdigit() else number for number in values.split(',') ])
         for keys, values in request.GET.items() 
         }
    
    response = JsonResponse(dict_numbers)

    return HttpResponse(response)
