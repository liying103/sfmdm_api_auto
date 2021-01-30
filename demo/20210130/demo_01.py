
import time

from nb_log import LogManager



time_= time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
log_name ='%s.log'%time_
print(log_name)
logger = LogManager('sfmdm_api_auto').get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                  log_filename=log_name)
logger.info("hahah")