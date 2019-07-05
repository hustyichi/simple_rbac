# coding: utf8

from app.login.login_manage import login
from app.rbac.user import User
from app.rbac.role import OperatorRole
from app.actions.action import write_file, exec_file


def test_rbac():
    # 创建用户，指定对应的角色，用户即可用于角色对应的权限
    operator_role = OperatorRole()
    current_user = User('opt', operator_role)

    # 登录用户，login 与 rbac 原理没有关系，这边简化处理
    login(current_user)

    # 写入文件，需要 WRITE_PERMISSION, 用户存在此权限
    write_file()

    # 执行文件，需要 EXEC_PERMISSION, 用户不存在此权限
    try:
        exec_file()
    except Exception as e:
        print('Execute file get exception: ' + str(e))


if __name__ == '__main__':
    test_rbac()
