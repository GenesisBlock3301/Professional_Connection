from django.contrib import admin
from . models import Post, PostLike, Comment, CommentLike, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id", "company", "user", "text"
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "author", "post", "text"
    )


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "post"
    )


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "comment"
    )


@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name"
    )

