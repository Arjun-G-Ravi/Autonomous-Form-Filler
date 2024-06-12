# Extract information from webpage

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the form
driver.get("https://form.jotform.com/241617189501153")

# Wait for the page to load completely
time.sleep(3)

# Find all writable input and textarea elements
writable_elements = driver.find_elements(By.XPATH, "//input[not(@type='hidden') and not(@type='submit') and not(@type='button')] | //textarea")

# Function to get the XPath of an element based on its attributes
def get_xpath(element):
    tag = element.tag_name
    id_attr = element.get_attribute('id')
    name_attr = element.get_attribute('name')
    
    if id_attr:
        return f'//*[@id="{id_attr}"]'
    elif name_attr:
        return f'//*[@name="{name_attr}"]'
    else:
        # Fallback to full XPath if no id or name attribute is present
        script = """
        function getElementXPath(elt) {
            var path = "";
            for (; elt && elt.nodeType == 1; elt = elt.parentNode) {
                var idx = getElementIdx(elt);
                var xname = elt.tagName.toLowerCase();
                if (idx > 1) xname += "[" + idx + "]";
                path = "/" + xname + path;
            }
            return path;
        }
        function getElementIdx(elt) {
            var count = 1;
            for (var sib = elt.previousSibling; sib; sib = sib.previousSibling) {
                if (sib.nodeType == 1 && sib.tagName == elt.tagName) count++;
            }
            return count;
        }
        return getElementXPath(arguments[0]).toLowerCase();
        }
        return driver.execute_script(script, element)
        """
        return driver.execute_script(script, element)

# Extract and print the XPaths and names of each writable element
for element in writable_elements:
    element_xpath = get_xpath(element)
    parent = element.find_element(By.XPATH, "..")
    name = parent.text.strip()
    print(f"{element_xpath} - {name}")

# Close the browser
driver.quit()