from rest_framework.views import APIView
from rest_framework.response import Response

from common.responses import POST_SUCCESS_RESPONSE, POST_ERROR_RESPONSE, GET_DATA_FROM_SERIALIZER
from common.helper import HelperAdapter

from post.helper import PostHelper
from post.serializers import PostSerializer, CreatePostSerializer


class PostApiView(APIView):

    def get(self, request, pk=None):
        posts = HelperAdapter(common_helper=PostHelper(request=request))
        if pk:
            data = posts.get_item(pk)
            serializer = PostSerializer(data)
            return Response(GET_DATA_FROM_SERIALIZER(serializer))

        else:
            is_my_post = request.query_params.get("is_mypost", None)
            if is_my_post == "True":
                return posts.pagination(posts.my_items(request.user), PostSerializer)
            else:
                return posts.pagination(posts.all_items(), PostSerializer)

    def post(self, request):
        data = request.data
        post_data = {
            "user": request.user.id,
            **data
        }
        serializer = CreatePostSerializer(data=post_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(POST_SUCCESS_RESPONSE)
        return Response(POST_ERROR_RESPONSE)

