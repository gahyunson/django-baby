from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Post, Comment, Tag

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site(register(Post, PostAdmin))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'photo_tag', 'message_length', 'message', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 50px"/>')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass