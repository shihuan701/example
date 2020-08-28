from utils.pathBase import LOGIN_PATH
from utils.pathBase import WEB_TOKEN_PATH
from utils.pathBase import readYamlFile
import json
from utils.myrequest import _requests

global null
null=''

LOGINFILE = readYamlFile(LOGIN_PATH)
WEB_URL = LOGINFILE[0].get('config').get('test_url')
INTER = LOGINFILE[1].get('web').get('request').get('url')
REQUEST_TYPE = LOGINFILE[1].get('web').get('request').get('method')
WEB_LOGIN_PARAM = LOGINFILE[1].get('web').get('params')
HEADERS = {"Content-type": "application/json;charset=UTF-8"}

def getWebToken(self):
    r = _requests._post(self,WEB_URL+INTER,WEB_LOGIN_PARAM,HEADERS)
    response_text = eval(r.text)
    token=''
    if response_text['message'] == '操作成功':
        token = response_text['data']['token']
        HEADERS.update(token=token)
        # HEADER写入json文件
    with open(WEB_TOKEN_PATH, 'w') as f:
        f.write(json.dumps(HEADERS))


def sendAuthCode():
    pass




if __name__ == '__main__':
    getWebToken()
