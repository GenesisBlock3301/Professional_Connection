from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser

from common.responses import POST_SUCCESS_RESPONSE, POST_ERROR_RESPONSE, GET_DATA_FROM_SERIALIZER
from company.serializers import CompanySerializer
from common.pagination import CustomPagination
from common.helper import HelperAdapter

from .helper import CompanyHelper


class CompanyAPIView(APIView):
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
        company = HelperAdapter(common_helper=CompanyHelper(request))
        if pk:
            data = company.get_item(pk)
            serializer = CompanySerializer(data)
            return Response(GET_DATA_FROM_SERIALIZER(serializer))
        else:
            data_query = company.all_items()
            paginator = CustomPagination()
            result_page = paginator.get_queryset(data=data_query, request=request)
            serializer = CompanySerializer(result_page, many=True)
            return paginator.get_response(serializer.data)
