# coding=utf8
import re


# 检测用户名格式
def check_username(username):
    pattern = re.compile("[a-zA-Z0-9_-]{4,16}$")
    match = pattern.match(username)
    if match:
        return True
    else:
        return False


# 检测密码格式
def check_password(password):
    pattern = re.compile("[a-zA-Z0-9_-]{6,18}$")
    match = pattern.match(password)
    if match:
        return True
    else:
        return False


# 检测昵称格式
def check_nickname(nickname):
    pattern = re.compile(u"[A-Za-z\u4e00-\u9fa5]{2,10}$")
    match = pattern.match(nickname)
    if match:
        return True
    else:
        return False


