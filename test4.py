from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# open Chrome
driver = webdriver.Chrome()

# Open URL
driver.get('https://form.jotform.com/241617189501153')

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
datas = [
    ['Mary D Joiner', 'MaryDJoiner@gmail.com', '4079025063', '2474  McDonald Avenue,Maitland', 'NA'],
    ['Karen B Johnson', 'KarenBJohnson@gmail.com', '3153437575', '2143  Oak Street,GRAND ISLE', 'NA'],
]

# textboxes = driver.find_elements()
# textareaboxes = driver.find_elements()
# print(textareaboxes, textboxes) 
# quit()

# Iterate through each data
for data in datas:
    # Initialize count is zero
    count = 0

    # contain input boxes
    textboxes = driver.find_elements(By.CLASS_NAME, "quantumWizTextinputPaperinputInput")

    # contain textareas
    textareaboxes = driver.find_elements(By.CLASS_NAME, "quantumWizTextinputPapertextareaInput")
    print(textareaboxes, textboxes) 


    # Iterate through all input boxes
    for value in textboxes:
        # enter value
        value.send_keys(data[count])
        # increment count value
        count += 1

    # Iterate through all textareas
    for value in textareaboxes:
        # enter value
        value.send_keys(data[count])
        # increment count value
        count += 1

    # click on submit button
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()

    # fill another response
    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

# close the window
driver.close()
