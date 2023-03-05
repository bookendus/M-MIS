from datetime import datetime
from typing import Any, Optional, List
from enum import Enum
import requests

from httpx_oauth.clients.google import GoogleOAuth2
from beanie import PydanticObjectId
from fastapi_users import schemas
from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.authentication.strategy import Strategy

from pydantic import Field, EmailStr

import motor.motor_asyncio
from fastapi_users.db import BaseOAuthAccount, BeanieBaseUser, BeanieUserDatabase, ObjectIDIDMixin

from app.server.configs import Configs
from app.server.models.base import AppBaseModel



google_oauth_client = GoogleOAuth2( client_id=Configs.GOOGLE_CLIENT_ID ,
                                    client_secret=Configs.GOOGLE_CLIENT_SECRET, 
                                   scopes=[
                                        "https://www.googleapis.com/auth/userinfo.email", # 구글 클라우드에서 설정한 scope
                                        "https://www.googleapis.com/auth/userinfo.profile",
                                        "openid"
                                    ], 
                      )
class SocialScope(str, Enum):
    email: str = "email"
    google: str = "google"

class OAuthAccount(BaseOAuthAccount):
    pass

class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

class User(BeanieBaseUser[PydanticObjectId], AppBaseModel):
    email: EmailStr
    username: Optional[str] = Field(None, description='Username')
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    picture: Optional[str] = Field(None)

    create_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    last_login_at: datetime = Field(default_factory=datetime.now) 

    oauth_accounts: List[OAuthAccount] = Field(default_factory=list)

async def get_user_db():
    yield BeanieUserDatabase(User, OAuthAccount)


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    # reset_password_token_secret = Configs.SECRET_KEY
    # verification_token_secret = Configs.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=Configs.SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

class GoogleAuthBackend(AuthenticationBackend):
    async def login(self, strategy: Strategy, user: User, response: Response) -> Any:
        strategy_response = await super().login(strategy, user, response)
        token = self.get_google_access_token(user)
        userinfo = get_profile_from_google(token)
        user.first_name = userinfo.get('given_name')
        user.last_name = userinfo.get('family_name')
        user.picture = userinfo.get('picture')
        user.last_login_at = datetime.now()
        await user.save()
        return strategy_response

    def get_google_access_token(self, user: User) -> Optional[str]:
        for account in user.oauth_accounts:
            if account.oauth_name == 'google':
                return account.access_token
        return None

def get_profile_from_google(access_token: str) -> dict:
    response = requests.get(url="https://www.googleapis.com/oauth2/v3/userinfo",
                            params={'access_token': access_token})
    if not response.ok:
        raise BadCredentialException(
            'Failed to get user information from Google.')
    return response.json()


# 새로 만든 구글 로그인용 인증 backend
auth_backend_google = GoogleAuthBackend(
    name="jwt-google",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)