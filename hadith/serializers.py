from rest_framework import serializers
from .models import AppUser, Post, Comment,FriendRequest,Friendship




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', "username", "email", "password",'Name']

    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user

class FriendRequestSerializer(serializers.ModelSerializer):
    sender=serializers.SerializerMethodField()
    reciever=serializers.SerializerMethodField()
    class Meta:
        model=FriendRequest
        fields=['id','from_user','to_user','created_at','accepted','sender','reciever']
        extra_kwargs={"from_user":{"read_only":True},"to_user":{"read_only":True}}

    def get_sender(self,obj):
        return obj.from_user.Name
    def get_reciever(self,obj):
        return obj.to_user.Name


class PostSerializer(serializers.ModelSerializer):
    like = UserSerializer(many=True, read_only=True)
    # user = serializers.SerializerMethodField()
    user=UserSerializer()
    like_count = serializers.SerializerMethodField()
    

    class Meta:
        model = Post
        fields = ['id',"user", "posted", "caption", "added", "like", "like_count"]
        extra_kwargs = {"user": {"read_only": True}}

    def get_user(self, obj):
        return obj.user.username

    def get_like_count(self, obj):
        return len(obj.like.all())


class CommentSerializer(serializers.ModelSerializer):
    author=serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ["post", "comment", "comment_date", "author"]
        extra_kwargs = {"author": {"read_only": True}, "post": {"read_only": True}}
    def get_author(self,obj):
        return obj.author.username
   
class FriendshipSerializer(serializers.ModelSerializer):
    # user_name=serializers.SerializerMethodField()
    user=UserSerializer()
    # friend_name=serializers.SerializerMethodField()
    friend=UserSerializer()
    class Meta:
        model=Friendship
        fields=['id','user','friend','created_at']
    
    def get_user_name(self,obj):
        return obj.user.Name
    
    def get_friend_name(self,obj):
        return obj.friend.Name

