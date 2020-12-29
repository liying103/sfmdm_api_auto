import configparser
from utils.file_utils import fileutils
from path import ini_path

'''
读取ini文件
'''
class ConfigUtils:
    def __init__(self,config_path = ini_path):
        self.config = configparser.ConfigParser()
        self.path = fileutils.local_file(config_path)
        self.config.read(self.path)


    def get_inidata(self,section,option):
        '''
        :param section: 节点名称
        :param option:  节点下item的key
        :return: value
        '''
        value = self.config.get(section,option)
        return value

configutils= ConfigUtils()

if __name__ == '__main__':
    a = configutils.get_inidata('test','host')
    print(a)






