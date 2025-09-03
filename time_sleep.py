# import string
# import time
# time.sleep(5)
# S = int(input("Enter your surname"))
# N = int(input("Enter your name"))
# time.sleep(10)
# print(N)

# Name = input("Enter Your name :")
# print(len(Name))


"""
Given a list of dictionaries, people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}], how would you sort this list based on the age of each person in descending order?
"""

people = [{'name': 'Alice', 'age': 30},
          {'name': 'Bob', 'age': 25}]
sorted_people = sorted(people, key=lambda x: x['age'], reverse=True)
print(sorted_people)