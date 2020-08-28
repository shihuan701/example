import os
import PyYAML
import json
import aiofiles
import re
'''
读取配置
'''

BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
REPORT_PATH = os.path.join(BASEPATH,'report')
CASE_PATH = os.path.join(BASEPATH,'configs')
SUITES_PATH = os.path.join(BASEPATH,'testsuites')
LOGIN_PATH = os.path.join(BASEPATH,'configs','login.yaml')
WEB_TOKEN_PATH = os.path.join(BASEPATH,'configs','web_login_token.txt')
DBCONFIG = os.path.join(BASEPATH,'configs','mysqlConf.yaml')
URL = os.path.join(BASEPATH,'configs','global_conf.yaml')


def readYamlFile(config):
    with open(config, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.Loader)


def readJsonFile(config):
    with open(config, 'r', encoding='utf-8') as f:
        return json.load(f)

def readFile(config):
    with open(config, 'r', encoding='utf-8') as f:
        return f.read()

def get_Url():
    urls = readYamlFile(URL)
    url = urls[0]['config']['test_url']
    return url

# 异步读取文件
async def load_yaml(dir='',file=''):
    pass

if __name__ == '__main__':
    get_Url()


