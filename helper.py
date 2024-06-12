from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from api_key import api
import openai
openai.api_key = api

def get_form_filling_answers(website_information):
    prompt = 'hello'
    response = openai.Completion.create(
    engine="gpt-4", prompt=prompt)
    print(response.choices[0].text.strip())

def extract_name_and_xpath(website):
    driver = webdriver.Chrome()
    driver.get("https://form.jotform.com/241617189501153")
    time.sleep(1)
    writable_elements = driver.find_elements(By.XPATH, "//input[not(@type='hidden') and not(@type='submit') and not(@type='button')] | //textarea")
    out = []
    for element in writable_elements:
        element_xpath = _get_xpath(element, driver)
        base_name = element.get_attribute('name')
        parent = element.find_element(By.XPATH, "..")
        grandparent = parent.find_element(By.XPATH, "..")
        label_elements = grandparent.find_elements(By.TAG_NAME, "label")
        for label in label_elements:
            if label.text.strip():
                name = label.text.strip()
                break
        else:
            name = ""
        out.append([element_xpath, name, base_name])
        # print(f"{element_xpath} - {name}")
    driver.quit()
    return out


def _get_xpath(element, driver):
    # tag = element.tag_name
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
    

if __name__ == '__main__':
    # ans = extract_name_and_xpath('https://form.jotform.com/241617189501153')
    # print(ans)
    ans = get_form_filling_answers('4')