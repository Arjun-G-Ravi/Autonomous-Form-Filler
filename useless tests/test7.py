from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeP1J4TiyjSM9dT2XgK3I2J1ZTFqfiDnoWVCJsMuTRW1BTd8w/viewform?usp=sf_link")
# Web title
print(driver.title)

# Input: Email
email = "afif_dev@emailcompany.com"
elEmail = driver.find_element(By.XPATH, "//div/div/div/input")
elEmail.send_keys(email)

# Input: Name
name = "Afif Dev"
elName = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/input")
elName.send_keys(name)

# Input: GitHub URL
gitUrl = "https://github.com/afif-dev"
elgitUrl = driver.find_element(By.XPATH, "//div[3]/div/div/div[2]/div/div/div/div/input")
elgitUrl.send_keys(gitUrl)

# Checkbox options 1
driver.find_element(By.CSS_SELECTOR, "#i18 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i21 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i24 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i33 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i39 > .uHMk6b").click()

# Checkbox options 2
driver.find_element(By.CSS_SELECTOR, "#i59 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i62 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i68 > .uHMk6b").click()
driver.find_element(By.CSS_SELECTOR, "#i74 > .uHMk6b").click()

# Input: Comment
comment = "Thanks to Selenium, Python, Chrome!"
elComment = driver.find_element(By.XPATH, "//div[6]/div/div/div[2]/div/div/div/div/input")
elComment.send_keys(comment)
# Submit Form
driver.find_element(By.XPATH, "//div[3]/div/div/div/span/span").click()

# Sleep & Close Browser
time.sleep(1)
print("OK Done. Bye!")
driver.close()