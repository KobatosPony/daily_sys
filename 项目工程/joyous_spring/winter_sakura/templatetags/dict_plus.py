from django import template

register = template.Library()


# d参数只会根据key值获取字典，所以html传递参数时要使用嵌套字典
@register.filter(name='dict_plus')
def key(d, key_name):
    value = 0
    if isinstance(d, dict):
        try:
            value = d[key_name]
        except KeyError:
            value = 0
        return value

    else:
        return value

register.filter('key', key)