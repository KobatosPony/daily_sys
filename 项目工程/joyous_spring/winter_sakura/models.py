from django.db import models
from django.contrib.sessions.models import Session
from django.conf import settings


# 系统设置表 SystemSetting
class SystemSetting(models.Model):
    setting = models.CharField(max_length=20, verbose_name='设置项', primary_key=True)

    value = models.IntegerField(verbose_name='参数', default=0)

    class Meta:
        verbose_name = '系统设置'
        verbose_name_plural = '系统设置'

    def __unicode__(self):
        return self.value

    def __str__(self):
        return self.value


# 时间设置表 TimeSetting
class TimeSetting(models.Model):
    setting = models.CharField(max_length=20, verbose_name='设置项', primary_key=True)

    value = models.TimeField(null=False, verbose_name='设置时间')

    class Meta:
        verbose_name = '时间设置'
        verbose_name_plural = '时间设置'

    def __unicode__(self):
        return self.value

    def __str__(self):
        return self.value


# 用户类型表 UserType
class UserType(models.Model):
    display = models.CharField(max_length=50, null=False, verbose_name='用户类型')

    class Meta:
        verbose_name = '用户类型'
        verbose_name_plural = '用户类型'

    def __unicode__(self):
        return self.display

    def __str__(self):
        return self.display


# 部门表 Dept
class Dept(models.Model):
    department = models.CharField(max_length=20, null=False, verbose_name='部门名称')

    charge = models.CharField(max_length=20, null=False, verbose_name='部门主管')

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'

    def __unicode__(self):
        return self.department

    def __str__(self):
        return self.department


# 员工表 Staff
class Staff(models.Model):
    username = models.CharField(max_length=25, null=False, primary_key=True, verbose_name='用户名')

    password = models.CharField(max_length=200, null=False, verbose_name='密码')

    sex_choices = {
        ('0', '男'),
        ('1', '女'),
    }

    staff_no = models.CharField(max_length=20, null=True, verbose_name='员工号')

    nickname = models.CharField(max_length=20, null=False, verbose_name='昵称',default='snow')

    sex = models.CharField(max_length=20, choices=sex_choices, null=False, verbose_name='性别')

    staff_dept = models.ForeignKey('Dept', verbose_name='所属部门')

    true_name = models.CharField(max_length=25, null=False, verbose_name='真实姓名')

    tel = models.CharField(max_length=25, null=False, verbose_name='联系电话')

    address = models.CharField(max_length=25, null=True, verbose_name='家庭住址')

    user_type = models.ForeignKey('UserType', verbose_name='用户类型')

    active_session = models.CharField(max_length=50, null=True, verbose_name='登录session')

    state = models.IntegerField(verbose_name='状态', default=0)

    day_note = models.IntegerField(verbose_name='记录', default=0)  # 记录今日的日志（0缺勤，1迟到，2早退，3迟到早退，4正常）

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


# 考勤类型表 CheckType
class CheckType(models.Model):
    type_name = models.CharField(max_length=10, verbose_name='类型')

    class Meta:
        verbose_name = '考勤类型'
        verbose_name_plural = '考勤类型'

    def __unicode__(self):
        return self.type_name

    def __str__(self):
        return self.type_name


# 考勤信息表 CheckInfo
class CheckInfo(models.Model):
    staff_id = models.ForeignKey('Staff', verbose_name='员工ID')

    dept_id = models.ForeignKey('Dept', verbose_name='部门ID')

    check_time = models.DateTimeField(auto_now_add=True, verbose_name='考勤时间')

    check_type = models.ForeignKey('CheckType', verbose_name='考勤类型')

    remarks = models.CharField(max_length=25, null=True, verbose_name='备注信息')

    class Meta:
        verbose_name = '考勤信息'
        verbose_name_plural = '考勤信息'

    def __unicode__(self):
        return self.staff_id

    def __str__(self):
        return self.staff_id


# 主题表 Theme
class Theme(models.Model):
    title = models.CharField(max_length=50,db_index=True, verbose_name='标题')

    content = models.CharField(max_length=720, null=False, verbose_name='内容')  #内容

    url = models.URLField()

    reply_count = models.IntegerField(default=0, verbose_name='回复数')    # 回复数

    user = models.ForeignKey("Staff", verbose_name='发布用户')

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    update_date = models.DateTimeField(auto_now=True,verbose_name='最后回复时间')

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# 回复表 Reply
class Reply(models.Model):
    content = models.TextField(verbose_name='回复内容')

    user = models.ForeignKey("Staff", verbose_name='回复用户')

    theme = models.ForeignKey("Theme", verbose_name='回复主题')

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='回复时间')

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = '回复'

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content


# 假条表 Leave
class Leave(models.Model):
    staff_id = models.ForeignKey('Staff', verbose_name='员工ID')

    reason = models.CharField(max_length=50, null=False, verbose_name='原因')

    start_date = models.DateTimeField(null=False, verbose_name='开始时间')

    end_date = models.DateTimeField(null=False, verbose_name='结束时间')

    state = models.IntegerField(verbose_name='状态', default=0) # 0为未查看，1为通过， 2为驳回

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='生成时间')

    staff_no = models.CharField(max_length=20, null=True, verbose_name='员工号')

    check_id = models.ForeignKey('CheckInfo' ,verbose_name='考勤号', null=True)

    class Meta:
        verbose_name = '假条'
        verbose_name_plural = '假条'

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content


# 日志表 Daily
class Daily(models.Model):
    staff_count = models.IntegerField(null=False, verbose_name='员工数')

    check_staff = models.IntegerField(null=False, verbose_name='正常考勤员工数')

    uncheck_staff = models.IntegerField(null=False, verbose_name='未考勤员工数')

    late_staff = models.IntegerField(null=False, verbose_name='迟到员工数')

    leave_staff = models.IntegerField(null=False, verbose_name='早退员工数')

    late_and_leave_staff = models.IntegerField(null=False, verbose_name='迟到并且早退员工数')

    daily_text = models.TextField(verbose_name='日志文本')

    create_time = models.DateField(auto_now_add=True, verbose_name='日志创建时间')

    class Meta:
        verbose_name = '日志'
        verbose_name_plural = '日志'


# 公告表 Notice
class Notice(models.Model):
    pub_user = models.ForeignKey("Staff", verbose_name='发布人')

    notice_text = models.TextField(verbose_name='公告内容')

    create_time = models.DateTimeField(auto_now_add=Theme, verbose_name='公告时间')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'

    def __unicode__(self):
        return self.pub_user

    def __str__(self):
        return self.pub_user


# 主题及回复的图片存放
class Reply_Img(models.Model):
    rid = models.ForeignKey('Reply')

    img_url = models.ImageField(upload_to='reply_img/', default='')

    class Meta:
        verbose_name = '回复图片'
        verbose_name_plural = '回复图片'


class Theme_Img(models.Model):
    tid = models.ForeignKey('Theme')

    img_url = models.ImageField(upload_to='theme_img/', default='')

    class Meta:
        verbose_name = '主题图片'
        verbose_name_plural = '主题图片'


# 公告图片存放
class Notice_Img(models.Model):
    tid = models.ForeignKey('Notice')

    img_url = models.ImageField(upload_to='notice_img/', default='')

    class Meta:
        verbose_name = '公告图片'
        verbose_name_plural = '公告图片'