from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from Moremodel.models import User


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        path_list = ['/mine/home','/mine/psonmodify']
        # print(request.path)
        if request.path in path_list:
            userid = request.session.get('phone', 0)
            if not userid:
                return JsonResponse({'code': -1, 'msg': '请先登录'})
            else:
                request.user = User.objects.get(phone=userid)
