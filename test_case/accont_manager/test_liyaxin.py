import allure
import requests


@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名1")
def test_no_params():
    #r = requests.get("https://www.hao123.com/")
    #print(r.text)
    sess = requests.session()
    r = sess.request(method="GET",url="https://www.hao123.com/")
    r = sess.request(method="GET",url="https://www.hao123.com/")
    print(r.text)

@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名2")
def test_get_path():
    r = requests.request("GET","http://qa.yansl.com:8084/cst/getAll/{pageNum}/{pageSize}".format(pageNum=1,pageSize=10))
    print(r.text)

#def test_no_params():
    # 使用requests.get发送一个get请求。
    # r = requests.get("https://www.baidu.com/")
    # 使用requests.request发送一个get请求。
    # r = requests.request(method="GET",url="https://www.baidu.com/")
    sess = requests.session() # 使用session建立连接
    r = sess.request(method="GET",url="https://www.baidu.com/") # 再发送请求，无论请求多少次，连接只建立
    r = sess.request(method="GET", url="https://www.baidu.com/")
    print(r.text)#text获取响应对象中，响应正文的数据

@allure.feature("get请求")
@allure.story("有参数")
@allure.title("用例名3")
def test_get_query():
    # get请求带参数
    with allure.step("第一步，准备测试数据"):pass
    pa = {"accountName":"xuepl123"} #把get参数都放入一个字典中
    with allure.step("第二步，发送请求"):pass
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params=pa) # 请求时以params关键字传参
    with allure.step("第三步，请求数据"):pass
    allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    print(r.text)


#def test_get_path():
    # get请求参数在path中
    # 使用.format进行字符串格式化
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1,pageSize=10))
    print(r.text)

@allure.feature("get请求")
@allure.story("下载")
@allure.title("用例名4")
def test_get_file(pub_data):
    # get请求下载文件
    with allure.step("第一步，准备测试数据"): pass
    p = {"pridCode":"63803y"}
    h={"token":pub_data["token"]}
    with allure.step("第二步，发送请求"): pass
    r = requests.request("GET","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步，请求数据"):pass
    allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    # r.content获取响应正文的字节码（二进制）
    with open("aa.xls","wb") as f: # with语法 打开文件，并赋值给变量f
        f.write(r.content) # 把响应中的数据写入到文件中

@allure.feature("post请求")
@allure.story("有参数")
@allure.title("用例名5")
def test_post_json():
    data = {
        "pwd":"abc123",
        "userName":"tuu653"
    }
    r = requests.post("http://qa.yansl.com:8084/login",json=data)
    print(r.text)

@allure.feature("post请求")
@allure.story("有参数")
@allure.title("用例名6")
def test_post_formdata(pub_data):
    data = {"userName":"tan242743"
}
    h = {"token": pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/user/lock",data=data,headers=h)
    print(r.text)
@allure.feature("post请求")
@allure.story("上传")
@allure.title("用例名7")
def test_post_upload_file(pub_data):
    # post请求上传文件
    with allure.step("第一步，准备测试数据"): pass
    data = {
        "file": open("aa.xls","rb")
    }
    h = {"token": pub_data["token"]}
    with allure.step("第二步，发送请求"): pass
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=h)  # files关键字发送文件类型数据
    with allure.step("第三步，请求数据"):pass
    allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    print(r.text)