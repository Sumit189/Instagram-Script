#Insta Follower 


def get_credential(uname_,pass_,tags_,tfollow_,tkWindow):
    from time import sleep
    from random import randint
    from random import seed
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from tkinter import messagebox
    import os
    full_path = os.path.realpath(__file__)
    location_input=os.path.dirname(full_path)
    filename = location_input+'\\followed_by_script.txt'
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    chromedriver_path = location_input+'\chromedriver.exe' 

    tags_=str(tags_)
    prev_user_list=[]
    new_hastag_list=[]

    hashtag_list = tags_.replace(',',' ').split()
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
                break
    total_acc_to_follow=int(int(tfollow_)/int(len(hashtag_list)))
    print(total_acc_to_follow)
    if all_ok==0:        
        webdriver = webdriver.Chrome(executable_path=chromedriver_path)
        sleep(2)
        print("Loading Login Page...")
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
            print("Logged in Successfully")
        except:
            print("Re run the program..")
            tkWindow.destroy()
        sleep(10)
        try:
             notnow = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
             notnow.click()
             print("Closed Save Details Message.")
        except:
            print("No Save Detail Message Appeared.")
        sleep(2)
        try:
            notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
            print("Closed allow notification PopUp.")
        except:
            sleep(10)
            notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
            print("Closed allow notification PopUp.")
        tag = -1
        followed = 0
        likes = 0
        comments = 0
        print("Starting to follow the profiles in tag..")
        for hashtag in hashtag_list:
            x=1 
            tag += 1
            count_num_array=0
            num_arr=[]
            print("Opening profile list for: "+ hashtag_list[tag])
            webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
            sleep(5)
            try:
                first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
                print("Opening 1st profile")
            except:
                total_acc_to_follow+=total_acc_to_follow
                continue
            first_thumbnail.click()
            sleep(randint(1,2))    
            while x<total_acc_to_follow+1:    
                print(x)
                webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text
                num_arr.append(x)
                if x>1:
                    if num_arr[-1]==num_arr[-2]:
                        count_num_array+=1
                if count_num_array>3:
                    webdriver.find_element_by_link_text('Next').click()
                    count_num_array=0
                    sleep(randint(1,8)) 
                try:
                    username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/div/a').text
                    if (username not in prev_user_list) or (len(prev_user_list)==0) :
                        if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                            prev_user_list.append(username)
                            x+=1
                            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                            print("Followed")
                            file1 = open(filename, append_write) # append mode 
                            file1.write(username+"\n") 
                            file1.close() 
                            followed += 1
                            button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                            button_like.click()
                            print("Liked the picture.")
                            likes += 1
                            sleep(randint(1,3))
                            seed(1)
                            do_=randint(0,2)
                            if do_>=1:
                                comm_prob=randint(1,10)
                                print('{}_{}: {}'.format(hashtag, x,comm_prob))
                                if comm_prob > 7:
                                    print("Given a comment.")
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
                            print("Already Following: {}".format(username))
                        # Next picture
                        print("Opening Next Profile.")
                        webdriver.find_element_by_link_text('Next').click()
                        sleep(randint(1,8))
                except:
                    print("Opening Next Profile.")
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(1,8))
            
        print('Liked {} photos.'.format(likes))
        print('Commented {} photos.'.format(comments))
        print('Followed {} new people.'.format(followed))
        print("Exiting...")
        tkWindow.destroy()
        exit(1)
