from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from common.helper import HelperAdapter
from .helper import GroupPostHelper
from .serializers import GroupPostSerializer, CreateGroupPostSerializer
from common.responses import GET_DATA_FROM_SERIALIZER, POST_ERROR_RESPONSE, POST_SUCCESS_RESPONSE


class GroupPostApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None):
        posts = HelperAdapter(common_helper=GroupPostHelper(request=request))
        if pk:
            data = posts.get_item(pk)
            serializer = GroupPostSerializer(data)
            return Response(GET_DATA_FROM_SERIALIZER(serializer))
        else:
            is_my_post = request.query_params.get("is_mypost", None)
            if is_my_post == "True":
                return posts.pagination(posts.my_items(request.user_id), GroupPostSerializer)
            else:
                return posts.pagination(posts.all_items(), GroupPostSerializer)

    def post(self, request):
        data = request.data
        post_data = {
            "user": request.user.id,
            **data
        }
        serializer = CreateGroupPostSerializer(data=post_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(POST_SUCCESS_RESPONSE)
        return Response(POST_ERROR_RESPONSE)
