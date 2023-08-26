from rest_framework.exceptions import APIException


class AlreadyExists(APIException):
    status_code = 400
    default_detail = "요청한 데이터가 이미 존재합니다."


class InvalidInput(APIException):
    status_code = 400
    default_detail = "요청이 잘못되었습니다."


class DoesNotExists(APIException):
    status_code = 400
    default_detail = "요청한 데이터가 존재하지 않습니다."


class NoPermission(APIException):
    status_code = 403
    default_detail = "권한이 없습니다."
