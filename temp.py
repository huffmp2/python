try:
    inp = float(input('Enter Fahrenheit Temperature: '))
except:
    print('Please enter a number.')
    quit()
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print (cel)
quit()
 

