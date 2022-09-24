from post.models import Post
from common.pagination import CustomPagination
from common.helper import CommonIterableItem


class PostHelper(CommonIterableItem):

    def __init__(self, request):
        self.request = request

    def get_item(self, _id):
        company = Post.objects.select_related("user", "company").filter(id=_id).first()
        return company

    def my_items(self, user):
        return Post.objects.select_related("user", "company").filter(user=user)

    def all_items(self):
        return Post.objects.select_related("user", "company").all()

    def pagination(self, data, serializer_class):
        paginator = CustomPagination()
        result_page = paginator.get_queryset(data=data, request=self.request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_response(serializer.data)




