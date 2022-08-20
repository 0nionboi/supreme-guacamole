#! python

'''
ex16.py - a program that erases a file, then asks the user for some lines to
write to it.
'''

target_file = open('ex16_text_file.txt', 'w')

print("Please add 3 lines to the file.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target_file.write(line1)
target_file.write(line2)
target_file.write(line3)
print(target_file)

target_file.close()
