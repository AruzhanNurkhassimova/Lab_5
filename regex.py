import re

with open("text for 1-7.txt") as f:
    data = f.read()

#1
task1 = re.findall(r'ab*',data)
print(task1)

#2
task2 = re.findall(r'abbb?',data)
print(task2)

#3
task3 = re.findall(r'[a-z]+_[a-z]+',data)
print(task3)

#4
task4 = re.findall(r'[A-Z][a-z]+', data)
print(task4)

#5
task5 = re.findall(r'a+.b', data)
print(task5)

#6
task6 = re.sub(r'[ ,.]', r':', data)
print(task6)

#7
task7 = re.sub('_', '', data)
print(task7)