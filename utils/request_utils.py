# coding=utf-8
import requests
import re
import json
import jsonpath
from utils.config_utils import configutils
from utils.check_utils import CheckUtils
class RequestUtils:

    def __init__(self):
        self.conf = configutils
        self.session = requests.session()
        self.temporary = {} # 临时变量

    def __get(self,case_info):
        url = self.conf.get_inidata('test','host')+ case_info['请求地址']
        temporary_list  = re.findall("\${\\w+}",case_info['请求参数(get)'])
        for temporary in temporary_list:
            case_info['请求参数(get)'] = case_info['请求参数(get)'].replace(temporary,
                                     "%s"%self.temporary[temporary[-2:1]])

        if not case_info['请求参数(get)']:
            get_params = None
        else:
            get_params = json.loads(case_info['请求参数(get)'])
        if not case_info['请求头部信息']:
            header_params = None
        else:
            header_params = json.loads(case_info['请求头部信息'])
        response = self.session.get(url=url,headers= header_params,params = get_params)
        response.encoding = response.apparent_encoding

        if case_info['取值方式'] == 'jsonpath':
            self.temporary[case_info['取值变量']] = jsonpath.jsonpath(response.json(),case_info['取值代码'])
        elif case_info['取值方式'] == 're':
            self.temporary[case_info['取值变量']] = re.findall(case_info['取值代码'],response.text)[0]


        rseult = CheckUtils(response).run_check(case_info["断言类型"], case_info["预期结果"])
        return rseult

    def __post(self, case_info):
        url = self.conf.get_inidata('test', 'host') + case_info['请求地址']
        get_variables_list = re.findall('\\${\w+}', case_info['请求参数(get)'])
        for variables in get_variables_list:
            case_info['请求参数(get)'] = case_info['请求参数(get)'].replace(variables,
                                                                            '"%s"' % self.temporary[
                                                                                variables[2:-1]])
        post_variables_list = re.findall('\\${\w+}', case_info['请求参数(post)'])
        for variables in post_variables_list:
            case_info['请求参数(post)'] = case_info['请求参数(post)'].replace(variables,
                                                                              '"%s"' % self.temporary[
                                                                                  variables[2:-1]])
        if not case_info['请求参数(get)']:
            get_params = None
        else:
            get_params = json.loads(case_info['请求参数(get)'])
        if not case_info['请求参数(post)']:
            post_params = None
        else:
            post_params = json.loads(case_info['请求参数(post)'])
        if not case_info['请求头部信息']:
            header_params = None
        else:
            header_params = json.loads(case_info['请求头部信息'])
        response = self.session.post(url=url,headers= header_params,params = get_params,json = post_params)
        response.encoding = response.apparent_encoding
        if case_info['取值方式'] == 'jsonpath':
            self.temporary[case_info['取值变量']] = jsonpath.jsonpath(response.json(), case_info['取值代码'])[0]
        elif case_info['取值方式'] == 're':
            self.temporary[case_info['取值变量']] = re.findall(case_info['取值代码'], response.text)[0]

        rseult = CheckUtils(response).run_check(case_info["断言类型"],case_info["预期结果"])
        return rseult

    def request(self,case_info):
        if case_info['请求方式'] == 'get':
            result = self.__get(case_info)
        elif case_info['请求方式'] == 'post':
            result = self.__post(case_info)
        else:
            result = {'code':2,"message":"请求方式不支持","check_result":False}
        return result
    def request_by_step(self,case_steps):
        for case_step in case_steps:
            rseult = self.request(case_step)
            print(rseult)
            if rseult['check_result'] == False:
                break
        return rseult



if __name__ == '__main__':
    data =  [{'测试用例编号': 'imcp_case_01', '测试用例名称': '用户登陆', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_01', '接口名称': 'login_in', '请求方式': 'post', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/login', '请求参数(get)': '{"account":"jintang","password":"YbjWkqAY5rEFzvztVjoD3g==","companyAccount":""}', '请求参数(post)': '', '取值方式': 'none', '取值代码': '', '取值变量': '', '断言类型': 'key', '预期结果': 'companyId'}, {'测试用例编号': 'imcp_case_01', '测试用例名称': '用户登陆验证', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_02', '接口名称': 'login_check', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/check', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..success', '取值变量': 'success', '断言类型': 'none', '预期结果': ' '}, {'测试用例编号': 'imcp_case_01', '测试用例名称': '获取登陆token', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_03', '接口名称': 'login_token', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/token', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..access_token', '取值变量': 'access_token', '断言类型': 'none', '预期结果': ''}, {'测试用例编号': 'imcp_case_01', '测试用例名称': '用户登陆状态', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_04', '接口名称': 'login_status', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/user', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..userId', '取值变量': 'userId', '断言类型': 'none', '预期结果': ''}]

    request = RequestUtils()
    print(request.request_by_step(data))



