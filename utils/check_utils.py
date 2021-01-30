import json
import jsonpath
import re
import time
from nb_log import LogManager

time_= time.strftime("%Y-%m-%d", time.localtime())
log_name ='%s.log'%time_
logger = LogManager('sfmdm_api_auto').get_logger_and_add_handlers(is_add_stream_handler=False,
                                                                  log_filename=log_name)

class CheckUtils:

    def __init__(self,response_body):
        self.response_body = response_body
        self.type_check ={
            'none':self.check_none,
            'key':self.check_body_key,
            'key_value':self.check_body_key_value,
            're':self.check_re,
            'code':self.check_code,
            'header_key':self.check_header_key,
            'header_key_value':self.check_header_key_value

        }
        self.pass_result = {
            "code": 0,
            "response_reason": self.response_body.reason,
            "response_body": self.response_body.text,
            "response_headers": self.response_body.headers,
            "response_url": self.response_body.url,
            "message": '',
            "check_result": True
        }
        self.fail_result = {
            "code": 1,
            "response_reason": self.response_body.reason,
            "response_body": self.response_body.text,
            "response_headers": self.response_body.headers,
            "response_url": self.response_body.url,
            "message": '',
            "check_result": False
        }

    def check_code(self,check_data):
        if check_data == self.response_body.status_code:
            return self.pass_result
        logger.error('请求失败,预期状态码为:%s,实际状态码为：%s'%(check_data,self.response_body.status_code))
        return self.fail_result
    def __check_key(self,actual_result,check_datas):
        keys = check_datas.split(",")
        for item in keys:
            content = jsonpath.jsonpath(actual_result, "$.." + item)
            if not content:
                logger.error('请求失败,预期结果为:%s,实际结果为：%s' % (keys, content))
                return self.fail_result
        return self.pass_result
    def __check_key_value(self,actual_result,check_datas):
        for key, value in json.loads(check_datas).items():
            content = jsonpath.jsonpath(actual_result, "$.." + key)
            if not content or jsonpath.jsonpath(actual_result, "$.." + key)[0] != value:
                logger.error('请求失败,实际结果中不存在：%s，%s' % (key,value ))
                return self.fail_result
        return self.pass_result

    def check_none(self):
        return self.pass_result
    def check_re(self,check_data):
        data = re.findall(check_data,self.response_body.text)
        if data:
            return self.pass_result
        logger.error('请求失败,预期结果为:%s,实际结果为：%s' % (check_data, self.response_body.text))
        return self.fail_result
    def check_body_key(self,check_datas):
        return self.__check_key(self.response_body.json(),check_datas)
    def check_header_key(self,check_datas):
        return self.__check_key(self.response_body.headers,check_datas)
    def check_body_key_value(self,check_datas):
        return self.__check_key_value(self.response_body.json(),check_datas)
    def check_header_key_value(self,check_datas):
        return self.__check_key_value(self.response_body.headers,check_datas)

    def run_check(self,check_type,check_data):
        if check_type =="none" or not check_data:
            logger.info('check_type= %s'%check_type)
            return self.type_check['none']()
        else:
            return self.type_check[check_type](check_data)



if __name__ == '__main__':
    data =[{'测试用例编号': 'imcp_case_01', '测试用例名称': '用户登陆', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_01', '接口名称': 'login_in', '请求方式': 'post', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/login', '请求参数(get)': '', '请求参数(post)': '{"account":"jintang","password":"YbjWkqAY5rEFzvztVjoD3g==","companyAccount":""}', '取值方式': 'none', '取值代码': '', '取值变量': '', '断言类型': 'none', '预期结果': ''}]
    check = CheckUtils()
    check.check_none()





