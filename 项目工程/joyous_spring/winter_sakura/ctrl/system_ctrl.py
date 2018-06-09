# coding=utf8
from winter_sakura import models    # 导入数据库表对象
from django.contrib.auth.hashers import make_password, check_password   # 生成密码密文
from django.db import transaction


# 获取部门
def get_dept():
    ret = {}

    with transaction.atomic():
        ret = models.Dept.objects.all()
        return ret


def get_leave_info():
    ret = {}

    with transaction.atomic():
        ret = models.Leave.objects.filter(state=0)
        return ret
