#!/usr/bin/env python3
"""Authentication module for the API"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication calss
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """List path that require authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Autorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
