from django.shortcuts import render_to_response, redirect


# session设置参考
# request.session['username'] = username
# response.set_cookie('username', username, 24*60*60)
# response.set_cookie('is_login', 1, 24*60*60)
# 检测登录状态装饰器函数
def check_login(request,*args,**kwargs):
    # 定义返回页面
    login_html = 'winter_sakura/login.html'
    se_user = request.session.get('username',None)
    co_user = request.COOKIES.get('username', None)
    is_login = request.COOKIES.get('is_login',0)
    if se_user != co_user:                                              # 比较session和cookie中的用户名
        ret = {'msg':"请先登录！"}
        return render_to_response(login_html, {"ret_data":ret})

    elif not is_login:
        ret = {'msg':"请先登录！"}
        return render_to_response(login_html, {"ret_data":ret})

    else:
        return None