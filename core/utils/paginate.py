from rest_framework.pagination import CursorPagination


class CursorPagination(CursorPagination):
    page_size = 10
    ordering = 'id'
    cursor_query_param = 'product'
