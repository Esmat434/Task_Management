from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated