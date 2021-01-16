import time
from nb_log import LogManager
from utils.file_utils import fileutils
from path import log_path


class LogUtils:
    def __init__(self):
            self.logs_path = fileutils.local_file(log_path)
            self.time_= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_name  ='%s/%s.log'%(self.logs_path,time)

    def log(self):

        logger = LogManager('sfmdm_api_auto').get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                    log_filename=self.log_name)

        return logger
log = LogUtils().log()

if __name__ == '__main__':
    log.info('hhh')