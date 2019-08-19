import io
import os
import random
import re
import uuid

import requests
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from MORE.settings import MEDIA_ROOT
from Moremodel.models import *

from mine.mytask import send_sms
# Create your views here.


# 手机验证码视图
def verify(request):
    try:
        phone = request.GET.get('phone')
        ret = re.match(r"^1[35678]\d{9}$", phone)
        cache_vcode = cache.get(phone)
        if cache_vcode:
            return JsonResponse({
                "code": -1,
                "msg": "The verify is not expire, please request until expire",
            })
        else:
            if ret:
                vcode = send_sms(phone)
                # print(phone)
                return JsonResponse({
                    "code": 1,
                    "msg": "success",
                    "data": {
                        "phone": phone,
                        "vcode": vcode,
                        "timeout": "180s"
                        }
                })
            else:
                return JsonResponse({
                    "code": -1,
                    "msg": "error1",
                    "data": {
                        "phone": phone,
                    }
                })
    except:
        return JsonResponse({
            "code": -1,
            "msg": "code error2",
        })


# 登录验证视图
def login(request):
    if request.method == 'GET':
        vcode = cache.get(request.GET.get('phone'))
        return JsonResponse({"vcode": vcode})

    elif request.method == 'POST':
        try:
            phone = request.POST.get('phone')
            vcode = request.POST.get('vcode')
            # ret = re.match(r"^1[35678]\d{9}$", phone)
            cache_vcode = cache.get(phone)
            if vcode == cache_vcode:
                users = User.objects.filter(phone=phone)
                if users.exists():
                    user = users.first()
                    request.session['phone'] = user.phone
                    return JsonResponse({
                                "code": 1,
                                "msg": "login success",
                                "data": {
                                    "phone": phone
                                }
                            })
                else:
                    user = User()
                    user.phone = phone
                    user.save()
                    request.session['phone'] = user.phone
                    return JsonResponse({
                                "code": 1,
                                "msg": "register success",
                                "data": {
                                    "phone": phone
                                }
                            })
            else:
                return JsonResponse({
                            "code": -1,
                            "msg": "vcode is failure",
                            "data": {
                                "phone": phone
                            }
                        })
        except:
            return JsonResponse({
                "code": -1,
                "msg": "login failure",
            })


# 个人主页

def home(request):
    if request.method == 'GET':
        return JsonResponse({
          'code': 1,
          'msg': "success",
          'data': {
              'phone': request.user.phone,
              'username': request.user.username,
              'sex': int(request.user.sex),
              'icon': request.user.icon,
          }
        })


def psonmodify(request):
    if request.method == 'GET':
        return JsonResponse({
          'code': 1,
          'msg': "success",
          'data': {
              'username': request.user.username,
              'icon': request.user.icon,
              'sex': int(request.user.sex),
              'introduct': request.user.introduct,
          }
        })

    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            sex = request.POST.get('sex')
            icon = request.FILES.get('icon')
            introduct = request.POST.get('introduct')

            user = request.user
            user.username = username
            user.sex = sex
            user.introduct = introduct
            user.save()
            print(icon)
            if icon:
                icon_name = uuid.uuid4().hex + icon.name[icon.name.rfind('.'):]
                icon_path = os.path.join(MEDIA_ROOT, icon_name)
                print('1221')
                with open(icon_path, 'ab') as fp:
                    for part in icon.chunks():
                        fp.write(part)
                        fp.flush()

                user.icon = '/uploads/'+icon_name
                user.save()

            return JsonResponse({
                'code': 1,
                'msg': "modify success",
                'data': {
                    'username': user.username,
                    'sex': int(user.sex),
                    'icon': user.icon,
                    'introduct': user.introduct,
                }
            })
        except:
            return JsonResponse({
                'code': 1,
                'msg': "modify error",
            })

