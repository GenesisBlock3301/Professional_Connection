from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from common.responses import POST_SUCCESS_RESPONSE, POST_ERROR_RESPONSE, GET_DATA_FROM_SERIALIZER
from company.serializers import CompanySerializer
from rest_framework.parsers import MultiPartParser
from .helper import CompanyHelper
from common.pagination import CustomPagination


class CompanyAPIView(APIView, CustomPagination):
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, )

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(POST_SUCCESS_RESPONSE)
        return Response(POST_ERROR_RESPONSE)

    def get(self, request, pk=None):
        company = CompanyHelper(request)
        if pk:
            data = company.get_company(pk)
            serializer = CompanySerializer(data)
            return Response(GET_DATA_FROM_SERIALIZER(serializer))
        else:
            data = company.get_all_companies()
            serializer = CompanySerializer(data, many=True)
            return self.get_paginated_response(serializer.data)
