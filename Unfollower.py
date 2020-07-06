def unfollow_it(uname_,pass_,tkWindow):
    import os
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    full_path = os.path.realpath(__file__)
    location_input=os.path.dirname(full_path)

    filename=location_input+"\\followed_by_script.txt"
    if not os.path.exists(filename):
        print("File Not Found")
        exit()

    file_=open(filename,'r')
    array_of_names=[]
    while True:
        lines=file_.readline()
        if not lines:
            break
        array_of_names.append(lines)
    if len(array_of_names)==0:
        print("No records found...")
        exit()


    chromedriver_path = location_input+'\chromedriver.exe' 
    webdriver = webdriver.Chrome(executable_path=chromedriver_path)
    sleep(2)
    print("Loading login page...")
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)
    try:
        print("Logging in...")
        username = webdriver.find_element_by_name('username')
        username.send_keys(str(uname_))
        password = webdriver.find_element_by_name('password')
        password.send_keys(str(pass_))
        button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
        button_login.click()
        print("Logged in Successfully.")
    except:
        print("Re run the program..")
        tkWindow.destroy()
        exit(1)

    sleep(10)
    try:
        notnow = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        notnow.click()
        print("Closed Save Details Message.")
    except:
        print("No Save Detail Message Appeared")
    try:
        notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
        print("Closed allow notification PopUp.")
    except:
        sleep(10)
        notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
        print("Closed allow notification PopUp.")

    unfollowed=0
    print("Unfollowing all followed profiles by Script.")
    for names in array_of_names:
        print("Loading profile: "+names)
        webdriver.get('https://www.instagram.com/'+names+'/')
        sleep(3)
        try:
            unfollow_button=webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span')
            unfollow_button.click()
            sleep(1)
            confirm_button=webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
            confirm_button.click()
            sleep(1)
            unfollowed+=1
            try:
                with open(filename, "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != names:
                            f.write(i)
                    f.truncate()
            except:
                print("File Not Found")
            print("Unfollowed : {}".format(names))
        except:
            continue

    print("Unfollowed : {}".format(unfollowed))
    tkWindow.destroy()
    exit(1)
