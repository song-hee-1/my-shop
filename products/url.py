from django.urls import path, include
from rest_framework.routers import SimpleRouter

from products.views import ProductViewSet

app_name = 'products'

router = SimpleRouter()
router.register('', ProductViewSet, 'products')

urlpatterns = [
    path('', include((router.urls, ''))),
]
