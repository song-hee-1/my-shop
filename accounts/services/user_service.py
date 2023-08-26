from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import SlidingToken

from accounts.models import User
from core.utils.base_service import BaseService


class UserService(BaseService):
    model = User

    def __init__(self, user=None):
        super(UserService, self).__init__()
        self._user = user

    def login(self, phone, password):
        user = authenticate(phone=phone, password=password)
        jwt_token = SlidingToken.for_user(user)
        jwt_token_output_dto = dict(
            access=str(jwt_token),
            refresh=str(jwt_token)
        )
        return jwt_token_output_dto

    def signup(self, phone, password):
        # todo. exception 처리
        # output_dto = self.check_available_phone(phone)
        # if output_dto.get('exists'):
        #     return JsonResponse({'error': '중복된 번호입니다'}, status=400)
        user = User.objects.create_user(phone=phone, password=password)
        jwt_token = SlidingToken.for_user(user)
        jwt_token_output_dto = dict(
            access=str(jwt_token),
            refresh=str(jwt_token)
        )
        return jwt_token_output_dto

    def check_available_phone(self, phone):
        is_exist = User.objects.filter(phone=phone).exists()
        output_dto = dict(exists=is_exist)
        return output_dto

    @property
    def user(self) -> User:
        return self._user
