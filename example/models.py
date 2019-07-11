from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_type_choices = (
        (1, 'normal user'),
        (2, 'vip'),
        (3, 'svip')
    )

    user_type = models.IntegerField(choices=user_type_choices)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)