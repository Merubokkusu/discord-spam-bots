#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import *
from sys import platform
import time
import sys
import os


email = sys.argv[1]
password = sys.argv[2]
inviteLink = sys.argv[3]
useBrowser = sys.argv[4]
PROXY = sys.argv[5]

if useBrowser == 'Chrome':
    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument("headless")
    chromeOptions.add_argument("disable-gpu")

    if os.path.exists('proxies.txt'):
        chromeOptions.add_argument('--proxy-server='+PROXY)
        chromeOptions.add_argument('--proxy-auto-detect')
        chromeOptions.add_argument("--incognito")

    print("Starting Server Join")
    if platform == "linux" or platform == "linux2":
        browser = webdriver.Chrome('resources/webdrivers/chromedriver-linux',chrome_options=chromeOptions)
    elif platform == "darwin":
        browser = webdriver.Chrome('resources/webdrivers/chromedriver-mac',chrome_options=chromeOptions)
    elif platform == "win32":
        browser = webdriver.Chrome('resources/webdrivers/chromedriver.exe',chrome_options=chromeOptions)

if useBrowser == 'Firefox':
    options = webdriver.FirefoxOptions()
    options.add_argument('headless')

    if os.path.exists('proxies.txt'):
        lines = open('proxies.txt').read().splitlines()
        PROXY = lines[0]
        del lines[0]
        prox = open('proxies.txt', 'w')
        for l in lines:
            prox.write(l+'\n')
        prox.close()

        proxy = Proxy({
        'proxyType': ProxyType.AUTODETECT,
        'httpProxy': PROXY,
        'ftpProxy': PROXY,
        'sslProxy': PROXY,
        'noProxy': '' 
        })
        if platform == "linux" or platform == "linux2":
            browser = webdriver.Firefox('resources/webdrivers/geckodriver-linux',options=options,proxy=proxy)
        elif platform == "darwin":
            browser = webdriver.Firefox('resources/webdrivers/geckodriver-mac',options=options,proxy=proxy)
        elif platform == "win32":
            browser = webdriver.Firefox('resources/webdrivers/geckodriver.exe',options=options,proxy=proxy)
    else:
        if platform == "linux" or platform == "linux2":
            browser = webdriver.Firefox('resources/webdrivers/geckodriver-linux',options=options)
        elif platform == "darwin":
            browser = webdriver.Firefox('resources/webdrivers/geckodriver-mac',options=options)
        elif platform == "win32":
            browser = webdriver.Firefox('resources/webdrivers/geckodriver.exe',options=options)

browser.get("https://discordapp.com/login")
browser.find_element_by_xpath("//input[@name='']").clear()
browser.find_element_by_xpath("//input[@name='']").send_keys(email)
print("Writing Email")
browser.find_element_by_xpath("(//input[@name=''])[2]").clear()
browser.find_element_by_xpath("(//input[@name=''])[2]").send_keys(password)
print("Writing Password")
browser.find_element_by_xpath("//button[@type='submit']").click()
element = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.CLASS_NAME, "guildsAddInner-1KMFy-")))
browser.execute_script('document.getElementsByTagName("body")[0].appendChild(document.getElementsByClassName("guildsWrapper-5TJh6A")[0])')
element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, "app-mount")))
browser.execute_script('var el = document.querySelector( "div.app-19_DXt.platform-web" ); el.parentNode.removeChild( el );')
mainmenu = browser.find_element_by_class_name("guildsAddInner-1KMFy-")
action=ActionChains(browser)
action.move_to_element(mainmenu).perform()
submenu = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "guildsAddInner-1KMFy-")))
print("Attempting to click") # Master hacking.
submenu.click()
print("Click success")
browser.find_element_by_css_selector("div.action.join > button.btn.btn-primary").click()
browser.execute_script("document.getElementsByClassName('link-container control-group')[0].style.top = 0;")
time.sleep(0.5);
browser.find_element_by_css_selector("div.link-container.control-group > input[type=\"text\"]").click()
browser.find_element_by_css_selector("div.link-container.control-group > input[type=\"text\"]").send_keys(inviteLink) #https://discord.gg/EksPfZ5
print("Writing invite link")
browser.find_element_by_css_selector("div.form-actions > button.btn.btn-primary").click()
time.sleep(0.5)
print("Joined Server | Closing Script")
browser.quit()
