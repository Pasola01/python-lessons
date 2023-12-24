user_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
user_name = ["Yurii", "Oleg", "Bob", "Konny", "lex"]

full_list = []
full_list.append(user_list)
full_list.append(user_name)

print(full_list)

def convert(listi):
    return tuple(listi)

print(convert(full_list))