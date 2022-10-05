from django.db.models import Count, Q
from .models import GroupPost
from common.pagination import CustomPagination
from common.helper import CommonIterableItem


class GroupPostHelper(CommonIterableItem):

    def __init__(self, request):
        self.request = request
        self.params = (
            Q(user__isnull=False)
        )

    def get_item(self, _id):

        post = GroupPost.objects.select_related("user", "group") \
            .annotate(num_of_likes=Count("gp_like", filter=self.params, distinct=True))\
            .annotate(num_of_comments=Count("gp_comment", filter=self.params, distinct=True))\
            .filter(id=_id).first()
        return post

    def my_items(self, user_id):
        posts = GroupPost.objects.select_related("user", "group") \
            .annotate(num_of_likes=Count("gp_like", filter=self.params, distinct=True)) \
            .annotate(num_of_comments=Count("gp_comment", filter=self.params, distinct=True)) \
            .filter(user__id=user_id).order_by("-id")

        return posts

    def all_items(self):
        return GroupPost.objects.select_related("user", "group") \
            .annotate(num_of_likes=Count("gp_like", filter=self.params, distinct=True)) \
            .annotate(num_of_comments=Count("post_comment", filter=self.params, distinct=True)) \
            .all().order_by("-id")

    def pagination(self, data, serializer_class):
        paginator = CustomPagination()
        result_page = paginator.get_queryset(data=data, request=self.request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_response(serializer.data)
