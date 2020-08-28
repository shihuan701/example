import pytest
from utils.pathBase import CASE_PATH
import os
from utils.myrequest import _requests
from utils.pathBase import readYamlFile
import json

class TestLogin():
    global null
    null = ''

    BASE_URL = 'http://116.62.42.21'
    HEADER = {"Content-type": "application/json;charset=UTF-8"}
    CASEPATH = os.path.join(CASE_PATH, 'login.yaml')
    CASEFILE = readYamlFile(CASEPATH)
    APP_URL = BASE_URL + CASEFILE[0].get('config').get('interface')
    req_type = CASEFILE[0].get('config').get('method')
    show_params = CASEFILE[1:]
    params = CASEFILE[1].get('app').get('params')
    print('#############',show_params)

    @classmethod
    def setup_class(cls):
        pass

    # def test_login(self):
    #     false = False
    #     true = True
    #     r = _requests._post(self,url=TestLogin.APP_URL, arg=TestLogin.params, headers=TestLogin.HEADER)
    #     response_text = eval(r.text)
    #     assert_params = TestLogin.CASEFILE[1].get('app').get('validate')
    #     for i in assert_params:
    #         #比较对象:
    #         assert_param = (i.get('eq'))[0]
    #         assert_value = (i.get('eq'))[1]
    #         assert (response_text.get(assert_param) == assert_value )

    @pytest.mark.parametrize(params,show_params)
    def test_login(self):
        false = False
        true = True
        r = _requests._post(self,url=TestLogin.APP_URL, arg=TestLogin.params, headers=TestLogin.HEADER)
        response_text = eval(r.text)
        assert_params = TestLogin.CASEFILE[1].get('app').get('validate')
        for i in assert_params:
            #比较对象:
            assert_param = (i.get('eq'))[0]
            assert_value = (i.get('eq'))[1]
            assert (response_text.get(assert_param) == assert_value )



    @classmethod
    def teardown_class(cls):
        pass

