from django.shortcuts import render, render_to_response, redirect
import winter_sakura.ctrl.test
from winter_sakura.ctrl import test, user_ctrl, system_ctrl, check_info_ctrl, paging_ctrl
import datetime
from winter_sakura import models    # 导入数据库表对象
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from winter_sakura.reg_check import basic_check
from django.utils.safestring import mark_safe
from winter_sakura.deco import login_check, deco_shade
from django.db import transaction
from django.forms.models import model_to_dict
from django.utils.safestring import mark_safe   # django自带安全字符串化模块


# 测试页面
def demo(request,*args, **kwargs):
    return render_to_response("winter_sakura/demo.html")


# 测试页面
def time_demo(request,*args, **kwargs):
    if request.method == 'POST':
        arrive_time = request.POST.get('arrive_time',None)
        back_time = request.POST.get('back_time',None)
        arrive_time = datetime.datetime.strptime(arrive_time, "%H:%M").time()
        print(type(arrive_time))
        print(arrive_time)
        ret_arrive_time = test.get_time()
        set_arr_time = ret_arrive_time["arrive_time"]
        if arrive_time > set_arr_time:
            print("迟到")
        return render_to_response("winter_sakura/time_demo.html")

    if request.method == 'GET':
        return render_to_response("winter_sakura/time_demo.html")


# 测试页面
def sign_demo(request,*args, **kwargs):
    # 定义回传数据
    ret = {}

    if request.method == 'POST':
        is_sign = request.POST.get("sign_flag", 0)
        request.session['is_sign'] = is_sign

        ret['is_sign'] = is_sign
        return render_to_response("winter_sakura/sign_demo.html", ret)

    if request.method == 'GET':
        ret['is_sign'] = request.session['is_sign']
        return render_to_response("winter_sakura/sign_demo.html", ret)


# 测试页面(主页)
def index_demo(request,*args, **kwargs):
    if request.method == 'GET':
        # 返回值
        ret = {}
        # 判断
        username = request.COOKIES.get('username', '')
        is_login = request.COOKIES.get('is_login', 0)

        if is_login:
            # 获取用户数据并存入字典
            ret_user = user_ctrl.select_user(request=request, username=username)
            ret['ret_user'] = ret_user

            return render_to_response('winter_sakura/index_demo.html', ret)
        else:
            return render_to_response('winter_sakura/index_demo.html', ret)


# 测试页面(登录)
def login_demo(request,*args, **kwargs):
    if request.method == 'GET':
        ret = {'msg':""}
        return render_to_response('winter_sakura/login.html',{"ret_data":ret})

    if request.method == 'POST':
        ret = {}
        # 通过name获取form中post来的数据
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # 检验用户名和密码
        if username is None or password is None:
            if request.is_ajax():
                ret['msg'] = '用户名和密码不能为空'
                return JsonResponse(ret)
            else:
                return render_to_response('winter_sakura/login.html')

        else:
            pass

        # 从数据库中对用户进行检测(记得传递request对象)
        ret_data = user_ctrl.select_user(request=request, username=username, password=password, login=1)

        # 判断返回的参数is_success是否为0
        if ret_data["is_success"] == 0:
            # 注意使用嵌套字典传递，方便使用自定义过滤器
            # 如登录未成功，跳转到错误页面
            # 判断ajax的使用
            if request.is_ajax():
                return JsonResponse(ret_data)
            else:
                return render_to_response('winter_sakura/login.html', {"ret_data": ret_data})
        else:
            # 如果登录成功则重定向到index
            if request.is_ajax():
                ret_data['msg'] = ''
                return JsonResponse(ret_data)

            else:
                response = redirect('/index/', {"ret_data":ret_data})

                # 设置 cookie保存用户信息，设置session给服务器用
                nickname = ret_data['nickname']
                request.session['username'] = username
                request.session['nickname'] = nickname
                response.set_cookie('username', username, 24*60*60)
                response.set_cookie('is_login', 1, 24*60*60)

                # 打印session_key
                # print(request.session.session_key)

                return response


# 测试页面（注册）
def register_demo(request,*args, **kwargs):
    # 返回数据
    ret = {}

    if request.method == 'GET':
        # 返回可供选择的部门信息
        ret['ret_dept'] = system_ctrl.get_dept()
        return render_to_response('winter_sakura/register.html', ret)

    if request.method == 'POST':
        # 获取post信息，用于注册的数据
        username = request.POST.get('username', None)
        nickname = request.POST.get('nickname',None)
        password = request.POST.get('password', None)
        sex = request.POST.get('sex',None)
        staff_dept = request.POST.get('staff_dept',None)
        true_name = request.POST.get('true_name',None)
        tel = request.POST.get('tel',None)
        address = request.POST.get('address',None)

        # 用正则表达式进行检验
        if request.is_ajax():
            pass
        else:
            username_flag = basic_check.check_username(username)
            if not username_flag:
                ret['msg'] = '用户名不符合规范'
                return render_to_response('winter_sakura/register.html',{"ret_data":ret})

            nickname_flag = basic_check.check_nickname(nickname)
            if not nickname_flag:
                ret['msg'] = '昵称不符合规范'
                return render_to_response('winter_sakura/register.html',{"ret_data":ret})

            password_flag = basic_check.check_password(password)
            if not password_flag:
                ret['msg'] = '密码不符合规范'
                return render_to_response('winter_sakura/register.html',{"ret_data":ret})

        # 调用用户添加方法
        ret_data = user_ctrl.register_user(username=username, password=password, nickname=nickname, sex=sex,
                                           staff_dept=staff_dept, true_name=true_name, tel=tel, address=address)

        # 注册出现问题
        if ret_data:
            if request.is_ajax():
                return JsonResponse(ret_data)
            else:
                # 转化为前端html显示
                ret['ret_dept'] = system_ctrl.get_dept()
                ret['msg'] = mark_safe('<li class="list-group-item col-md-6" style="color: red;">' + ret_data['msg'] +'</li>')
                return render_to_response('winter_sakura/register.html',ret)

        # 成功
        else:
            # 添加用户进数据库(判断是否为ajax)
            if not request.is_ajax():
                 ret_data = user_ctrl.register_user(username=username, password=password, nickname=nickname, sex=sex,
                                           staff_dept=staff_dept, true_name=true_name, tel=tel, address=address, create=1)

            ret['msg'] = '注册成功'
            ret['url'] = '/index/'
            ret['page_name'] = '首页'
            return redirect('/index/',{"ret_data":ret})


# 主页
def index(request,*args, **kwargs):
    # 返回值
    ret = {}
    if request.method == 'GET':

        # 判断
        username = request.COOKIES.get('username', '')
        is_login = request.COOKIES.get('is_login', 0)

        if is_login:
            # 获取用户数据并存入字典
            # 获取返回数据
            with transaction.atomic():
                ret_user = user_ctrl.select_user(request=request, username=username)
                ret['ret_user'] = ret_user

                ret_theme = models.Theme.objects.all().order_by('-create_date')[:5]
                ret['ret_theme'] = ret_theme

                ret_notice = models.Notice.objects.all().order_by('-create_time')[:5]
                ret['ret_notice'] = ret_notice

            return render_to_response('winter_sakura/index.html', ret)
        else:
            with transaction.atomic():
                ret_theme = models.Theme.objects.all().order_by('-create_date')[:5]
                ret['ret_theme'] = ret_theme

                ret_notice = models.Notice.objects.all().order_by('-create_time')[:5]
                ret['ret_notice'] = ret_notice
            return render_to_response('winter_sakura/index.html', ret)
    else:
        return render_to_response('winter_sakura/index.html')


# 退出登录用
def logout(request,*args, **kwargs):
    response = redirect('/index/')
    # 清空cookies,session
    try:
        del request.session['login']
    except KeyError:
        pass

    response.delete_cookie('username')
    response.delete_cookie('is_login')
    return response


# 个人中心
@deco_shade.deco_before(login_check.check_login)
def person(request,*args, **kwargs):
    # 定义返回数据
    ret = {}
    username = request.COOKIES.get('username', '')

    # 获取用户信息和考勤信息
    with transaction.atomic():
        ret_user = user_ctrl.select_user(request=request, username=username)
        ret_check_info = check_info_ctrl.select_check_info(username=username, num=5)

        ret['ret_user'] = ret_user
        ret['ret_check_info'] = ret_check_info

    # 跳转页面
    return render_to_response('winter_sakura/person.html',ret)


# 签到（ajax）
@deco_shade.deco_before(login_check.check_login)
def ajax_check_in(request, *args, **kwargs):
    ret = {}
    if request.is_ajax():
        check_type = request.POST.get('type', 0)
        # 获取部门id
        username = request.session.get('username', '')
        staff_id = models.Staff.objects.filter(username=username)[0]
        dept_id = models.Staff.objects.filter(username=username)[0].staff_dept
        check_type = models.CheckType.objects.get(id=check_type)

        # 添加签到信息
        with transaction.atomic():
            ret_check_info = models.CheckInfo.objects.create(dept_id=dept_id, check_type=check_type, staff_id=staff_id)
            models.Staff.objects.filter(username=username).update(state=1)

            # 获取签到时间和设定上班时间
            arrive_time = ret_check_info.check_time.time()
            setting_time = models.TimeSetting.objects.get(setting=1).value

            # 比较，判断是否迟到
            if arrive_time > setting_time:
                models.Staff.objects.filter(username=username).update(day_note=1)

            else:
                models.Staff.objects.filter(username=username).update(day_note=4)

        # 获取返回信息
        ret['ret_check_type'] = ret_check_info.check_type.type_name
        ret['ret_check_time'] = ret_check_info.check_time.strftime("%Y-%m-%d  %H:%M")
        return JsonResponse(ret)


# 签退（ajax）
@deco_shade.deco_before(login_check.check_login)
def ajax_check_out(request,*args, **kwargs):
    ret = {}
    if request.is_ajax():
        check_type = request.POST.get('type', 0)
        # 获取部门id
        username = request.session.get('username', '')
        staff_id = models.Staff.objects.filter(username=username)[0]
        dept_id = models.Staff.objects.filter(username=username)[0].staff_dept
        check_type = models.CheckType.objects.get(id=check_type)
        check_type_in = models.CheckType.objects.get(id=1)

        # 如果签退时没有签到，则自动签到
        if models.Staff.objects.filter(username=username)[0].state == 0:
            ret_check_info_in = models.CheckInfo.objects.create(dept_id=dept_id, check_type=check_type_in, staff_id=staff_id)

            # 获取签到时间和设定上班时间
            arrive_time = ret_check_info_in.check_time.time()
            setting_time = models.TimeSetting.objects.get(setting=1).value

            # 比较，判断是否迟到
            if arrive_time > setting_time:
                models.Staff.objects.filter(username=username).update(day_note=1)
            else:
                models.Staff.objects.filter(username=username).update(day_note=4)

            ret['ret_check_type_in'] = ret_check_info_in.check_type.type_name
            ret['ret_check_time_in'] = ret_check_info_in.check_time.strftime("%Y-%m-%d  %H:%M")
            ret['check_in'] = 1

        # 添加签退信息
        with transaction.atomic():
            ret_check_info = models.CheckInfo.objects.create(dept_id=dept_id, check_type=check_type, staff_id=staff_id)
            models.Staff.objects.filter(username=username).update(state=2)

            # 获取签退时间和设定下班时间
            out_time = ret_check_info.check_time.time()
            setting_time = models.TimeSetting.objects.get(setting=2).value

            # 比较，判断是否早退
            if out_time < setting_time:
                if models.Staff.objects.filter(username=username)[0].day_note == 1:
                    models.Staff.objects.filter(username=username).update(day_note=3)
                else:
                    models.Staff.objects.filter(username=username).update(day_note=2)
            else:
                models.Staff.objects.filter(username=username).update(day_note=4)

        # 获取返回信息
        ret['ret_check_type'] = ret_check_info.check_type.type_name
        ret['ret_check_time'] = ret_check_info.check_time.strftime("%Y-%m-%d  %H:%M")
        return JsonResponse(ret)


# 请假提交
@deco_shade.deco_before(login_check.check_login)
def leave_publish(request,*args, **kwargs):
    ret = {}
    if request.method == 'POST':
        start_date = request.POST.get('start_time',None)
        end_date = request.POST.get('end_time',None)
        reason = request.POST.get('reason',None)
        username = request.COOKIES.get('username', '')
        ret_user = user_ctrl.select_user(request=request, username=username)

        # 保存请假信息
        with transaction.atomic():
            check_type_in = models.CheckType.objects.get(id=3)
            ret_check_info = models.CheckInfo.objects.create(dept_id=ret_user.staff_dept, check_type=check_type_in,
                                                             staff_id=ret_user, remarks='未查看')
            models.Leave.objects.create(reason=reason, start_date=start_date, end_date=end_date, staff_id = ret_user,
                                        staff_no = ret_user.staff_no, check_id = ret_check_info)
        return redirect('/person/', ret)


# 人事管理
@deco_shade.deco_before(login_check.check_login)
def master(request,*args, **kwargs):
    # 定义返回数据
    ret = {}
    username = request.COOKIES.get('username', '')

    # 返回用户信息
    with transaction.atomic():
        ret_user = user_ctrl.select_user(request=request, username=username)
        # 判断用户类型
        if ret_user.user_type_id != 2:
            return redirect('/index/', ret)

        ret['ret_user'] = ret_user

        # 返回请假信息
        ret_leave_info = system_ctrl.get_leave_info()
        ret['ret_leave_info'] = ret_leave_info

        # 返回设定时间
        ret['ret_setting_1'] = models.TimeSetting.objects.get(setting=1)
        ret['ret_setting_2'] = models.TimeSetting.objects.get(setting=2)

    return render_to_response('winter_sakura/master.html', ret)


# 考勤信息查看
@deco_shade.deco_before(login_check.check_login)
def check_info_view(request,*args, **kwargs):
    # 定义返回数据
    ret = {}
    return render_to_response('winter_sakura/registerInfo.html', ret)


# 公司公告发布
@deco_shade.deco_before(login_check.check_login)
def publish_notice(request,*args, **kwargs):
    ret ={}
    username = request.COOKIES.get('username', '')
    ret_user = user_ctrl.select_user(request=request, username=username)
    ret['ret_user'] = ret_user

    if request.method == 'GET':
        return render_to_response('winter_sakura/publish.html' ,ret)

    if request.method == 'POST':
        notice_text = request.POST.get('publishContent',None)
        with transaction.atomic():
            models.Notice.objects.create(notice_text=notice_text,pub_user = ret_user)
        return redirect('/index/' ,ret)


# 考勤信息（详细）
@deco_shade.deco_before(login_check.check_login)
def attendance_info(request,*args, **kwargs):
    ret = {}
    return render_to_response('winter_sakura/registerInfo.html', ret)


# 设置签到签退时间（ajax）
@deco_shade.deco_before(login_check.check_login)
def check_time_setting_ajax(request,*args, **kwargs):
    ret = {}
    if request.is_ajax():
        # 获取设置时间
        setting_1 = request.POST.get('setting_1',None)  # 上班时间
        setting_2 = request.POST.get('setting_2',None)  # 下班时间

        # 保存设置时间
        with transaction.atomic():
            models.TimeSetting.objects.filter(setting=1).update(value=setting_1)
            models.TimeSetting.objects.filter(setting=2).update(value=setting_2)

        ret['ret_time_1'] = setting_1
        ret['ret_time_2'] = setting_2
        return JsonResponse(ret)


# 主题页面
@deco_shade.deco_before(login_check.check_login)
def theme(request, page=1):
    # 定义初始数据
    url = '/theme/'
    page = page
    item_num = 5
    username = request.COOKIES.get('username','')
    with transaction.atomic():
        ret_user = models.Staff.objects.get(username=username)

        # 获取返回数据
        ret = paging_ctrl.theme_paging(url=url, page=page, item_num=item_num)
        ret['ret_user'] = ret_user

    return render_to_response('winter_sakura/community.html', ret)


# 回复页面(详细页面)
@deco_shade.deco_before(login_check.check_login)
def theme_part(request, theme_id=0, page=1):
    # 定义初始数据
    url = '/note/id' + str(theme_id) + '/'
    page = page
    item_num = 5
    username = request.COOKIES.get('username','')

    with transaction.atomic():
        ret_user = models.Staff.objects.get(username=username)

        # 获取返回数据
        ret = paging_ctrl.reply_paging(url=url, page=page,theme_id=theme_id, item_num=item_num)
        ret['ret_user'] = ret_user

    response = render_to_response('winter_sakura/communityDetail.html', ret)
    response.set_cookie('theme_id', theme_id)
    return response


# 主题发布
def theme_publish(request):
    ret = {}
    username = request.COOKIES.get('username','')
    if request.method == 'POST':
        title = request.POST.get('publishTitle',None)
        content = request.POST.get('publishContent',None)
        if title is None or content is None:
            return redirect('/theme/page1')

        # 存入数据库
        with transaction.atomic():
            user = models.Staff.objects.get(username=username)
            ret_data = models.Theme.objects.create(title=title, content=content, user=user)

        return redirect('/theme/page1')


# 主题回复
def theme_reply(request):
    ret = {}
    username = request.COOKIES.get('username','')
    if request.method == 'POST':
        theme_id = request.COOKIES.get('theme_id', 1)
        content = request.POST.get('replayContent',None)
        if content is None:
            return redirect('/note/id'+str(theme_id)+'/page1')

        # 存入数据库
        with transaction.atomic():
            user = models.Staff.objects.get(username=username)
            set_count = models.Theme.objects.filter(id=theme_id)
            set_count.update(reply_count=set_count[0].reply_count+1)

            theme_k = models.Theme.objects.get(id=theme_id)
            ret_data = models.Reply.objects.create(content=content, user=user, theme=theme_k)

        return redirect('/note/id'+str(theme_id)+'/page1')


# 请假同意（ajax）
@deco_shade.deco_before(login_check.check_login)
def access(request):
    ret = {}
    if request.is_ajax():
        leave_id = request.POST.get('leave_id',None)

        with transaction.atomic():
            models.Leave.objects.filter(check_id=leave_id).update(state=1)
            models.CheckInfo.objects.filter(id=leave_id).update(remarks='已通过')

    return JsonResponse(ret)


# 请假驳回(ajax)
@deco_shade.deco_before(login_check.check_login)
def unaccess(request):
    ret = {}
    if request.is_ajax():
        leave_id = request.POST.get('leave_id',None)

        with transaction.atomic():
            models.Leave.objects.filter(check_id=leave_id).update(state=2)
            models.CheckInfo.objects.filter(id=leave_id).update(remarks='已驳回')

    return JsonResponse(ret)


# 考勤记录查看
@deco_shade.deco_before(login_check.check_login)
def check_record(request):
    ret = {}
    username = request.COOKIES.get('username','')
    with transaction.atomic():
        ret_data = models.CheckInfo.objects.all().order_by('-check_time')[:20]
        ret['ret_data'] = ret_data

        ret_user = user_ctrl.select_user(request=request, username=username)
        ret['ret_user'] = ret_user

    return render_to_response('winter_sakura/registerInfo.html', ret)


# 生成统计报表
@deco_shade.deco_before(login_check.check_login)
def statistics(request):
    ret = {}
    if request.is_ajax():
        with transaction.atomic():
            staff_count = models.Staff.objects.all().count()  # 总人数
            uncheck_staff = models.Staff.objects.filter(day_note=0).count()  # 缺勤员工数
            check_staff = models.Staff.objects.filter(day_note=4).count()   # 正常考勤员工数

            late_staff = models.Staff.objects.filter(day_note=1).count()  # 迟到员工数
            # 这里 leave_staff 代表早退人数
            leave_staff = models.Staff.objects.filter(day_note=2).count()   # 早退员工数

            late_and_leave_staff = models.Staff.objects.filter(day_note=3).count() # 迟到早退员工数

            # 生成日志文本
            daily_text = ""
            temp = ""
            uncheck_staff_text = models.Staff.objects.filter(day_note=0)
            for i in uncheck_staff_text:
                temp = temp + i.true_name +'('+i.staff_no+')'
            uncheck_staff_text = temp

            temp = ""
            check_staff_text = models.Staff.objects.filter(day_note=4)
            for i in check_staff_text:
                temp = temp + i.true_name +'('+i.staff_no+')'
            check_staff_text = temp

            temp = ""
            late_staff_text = models.Staff.objects.filter(day_note=1)
            for i in late_staff_text:
                temp = temp + i.true_name +'('+i.staff_no+')'
            late_staff_text = temp

            temp = ""
            leave_staff_text = models.Staff.objects.filter(day_note=2)
            for i in leave_staff_text:
                temp = temp + i.true_name +'('+i.staff_no+')'
            leave_staff_text = temp

            temp = ""
            late_and_leave_staff_text = models.Staff.objects.filter(day_note=3)
            for i in late_and_leave_staff_text:
                temp = temp + i.true_name +'('+i.staff_no+')'
            late_and_leave_staff_text = temp

            # 拼接文本
            daily_text = "缺勤人员："+uncheck_staff_text+"  |"+\
                         "正常考勤人员:"+check_staff_text+"  |"+\
                         "迟到人员:"+late_staff_text+"  |"+\
                         "早退人员:"+leave_staff_text+"  |"+\
                         "迟到早退人员:"+late_and_leave_staff_text
            daily_text = mark_safe(daily_text)
            ret_data = models.Daily.objects.create(staff_count=staff_count, uncheck_staff=uncheck_staff,
                                        check_staff=check_staff, late_staff=late_staff,
                                        leave_staff=leave_staff, late_and_leave_staff=late_and_leave_staff,
                                        daily_text=daily_text)

            # 重置员工日常状态
            models.Staff.objects.all().update(day_note=0,state=0)

        # 定义返回值
        ret['staff_count'] = staff_count
        ret['uncheck_staff'] = uncheck_staff
        ret['check_staff'] = check_staff
        ret['late_staff'] = late_staff
        ret['leave_staff'] = leave_staff
        ret['late_and_leave_staff'] = late_and_leave_staff

        # 返回文本定义
        ret['uncheck_staff_text'] = "缺勤人员:"+uncheck_staff_text
        ret['check_staff_text'] = "正常考勤人员:"+check_staff_text
        ret['late_staff_text'] = "迟到人员:"+late_staff_text
        ret['leave_staff_text'] = "早退人员:"+leave_staff_text
        ret['late_and_leave_staff_text'] = "迟到早退人员:"+late_and_leave_staff_text

        ret['daily_text'] = daily_text
        return JsonResponse(ret)


# 查看统计报表
@deco_shade.deco_before(login_check.check_login)
def select_daily(request):
    ret = {}
    if request.is_ajax():
        select_time = request.POST.get('select_time',None)
        with transaction.atomic():
            ret_data = models.Daily.objects.filter(create_time=select_time).order_by('-id')
            if not ret_data.exists():
                ret['flag'] = 0
                ret['msg'] = "未找到相关信息"
            else:
                ret_data = ret_data[0]
                ret['staff_count'] = ret_data.staff_count
                ret['uncheck_staff'] = ret_data.uncheck_staff
                ret['check_staff'] = ret_data.check_staff
                ret['late_staff'] = ret_data.late_staff
                ret['leave_staff'] = ret_data.leave_staff
                ret['late_and_leave_staff'] = ret_data.late_and_leave_staff
                ret['daily_text'] = ret_data.daily_text

                # 返回文本定义
                text_d =  ret_data.daily_text.split('|')

                ret['uncheck_staff_text'] = text_d[0]
                ret['check_staff_text'] = text_d[1]
                ret['late_staff_text'] = text_d[2]
                ret['leave_staff_text'] = text_d[3]
                ret['late_and_leave_staff_text'] = text_d[4]

                ret['flag'] = 1

        return JsonResponse(ret)