# print * in line with for loop

# for i in range(1,6):
#     print("* ", end="")


# print pattern with for loop

# for i in range(1,6):
#     for j in range(1,6 -i):
#         print("* ", end="")
#     print("*")


# print pattern with for loop in conditional operator

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print("* ", end="")
#     print("*" if i < 6 else "")

# print pattern without nasted loop

# for i in range(1,6):
#     print("* " * (5 - i),end="")
#     print("* " if i < 6 else "")

# print piramid pattern


# for i in range(1,6):
#     for j in range(1,6 - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("* ", end="")
#     print("*" if i < 6 else "")

# for i in range(17 + 1):
#     print(i)

# hollow ful piramid pattern proper triangle
# with for loop

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         if k == 1 or k == i or i == 5:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# square pattern

# for i in range(1,6):
#     for j in range(1,6):
#         print("* ",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("* ", end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print("* ",end="")
#     print("*")

#print number in reverse order without pattern and with any loops

print("\n")
num = int(input("Enter a number: "))
print("\n")
rev = 0
origin = num

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("\nReversed number is:", rev)
print("\n")

if origin == rev:
    for i in range(1,20):
        print("=",end="")
    print("The number is a palindrome =>",origin,"<=",end="")
    for j in range(1,20):
        print("=",end="")
else:
    print("\nThe number is not a palindrome.",)
