# coding: utf8

# 为需要权限管理的操作增加权限管理操作
# 使用 permission_required 即可比较方便地增加权限管理功能

from app.rbac import constants as RBAC
from app.rbac.permission import permission_required


@permission_required(RBAC.READ_PERMISSION)
def read_file():
    print('read successfully')


@permission_required(RBAC.WRITE_PERMISSION)
def write_file():
    print('write successfully')


@permission_required(RBAC.EXEC_PERMISSION)
def exec_file():
    print('execute successfully')


@permission_required(RBAC.WRITE_PERMISSION)
def delete_file():
    print('delete suessfully')
