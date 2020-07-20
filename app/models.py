from django.db import models

import uuid
from django.utils import timezone
from services.models import AbstractUser, ModelMixin

class PhoneAuth(ModelMixin):
    token = models.TextField(help_text='토큰값')

class User(AbstractUser, ModelMixin):

    # device_token = models.CharField(max_length=255, blank=True, null=False)
    nickname = models.CharField(max_length=16)
    phone_auth = models.OneToOneField(PhoneAuth, models.SET_NULL, null=True, blank=True, default=None,
                                      help_text="유저가 회원가입 시 사용한 PhoneAuth 객체. 없으면 인증받지 않았음을 의미")

    def __str__(self):
        return self.phone