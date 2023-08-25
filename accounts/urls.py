from django.urls import path, include
from rest_framework.routers import SimpleRouter

from accounts.views import UserViewSet

app_name = 'accounts'

router = SimpleRouter()
router.register('user', UserViewSet, 'user')

urlpatterns = [
    path('', include((router.urls, 'accounts'))),
]
