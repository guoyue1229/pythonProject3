import logging

from common.run_method import Run_method
from common.read_info import ReadYaml
from common.deal_token import write_token
from common.get_log import get_log
from common.deal_token import read_token
from common.function import Function
import json

class AllApi(object):
    def __init__(self):
        self.run = Run_method()
        self.read = ReadYaml()
        self.logger = get_log()
        self.function = Function()
    def login_getversionv2(self,api_name):
        #try :
            #获取接口信息
            self.function.GetTime(1,api_name)
            method = self.read.get_method(api_name=api_name)
            url = self.read.get_url(api_name=api_name)
            data = self.read.get_jsondata(api_name=api_name)
            headers = self.read.get_headers(api_name=api_name)
            #jsondata = json.dumps(data)
            response = self.run.run_main(method,url,headers,data)
            #获取token并写入token.yaml中
            if api_name == 'login':
                write_token(res=response)
                response = response.json()
                logging.info("出参：" + json.dumps(response, indent=2, ensure_ascii=False, sort_keys=False))
                return response
            else:
                response = response.json()
                logging.info("出参：" + json.dumps(response, indent=2, ensure_ascii=False, sort_keys=False))
                return response
        #except Exception as e:
            #self.logger.info("接口访问出错了~ %s" % e)
    #其他接口请求封装
    def send_requset(self,api_name):
        #try :
            #获取接口信息
            self.function.GetSig(api_name=api_name, token=read_token())
            url = self.read.get_url(api_name=api_name)
            method = self.read.get_method(api_name=api_name)
            headers = self.read.get_headers(api_name=api_name)
            data = self.read.get_jsondata(api_name=api_name)
            #区分请求方法
            if method == "GET":
                response = self.run.get_send(url,headers,data)
            elif method == "POST":
                response = self.run.post_send(url,headers,data)
            response=response.json()
            #print(json.dumps(response,indent=2,ensure_ascii=False,sort_keys=False))
            jsonres=json.dumps(response,indent=2,ensure_ascii=False,sort_keys=False)
            #sort_keys=False:不按照字典key排序  indent=2:缩进空格式2   ensure_ascii=False：输出中文
            logging.info("出参："+jsonres)
            #print(jsonres["IsSuccess"])
            return response
        #except Exception as e:
            #self.logger.info("接口访问出错了~ %s" % e)

    def get_expect(self,api_name):
        try:
            #获取配置文件里的预期结果
            expect = self.read.get_expected(api_name)
            print(expect)
            return expect
        except Exception as e:
            self.logger.info("获取预期结果出错了~ %s" % e)

if __name__ == '__main__':
    #allapi=AllApi().get_expect(api_name="login")
    #allapi=AllApi().login(api_name="login")
    allapi=AllApi().send_requset(api_name='cancelorder')
