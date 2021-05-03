
for i in range(1, 101):
    result = i
    if (result % 3 == 0):
        if (result % 3 == 0 and result % 5 == 0):
            print(result, "FizzBuzz")
        else:
            print(result, "Fizz")
    elif (result % 5 == 0):
        if (result % 3 == 0 and result % 5 == 0):
            print(result, "FizzBuzz")
        else:
            print(result, "Buzz")
    else:
        print(result)
