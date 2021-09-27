cod = 123
counter = 0
pass_us = 0
print("password")
while counter <= 3:
    pass_us = int(input())
    counter = counter + 1
    if pass_us == cod:
        print("welcome")
        break
    if not pass_us == cod:
        print("the password is incorrect")
    if counter == 2:
        print("last attempt")
