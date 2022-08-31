from django.contrib import admin
from .models import Group, GroupMember, GroupPost, GroupPostComment, GroupPostLike, GroupPostCommentLike

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupPost)
admin.site.register(GroupPostComment)
admin.site.register(GroupPostLike)
admin.site.register(GroupPostCommentLike)
