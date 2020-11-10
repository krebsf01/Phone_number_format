#!python3
#Phone number and zip-code format.

import sys, pyperclip, re, os
from pathlib import Path

if len(sys.argv) == 0:
    pyperclip.copy(r'Você esqueceu de copiar os ceps e/ou os telefones')

phoneRegex = re.compile(r'''(
(\d{2})
(\s|-)?
(\d{4}|\d{5})
(\s|-)?
(\d{4})
)''', re.VERBOSE)


phoneNumbers = phoneRegex.findall(pyperclip.paste())
phoneNumberList = pyperclip.paste().split('\n')
print(phoneNumbers)
print(phoneNumberList)
for phone in phoneNumbers:
    for i in range(len(phoneNumberList)):
        if phoneNumberList[i] == phone[0]+'\r':
            phoneNumberList[i] = f'{phone[1]} {phone[3]}-{phone[5]}\n'
    
pyperclip.copy(''.join(phoneNumberList))
       
        


