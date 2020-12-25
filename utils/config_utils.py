import configparser
from utils.file_utils import fileutils
from path import ini_path


class ConfigUtils:
    def __init__(self,config_path = ini_path):
        self.config = configparser.ConfigParser()
        self.path = fileutils.local_file(config_path)
        print(self.path)
        self.config.read(self.path)


    def get_inidata(self,section,option):
        value = self.config.get(section,option)
        return value

    @property
    def test_02(self):
        a = 'dfdsf'
        return a
configutils= ConfigUtils()

if __name__ == '__main__':
    a = configutils.get_inidata('test','host')
    print(a)
    print(configutils.test_02)





