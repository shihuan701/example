from selenium.webdriver.common.by import By
from ui_operation.web_pages.BasePage import BasePage


class LoginPage(BasePage):
    username_input = BasePage().find_element(By.NAME,'userName')
    password_input = BasePage().find_element(By.NAME,'authStr')
    slide_btn = BasePage().find_element(By.NAME,'nc_iconfont')
    smsVC_btn = BasePage().find_element(By.CLASS_NAME, 'smsVC-btn')
    vcode_input = BasePage().find_element(By.NAME,'vcode')
    login_btn = BasePage().find_element(By.CLASS_NAME,'el-button--primary')

    def login(self,username,password):
        self.sendKeys(*self.username_input,username)
        self.sendKeys(*self.password_input, password)
        self.move_element(*self.slide_btn)
        self.click_element(*self.slide_btn)

if __name__ == '__main__':
    LoginPage.login('18802681032','sybilshi2018')
