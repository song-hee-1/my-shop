import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_success_signup(api_client, test_phone, test_password):
    url = reverse('accounts:accounts:user-signup')
    data = {
        'phone': test_phone,
        'password': test_password,
    }
    response = api_client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_fail_signup_wrong_phone(api_client, test_password):
    url = reverse('accounts:accounts:user-signup')
    data = {
        'phone': '010-1234-5678',
        'password': test_password,
    }
    with pytest.raises(Exception):
        api_client.post(url, data)


@pytest.mark.django_db
def test_fail_signup_max_phone(api_client, test_password):
    url = reverse('accounts:accounts:user-signup')
    data = {
        'phone': '0102334453423423423423425235235235252352352',
        'password': test_password,
    }
    response = api_client.post(url, data)
    assert response.status_code != 200


@pytest.mark.django_db
def test_success_login(create_user, test_phone, test_password, api_client):
    create_user()
    url = reverse('accounts:accounts:user-login')
    data = {
        'phone': test_phone,
        'password': test_password
    }
    response = api_client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_logout(api_client_with_credentials):
    url = reverse('accounts:accounts:user-logout')
    response = api_client_with_credentials.post(url)
    assert response.status_code == 200
