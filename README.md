# sfmdm_api_auto
201222：
需求：
1.三个环境;
2.每天定时检查：验证接口正常跑通，流程化，检查请求，字段，格式；
3.报告
步骤：
1.config中创建ini文件，测试环境，生产环境，正式环境
2.创建各个模块，包括数据，log，report，testcase，utils
3.git进行源码管理
4.jenkins进行持续集成
5.utils中创建编写file_utils，文件，相对路径转换为绝对路径，其中
  返回绝对路径：os.path.abspath("..")  #上级目录的绝对路径
  
201225：
1.学习configparser模块
2.封装config_utils
3.@property装饰器：将方法转换为属性访问
4.优化file_utils 中代码,使用os.path.abspath(相对路径转换为绝对路径)
5.若a,b,c,d,e= ['sadhs','shajkd',11,1213,343],那么abcde即对应列表中的五个值

201227:
1.封装excel_utils 模块，包阔读取合并单元格，读取总行数，总列数
2.学习字典的setdefaultf方法，已存在就不变，没有就增加默认
3.学习jsonpath取值
4.封装data_analysis方法

210106:
1.request_utils模块编写，get方法
2.定义self.temporary = {} 临时变量，存储取值代码中所获得的值
3.防止乱码:response.encoding = response.apparent_encoding

210109:
1.request_utils post方法，分步执行，变量提取，赋值，校验
其中get参数，post参数，header参数 存在空的情况处理
2.check_utils 封装，根据属性执行相对应的方法
3.pytest 参数化执行 
