from django.urls import path, re_path

from guide.views import *

urlpatterns = [
    re_path('/', home, name='home'),
    re_path('guide/', guide,name='guide'),
]