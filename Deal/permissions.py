from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            request.user.is_manager
        except:
            raise PermissionDenied
        return bool(request.user and request.user.is_manager)

class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            request.user.is_client
        except:
            raise PermissionDenied
        return bool(request.user and request.user.is_client)

class IsDriver(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            request.user.is_driver
        except:
            raise PermissionDenied
        return bool(request.user and request.user.is_driver)





