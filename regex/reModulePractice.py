#! python3

import re

line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'

print(bool(re.search(r'0xB0', line1)))
print(bool(re.search(r'0xB0', line2)))

fruit = 'They ate 5 apples and 5 oranges'
print(re.sub(r'5','five',fruit))
print(re.sub(r'5','five',fruit,count=1))

items = ['goal','new','user','sit','eat','dinner']
print([w for w in items if not re.search(r'e',w)])

