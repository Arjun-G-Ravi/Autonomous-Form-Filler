from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeP1J4TiyjSM9dT2XgK3I2J1ZTFqfiDnoWVCJsMuTRW1BTd8w/viewform?usp=sf_link")

# Example: Extracting XPath or CSS Selectors
# Finding the element by a known attribute (e.g., name or id)
email_element = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')

# Extracting XPath (this is just for demonstration; Selenium itself does not provide a direct method to extract XPath)
def get_xpath(element):
    components = []
    child = element if element else driver.find_element(By.XPATH, '/html/body')
    while child.tag_name != 'html':
        parent = child.find_element(By.XPATH, '..')
        children = parent.find_elements(By.XPATH, '*')
        index = 1
        for i in range(len(children)):
            if children[i] == child:
                break
            if children[i].tag_name == child.tag_name:
                index += 1
        components.append(child.tag_name if index == 1 else f"{child.tag_name}[{index}]")
        child = parent
    components.reverse()
    return '/' + '/'.join(components)

email_xpath = get_xpath(email_element)
print(f"Email XPath: {email_xpath}")

# Extracting CSS Selector (manual example for demonstration)
email_css_selector = 'input[type="email"]'
print(f"Email CSS Selector: {email_css_selector}")

# Close the browser
driver.quit()
