# coding: utf8

# rbac 一般用于 web 网站，需要用户登录后获取当前用户信息
# 因为登录与 rbac 本身的原理无关，这边简化为两个接口
logined_user = None


def login(user):
    global logined_user
    logined_user = user


def get_logined_user():
    return logined_user
