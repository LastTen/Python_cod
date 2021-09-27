name_us = str(input("""введіть ваше ім\'я """))
stored_pass = "123"
counter = 0
pass_us = 0
print("Введіть пароль")
while counter <= 2:
    pass_us = str(input(""))
    counter = counter + 1
    if stored_pass == pass_us:
        print("Вітаю " + str(name_us))
        while True:
            first_operand = float(input("first_operand="))
            operator = str(input("дія "))
            second_operand = float(input("second_operand="))
            if first_operand == 0 or second_operand == 0:
                break
            elif operator == "+":
                result = first_operand + second_operand
                print("answer" + str(result))
            elif operator == "-":
                result = first_operand - second_operand
                print("answer" + str(result))
            elif operator == "*":
                result = first_operand * second_operand
                print("answer" + str(result))
            elif operator == "/":
                result = first_operand / second_operand
                print("answer " + str(result))
            else:
                print(" невірна дія ")
        print(name_us + (" ") + "дії з 0 не проходять")
        print("Введіть пароль")
    if not pass_us == stored_pass:
        print("try again")
    if counter == 2:
        print("last attempt")
print("try another time")
print()
