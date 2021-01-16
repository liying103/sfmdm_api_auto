import os
from path import  ini_path
from path import log_path

class FileUtils:
    def local_file(self,path):
        current_path = os.path.dirname(__file__)
        expect_path = os.path.abspath(os.path.join(current_path,'..',path))

        return expect_path
# 单例模式：保证类的唯一实例，当前只允许单线程操作
fileutils = FileUtils()

if __name__ == '__main__':

    print(fileutils.local_file(log_path))