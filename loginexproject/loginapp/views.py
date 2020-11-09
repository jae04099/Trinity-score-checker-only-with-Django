from django.shortcuts import render, redirect
from .forms import CreateLogin
from .models import Login
from django.test import TestCase
from selenium import webdriver
import time

# Create your views here.
def index(request):
    _Id = Login.objects.values_list('trinity_id', flat=True).get(pk=1)
    _Password = Login.objects.values_list('trinity_password', flat=True).get(pk=1)
    if request.method == 'POST':
        form = CreateLogin(request.POST)
        print(_Id)
        print(_Password)
        form.save()
        return redirect('result')
    
    else:
        form = CreateLogin()
        return render(request, 'index.html', {'form': form})

def result(request):
    return render(request, 'result.html')

def useSelenium(_Tid, _Tpw):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome('C:\\Users\\jae04\\Desktop\\chromedriver_win32\\chromedriver.exe')
    driver.get('https://uportal.catholic.ac.kr/sso/jsp/sso/ip/login_form.jsp')
    driver.find_element_by_name('userId').send_keys(_Tid)
    driver.find_element_by_name('password').send_keys(_Tpw)

    driver.find_element_by_xpath('/html/body/div/form/div/div/div[1]/dl/dd[3]/button').click()

    time.sleep(0.5)
    driver.get("https://uportal.catholic.ac.kr/stw/scsr/ssco/sscoSemesterGradesInq.do")
    time.sleep(1)
    score_num = driver.find_element_by_class_name('ucups-grid-cq')
    print(score_num.text)
