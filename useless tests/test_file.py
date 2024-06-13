
from helper import LLM, extract_name_and_xpath
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



driver = webdriver.Chrome()
website = 'https://form.jotform.com/241635027272149'# 'https://form.jotform.com/241635560266457' # 'https://docs.google.com/forms/d/e/1FAIpQLSdAGguGnAVrFTCO6HEdKyyHgOEK_ZFnQQ_ax0zcFWHb8iwKfA/viewform?usp=sf_link'
driver.get(website)



# Add code to put a file at the file_out[0]
file_path = '/home/arjun/Desktop/GitHub/Autonomous-Form-Filler/to_upload.txt'
# Locate the file input element and upload the file
file_input = driver.find_element(By.XPATH, '//*[@id="input_17"]')
file_input.send_keys(file_path)

# The rest of the script
sleep(10)
driver.quit()
