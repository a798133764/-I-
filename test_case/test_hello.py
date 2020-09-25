import random
import pytest
from tools.data import excel_tool
from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
@pytest.mark.dff
def test_signup(pub_data):
    pub_data["userName"] = "自动生成 字符串 4,6 数字字母 liyx"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "phone": "自动生成 手机号",
  "pwd": "1a2s3d",
  "rePwd": "1a2s3d",
  "userName": "${userName}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
@pytest.mark.dff
def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "pwd": "1a2s3d",
  "userName": "${userName}"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token":"$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data,json_path=json_path)
@pytest.mark.dff
def test_recharge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "自动生成 数字 20000,80000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
@pytest.mark.dff
def test_getBills(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询余额'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

@pytest.mark.dff
def test_withdraw(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "cardNo": "自动生成 字符串 10,18 数字",
  "changeMoney": "自动生成 数字 20,80"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
@pytest.mark.dff
def test_getBillss(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询余额'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_accLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户冻结'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_accUnLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户解冻'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_recharges(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "changeMoney": "自动生成 数字 20000,80000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_withdraws(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "cardNo": "自动生成 字符串 10,18 数字",
  "changeMoney": "自动生成 数字 20,80"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_lock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户冻结'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/lock"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'userName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_logins(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "pwd": "1a2s3d",
  "userName": "${userName}"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token":"$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data,json_path=json_path)

def test_unLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户解冻"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/unLock"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'userName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_loginss(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户查询'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "pwd": "1a2s3d",
  "userName": "${userName}"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token":"$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data,json_path=json_path)


def test_get_params(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = "查询单个用户"  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getCustomer"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"phone":"18103909786"}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


def test_get_dududu(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getAll/{}/{}"  .format(1,10)# 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = None
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

@pytest.mark.dff
def test_get_file(pub_data,db):
    file_name = "e:\\sku.xlsx" # 下载文件地址
    method = "GET"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载库存信息'  # allure报告中二级分类
    title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    se = db.select_execute ("SELECT product_code FROM t_prod_product ;")
    params = {"pridCode":random.choice(se)[0]}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    with open(file_name,"wb") as f :
        f.write(r.content)
@pytest.mark.dff
def test_post_file(pub_data):

    file_name = "e:\\sku.xls" # 上传文件地址
    method = "POST"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '盘点库存'  # allure报告中二级分类
    title = "盘点库存"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    files = {"file":open(file_name,'rb')}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

data = excel_tool.get_test_case("d:\\充值测试.xlsx")
@pytest.mark.parametrize("account_name,changeMoney,expect_",data[1],ids=data[0])
def test_post_chonbgzhi(pub_data,account_name,changeMoney,expect_):
    pub_data["account_name"] = account_name
    pub_data["changeMoney"] = changeMoney
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户充值'  # allure报告中二级分类
    title = None # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {"token": "${token}"}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${account_name}",
  "changeMoney": "${changeMoney}
}
    '''
    status_code = 200  # 响应状态码
    expect = "expect_"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)



