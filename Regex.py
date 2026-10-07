import re

with open('contacts.txt', 'r') as f:
    text = f.read()

pattern = r'[a-zA-Z0-9._%+-]+@' \
          r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

if emails:
    print(f'Found {len(emails)} email(s):')

    for e in emails:
        print(' -', e)
else:
    print('No emails found in text')