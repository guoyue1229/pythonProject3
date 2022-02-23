import requests

import json

class Run_method:

     def get_send(self,url,headers,data):
         requests.packages.urllib3.disable_warnings()
         response = requests.get(url=url, headers=headers, data=data)
         return response
     def post_send(self,url,headers,data):
         requests.packages.urllib3.disable_warnings()
         response = requests.post(url=url, headers=headers , data=data)
         return  response
     def run_main(self,method,url,headers,data):
         requests.packages.urllib3.disable_warnings()
         if method == 'POST':
            response = self.post_send(url, headers, data)
         else:
            response = self.get_send(url, headers, data)
         return  response
if __name__ == '__main__':
    run = Run_method()
    method = 'POST'
    url = 'http://butlerapp-gray.diyibox.com/User/Login'
    headers = {
        "User-Agent": "okhttp/3.12.0",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer "
    }
    data = {
	"ReqTime": "1638265699877",
	"Phone": "15011111111",
	"Nonce": "sgiioaxsj4hpbtrkbkkf",
	"TerminalVersion": "1.7.1t1",
	"Password": "pPHjpXms4kk=",
	"Signature": "AA593BEE36AB443434412EDF830DB3CA",
	"TerminalType": "Android",
	"AppID": "10100"
}
    jsondata = json.dumps(data)
    print(jsondata)
    response = run.run_main(method,url, headers, jsondata)
    #response = run.run_main(method, url, headers, data)
    print(response.text)