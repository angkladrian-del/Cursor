print("FizzBuzz")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: # si el número es divisible por 3 y 5, se imprime FizzBuzz
        print("FizzBuzz")
    elif i % 3 == 0: # si el número es divisible por 3, se imprime Fizz
        print("Fizz")
    elif i % 5 == 0: # si el número es divisible por 5, se imprime Buzz
        print("Buzz")
    else: # si el número no es divisible por 3 ni por 5, se imprime el número   
        print(i)