from common.pagination import CustomPagination
from common.helper import CommonIterableItem
from django.contrib.auth import get_user_model

User = get_user_model()


class FriendHelper(CommonIterableItem):
    def __init__(self, request):
        self.request = request
        self.user = User.objects.prefetch_related("friends")

    def get_item(self, friend_id):
        pass

    def my_items(self, user_id):
        return self.user.get(id=user_id).friends.values("id", "email").order_by("-id")

    def all_items(self):
        pass

    def pagination(self, data, serializer_class):
        paginator = CustomPagination()
        result_page = paginator.get_queryset(data=data, request=self.request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_response(serializer.data)
