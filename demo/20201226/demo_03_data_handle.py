# setdefualt
data = [{'测试用例编号': 'imcp_case_01', '测试用例模块': '登陆操作接口', '测试用例名称': '用户登陆', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_01', '接口名称': 'login_in', '请求方式': 'post', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/login', '请求参数(get)': '', '请求参数(post)': "{'account':'${username},'password','${password'},'companyAccount':'${conpany}'}", '取值方式': 'jsonpath', '取值代码': '$..companyId', '取值变量': 'companyId', '断言类型': '', '预期结果': ''}, {'测试用例编号': 'imcp_case_01', '测试用例模块': '登陆操作接口', '测试用例名称': '用户登陆验证', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_02', '接口名称': 'login_check', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/check', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..success', '取值变量': 'success', '断言类型': '', '预期结果': ''}, {'测试用例编号': 'imcp_case_01', '测试用例模块': '登陆操作接口', '测试用例名称': '获取登陆token', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_03', '接口名称': 'login_token', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/token', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..access_token', '取值变量': 'access_token', '断言类型': '', '预期结果': ''}, {'测试用例编号': 'imcp_case_01', '测试用例模块': '登陆操作接口', '测试用例名称': '用户登陆状态', '是否依赖': '', '依赖接口名称': '', '用例执行': '是', '用例步骤': 'step_04', '接口名称': 'login_status', '请求方式': 'get', '请求头部信息': '', '请求地址': '/api/sfmdm/v1/auth/user', '请求参数(get)': '', '请求参数(post)': '', '取值方式': 'jsonpath', '取值代码': '$..userId', '取值变量': 'userId', '断言类型': '', '预期结果': ''}]
data_dict = {}

for t in data:
    if t['用例执行'] == '是':
        data_dict.setdefault(t['测试用例编号'],[]).append(data)



