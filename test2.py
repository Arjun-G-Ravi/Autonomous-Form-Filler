from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Open the web page
# driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdAGguGnAVrFTCO6HEdKyyHgOEK_ZFnQQ_ax0zcFWHb8iwKfA/viewform?usp=sf_link')
driver.get('https://form.jotform.com/241617189501153')

# Extract all input elements
input_elements = driver.find_elements(By.TAG_NAME, 'input')

# Print details of each input element
for element in input_elements:
    print(f"Input Element: name={element.get_attribute('name')}, type={element.get_attribute('type')}, value={element.get_attribute('value')}")

# Extract all textarea elements
textarea_elements = driver.find_elements(By.TAG_NAME, 'textarea')

# Print details of each textarea element
for element in textarea_elements:
    print(f"Textarea Element: name={element.get_attribute('name')}, value={element.get_attribute('value')}")

# Extract all select elements
select_elements = driver.find_elements(By.TAG_NAME, 'select')

# Print details of each select element
for element in select_elements:
    print(f"Select Element: name={element.get_attribute('name')}, value={element.get_attribute('value')}")

# Extract all div elements (Google Forms fields are often within divs with specific classes)
div_elements = driver.find_elements(By.TAG_NAME, 'div')

# Print details of each div element
for element in div_elements:
    class_name = element.get_attribute('class')
    if 'freebirdFormviewerViewItemsItemItem' in class_name:
        print(f"Div Element: class={class_name}")

# Close the WebDriver
driver.quit()
