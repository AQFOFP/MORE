from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from Moremodel.models import *


def index(request):
    User.objects.filter()
    return JsonResponse({"code":1})