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


uname=str(input("Enter Username: "))
pass_=str(input("Enter Password: "))

chromedriver_path = location_input+'\chromedriver.exe' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

#Login
username = webdriver.find_element_by_name('username')
username.send_keys(uname)
password = webdriver.find_element_by_name('password')
password.send_keys(pass_)

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(10)
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()

unfollowed=0

for names in array_of_names:
    webdriver.get('https://www.instagram.com/'+names+'/')
    sleep(3)
    try:
        unfollow_button=webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span')
        unfollow_button.click()
        sleep(1)
        confirm_button=webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
        confirm_button.click()
        unfollowed+=1
        print("Unfollowed : {}".format(names))
    except:
        continue

print("Unfollowed : {}".format(unfollowed))
