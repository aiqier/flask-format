# -*- encoding: utf-8 -*-

"""
入门: 第一个单元测试
"""

import os
import sys
sys.path.append(os.path.join(sys.path[0], '../'))

import nose
import nose.tools
import logging

from app.utils.taout import LogAnalyzer

def setup():
    """
    不建议使用setup, setup会执行一次
    """
    pass

def teardown():
    """
    几乎永远都不会用到teardown, teatdown会执行一次
    """
    pass


def test_isvalidfilename_badextension_returnsfalse():
    """
    测试函数命名三要素
    UnitOfWorkName:被测试的方法
    Scenario: 测试进行的假设条件
    ExpectedBehavior: 在测试场景指定的条件下，你对被测试方法命名行为的预期
    """
    expect = False
    analyzer = LogAnalyzer()
    actual = analyzer.is_valid_logfilename("xxx.foo")
    assert expect == actual

def test_isvalidfilename_goodextension_returnstrue():
    """
    正检验
    """
    expect = True
    analyzer = LogAnalyzer()
    actual = analyzer.is_valid_logfilename('xxx.SLF')
    assert expect == actual

def isvalidfilename_extension_returns(extension, ret):
    """
    可传入参数测试
    """
    expect = ret
    analyzer = LogAnalyzer()
    actual = analyzer.is_valid_logfilename(extension)
    assert expect == actual

def test_isvalidfilename_params_extension_returns_params():
    """
    传入参数,方便使用
    """
    exten_rets = {
        "xxx.foo": False,
        "xxx.SLF": True,
        "xxx.slf": False
        }
    for k,v in exten_rets.items():
        isvalidfilename_extension_returns(k, v)

def test_isvalidfilename_emptyfilename_throwexception():
    """
    抛出指定异常
    """
    analyzer = LogAnalyzer()
    nose.tools.assert_raises(ValueError, analyzer.is_valid_logfilename,"")

def test_isvalidfilename_whencalled_changeswaslastfilenamevalid():
    """
    测试系统状态的改变而非返回值
    """
    analyzer = LogAnalyzer()
    analyzer.is_valid_logfilename("xxx.SLF")
    assert True == analyzer.was_last_file_name_valid

@nose.tools.with_setup(setup, teardown)    
def test_isvalidfilename_xxxextension_returnsxxx():
    """
    指定在此函数前和后运行setup,teardown
    """
    pass
        
if __name__ == "__main__":
    nose.runmodule()
