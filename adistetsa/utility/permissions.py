from django.contrib.auth.models import Group
from rest_framework import permissions


def is_in_group(user, group_name):
    """
    Return true jika user termasuk dalam grup
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class HasGroupPermissionAny(permissions.BasePermission):
    """
    Memberikan akses kepada user berdasarkan role, membutuhkan variabel required_groups
    required_groups = {
        'get': ['__all__'],
        'post': ['Staff'],
        'put': ['Staff'],
        'delete': ['Staff'],
    }
    """

    def has_permission(self, request, view):
        required_groups_mapping = getattr(view, "required_groups", {})
        required_groups = required_groups_mapping.get(request.method, [])

        return any(
            [
                is_in_group(request.user, group_name)
                if group_name != "__all__"
                else True
                for group_name in required_groups
            ]
        )


class IsSuperAdmin(permissions.BasePermission):
    """
    Memberikan akses jika merupakan Super Admin
    """

    def has_permission(self, request, view):
        return request.user.is_superuser
