import pytest
from API.all_api import AllApi
from common.get_log import get_log
logger = get_log()

@pytest.mark.login_getversionv2
class TestLogin():
    #登录用例初始化
    @pytest.fixture(scope="class")
    def init_login(self):
        logger.info("/n ============================= 【登录】测试用例开始 =============================")
        all_login = AllApi()
        return all_login
    @pytest.mark.parametrize("api_name",["login"])
    def test_login(self,api_name,init_login):
        print("\n 用例名称：驿站管理员账号登录\n")
        res = init_login.login_getversionv2(api_name)
        expected = init_login.get_expect('login')
        assert res['Code'] == expected['Code'],"Code的值为：%s" %res['Code']
        assert res['Data']['Token'] is not None,"Token的值为：%s" %res['Data']['Token']

if __name__ == '__main__':
    pytest.main(['-v','test_login.py','--html=C:\\Users\\18838\\Desktop\\python脚本\\pythonProject3\\report\\login_report.html', '--self-contained-html'])


