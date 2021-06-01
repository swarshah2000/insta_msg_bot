
from selenium import webdriver
import os
import time
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager





driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')





audience = [ 'target_user_name']
temp="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
msg=list(temp.split(" "))





class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
  
    def login(self):
        self.bot.get(self.base_url)
  
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
  
        # first pop-up
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)
  
        # 2nd pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)
  
        # direct button
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(3)
  
        # clicks on pencil icon
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)
        
        for i in self.user:
  
            # enter the username
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)
  
            # click on the username
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div[2]/div[1]').click()
            time.sleep(2)
  
            # next button
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(2)
  
           


            for j in msg:
                # click on message area
                send = self.bot.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')


                # types message
                send.send_keys(j)
                

                # send message
                send.send_keys(Keys.RETURN)
                
  
            # clicks on direct option or pencl icon
            self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)
  




def init():
    bot('your_username', 'your_password', audience, msg)
  
    # when our program ends it will show "done".
    input("DONE")
  

init()





