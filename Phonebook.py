print("Content-type: text/html \n")

import magicwand
import random


phonebook_file = open('phone-data.txt')

phonebook = {}


for line in phonebook_file.read().split('\n'):
    newline = line.rstrip()
    contact = newline.split(',')
    phonebook[contact[0]] = contact[1]


for contact in phonebook:
    print(contact, ':', phonebook[contact])
