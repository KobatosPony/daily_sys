# coding=utf8
from winter_sakura import models    # 导入数据库表对象
from django.contrib.auth.hashers import make_password, check_password   # 生成密码密文
from django.db import transaction


# 获取考勤信息
# 可提供两个参数，分别为用户名和获取的数目
def select_check_info(username=0, num=0):
    with transaction.atomic():
        if username == 0:
            if num == 0:
                ret = models.CheckInfo.objects.all()
            else:
                ret = models.CheckInfo.objects.all().order_by('-check_time')[:num]
        else:
            staff_id = models.Staff.objects.get(username=username)
            if num == 0:
                ret = models.CheckInfo.objects.filter(staff_id=staff_id).order_by('-check_time')
            else:
                ret = models.CheckInfo.objects.all().filter(staff_id=staff_id).order_by('-check_time')[:num]

        return ret

