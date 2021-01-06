# -*- coding: UTF-8 -*-
import requests
import re
from utils.config_utils import configutils

class RequestUtils:

    def __init__(self):
        self.conf = configutils
        self.sesson = requests.session()
        self.temporary = {} # 临时变量

    def get(self,case_info):
        url = self.conf.get_inidata('test','host')+ case_info['请求地址']
        temporary_list  = re.findall("\${\\w+}",case_info['请求参数(get)'])
        for temporary in temporary_list:
            case_info['请求参数(get)'] = case_info['请求参数(get)'].replace(temporary,
                                     "%s"%self.temporary[temporary[-2:1]])
        response = self.sesson.get(url = url,params= case_info['请求参数(get)'],headers= case_info['请求头部信息'])
        response.encoding = response.apparent_encoding
        return response





if __name__ == '__main__':
    data1 = [{'测试用例编号': 'imcp_case_01', '测试用例名称': '用户登陆验证', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_02', '接口名称': 'login_check', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/check', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..success', '取值变量': 'success', '断言类型': '', '预期结果': ''}, {'测试用例编号': 'imcp_case_01', '测试用例名称': '获取登陆token', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_03', '接口名称': 'login_token', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/token', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..access_token', '取值变量': 'access_token', '断言类型': '', '预期结果': ''}, {'测试用例编号': 'imcp_case_01', '测试用例名称': '用户登陆状态', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_04', '接口名称': 'login_status', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/user', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..userId', '取值变量': 'userId', '断言类型': '', '预期结果': ''}]
    request = RequestUtils()
    print(request.get(data1[0]))
