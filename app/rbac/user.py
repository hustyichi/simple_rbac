# coding: utf8

# 对应于 rbac 中的用户管理
# 目前设计的是单个用户只能拥有一个角色，如果需要多个角色，维护好用户与角色之间的联系即可


class User:
    def __init__(self, name, role=None):
        self._name = name
        self._role = role

    def set_role(self, role):
        self._role = role

    def can(self, permission):
        return self._role.has(permission)
