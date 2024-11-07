from django.contrib import admin
from .models import Post, AppUser, Comment,FriendRequest,Friendship,Profile,ChatModel

# Register your models here.
admin.site.register(Post)
admin.site.register(AppUser)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(ChatModel)


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'created_at', 'accepted']

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend', 'created_at']