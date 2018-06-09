# coding=utf8
import re


# 检测用户名格式
def check_username(username):
    pattern = re.compile("[a-zA-z]\\w{4,10}$")
    match = pattern.match(username)
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


# 检测密码格式
def check_password(password):
    pattern = re.compile("(\w){6,18}$")
    match = pattern.match(password)
    if match:
        return True
    else:
        return False


# 检测邮箱格式
def check_email(email):
    pattern = re.compile("\w{1,10}@\w{1,5}\.\w{1,5}$")
    match = pattern.match(email)
    if match:
        return True
    else:
        return False


# 检测QQ号码格式
def check_qq(qq):
    pattern = re.compile("\d{4,14}$")
    match = pattern.match(qq)
    if match:
        return True
    else:
        return False


# 检测电话号码格式
def check_tel_number(tel):
    pattern = re.compile("\d{11}$")
    match = pattern.match(tel)
    if match:
        return True
    else:
        return False
