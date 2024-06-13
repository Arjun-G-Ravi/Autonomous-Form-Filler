from helper import LLM, extract_name_and_xpath
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

llm = LLM()
driver = webdriver.Chrome()
website = 'https://form.jotform.com/241635027272149'# 'https://form.jotform.com/241635560266457' # 'https://docs.google.com/forms/d/e/1FAIpQLSdAGguGnAVrFTCO6HEdKyyHgOEK_ZFnQQ_ax0zcFWHb8iwKfA/viewform?usp=sf_link'
driver.get(website)
sleep(1)
file_out, text_out= extract_name_and_xpath(website, driver)
print(text_out)
questions = []
for text_block in text_out:
    questions.append(text_block[1] + ' or ' + text_block[2])

print(questions)

llm_output = llm.generate(f'''You are an AI agent that is used to fill up application forms. Given som basic information, try to create a sample answer to the questions.
Answer the question in the format starting with [ and ending with ]. Each element is separated by @@@ symbol, as shown below:
Eg: [Ans1@@@Ans2@@@Ans3@@@ ... Ans22@@@Ans23]
Dont output anything other than the answers. Remember to output in the correct format by answering between square brackets. For the cover letter question, write a very short cover letter.
Make sure to answer every question in the following :{questions}.''')
print(llm_output)

print('-' *50)
matches = re.findall(r'\[(.*?)\]', llm_output)[0]

new = matches.split('@@@')
answers = []
for i in new:
    answers.append(i)

# print(answers)
print(len(answers), len(questions))
for q,a in zip(questions, answers):
    print(q,' -> ',a)

print('\n'*3)
for t,a in zip(text_out, answers):
    print( t[0])
    el = driver.find_element(By.XPATH, t[0])
    el.send_keys(a)
    sleep(.1)


file_path = '/home/arjun/Desktop/GitHub/Autonomous-Form-Filler/to_upload.txt'
# Locate the file input element and upload the file
file_input = driver.find_element(By.XPATH, '//*[@id="input_17"]')
file_input.send_keys(file_path)

sleep(10)
driver.quit()