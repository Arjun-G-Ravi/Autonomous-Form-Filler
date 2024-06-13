from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from groq import Groq
from api_key import api

class LLM:
    def __init__(self, temperature = 0.2, top_p=0.3):
        self.temperature = temperature
        self.top_p = top_p
        self.client = Groq(api_key=api)

    def generate(self, inp):
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user","content": f"{inp}"}],
            model="llama3-70b-8192",
            # Other models: llama3-8b-8192 llama3-70b-8192 gemma-7b-it mixtral-8x7b-32768
            temperature = self.temperature,
            top_p=self.top_p)

        return chat_completion.choices[0].message.content


def extract_name_and_xpath(website, driver):
    # driver = webdriver.Chrome()
    # driver.get(website)
    time.sleep(1)
    writable_elements = driver.find_elements(By.XPATH, "//input[not(@type='hidden') and not(@type='submit') and not(@type='button')] | //textarea")
    print(writable_elements)
    text_out = []
    file_out = []
    for element in writable_elements:
        element_xpath = _get_xpath(element, driver)
        if not element_xpath: continue
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
        if base_name == 'file': file_out.append([element_xpath, name, base_name])
        else: text_out.append([element_xpath, name, base_name])
        # print(f"{element_xpath} - {name}")

    # print(text_out)
    # print(file_out)
    # time.sleep(10)
    return file_out, text_out


def _get_xpath(element, driver):
    # tag = element.tag_name
    id_attr = element.get_attribute('id')
    name_attr = element.get_attribute('name')
    
    if id_attr:
        return f'//*[@id="{id_attr}"]'
    elif name_attr:
        return None # f'//*[@name="{name_attr}"]'
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
    website = 'https://form.jotform.com/241635027272149'
    driver = webdriver.Chrome()
    ans = extract_name_and_xpath(website, driver)
    print(ans)
    # llm = LLM()
    # print(llm.generate('hey'))