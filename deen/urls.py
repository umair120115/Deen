"""
URL configuration for deen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from hadith.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hadith-auth/", include("rest_framework.urls")),
    path("hadith/token/", TokenObtainPairView.as_view(), name="access"),
    path("hadith/refresh/token/", TokenRefreshView.as_view(), name="refresh"),
    path("hadith/user/register/", UserView.as_view(), name="register"),
    path("hadith/posts/", PostView.as_view(), name="posts"),
    path('hadith/posts/<int:pk>/like_post/',like_post,name="like_post"),
    path("hadith/post/<int:post_id>/comment/", CommentView.as_view(), name="comment"),
    path('hadith/user/<int:pk>/update/',UpdateDelete.as_view(),name='user-update'),
    path('hadith/users/',Users.as_view(),name='users'),
    path('hadith/request/<int:user_id>/friend/', send_friend_request_view, name='send-friend-request'),
    path('hadith/requests/',RequestView.as_view(),name='requests'),
    path('hadith/accept_request/',accept_friend_request,name='accepted_friend_request'),
    path('hadith/delete_request/',decline_friend_request,name="delete_request"),
    path('hadith/friends/',Friends.as_view(),name='your_friends'),
    # path('hadith/friends/', UserFilter.as_view(), name='friend-list'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
