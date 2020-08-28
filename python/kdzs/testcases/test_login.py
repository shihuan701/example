import pytest
from utils.pathBase import CASE_PATH
import os
from utils.myrequest import _requests
from utils.getData import GetData
import allure

class TestLogin:
    global null
    null = ''
    BASE_URL = 'http://116.62.42.21'
    HEADER = {"Content-type": "application/json;charset=UTF-8"}
    CASEPATH = os.path.join(CASE_PATH, 'login.yaml')
    getData = GetData(CASEPATH)
    APP_URL = BASE_URL + getData.url



    @classmethod
    def setup_class(cls):
        pass

    @allure.feature('登录模块')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('desc,params,validate',getData.checks)
    def test_login(self,desc,params,validate):
        false = False
        true = True
        r = _requests._post(self, url=TestLogin.APP_URL, arg=params, headers=TestLogin.HEADER)
        response_text = eval(r.text)
        # 比较对象:
        print(validate)
        for i in validate:
            assert_param = (i.get('eq'))[0]
            assert_value = (i.get('eq'))[1]
            assert (response_text.get(assert_param) == assert_value)

    @classmethod
    def teardown_class(cls):
        pass

