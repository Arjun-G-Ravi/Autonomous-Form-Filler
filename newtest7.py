from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome()

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless") Use this and the following option to run Headless
#option.add_argument("disable-gpu")
# browser = webdriver.Chrome(executable_path='/home/srujan/chromedriver', options=option)

browser.get("https://forms.gle/FoAoauz53Xy7A4n68")

# Use the following snippets to get elements by their class names
# textboxes = browser.find_elements('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
# checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
# submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# Use the following snippets to get elements by their XPath
# otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")

# textboxes[0].send_keys("Hello World")

# radiobuttons[2].click()

# checkboxes[1].click()
# checkboxes[3].click()

# submitbutton[0].click()

#browser.close()
