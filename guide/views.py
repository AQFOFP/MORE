from django.http import JsonResponse
from django.shortcuts import render, redirect,reverse

from Moremodel.models import *

def home(request):
    return redirect(reverse('guide'))


def guide(request):

    imgs = GuideImg.objects.all()
    data = {
        'img' : imgs
    }

    return JsonResponse(data)

















