import pytest
import time

from utils.data_analysis import DataAnalysis
from utils.request_utils import request
from nb_log import LogManager

time_= time.strftime("%Y-%m-%d", time.localtime())
log_name ='%s.log'%time_
logger = LogManager('sfmdm_api_auto').get_logger_and_add_handlers(is_add_stream_handler=False,
                                                                  log_filename=log_name)



test_data = DataAnalysis("登陆模块").convert_testcase_data_list()
# print(test_data)
# print(test_data[0]['case_id'])
print(test_data)
# print([test_data['case_id'],test_data['case_step']])

class TestLogin:

    @classmethod
    def setup_class(cls):
        logger.info("$登陆模块$" )


    @pytest.mark.parametrize('test_info',test_data)
    def test_login_case(self,test_info):
        logger.info("$%s_%s$" % (test_info["case_id"],test_info["case_step"][0]['测试用例名称']))
        result = request.request_by_step(test_info["case_step"])
        assert result['check_result'],result['message']



if __name__ == '__main__':
    pytest.main()

