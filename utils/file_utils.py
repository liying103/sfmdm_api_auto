import os

class FileUtils:
    def local_file(self,path):
        expect_path = os.path.abspath('..')+"/"+path
        return expect_path
# 单例模式：保证类的唯一实例，当前只允许单线程操作
fileutils = FileUtils()

if __name__ == '__main__':
    fileutils.local_file('data')