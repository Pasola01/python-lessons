correct_pin = 0000

print("Enter your pin")

entered_pin = input()

if correct_pin == entered_pin:
    print("success")
else:
    print("error try again you have 2")
    entered_pin = input()
    if correct_pin == entered_pin:
        print("success")
    else:
        print("error you have 1 try")
        entered_pin = input()
        if correct_pin == entered_pin:
            print("ok")
        else:
            print(" blocked")