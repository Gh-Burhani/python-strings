def print_message(message, repeat_count = 1):
    for a in range(repeat_count):
        print(message)


message = input("Enter a message: ")
repeat_count = int(input("Enter count: "))

print_message(message, repeat_count)


