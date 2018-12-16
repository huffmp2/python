filename = 'pro_poll.txt'

print("Enter 'quit' when you are finished.")
while True:
    why = input("\nWhy do you like programming? ")
    if why == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(why + "\n")
