from enum import Enum

from django.db import models

from core.models import TimeStampModel
from core.utils.choice import get_choices


class ProductSizeType(Enum):
    UNDEFINED = 'undefined'
    SMALL = 'small'
    LARGE = 'large'


class ProductStatusType(Enum):
    UNDEFINED = 'undefined'
    REGISTERED = 'registered'
    DELETED = 'deleted'


class Product(TimeStampModel):
    user = models.ForeignKey('accounts.User', related_name='foods', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(help_text='가격')
    origin_price = models.PositiveIntegerField(help_text='원가')
    name = models.CharField(max_length=255, help_text='이름')
    name_initials = models.CharField(max_length=255, null=True, help_text='이름의 초성')
    description = models.TextField(help_text='설명')
    barcode = models.CharField(max_length=100, help_text='바코드')
    expired_date = models.DateField(help_text='유통 기한')
    size = models.CharField(
        choices=get_choices(ProductSizeType), default=ProductSizeType.UNDEFINED, max_length=30, help_text='사이즈'
    )
    status = models.CharField(
        choices=get_choices(ProductStatusType), default=ProductStatusType.UNDEFINED, max_length=30, help_text='상태'
    )


class ProductCategory(TimeStampModel):
    name = models.CharField(max_length=40, help_text='카테고리 이름')
    code = models.IntegerField(unique=True, null=True, default=None, help_text='카테고리 코드')
    product = models.ManyToManyField(Product, related_name='categories', help_text='상품')
