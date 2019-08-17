from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from Moremodel.models import *


def index(request):
	return JsonResponse({"code":123})

