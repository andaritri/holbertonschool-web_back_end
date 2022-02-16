#!/usr/bin/env python3
"""Basic Authentication module for the API"""
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """Basic Authentication class
    """
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """ Extract authorization header"""
        if (
            not authorization_header or
            not isinstance(authorization_header, str) or
            not authorization_header.startswith("Basic ")
        ):
            return None
        return authorization_header.split(maxsplit=1)[-1]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """check base64 string
        """
        if (
            not base64_authorization_header or
            not isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            utf8_str = base64_authorization_header.encode('utf-8')
            return base64.b64decode(utf8_str).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """ Extract user credentials
        """
        if (
            decoded_base64_authorization_header is None or
            not isinstance(decoded_base64_authorization_header, str) or
            ":" not in decoded_base64_authorization_header
        ):
            return None, None
        return tuple(
            decoded_base64_authorization_header.split(sep=":", maxsplit=1)
        )

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """User object
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            return self.user_object_from_credentials(*credentials)
        except Exception:
            return None
