# coding: utf8

from functools import wraps
from app.login.login_manage import get_logined_user


# 权限管理装饰器，通过此装饰器可以比较容易地为操作增加权限管理的能力
def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def decorator_function(*args, **kwargs):
            user = get_logined_user()
            if not user or not user.can(permission):
                raise Exception('无权限')

            return func(*args, **kwargs)
        return decorator_function
    return decorator
