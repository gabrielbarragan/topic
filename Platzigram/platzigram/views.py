""" Platzigram views"""

from django.http import HttpResponse
from django.http import JsonResponse
import json

#utilities
from datetime import datetime


def hello_world(request):
    """ Return a time of server"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs',)

    return HttpResponse(f'Oh, hi! Current server time is {now}')


def challenge_sol_teacher(request):
    
    numbers = [int(number) for number in request.GET['numbers'].split(',')]
    sorted_nums = sorted(numbers)
    data = {
        'satus': 'ok',
        'numbers': sorted_nums,
        'message': 'Integers sorted successfully.'
        }
    return JsonResponse(data)

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f'sorry {name}, you are not allowed here.'
    else:
        message = f'Hi! {name}, Welcome to Platzigram.'
    
    return HttpResponse(message)
