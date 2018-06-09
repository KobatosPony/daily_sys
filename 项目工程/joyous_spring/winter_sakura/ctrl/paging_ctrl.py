from winter_sakura import models
from django.utils.safestring import mark_safe   # django自带安全字符串化模块


# 回复分页
def reply_paging(url, page, theme_id, item_num):
    # 定义变量
    ret = {}
    page = int(page)
    start = (page - 1) * item_num
    end = page * item_num

    # 获取当前页数据
    ret_theme_data = models.Theme.objects.filter(id=theme_id)[0]
    ret_reply_data = models.Reply.objects.filter(theme_id=ret_theme_data).order_by('-create_date')[start:end]

    # 获取总数目并计算页数
    all_count= models.Reply.objects.filter(theme_id=ret_theme_data).count()
    # 获取总页数 all_page
    temp = divmod(all_count, item_num)
    if temp[1] == 0:
        all_page = temp[0]
    else:
        all_page = temp[0] + 1

    if all_page == 0:
        all_page = 1

    # 定义分页a标签
    page_html = []
    # 首页html
    first_html = "<a href='%spage%d' class='pageClass'>首页</a>"%(url, 1)
    page_html.append(first_html)

    # 上一页
    if page > 1:
            page_html.append("<a href='%spage%d' class='pageClass'>上一页</a>"%(url, page-1))

    # 中间页
    if all_page > 10:
        # 定义获取范围
        limit = 4

        # 添加代表省略号的标签
        if page > limit+1:
            page_html.append("<a href='#' class='pageClass'>...</a>")
        # 得到可获取页面列表
        page_list = range(all_page)[(page-limit-1 if page-limit-1>=0 else 0):page+limit]
        for i in page_list:
            if page == i+1:
                page_html.append("<a href='%spage%d' class='pageClass pageCurrent'>%d</a>"%(url, i+1, i+1))
            else:
                page_html.append("<a href='%spage%d' class='pageClass'>%d</a>"%(url, i+1, i+1))

        # 添加代表省略号的标签
        if page < all_page - limit:
            page_html.append("<a href='#' class='pageClass'>...</a>")

    else:
        for i in range(all_page):
            if page == i+1:
                page_html.append("<a href='%spage%d' class='pageClass pageCurrent'>%d</a>"%(url, i+1, i+1))
            else:
                page_html.append("<a href='%spage%d' class='pageClass'>%d</a>"%(url, i+1, i+1))

    # 下一页
    if page < all_page:
            page_html.append("<a href='%spage%d' class='page_a'>下一页</a>"%(url, page+1))

    # 尾页html
    end_html = "<a href='%spage%d' class='pageClass'>尾页</a>"%(url, all_page)
    page_html.append(end_html)

    page = mark_safe(''.join(page_html))

    # 定义返回数据
    ret['ret_theme_data'] = ret_theme_data
    ret['ret_reply_data'] = ret_reply_data
    ret['page_html'] = page
    return  ret


# 主题分页
def theme_paging(url, page, item_num):
    # 定义变量
    ret = {}
    page = int(page)
    start = (page - 1) * item_num
    end = page * item_num

    # 获取当前页数据
    ret_data = models.Theme.objects.all().order_by('-create_date')[start:end]

    # 获取总数目并计算页数
    all_count= models.Theme.objects.all().count()
    # 获取总页数 all_page
    temp = divmod(all_count, item_num)
    if temp[1] == 0:
        all_page = temp[0]
    else:
        all_page = temp[0] + 1

    if all_page == 0:
        all_page = 1

    # 定义分页a标签
    page_html = []
    # 首页html
    first_html = "<a href='%spage%d' class='pageClass'>首页</a>"%(url, 1)
    page_html.append(first_html)

    # 上一页
    if page > 1:
            page_html.append("<a href='%spage%d' class='pageClass'>上一页</a>"%(url, page-1))

    # 中间页
    if all_page > 10:
        # 定义获取范围
        limit = 4

        # 添加代表省略号的标签
        if page > limit+1:
            page_html.append("<a href='#' class='pageClass'>...</a>")
        # 得到可获取页面列表
        page_list = range(all_page)[(page-limit-1 if page-limit-1>=0 else 0):page+limit]
        for i in page_list:
            if page == i+1:
                page_html.append("<a href='%spage%d' class='pageClass pageCurrent'>%d</a>"%(url, i+1, i+1))
            else:
                page_html.append("<a href='%spage%d' class='pageClass'>%d</a>"%(url, i+1, i+1))

        # 添加代表省略号的标签
        if page < all_page - limit:
            page_html.append("<a href='#' class='pageClass'>...</a>")

    else:
        for i in range(all_page):
            if page == i+1:
                page_html.append("<a href='%spage%d' class='pageClass pageCurrent'>%d</a>"%(url, i+1, i+1))
            else:
                page_html.append("<a href='%spage%d' class='pageClass'>%d</a>"%(url, i+1, i+1))

    # 下一页
    if page < all_page:
            page_html.append("<a href='%spage%d' class='page_a'>下一页</a>"%(url, page+1))

    # 尾页html
    end_html = "<a href='%spage%d' class='pageClass'>尾页</a>"%(url, all_page)
    page_html.append(end_html)

    page = mark_safe(''.join(page_html))

    # 定义返回数据
    ret['ret_theme'] = ret_data
    ret['page_html'] = page
    return  ret
