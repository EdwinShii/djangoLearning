"""djangoLearning URL Configuration

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
from django.urls import path,include

from example import views as example_view
from quickstart import views as quickstart_view

from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'users', quickstart_view.UserViewSet)
router.register(r'groups', quickstart_view.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/v1/', example_view.AuthView.as_view()),
    path('orderView/v1/', example_view.OrderView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
