#!/usr/bin/env python3
"""Authentication module for the API"""

from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Authentication calss
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """List path that require authentication
        """
        if path is None or not excluded_paths:
            return True
        for pth in excluded_paths:
            if fnmatch.fnmatch(path, pth):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Autorization header
        """
        if request is None or not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
