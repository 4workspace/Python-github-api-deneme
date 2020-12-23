#from githupUserinfo import username, password
username = "4workspace"
password = "**********"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # enter veya space tuşunu import etmek için
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []                 # boş liste olusturuldu
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element_by_xpath('//*[@id="login_field"]')
        password = self.browser.find_element_by_xpath('//*[@id="password"]')

        username = username.send_keys(self.username)
        password = password.send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]').click()

    def getFollowers(self):
        self.browser.get("https://github.com/sadikturan?tab=followers")
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")              

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray.pl-1").text)



github = Github(username, password)
github.signIn()
# github.browser.maximize_window()
github.getFollowers()
time.sleep(2)
print(github.followers)
# github.browser.close
