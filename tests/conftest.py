import pytest
from rest_framework_simplejwt.tokens import SlidingToken


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture()
def test_phone():
    return '01012345678'


@pytest.fixture
def create_user(db, django_user_model, test_password, test_phone):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        kwargs['phone'] = test_phone
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def get_or_create_token(db, create_user):
    user = create_user()
    token = SlidingToken.for_user(user)
    return token


@pytest.fixture
def create_superuser(db, django_user_model, test_password, test_phone):
    return django_user_model.objects.create_superuser(
        phone=test_phone,
        password=test_password
    )


@pytest.fixture
def api_client_with_credentials(db, create_user, api_client):
    user = create_user()
    api_client.force_authenticate(user=user)
    yield api_client
