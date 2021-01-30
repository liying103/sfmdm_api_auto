import pytest
import time
from utils.file_utils import fileutils
from path import report_path
from utils.SmtpReport import SmtpReport
from utils.config_utils import configutils



reports_path = fileutils.local_file(report_path)
report_ = time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime())

report_html ='%s/%s.html'%(reports_path,report_)
email = SmtpReport(configutils.get_inidata('email','receiver'))
print(report_html)




pytest.main(['-s','testcases'])
#email.email_image_send(report_html,"接口自动化测试报告")
