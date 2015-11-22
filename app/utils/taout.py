# -*- encoding:utf-8 -*-

"""
The Art of Unit Testing
单元测试的艺术，用python进行翻译的例子
"""

class LogAnalyzer(object):
    def __init__(self):
        self.was_last_file_name_valid = False
        
    def  is_valid_logfilename(self, filename):
        if filename == "" or filename is None:
            raise ValueError(u"值错误")
        if not filename.endswith('.SLF'):
            return False
        
        self.was_last_file_name_valid = True
        return True

    
