# coding: utf8

# 支持的权限
READ_PERMISSION = 'READ'
WRITE_PERMISSION = 'WRITE'
EXEC_PERMISSION = 'EXECUTE'

# 支持的角色
VISITOR_TYPE = 'VISITOR'
OPERATOR_TYPE = 'OPERATOR'
MANAGER_TYPE = 'MANAGER'

# 定义角色对应的权限，这边处于简单考虑，使用的静态的角色与权限的对应关系，在实际中如果有需要可以动态管理
PERMISSION_MAP = {
    VISITOR_TYPE: {READ_PERMISSION},
    OPERATOR_TYPE: {READ_PERMISSION, WRITE_PERMISSION},
    MANAGER_TYPE: {READ_PERMISSION, WRITE_PERMISSION, EXEC_PERMISSION},
}