from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()

website = 'https://form.jotform.com/241635027272149'#'https://form.jotform.com/241617189501153'#"https://docs.google.com/forms/d/e/1FAIpQLSeP1J4TiyjSM9dT2XgK3I2J1ZTFqfiDnoWVCJsMuTRW1BTd8w/viewform?usp=sf_link"
driver.get(website)
time.sleep(2)
website_info = [
    ('first name', '//*[@id="first_11"]'),
    ('middle name', '//*[@id="middle_11"]'),
    ('last name', '//*[@id="last_11"]'),
    ('current address', ''),
    ('street address line 1', ''),
    ('street address line 2', ''),
    ('City', ''),
    ('State/ Province', ''),
    ('Postal/ Zip code', ''),
    ('Email adress', ''),
    ('Phone Number', ''),
    ('LinkedIn', ''),
    ('Write something interesting about AI Agents/ LLMs', ''),
    ('Reverse a LinkedList',''),
    ('Cover Letter','')
]
print(website_info[0][1])

name = "Afif Dev"
elName = driver.find_element(By.XPATH,'//*[@id="first_11"]') #website_info[1][1])
elName.send_keys(name)


time.sleep(1)
print("OK Done. Bye!")
driver.close()