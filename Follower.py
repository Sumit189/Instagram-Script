#Insta Follower 
import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint


full_path = os.path.realpath(__file__)
location_input=os.path.dirname(full_path)
filename = location_input+'\\followed_by_script.txt'
if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

chromedriver_path = location_input+'\chromedriver.exe' 

def get_credential(uname_,pass_,tags_):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from tkinter import messagebox
    tags_=str(tags_)
    new_hastag_list=[]
    hashtag_list = tags_.replace(' ','').split(',')
    for list_items in hashtag_list:
        if list_items[0]=='#':
            new_hastag_list.append(list_items[1:])
        else:
            new_hastag_list.append(list_items)
    hashtag_list=new_hastag_list
    all_ok=0
    print(hashtag_list)
    for list_items in hashtag_list:
        for x in range (len(list_items)):
            if list_items[x]=="#":
                messagebox.showerror("Tags Error", "Invalid Tags are provided")
                all_ok=1
    if all_ok==0:        
        webdriver = webdriver.Chrome(executable_path=chromedriver_path)
        sleep(2)
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        username = webdriver.find_element_by_name('username')
        username.send_keys(str(uname_))
        password = webdriver.find_element_by_name('password')
        password.send_keys(str(pass_))

        button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
        button_login.click()
        sleep(10)
        notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

        new_followed = []
        tag = -1
        followed = 0
        likes = 0
        comments = 0

        for hashtag in hashtag_list:
            tag += 1
            webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
            sleep(5)
            first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
            
            first_thumbnail.click()
            sleep(randint(1,2))    
            try:      
                for x in range(1,10):    
                    username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                    
                    if username not in prev_user_list:

                        # If we already follow, do not unfollow
                        if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                            
                            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                            file1 = open("followed.txt", append_write) # append mode 
                            file1.write(username+"\n") 
                            file1.close() 
                            new_followed.append(username)
                            followed += 1

                            # Liking the picture
                            
                            button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                            
                            button_like.click()
                            likes += 1
                            sleep(randint(1,3))

                            # Comments and tracker
                            comm_prob = randint(1,10)
                            random.seed(444)
                            do_=randint(0,1)
                            if do_==1:
                                print('{}_{}: {}'.format(hashtag, x,comm_prob))
                                if comm_prob > 7:
                                    comments += 1
                                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
                                    comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                                    if (comm_prob < 7):
                                        comment_box.send_keys('Really cool!')
                                        sleep(1)
                                    elif (comm_prob > 6) and (comm_prob < 9):
                                        comment_box.send_keys('Superb :)')
                                        sleep(1)
                                    elif comm_prob == 9:
                                        comment_box.send_keys('Nice gallery!!')
                                        sleep(1)
                                    elif comm_prob == 10:
                                        comment_box.send_keys('So cool! :)')
                                        sleep(1)
                                # Enter to post comment
                                    comment_box.send_keys(Keys.ENTER)
                                    sleep(randint(1,3))
                            else:
                                print("Skipping comment on {}_{}".format(hashtag, x))

                        # Next picture
                        webdriver.find_element_by_link_text('Next').click()
                        sleep(randint(1,5))
                    else:
                        webdriver.find_element_by_link_text('Next').click()
                        sleep(randint(1,5))
            except:
                continue
            
        print('Liked {} photos.'.format(likes))
        print('Commented {} photos.'.format(comments))
        print('Followed {} new people.'.format(followed))