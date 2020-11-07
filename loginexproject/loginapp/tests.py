from django.test import TestCase

# Create your tests here.
#<--------- 셀레니움으로 크롤링 ------------>
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("--log-level=3")


driver = webdriver.Chrome('C:\\Users\\jae04\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.get('https://uportal.catholic.ac.kr/sso/jsp/sso/ip/login_form.jsp')
driver.find_element_by_name('userId').send_keys()
driver.find_element_by_name('password').send_keys()

driver.find_element_by_xpath('/html/body/div/form/div/div/div[1]/dl/dd[3]/button').click()

time.sleep(0.5)
driver.get("https://uportal.catholic.ac.kr/stw/scsr/ssco/sscoSemesterGradesInq.do")
time.sleep(1)
score_num = driver.find_element_by_class_name('ucups-grid-cq')
print(score_num.text)

# @api_view(['GET', 'POST'])
# def getfromJs(request):
#     if request.method == 'POST':
#         print(request)