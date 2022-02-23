import pytest
from API.all_api import AllApi
from common.get_log import get_log
logger = get_log()

@pytest.mark.allapi
@pytest.mark.usefixtures('init_setup_teardown','init_expressno')
class TestAllApi():
    @pytest.fixture()
    def init_allapi(self):
        run_all = AllApi()
        return run_all

    @pytest.mark.parametrize("api_name",["getversionv2"])
    def test_getversionv2(self,api_name,init_allapi):
        res = init_allapi.login_getversionv2(api_name)
        expected = init_allapi.get_expect(api_name)
        assert res["Code"] == expected["Code"],"Code的值为：%s" % res["Code"]

    @pytest.mark.parametrize("api_name", ["login"])
    def test_login(self,api_name,init_allapi):
        res = init_allapi.login_getversionv2(api_name)
        expected = init_allapi.get_expect(api_name)
        assert res["Code"] == expected["Code"],"Code的值为：%s" % res["Code"]

    @pytest.mark.parametrize("api_name",["getstationappadverlist"])
    def test_getstationappadverlist(self,api_name,init_allapi):
        res = init_allapi.send_requset(api_name)
        expected = init_allapi.get_expect(api_name)
        assert res["Code"] == expected["Code"], "Code的值为：%s" % res["Code"]


if __name__ == '__main__':
    pytest.main("-v",'test_allapi.py')