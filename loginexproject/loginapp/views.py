from django.shortcuts import render, redirect
from .forms import CreateLogin
from .models import Login
from django.test import TestCase
from selenium import webdriver
import time

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = CreateLogin(request.POST)

        if form.is_valid():
            _Id = form.cleaned_data['trinity_id']
            _Password = form.cleaned_data['trinity_password']
            request.session['result'] = useSelenium(_Id, _Password)
            return redirect('result')
        else:
            return redirect('login')

    else:
        form = CreateLogin()
        return render(request, 'index.html', {'form': form})


def result(request):
    session_id = request.session.session_key
    result = request.session['result']

    contents = {
        'session_id': session_id,
        'result': result 
    }
    return render(request, 'result.html', contents)


def useSelenium(_Tid, _Tpw):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver = 'C:\\Users\\jae04\\Desktop\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.get('https://uportal.catholic.ac.kr/sso/jsp/sso/ip/login_form.jsp')
    driver.find_element_by_name('userId').send_keys(_Tid)
    driver.find_element_by_name('password').send_keys(_Tpw)

    driver.find_element_by_xpath(
        '/html/body/div/form/div/div/div[1]/dl/dd[3]/button').click()

    time.sleep(0.3)
    driver.get(
        "https://uportal.catholic.ac.kr/stw/scsr/ssco/sscoSemesterGradesInq.do")
    time.sleep(0.3)
    score_num = driver.find_element_by_class_name('ucups-grid-cq')
    scoreresult = score_num.text

    return scoreresult
