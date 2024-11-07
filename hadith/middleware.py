from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from jwt import decode as jwt_decode
from django.conf import settings

User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class JWTAuthMiddleware(BaseMiddleware):
    """
    Custom middleware that takes a JWT token from the WebSocket connection and authenticates the user.
    """
    async def __call__(self, scope, receive, send):
        # Extract token from query string (or you can change it to use headers)
        query_string = parse_qs(scope['query_string'].decode())
        token = query_string.get('token', [None])[0]
        
        if token is None:
            scope['user'] = AnonymousUser()
        else:
            try:
                # Decode the token to get the payload
                payload = jwt_decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = payload['user_id']

                # Fetch the user based on the decoded token
                scope['user'] = await get_user(user_id)

            except (InvalidToken, TokenError, KeyError):
                scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)
