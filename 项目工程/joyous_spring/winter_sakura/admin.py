from django.contrib import admin
from winter_sakura.models import *
# Register your models here.
# 通过注册时你的表可以在django自带的后台管理中操作


@admin.register(Staff)
class CheckInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'true_name', 'tel', 'staff_dept', 'user_type')


admin.site.register(UserType)
admin.site.register(SystemSetting)
admin.site.register(TimeSetting)
admin.site.register(Dept)
admin.site.register(Theme)
admin.site.register(Reply)
admin.site.register(CheckType)


@admin.register(CheckInfo)
class CheckInfoAdmin(admin.ModelAdmin):
    list_display = ('check_time', 'staff_id', 'check_type')
    search_fields =('staff_id','check_type') #搜索字段
    # 筛选器
    list_filter =('check_type', 'staff_id') #过滤器


admin.site.register(Daily)
admin.site.register(Theme_Img)
admin.site.register(Reply_Img)


# 修改admin页面的显示
admin.site.site_header = '员工考勤系统'
admin.site.site_title = 'big boss'

