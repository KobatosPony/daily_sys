# coding=utf8
from winter_sakura import models    # 导入数据库表对象
from django.contrib.auth.hashers import make_password, check_password   # 生成密码密文
from django.db import transaction


# 用户注册（create决定是注册还是检查）
def register_user(username, password, nickname, sex, staff_dept, true_name, tel, address, create=0):
    ret = {}
    with transaction.atomic():
        # 获取用户数据
        user_username = models.Staff.objects.filter(username=username)
        user_nickname = models.Staff.objects.filter(nickname=nickname)
        count = models.Staff.objects.count()

        # 检查重复用户名（如果存在，返回错误信息）
        if user_username.exists():
            # html_tag为页面中提示错误的标签id
            ret['html_tag'] = 'regist_username_help'
            ret["msg"] = "用户名重复"
            return ret

        # 检查重复昵称
        if user_nickname.exists():
            ret['html_tag'] = 'regist_nickname_help'
            ret["msg"] = "昵称重复"
            return ret

        if create:
            secret_password = make_password(password, None, 'pbkdf2_sha256') # 使用加密密码

            # 获取外键
            user_type = models.UserType.objects.get(id = 1)
            staff_dept = models.Dept.objects.get(department=staff_dept)

            # 生成员工号
            staff_no = str(staff_dept.id)+str(user_type.id)+str(count)

            models.Staff.objects.create(username=username, nickname=nickname, password=secret_password, user_type=user_type,
                                        sex=sex, staff_dept=staff_dept, true_name=true_name, tel=tel, address=address,
                                        active_session=None, staff_no=staff_no, state=0)
            return False
        else:
            return False


# 查找用户(login参数为1时执行登录的功能)
def select_user(request, username, password="", login=0):
    # 定义返回数据
    ret = {"is_success": 0, "msg":"", "ex_msg": "", "username": "", "nickname": ""}

    # 用于登录
    if login:
        try:
            user_data = models.Staff.objects.filter(username=username)
            # 更新用户表中的session值（防止多次登录）
            # user_data.update(active_session=request.session.session_key)

            # 用户名不存在时返回错误信息
            if not user_data.exists():
                ret["msg"] = "用户名不存在"
                return ret

            # 不为空时对密码进行判断
            elif user_data.exists():
                try:
                    if check_password(password, user_data[0].password):
                        ret["username"] = user_data[0].username
                        ret["nickname"] = user_data[0].nickname
                        ret["is_success"] = 1
                        ret["msg"] = "登录成功"
                        return ret

                    elif not check_password(password, user_data[0].password):
                        ret["msg"] = "用户名或密码错误"
                        return ret

                    else:
                        ret["msg"] = "出现未知错误"
                        return ret

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
            return ret
        return ret

    # 用于查询用户
    else:
        try:
            user_data = models.Staff.objects.filter(username=username)[0]
            return user_data
        except Exception as e:
            return None
