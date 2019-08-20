from django.urls import path, re_path

from graphexplain.views import *

urlpatterns = [
    re_path('latest', latest,name='latest'),
    re_path('relatest/(\d+)/', relatest,name='relatest'),
    re_path('usercomment/', usercomment,name='usercomment'),
]