print("Content-type: text/html \n")

import magicwand
import random

firstname_file = open('first-names.txt')

first_names = []

for line in firstname_file:
    newline = line.rstrip()
    first_names.append(newline)
    
firstname_file.close()
print(len(first_names), 'First Names')

f_name = random.choice(first_names)
print(f_name)


middlename_file = open('middle-names.txt')
middle_names = middlename_file.read().split('\n')
middlename_file.close()

m_name = random.choice(middle_names)
print(m_name)



lastname_file = open('last-names.txt')
last_names = lastname_file.read().split('\n')
lastname_file.close()

l_name = random.choice(last_names)
print(l_name)
