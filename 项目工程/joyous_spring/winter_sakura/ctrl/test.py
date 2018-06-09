from winter_sakura import models    # 导入数据库表对象
from django.contrib.auth.hashers import make_password, check_password   # 生成密码密文
from django.db import transaction


def get_time():
    ret = {"arrive_time":""}

    with transaction.atomic():
        arrive_time = models.TimeSetting.objects.get(setting=1)
        print(type(arrive_time.value))
        print(arrive_time.value)

        ret["arrive_time"] = arrive_time.value
    return ret


def sign():
    pass