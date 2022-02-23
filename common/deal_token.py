import os
import yaml
import json
from common.run_method import  Run_method


# 把token值写到配置文件access_token.yml中
def write_token(res):
    curpath = os.path.abspath(os.path.dirname(__file__))
    #print(curpath)
    yamlpath = os.path.abspath(os.path.dirname(curpath) + os.path.sep + "config/token.yml")
    #print(yamlpath)
    res_json = res.json()
    tokenvalue = {
        'Token': res_json['Data']['Token']
    }
    with open(yamlpath, 'w', encoding='utf-8') as f:
        yaml.dump(tokenvalue, f)

def read_token():
    curpath = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(curpath) + os.path.sep + "config/token.yml")
    with open(path,'r') as f :
        read = f.read()
        #Loader=yaml.FullLoader: 加载全部的yaml文件，防止任意代码调用
        load = yaml.load(read,Loader=yaml.FullLoader)
        return load['Token']

    #file = open(path)
    #read = file.read()
    #load = yaml.load(read, Loader=yaml.FullLoader)
    #file.close()


if __name__ == '__main__':
    run = Run_method()
    method = 'POST'
    url = 'https://butlerapp.diyibox.com/User/Login'
    headers = {
        "User-Agent": "okhttp/3.12.0",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer "
    }
    data = {
	"ReqTime": "1644484748707",
	"Phone": "15011111111",
	"StationId": "",
	"TenantID": "",
	"Nonce": "j13dtwv4692as7ike1cn",
	"TerminalVersion": "1.7.3",
	"AccountID": "",
	"Password": "pPHjpXms4kk=",
	"Signature": "58EE91588DC5145CAD9BE50E359B735E",
	"TerminalType": "Android",
	"AppID": "10100"
}
    jsondata = json.dumps(data)
    res = run.run_main(method,url,headers,jsondata)
    print(res.text)
    #res_json = res.json()
    #write_token(res_json)
    write_token(res)
    print("token的值：",read_token())
