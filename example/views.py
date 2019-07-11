from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from example import permission
from example import models
from example import authentication

from django.http import JsonResponse


@method_decorator(csrf_exempt,name="dispatch")
class StudentView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('get')


def md5(user):
    import hashlib
    import time

    ctime = str(time.time())
    m = hashlib.md5(bytes(ctime, encoding='utf-8'))
    m.update(ctime.encode('utf-8'))
    return m.hexdigest()


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'msg': None
        }
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(user_name=user, password=pwd)
            if not obj:
                ret['code'] = 1001
                ret['msg'] = "用户名密码错误"
            obj = obj[0]
            token = md5(user)
            res = models.UserToken.objects.update_or_create(user_id=obj.id, defaults={'user': obj, 'token': token})
            ret['token'] = token
        except Exception as ex:
            print(ex)
            ret['code'] = 2001
            ret['msg'] = "请求异常"

        return JsonResponse(ret)


class OrderView(APIView):
    """
    just for user type 3
    """
    authentication_classes = [authentication.AuthenticateForOrder]
    permission_classes = [permission.SVIPPermission, ]

    def get(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'msg': None
        }
        try:
            ret['data'] = 'ORDER_DICT'
        except Exception as ex:
            ret['code'] = 2001
            ret['msg'] = "请求异常"

        return JsonResponse(ret)


