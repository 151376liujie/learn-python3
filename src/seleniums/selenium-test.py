import os
import time
import warnings
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumTest:

    @staticmethod
    def show_process():
        out = os.popen("ps aux | grep chrome").read()
        for line in out.splitlines():
            print(line)

    @staticmethod
    def testLogin():
        opt = Options()
        opt.add_argument('--no-sandbox')
        opt.add_argument('--disable-dev-shm-usage')
        opt.add_argument('--headless')
        opt.add_argument('blink-settings=imagesEnabled=false')
        opt.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=opt)
        driver.get("https://www.51tracking.com/login")
        locator = (By.NAME, "email")
        print(type(locator))
        try:
            WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("can not find ele:[email]")
            driver.quit()
            return
        print("redirect to login page, body is: %s" % driver.find_element_by_tag_name("body").text)
        driver.find_element_by_name("email").send_keys("rujiahua@payeasenet.com")
        driver.find_element_by_name("password").send_keys("0418YXYwlx")
        driver.find_element_by_tag_name("button").click()
        locator2 = (By.CLASS_NAME, "tt51_pc_user_info")
        try:
            WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located(locator2))
            print("login success, body is %s" % driver.find_element_by_tag_name("body").text)
        except TimeoutException:
            print("login failed")
            driver.quit()
            return

        driver.get(
            "https://my.51tracking.com/numbers.php?lang=cn&keywordType=trackNumber&p=1&searchnumber=EY684075673FR")
        # driver.maximize_window()
        driver.fullscreen_window()
        try:
            locator3 = (By.ID, "trackItem_0")
            WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located(locator3))
            print("tracking success, body is %s" % driver.find_element_by_id("trackItem_0").text)
            driver.find_element_by_id('trackItem_0').click()
            driver.save_screenshot("detail.png")
        except TimeoutException:
            print("login failed")
        driver.quit()

    @staticmethod
    def run_in_chrome():
        # opt = Options()
        # opt.headless = True
        # print(opt.experimental_options)
        # prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        # opt.add_experimental_option("prefs", prefs)
        # opt.add_argument('headless')
        # opt.add_argument('--no-sandbox')
        # opt.add_argument('--disable-dev-shm-usage')
        # opt.add_argument('--headless')
        # opt.add_argument('blink-settings=imagesEnabled=false')
        # opt.add_argument('--disable-gpu')

        show_process()
        chrome = webdriver.Chrome(options=opt)
        print("###########启动一个Chrome后###################")
        show_process()
        chrome.set_page_load_timeout(10)
        chrome.set_script_timeout(10)
        chrome.get("https://www.51tracking.com/login")
        chrome.maximize_window()
        print("title: ", chrome.title)
        # chrome.save_screenshot("baidu_chrome.png")
        chrome.find_element_by_name("email").send_keys("rujiahua@payeasenet.com")
        chrome.find_element_by_name('password').send_keys("0418YXYwlx")
        button = chrome.find_element_by_tag_name("button")
        print(button.text)
        button.click()
        time.sleep(3)
        # WebDriverWait(driver=chrome,5).until()
        chrome.save_screenshot("baidu_chrome_nvren.png")
        for num in ["YT2112321272112048", "AQ836326947CN"]:
            chrome.get("https://my.51tracking.com/numbers.php?lang=cn&keywordType=trackNumber&p=1&searchnumber=" + num)
            time.sleep(3)
            chrome.save_screenshot(num + ".png")


if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    SeleniumTest.testLogin()
