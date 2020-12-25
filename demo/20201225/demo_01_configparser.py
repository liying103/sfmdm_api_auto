import configparser
from utils.file_utils import fileutils
from path import ini_path

cfg = configparser.ConfigParser()
ini_path = fileutils.local_file(ini_path)
cfg.read(ini_path,encoding="utf-8")
'''# 1.获取所用的section节点
print(cfg.sections())
# 2.获取指定节点中的key
print(cfg.options('test'))

# 3.获取指定section中option的value
print(cfg.get('test','host'))
#print(cfg.getint('test','host')) # 将获取到值转换为int型,只能转换整数
#print(cfg.getfloat('test','host')) #将获取到值转换为浮点型,只能转换数字
#print(cfg.getboolean('test','host')) #将获取到值转换为bool型,只能转换Ture和false
# 4.获取指点section的所有配置信息
print（cfg.items('test')）
'''
# opti = cfg.items('test')
# print(opti)
# for i in range(0,len(opti)):
#     key = opti[i][0]
#     value = opti[i][1]
#     print('%s====%s'%(key,value))
# opti = [('host', 'http://180.169.51.178:19081/',0), ('username', 'jintang',1), ('password', '123@abAB',2)]
# a,b,c,d,e= ['sadhs','shajkd',11,1213,343]
# print(a,b,c,d,e)
# for key,value,w in opti:
#     print('%s====%s===%s' % (key, value,w))
'''cfg.set('test','username','liyi')
print(cfg.items('test'))
cfg.write(open(ini_path,'w'))
print(cfg.items('test'))'''
# print(cfg.has_section('test')) #是否存在该section
#print(cfg.has_option('test','hos')) #是否存在该option
'''if not cfg.has_section('defau'):
    cfg.add_section('defau')
    cfg.write(open(ini_path,'w'))
if not cfg.has_option('test','test01'):
    cfg.set('test','test01','111')
    cfg.write(open(ini_path,'w'))
print(cfg.items('test'))'''
cfg.remove_section('default')
cfg.remove_option('test','test01')
cfg.write(open(ini_path,'w'))
print(cfg.sections())
print(cfg.items('test'))