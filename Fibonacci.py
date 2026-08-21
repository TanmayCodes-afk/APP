# Fibonacci using Tabulation and Memoization

# Tabulation
def Tabulation_Fibonacci(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[:n + 1]


# Memoization
def Memoization_Fibonacci(n):
    memo = {0: 0, 1: 1}

    def fibonacci(i):
        if i not in memo:
            memo[i] = fibonacci(i - 1) + fibonacci(i - 2)
        return memo[i]

    fibonacci(n)
    return [memo[i] for i in range(n + 1)]


# Main program
while True:
    print("--- Menu ---")
    print("1.Find Fibonacci sequence through Tabulation")
    print("2.Find Fibonacci sequence through Memoization")
    print("3.exit")

    choice = int(input("Enter your choice :"))

    if choice == 3:
        print("Exiting the program")
        break

    elif choice == 1:
        n = int(input("Enter n :"))
        sequence = Tabulation_Fibonacci(n)
        print("Sequence:", sequence)
        print("Fibonacci number:", sequence[-1])

    elif choice == 2:
        n = int(input("Enter n :"))
        sequence = Memoization_Fibonacci(n)
        print("Sequence:", sequence)
        print("Fibonacci number:", sequence[-1])

    else:
        print("Enter valid Choice!!!")
