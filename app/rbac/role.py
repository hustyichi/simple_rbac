# coding: utf8

# 对应于 rbac 中的角色管理，每个角色对应于多种权限
# 这边简化处理，角色的权限是不可变的，实际情况中如果需要角色的权限可变，维护好角色与权限的映射关系即可
from abc import abstractmethod

from .constants import (MANAGER_TYPE, OPERATOR_TYPE, PERMISSION_MAP,
                        VISITOR_TYPE)


class Role:
    @abstractmethod
    def _role_type(self):
        pass

    def has(self, permission):
        return permission in PERMISSION_MAP[self._role_type()]


class VisitorRole(Role):
    def _role_type(self):
        return VISITOR_TYPE


class OperatorRole(Role):
    def _role_type(self):
        return OPERATOR_TYPE


class ManagerRole(Role):
    def _role_type(self):
        return MANAGER_TYPE
