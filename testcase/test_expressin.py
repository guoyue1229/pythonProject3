from API.all_api import AllApi
import pytest
from common.get_log import get_log
logger = get_log()

#入库模块测试用例
@pytest.mark.expressin
@pytest.mark.usefixtures('init_setup_teardown','init_token',"init_expressno")
class TestExpressin(object):
    # def __init__(self):
    #     self.getsig = Function
    @pytest.fixture(scope="class")
    def init_expressin(self):
        logger.info("\n ==============================【入库】测试用例开始 ==============================")
        all_request = AllApi()
        return all_request

    @pytest.mark.test
    @pytest.mark.parametrize("api_name",['expressin'])
    def test_expressin_main(self,api_name,init_expressin):
        print("\n用例名称：人工货架入库\n")
        res = init_expressin.send_requset(api_name)
        expected = init_expressin.get_expect(api_name)
        assert res['Code'] == expected['Code'],"Code的值为: %s" % res['Code']
        # api_name = 'expressin'
        # #url = "https://butlerapp.diyibox.com/V2/SendOrder/ExpressIn"
        # url = ReadYaml().get_url(api_name=api_name)
        # #method = "POST"
        # method = ReadYaml().get_method(api_name=api_name)
        # # print(method)0
        # headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+ str(read_token())}
        # #headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoie1wiVXNlcklkXCI6MjgyLFwiVGVuYW50SWRcIjo4MDAwMDAwOCxcIlN0YXRpb25JZFwiOm51bGwsXCJTbWFydEJveFNuXCI6bnVsbH0iLCJuYmYiOjE2NDQ0NjMwOTgsImV4cCI6MTY0NTA2Nzg5OCwiaWF0IjoxNjQ0NDYzMDk4fQ.kHW7Qdk-zcO_ts6NG3Iv7xEBLlbzTBthpcyxHdDTYOw'}
        # #print(headers)
        # data = ReadYaml().get_jsondata(api_name=api_name)
        # # print(type(data))
        # #ata = json.dumps(data)
        # # print(type(data))
        # response = run.run_main(method, url, headers, data)
        # jsonres= response.json()
        # assert jsonres['Code'] == 200,"Code的值为: %s" % jsonres['Code']
if __name__ == '__main__':
    pytest.main(['-v','test_expressin.py', '--html=C:\\Users\\18838\\Desktop\\python脚本\\pythonProject3\\report\\expressin_report.html', '--self-contained-html'])
    #pytest.main(['-v', 'conftest.py', '--html=report/login_report.html', '--self-contained-html'])
    # pytest.main()：main中传入不同的指令用以执行指定测试用例
    # -s: 显示程序中的print / logging输出
    # -v: 丰富信息模式, 输出更详细的用例执行信息
    # -q: 安静模式, 不输出环境信息
    # -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）