"""MORE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('figure/', include(('figure.urls', 'figure'), namespace='figure')),
    path('found/', include(('found.urls', 'found'), namespace='found')),
    path('latest/', include(('latest.urls', 'latest'), namespace='latest')),
    path('mine/', include(('mine.urls', 'mine'), namespace='mine')),

    #1.引导页
    path('guide/', include(('guide.urls', 'guide'), namespace='guide')),
]
