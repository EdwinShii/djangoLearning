
from rest_framework.authentication import BaseAuthentication
from example import models
from rest_framework import exceptions

# BaseAuthentication 返回值分三类：None、异常、元组
# None表示该认证部进行任何操作
# 元组形如：(token_obj.user, token_obj)
# 则会将这两个字段赋值给request的request.user和 request.auth


class AuthenticateForOrder(BaseAuthentication):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('authenticate failed')

        return (token_obj.user, token_obj)

    def authenticate_header(self,val):
        pass

