import pytest
import nb_log
from utils.data_analysis import DataAnalysis
from utils.request_utils import RequestUtils


test_data = DataAnalysis().convert_testcase_data_list()
# print(test_data)
# print(test_data[0]['case_id'])
print(test_data)
# print([test_data['case_id'],test_data['case_step']])

class TestCaseAll:


    @pytest.mark.parametrize('test_info',test_data)
    def test_all_case(self,test_info):
        request = RequestUtils()
        print(test_info["case_step"])
        print(type(test_info["case_step"]))
        result = request.request_by_step(test_info["case_step"])
        assert result['check_result'],result['message']



if __name__ == '__main__':
    pytest.main()

