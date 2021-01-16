import pytest
import time
from utils.log_utils import log
from utils.data_analysis import DataAnalysis

from utils.request_utils import RequestUtils



test_data = DataAnalysis("主页图表").convert_testcase_data_list()
# print(test_data)
# print(test_data[0]['case_id'])
print(test_data)
# print([test_data['case_id'],test_data['case_step']])

class TestMainPage:

    @classmethod
    def setup_class(cls):
        log.info("$主页图表$" )


    @pytest.mark.parametrize('test_info',test_data)
    def test_main_page(self,test_info):
        log.info("$%s_%s$" % (test_info["case_id"],test_info["case_step"][0]['测试用例名称']))
        request = RequestUtils()
        result = request.request_by_step(test_info["case_step"])
        assert result['check_result'],result['message']



if __name__ == '__main__':
    pytest.main()

