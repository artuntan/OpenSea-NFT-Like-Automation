from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

import pyautogui
from sympy import false, true
# from Common_Methods.GenericMethods import *

url = "https://opensea.io/assets/0xa1de9f93c56c290c48849b1393b09eb616d55dbb/5396"

# bir defa sign yapınca 24 saat içinde tekrar sign yapmaya gerek yok.
# bununn için sign kısmının devreye sokup sokmamaya bunun ile karar veriyoruz

sign_gereklimi = true

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\white\AppData\Local\Google\Chrome\User Data\Profile 1") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Profile 1') #Selenium 1
# options.add_argument(r'--profile-directory=Profile 3') #Selenium 2

# Cookie prevention did not work
# options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
# options.add_experimental_option("prefs", {"profile.cookie_controls_mode": 1})

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

#Main Windows Tite 1
# print("Initial Page Title is : %s" %driver.title)

orgiginal_window  = driver.current_window_handle
# print("First Window Handle is : %s" %orgiginal_window)

time.sleep(5)

# driver.execute_script('''window.open("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/popup.html", "_blank");''')

driver.execute_script('''window.open("https://www.google.com", "_blank");''')

input("Login Metamask and select first account")

new_window  = driver.current_window_handle
# print("New Window Handle is : %s" %new_window)

#go back to origin and open opensea
driver.switch_to_window(driver.window_handles[0])

time.sleep(3)

driver.get(url)

time.sleep(6)


driver.switch_to_window(driver.window_handles[1])

time.sleep(1)

driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/popup.html")

import keyboard
keyboard.press_and_release('F12')

input("check F12 works? If not press F12")

time.sleep(2)

for x in range(50, 136):
    
    time.sleep(2) 

    # find account text
    submit = driver.find_element_by_xpath('//div[@class="identicon__address-wrapper"]')
    submit.click()
    submit =driver.find_element_by_xpath("//div[text()='Account "+str(x)+"']")
    submit.click()

    time.sleep(1)

    #delete all cookies
    

    #return to home page and open relevant nft
    driver.switch_to_window(driver.window_handles[0])
    driver.delete_all_cookies()

    time.sleep(3)

    driver.get(url)

    time.sleep(6)

    #like click
    submit = driver.find_element_by_xpath("//i[@value='favorite_border']")
    submit.click()

    time.sleep(1)

    #back to metamask, refresh and sign
    #If the account has signed once, there is no need to do it again within 24 hours.
    driver.switch_to_window(driver.window_handles[1])

    time.sleep(1)

    #refresh page
    driver.refresh()

    # keyboard.press_and_release('F5')

    time.sleep(3)
    if sign_gereklimi == true:
        try:
            submit = driver.find_element_by_xpath("//button[@role='button' and @data-testid='request-signature__sign']")
            submit.click()
        except:
            input("no sign, check and enter to continue")



time.sleep(5)

# metamask window olarak açılmıyor.
# for window_handle in driver.window_handles:
#     print("For loop windows : %s" %window_handle)
#     if window_handle != orgiginal_window:
#         driver.switch_to.window(window_handle)
#         break


# password= driver.switch_to_frame(driver.find_element_by_css_selector("input[id='password']"))


input("Press Enter to continue...")