from API.all_api import AllApi
import pytest
from common.get_log import get_log
from common.function import Function
logger = get_log()
import os

curpath = os.path.abspath(os.path.dirname(__file__))
tokenpath = os.path.abspath(os.path.dirname(curpath) + os.path.sep + "config/token.yml")

@pytest.fixture(scope="session")
def init_setup_teardown():
    logger.info("\n ============================= 测试开始 =============================")
    yield
    # logger.info("\n ============================= token开始清理 =============================")
    # with open(tokenpath,'w',encoding='utf-8') as f:
    #     f.truncate()
    # logger.info("\n ============================= token清理完毕 =============================")
#在执行所有用例之前先执行登录接口，获取toekn
#scope="session" 多用例只需要调用一次
@pytest.fixture(scope="session")
def init_token():
    logger.info("\n ============================= 在用例执行之前，生成token =============================")
    all_login = AllApi()
    all_login.login_getversionv2("login")

@pytest.fixture(scope="session")
def init_expressno():
    logger.info("\n ============================= 在用例执行之前，生成ExpressNo =============================")
    all_getexno = Function()
    all_getexno.GetExpressNo(Firstname='JT')

# @pytest.fixture(scope="session")
# def init_Sig(api_name):
#     logger.info("\n ============================= 用例执行之前，生成Signature并写入API_config文件中 =============================")
#     all_getsig = Function()
#     all_getsig.GetSig(api_name)
