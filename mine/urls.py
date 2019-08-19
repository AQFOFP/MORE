
from django.urls import path, re_path

from mine.views import *

urlpatterns = [
    path('login', login, name="login"),
    path('verify', verify, name="verify"),
    path('home', home, name="home"),
    path('psonmodify', psonmodify, name="psonmodify"),
]

