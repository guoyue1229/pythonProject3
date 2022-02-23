import hashlib
import json
import time
import os
from common.read_info import ReadYaml
import yaml
from common.get_log import get_log
from common.deal_token import read_token
from string import Template
import random

logger = get_log()
curpath = os.path.abspath(os.path.dirname(__file__))
yamlpath = os.path.abspath(os.path.dirname(curpath) + os.path.sep + 'config/API_config.yml')


class Function:

    def GetNonce(self,api_name):
        nonce = "".join(random.choice("0123456789abcdefghijklmnopqrstuvwsyz")for i in range(20))
        with open(yamlpath,'r',encoding='utf-8') as f:
            read = f.read()
            x = yaml.load(read,Loader=yaml.FullLoader)
            x[api_name]["data"]["Nonce"] = nonce
            with open(yamlpath,'w',encoding="utf-8") as w_f:
                yaml.safe_dump(x,w_f)

    def GetExpressNo(self, Firstname):
        exno = Firstname + "".join(random.choice("0123456789") for i in range(15))
        with open(yamlpath, 'r', encoding='utf-8') as f:
            read = f.read()
            template1 = Template(read)
            c = template1.safe_substitute({"ExpressNo": exno})
            y = yaml.safe_load(c)
            with open(yamlpath, 'w', encoding='utf-8') as w_f:
                yaml.safe_dump(y, w_f)

    def GetTime(self, Time, api_name):
        t = time.time()
        # curpath = os.path.abspath(os.path.dirname(__file__))
        # yamlpath =os.path.abspath(os.path.dirname(curpath)+os.path.sep+'config/API_config.yml')
        # 返回13位时间戳
        if Time == 1:
            reqtime = str(int(round(t * 1000)))
            with open(yamlpath, 'r', encoding='utf-8') as f:
                read = f.read()
                y = yaml.load(read, Loader=yaml.FullLoader)
                y[api_name]["data"]["ReqTime"] = reqtime
                with open(yamlpath, 'w', encoding='utf-8') as w_f:
                    yaml.safe_dump(y, w_f)
        # 返回10位时间戳
        if Time == 2:
            reqtime = str(int(t))
            with open(yamlpath, 'r', encoding='utf-8') as f:
                read = f.read()
                x = yaml.load(read, Loader=yaml.FullLoader)
                x[api_name]["data"]["ReqTime"] = reqtime
                with open(yamlpath, 'w', encoding='utf-8') as w_f:
                    yaml.safe_dump(x, w_f)

    def GetSig(self, api_name, token=None):
        # token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoie1wiVXNlcklkXCI6MTU5MjcyLFwiVGVuYW50SWRcIjo4MDAwMDAwOCxcIlN0YXRpb25JZFwiOm51bGwsXCJTbWFydEJveFNuXCI6bnVsbH0iLCJuYmYiOjE2NDQ0NjE1OTgsImV4cCI6MTY0NTA2NjM5OCwiaWF0IjoxNjQ0NDYxNTk4fQ.6T6aTC0OXn6bntI1ZLHpEUKhJ0Cz937Xv6aKbAGyp_E"
        data = ReadYaml().get_data(api_name=api_name)
        # curpath = os.path.abspath(os.path.dirname(__file__))
        # yamlpath = os.path.abspath(os.path.dirname(curpath) + os.path.sep + "config/API_config.yml")
        arr = []
        DataStr = ""
        for i in sorted(data):
            if i == 'Signature':
                continue
            arr.append(i)
            # print(arr)
        for i in arr:
            if data[i] == "":
                continue
            # 如果遍历的对象是个数组，就去掉数组内冒号前面的空格
            if isinstance(data[i], list):
                data[i] = json.dumps(data[i], separators=(',', ':'))
            DataStr = DataStr + i + "=" + str(data[i]) + "&"
        if token is None:
            DataStr = DataStr[:-1]
            Sig = hashlib.md5(DataStr.encode(encoding='UTF-8')).hexdigest().upper()
            print(Sig)
            try:
                with open(yamlpath, 'r', encoding='utf-8') as f:
                    read = f.read()
                    x = yaml.load(read, Loader=yaml.FullLoader)
                    print(x)
                    y = x[api_name]['data']['Signature']
                    print(y)
                    x[api_name]['data']['Signature'] = Sig
                    print(x[api_name]['data']['Signature'])
                with open(yamlpath, 'w', encoding='utf-8') as w_f:
                    yaml.safe_dump(x, w_f)
            except Exception as e:
                logger.info("读写Signature异常啦~ %s" % e)

        else:
            DataStr = DataStr + "key=" + token
            Sig = hashlib.md5(DataStr.encode(encoding='UTF-8')).hexdigest().upper()
            # print(Sig)
            try:
                with open(yamlpath, 'r', encoding='utf-8') as f:
                    read = f.read()
                    x = yaml.load(read, Loader=yaml.FullLoader)
                    # print(x)
                    y = x[api_name]['data']['Signature']
                    # print(y)
                    x[api_name]['data']['Signature'] = Sig
                    z = x[api_name]['data']['Signature']
                    # print(x[api_name]['data']['Signature'])
                with open(yamlpath, 'w', encoding='utf-8') as w_f:
                    yaml.safe_dump(x, w_f)
            except Exception as e:
                logger.info("读写Signature异常啦~ %s" % e)


if __name__ == '__main__':
    # run=Function().GetSig(api_name='expressin', token=read_token())
    # run=Function().GetTime(Time=2,api_name='expressin')
    #run = Function().GetExpressNo(Firstname="JT")
    run = Function().GetNonce("login")
    # run =
    # Function().GetSig(api_name='expressin', token=read_token())
    # run.GetTime(Time=1)
    # run.GetSig(api_name='login',token=None)
