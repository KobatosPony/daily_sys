"""joyous_spring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from winter_sakura import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 测试页面（测试静态文件是否能成功加载）
    url(r'^demo/$', views.demo, name='demo'),

    # 测试页面（测试时间的计算）
    url(r'^time_demo/$', views.time_demo, name='time_demo'),

    # 测试页面（签到）
    url(r'^sign_demo/$', views.sign_demo, name='sign_demo'),

    # 测试页面（主页）
    url(r'^index_demo/$', views.index_demo, name='index_demo'),

    # 测试页面（登录）
    url(r'^login/$', views.login_demo, name='login_demo'),

    # 测试页面（注册）
    url(r'^register/$', views.register_demo, name='register_demo'),

    # 主页
    url(r'^index/$', views.index, name='index'),

    # 退出登录
    url(r'^logout/$', views.logout, name='logout'),

    # 个人信息
    url(r'^person/$', views.person, name='person'),

    # 考勤签到（ajax）
    url(r'^ajax_check_in/$', views.ajax_check_in, name='ajax_check_in'),

    # 考勤签退（ajax）
    url(r'^ajax_check_out/$', views.ajax_check_out, name='ajax_check_out'),

    # 人事管理
    url(r'master/$', views.master, name='master'),

    # 考勤信息
    url(r'check_info/$', views.check_info_view, name='check_info'),

    # 发布公告
    url(r'publish_notice/$', views.publish_notice, name='publish_notice'),

    # 员工请假提交
    url(r'leave_publish/$', views.leave_publish, name='leave_publish'),

    # 设置签到签退时间(ajax)
    url(r'check_time_setting_ajax/', views.check_time_setting_ajax, name='check_time_setting_ajax'),

    # 主题页面
    url(r'theme/$', views.theme, name='theme'),
    url(r'theme/page(?P<page>\d+)$', views.theme, name='theme'),

    # 主题详细用（回复）
    # url(r'note/id(?P<theme_id>\d+)$', views.theme_part, name='theme_part'),
    url(r'note/id(?P<theme_id>\d+)/page(?P<page>\d+)$', views.theme_part, name='theme_part'),

    # 发布主题
    url(r'theme_publish', views.theme_publish, name='theme_publish'),

    # 回复主题
    url(r'theme_reply', views.theme_reply, name='theme_reply'),

    # 请假驳回（ajax）
    url(r'unaccess/', views.unaccess, name='unaccess'),

    # 请假同意（ajax）
    url(r'access/', views.access, name='access'),

    # 考勤信息查看
    url(r'check_record/$', views.check_record, name='check_record'),

    # 生成统计
    url(r'statistics/$', views.statistics, name='statistics'),

    # 查看统计
    url(r'select_daily/$', views.select_daily, name='select_daily')
]
