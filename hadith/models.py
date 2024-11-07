from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class AppUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required!")
        if not password:
            raise ValueError("Password is required!")

        extra_fields.setdefault("is_active", True)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        return self.create_user(username, password, **extra_fields)


class AppUser(AbstractBaseUser):
    username = models.CharField(unique=True,  max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    Name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["Name", "password", "email"]

    objects = AppUserManager()

    def __str__(self):
        return self.Name

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
    
class Profile(models.Model):
    user=models.OneToOneField(to=AppUser,related_name='user_profile',on_delete=models.CASCADE)
    profile_photo=models.ImageField(upload_to='profile_photo')
    bio=models.TextField(blank=True,null=True)
    education=models.CharField(max_length=200)
    online_status=models.BooleanField(default=False)

class FriendRequest(models.Model):
    from_user=models.ForeignKey(AppUser,related_name='friend_request_send',on_delete=models.CASCADE)
    to_user=models.ForeignKey(AppUser,related_name='friend_request_got',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    accepted=models.BooleanField(default=False)

    def __str__(self):
        return  f"Friend Request from {self.from_user} to {self.to_user}"
    
    class Meta:
        unique_together=('from_user','to_user')

class Friendship(models.Model):
    user = models.ForeignKey(AppUser, related_name='friendships', on_delete=models.CASCADE)
    friend = models.ForeignKey(AppUser, related_name='friends_with', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f"{self.user} is friends with {self.friend}"
    



class Post(models.Model):
    user = models.ForeignKey(AppUser, related_name="user", on_delete=models.CASCADE)
    posted = models.ImageField(upload_to="posts")
    caption = models.TextField()
    added = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(AppUser, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="post_comment", on_delete=models.CASCADE
    )
    comment = models.TextField()
    author = models.ForeignKey(AppUser, related_name="author", on_delete=models.CASCADE)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.post)

class ChatModel(models.Model):
    sender=models.CharField(max_length=100,default=None)
    message=models.TextField(null=True,blank=True)
    thread_name=models.CharField(null=True,blank=True,max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    
