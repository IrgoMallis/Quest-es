def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)

    return fib_sequence

def verifica_fibonacci(num):

    fib_sequence = fibonacci_sequence(num)

    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número: "))
resultado = verifica_fibonacci(numero)
print(resultado)