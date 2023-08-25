from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')

        if self.filter(phone=phone).exists():
            raise ValueError('A user with this phone number already exists')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser):
    phone = models.CharField(
        max_length=20, null=True, unique=True, help_text='- 기호 없이 숫자만 넣어주세요.',
        validators=[
            MinLengthValidator(9, message='전화번호는 최소 9자 이상이어야 합니다.'),
            MaxLengthValidator(11, message='전화번호는 최대 11자까지 허용됩니다.')
        ]
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'

    objects = UserManager()
