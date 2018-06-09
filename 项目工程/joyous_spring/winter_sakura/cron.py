from winter_sakura import models    # 导入数据库表对象
from django.contrib.auth.hashers import make_password, check_password   # 生成密码密文
from django.db import transaction


# 定时执行任务
def log():
    print(123)