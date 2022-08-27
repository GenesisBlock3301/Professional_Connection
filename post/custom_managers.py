from django.db.models import Count
from django.db.models.query import QuerySet
from django.db import models


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("user", "company").prefetch_related("post_comment", "post_like")

    def num_of_comments(self, _id: int) -> QuerySet:
        return self.select_related("user", "company").prefetch_related("post_comment", "post_like")\
            .filter(id=_id).annotate(num_of_comments=Count("post_comment")).first()

    def num_of_likes(self, _id: int) -> QuerySet:
        return self.select_related("user", "company").prefetch_related("post_comment", "post_like") \
            .filter(id=_id).annotate(num_of_comments=Count("post_like")).first()
