from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
#COUNTER
pts = 0
limit = 400

USER = input("INPUT USER EMAIL : ")
PASSWORD = input("INPUT USER PASSWORD : ")
#DATE AND TIME
date_and_time = datetime.datetime.now()

print(f"DATE : {date_and_time.date()} TIME : {date_and_time.time()}")


with open ('logs.txt', 'a+') as log:
    log.write(f'DATE : {date_and_time.date()} TIME : {date_and_time.time()} \n')
    

#MAIN AUTOMATION
def main(pts, PASSWORD, USER):



    #NUM_OF_LOOP = input("NUMBER OF LOGINS : ")
    PATH = "geckodriver.exe"
    driver = webdriver.Firefox()
    driver.set_window_position(0, 0)
    driver.set_window_size(600, 600)
    

    driver.get("https://hpcs-admin.com/router/login.php")
    time.sleep(3)
    print(f"{driver.title} : AUTOMATION BY RAGEJAX")
    print('Driver loaded')


    #driver.find_elements_by_

    #search = driver.find_elementby_id("ELEMENT")
    #search.send_keys("TEST")
    #search.send_keys(Key.RETURN)

    #INPUT EMAIL


    #INPUTS
    class main_login_page():
        def __init__(self) -> None:
            self.address = driver.find_element_by_name("member_id")
            self.password = driver.find_element_by_id("loginPassword")
            self.login_btn = driver.find_element_by_css_selector('.loginpage-btn')
            
        def update_address(self, email):
            self.address.send_keys(email)

        def update_password(self, password):
            self.password.send_keys(password)

        def update_login(self):
            self.login_btn.click()

        def update_close(self):
            #<button class="btn btn_f" type="button">
            #self.close_btn = driver.find_element_by_xpath('//button[@class="btn btn_f"]')
            self.close_btn = driver.find_element_by_xpath('//button[contains(@onclick, "go_mov()")]')
            #print(self.close_btn)
            self.close_btn.click()

        def update_continue(self):
            self.con_btn = driver.find_element_by_xpath('//button[contains(@onclick, "vclose0()")]')
            self.con_btn.click()
    
    run = main_login_page()


    #UPDATE

    run.update_address(USER)
    run.update_password(PASSWORD)
    time.sleep(3)
    run.update_login()
    time.sleep(2)
    run.update_close()
    time.sleep(1)
    run.update_continue()
    time.sleep(70)

    pts + 4
    limit + 1

    with open ('logs.txt', 'a+') as log:
        log.write(f"POINTS : {pts} \n")


    driver.close()
        
#LOOP
while True:
    main(pts, PASSWORD, USER)
    if limit > 400:
        with open ('logs.txt', 'a+') as log:
            log.write(f"BREAK TIME : {date_and_time()}\n TOTAL EARNED : {pts}")
            
        break
