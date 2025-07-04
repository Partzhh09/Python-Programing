# print * in line with for loop

# for i in range(1,6):
#     print("* ", end="")


# print pattern with for loop

for i in range(1,6):
    for j in range(1,6 -i):
        print("* ", end="")
    print("*")


# print pattern with for loop in conditional operator