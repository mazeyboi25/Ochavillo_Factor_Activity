def factor(n):
    for i in range(2, n + 1):
        if n % 1 == 0:
            return i


number = int(input("Enter a number that is greater than 2:"))
result = factor(number)

print(f"The smallest factor of {number} other than 1 is {result}.")

while True:
    if number < 2:
        print("Invalid input. Input a number greater than 2.")
        break
