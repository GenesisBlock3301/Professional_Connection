from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


class CustomPagination:
    def __init__(self):
        self.paginator = PageNumberPagination()

    def get_queryset(self, data, request):
        result_page = self.paginator.paginate_queryset(queryset=data, request=request)
        return result_page

    def get_response(self, serialized_data):
        return self.paginator.get_paginated_response(serialized_data)
