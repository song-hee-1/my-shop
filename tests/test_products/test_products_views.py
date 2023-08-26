import pytest
from django.urls import reverse
from rest_framework import status


@pytest.fixture()
def product_data_with_categories():
    data = {
        "price": 5000,
        "origin_price": 2500,
        "name": "슈크림 라떼",
        "description": "천연 바닐라 빈을 사용한 슈크림의 달콤함 풍미와 우유, 에스프레소가 조화된 음료.",
        "barcode": "123456789",
        "expired_date": "2023-12-31",
        "size": "small",
        "status": "registered",
        "categories": [
            {"name": "Category 1", "code": 1}
        ]
    }
    return data


@pytest.fixture()
def product_data():
    data = {
        "price": 5000,
        "origin_price": 2500,
        "name": "슈크림 라떼",
        "description": "천연 바닐라 빈을 사용한 슈크림의 달콤함 풍미와 우유, 에스프레소가 조화된 음료.",
        "barcode": "123456789",
        "expired_date": "2023-12-31",
        "size": "small",
        "status": "registered",
    }
    return data


@pytest.mark.django_db
def test_create_product(product_data_with_categories, api_client_with_credentials):
    url = reverse('products:products:products-list')
    data = product_data_with_categories
    response = api_client_with_credentials.post(url, data=data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_list_products(api_client_with_credentials):
    url = reverse('products:products:products-list')
    response = api_client_with_credentials.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_product(product_data_with_categories, api_client_with_credentials):
    create_url = reverse('products:products:products-list')
    data = product_data_with_categories
    create_response = api_client_with_credentials.post(create_url, data=data, format='json')
    product_id = create_response.data.get('id')
    url = reverse('products:products:products-detail', kwargs={'pk': product_id})
    response = api_client_with_credentials.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_product(product_data_with_categories, api_client_with_credentials):
    create_url = reverse('products:products:products-list')
    data = product_data_with_categories
    create_response = api_client_with_credentials.post(create_url, data=data, format='json')
    product_id = create_response.data.get('id')

    data = {
        "price": 6000,
    }

    url = reverse('products:products:products-detail', kwargs={'pk': product_id})
    response = api_client_with_credentials.put(url, data=data)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("keyword", ["ㅅㅋㄹ", "ㄹㄸ", "ㅅㅋㄹ ㄹㄸ", "슈크림", "라떼"])
def test_search_products(keyword, product_data_with_categories, api_client_with_credentials):
    create_url = reverse('products:products:products-list')
    data = product_data_with_categories
    api_client_with_credentials.post(create_url, data=data, format='json')

    url = reverse('products:products:products-search')
    response = api_client_with_credentials.get(url, {"keyword": keyword})

    assert response.status_code == 200
    assert len(response.data) > 0
