# coding=utf8
import re


# 检测违规字符
def check_char(content):
    pattern = re.compile('[A-Za-z0-9\u4e00-\u9fa5’!"#$%&\'()*+,-./:;<=>?@，。★、…【】《》？“”‘！[\\]^`{|}\\s~]+$')
    match = pattern.match(content)
    if match:
        return True
    else:
        return False


# 检测标题
def check_title(title):
    pattern = re.compile('[A-Za-z0-9\u4e00-\u9fa5’!"\'()*+,-./:;，。、…【】《》？“”‘！[\\]^`{|}\\s~]{3,40}$')
    match = pattern.match(title)
    if match:
        return True
    else:
        return False


# 检测内容
def check_content(content):
    pattern = re.compile('[A-Za-z0-9\u4e00-\u9fa5’!"#$%&\'()*+,-./:;<=>?@，。、…【】《》？“”‘！[\\]^`{|}\\s~]{5,700}$')
    match = pattern.match(content)
    if match:
        return True
    else:
        return False
