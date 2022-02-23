import json

import yaml
import os
import time
from common.deal_token import read_token
from common.get_log import get_log

logger = get_log()


class ReadYaml():
    def read_yml(self):
        # os.path.abspath:返回绝对路径  os.path.dirname：返回文件路径
        curPath = os.path.abspath(os.path.dirname(__file__))
        # print(curPath)
        # os.path.sep 分隔符"/"
        yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "config/API_config.yml")
        # print(yamlPath)
        # 开启只读模式
        f = open(yamlPath, 'r', encoding='utf-8')
        # 读取yml数据
        content = f.read()
        # print(content)
        # 转化为列表或者字典
        contents = yaml.load(content, Loader=yaml.FullLoader)
        return contents

    def get_url(self, api_name):
        content = self.read_yml()
        new_url = content['host'] + content[api_name]['url']
        logger.info("请求路径：" + str(new_url))
        return new_url

    def get_method(self, api_name):
        content = self.read_yml()
        content = content[api_name]['method']
        logger.info("请求方式：" + content)
        return content

    def get_jsondata(self, api_name):
        content = self.read_yml()
        data = content[api_name]['data']
        jsondata = json.dumps(data)
        logger.info("json格式入参：" + jsondata)
        return jsondata

    def get_data(self, api_name):
        content = self.read_yml()
        data = content[api_name]['data']
        # print("字典格式入参：", data)
        return data

    def get_headers(self, api_name):
        content = self.read_yml()
        if api_name == 'login':
            logger.info("请求头：" + str(content[api_name]['headers']))
            return content[api_name]['headers']
        elif api_name == "getversionv2":
            logger.info("请求头：" + str(content[api_name]['headers']))
            return content[api_name]['headers']
        else:
            auth = content[api_name]['headers']['Authorization'] + " " + read_token()
            content[api_name]['headers']['Authorization'] = auth
            logger.info("请求头：" + str(content[api_name]['headers']))
            return content[api_name]['headers']

    def get_expected(self, api_name):
        content = self.read_yml()
        return content[api_name]['expected']


if __name__ == '__main__':
    ry = ReadYaml()
    # ry.get_time()
    # ry.read_yml()
    # ReadYaml().get_headers(api_name='login')
    ry.get_headers("getversionv2")
