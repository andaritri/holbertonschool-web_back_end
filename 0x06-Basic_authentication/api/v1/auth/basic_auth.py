#!/usr/bin/env python3
"""Basic Authentication module for the API"""
from api.v1.auth.auth import Auth
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
