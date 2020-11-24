from django.shortcuts import render, redirect
from .forms import CreateLogin
from .models import Login
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException

import time

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CreateLogin(request.POST)

        if form.is_valid():
            _Id = form.cleaned_data['trinity_id']
            _Password = form.cleaned_data['trinity_password']
            request.session['result'] = useSelenium(_Id, _Password)
            if request.session['result'] == False:
                return redirect('index')
            else:
                return redirect('result')
        # else:
        #     return redirect('login')

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
    options.add_argument("disable-gpu") 
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # 속도 향상을 위한 옵션 해제
    prefs = {'profile.default_content_setting_values': {'images': 2, 'plugins' : 2, 'geolocation': 2, 'notifications' : 2, 'fullscreen' : 2, 'mouselock' : 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)
    chromedriver = 'C:\\Users\\jae04\\Desktop\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.get('https://uportal.catholic.ac.kr/sso/jsp/sso/ip/login_form.jsp')
    driver.find_element_by_name('userId').send_keys(_Tid)
    driver.find_element_by_name('password').send_keys(_Tpw)
    driver.find_element_by_xpath(
        '/html/body/div/form/div/div/div[1]/dl/dd[3]/button').click()
    time.sleep(1)
    # driver.switch_to.alert.get_text();
    try:
        driver.switch_to_alert()
        return False
    except:

        driver.get("https://uportal.catholic.ac.kr/stw/scsr/ssco/sscoSemesterGradesInq.do")
        scoreresult = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ucups-grid-cq'))
        )
        finalresult = scoreresult.text
        driver.close()

        return finalresult
    
    # score_num = driver.find_element_by_class_name('ucups-grid-cq')