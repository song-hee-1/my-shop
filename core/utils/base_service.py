from django.db.models import Model, QuerySet
from django.core.exceptions import ImproperlyConfigured


class BaseService:
    model: Model = None

    def __init__(self, queryset: QuerySet = None):
        if queryset is None:
            queryset = self.get_queryset()
        self.queryset: QuerySet = queryset

    def get_queryset(self) -> QuerySet:
        if self.model is None:
            raise ImproperlyConfigured('you have to set default model.')
        return self.model.objects.all()
