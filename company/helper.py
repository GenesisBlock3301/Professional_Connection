from .models import Company
from common.helper import CommonIterableItem
from common.pagination import CustomPagination


class CompanyHelper(CommonIterableItem):
    def __init__(self, request):
        self.request = request

    def all_items(self):
        companies = Company.objects.select_related("manager").all().order_by("name")
        return companies

    def get_item(self, _id):
        company = Company.objects.select_related("manager").filter(id=_id).first()
        return company

    def my_items(self, manager):
        return Company.objects.select_related("manager").filter(manager=manager)

    def pagination(self, data, serializer_class):
        paginator = CustomPagination()
        result_page = paginator.get_queryset(data=data, request=self.request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_response(serializer.data)

    # def get_common_items(self, posts, serializer_class):
    #     return self.common_paginate(posts, serializer_class)
