from helper import LLM, extract_name_and_xpath
import re

llm = LLM()
website = 'https://form.jotform.com/241635027272149'# 'https://form.jotform.com/241635560266457' # 'https://docs.google.com/forms/d/e/1FAIpQLSdAGguGnAVrFTCO6HEdKyyHgOEK_ZFnQQ_ax0zcFWHb8iwKfA/viewform?usp=sf_link'
file_out, text_out= extract_name_and_xpath(website)

questions = []
for text_block in text_out:
    questions.append(text_block[1] + ' or ' + text_block[2])


llm_output = llm.generate(f'''You are an AI agent that is used to fill up application forms. Given som basic information, try to create a sample answer to the questions.
Answer the question in the format starting with @[ and ending with ]@ separated by @@@ symbol, as shown below:
Eg: @[Ans1@@@Ans2@@@Ans3@@@ ... Ans22@@@Ans23]@
Dont output anything other than the answers. Remember to output in the correct format by answering between @-square brackets.
Make sure to answer every question in the following :{questions}.''')
print(llm_output)
print()
matches = re.findall(r'@\[(.*?)\]@', llm_output)[0]

# matches = re.findall(r'\[([^\]]+)\]', llm_output)[0]
new = matches.split('@@@')
answers = []
for i in new:
    answers.append(i)

print(answers)
print(len(answers), len(questions))
for q,a in zip(questions, answers):
    print(q,' -> ',a)


