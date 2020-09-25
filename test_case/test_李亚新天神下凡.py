import pytest


@pytest.fixture(scope="class")
def pub():
     print("我叫李亚新")
     return "12313"
print(pub)

@pytest.fixture(scope="class") # 作用域
def aa():
    print("fixture函数被运行了")
    return 11

class Test111():
    def test_aa(self,aa):
        print(aa)
    def test_bb(self,aa):
        print(aa)

class Test222():
    def test_aa(self,aa):
        print(aa)
    def test_bb(self,aa):
        print(aa)