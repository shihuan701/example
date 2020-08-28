from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from time import sleep
from utils.pathBase import LOGIN_PATH
from utils.pathBase import readYamlFile

class BasePage():
    _driver=''
    LOGINFILE = readYamlFile(LOGIN_PATH)
    base_url=LOGINFILE[0].get('config').get('test_url')
    def __init__(self,reuse=False):
        option = webdriver.ChromeOptions()
        option.add_argument('--user-agent=iphone')
        if reuse:
            self._driver = webdriver.Chrome()
        else:
            self._driver = webdriver.Chrome()
        print('--------------------------------------------',self.base_url)
        self._driver.get(self.base_url)
        self._driver.implicitly_wait(10)

        def driver_quit(self):
            self._driver.quit()
            print('exc driver quit')

        def find_element(self, by, value):
            return self._driver.find_element(by, value)

        def find_elements(self, by, value):
            return self._driver.find_elements(by, value)

        def wait_for(self, func):
            WebDriverWait(self._driver, 10).until(func)

        def sendKeys(self, by, locate, value, isclean=True):
            element = self.find_element(by, locate)
            if isclean:
                element.clear()
            element.send_keys(value)

        def move_element(self, by, locate):
            element = self.find_element(by,locate)
            actions = ActionChains(BasePage()._driver)
            actions.click_and_hold(element).perform()
            for index in range(200):
                actions.move_by_offset(2,0).perform()
                actions.reset_actions()
                sleep(0.1)

        def click_element(self,by,locate):
            element = self.find_element(by,locate)
            element.click()