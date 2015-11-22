# -*- coding: utf-8 -*-

"""
所有的基础校验模块

遵循原则:
基础校验:
输入: 校验对象
返回: 成功, 失败

集成校验:
输入: 校验对象, 访问路径
返回: 成功+None, 失败+错误原因

"""

def is_int(i, n):
    """
    判断是否为整数
    :param i: 变量
    :param n: 变量名
    """
    if isinstance(i, int):
        return True, None
    else:
        return False, u"{}非整数".format(n)

def is_str(s, n):
    """
    判断是否为字符串
    """
    if isinstance(s, (str, unicode)):
        return True, None
    else:
        return False, u"{}非字符串".format(n)

def is_legal_amt(a, n):
    """
    判断是否合法金额
    """
    if a > 0:
        return True, None
    else:
        return False, u"{}:{}非法金额".format(n, a)

def is_legal_bank_card(s, n):
    """
    判断是否是合法银行卡
    """
    if n.strip() == "" or len(s) > 20:
        return False, u"{}:{}非法银行卡".format(n, s)
    return True, None

def is_legal_digit(s, n):
    """
    判断是否是合法数字字符串
    """
    if n.isdigit():
        return True, None
    return False, u"{}:{}非法数字字符串".format(n, s)
