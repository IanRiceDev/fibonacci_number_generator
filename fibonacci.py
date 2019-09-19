
fibonacci_iterator_1 = 1
fibonacci_iterator_2 = 1

print(fibonacci_iterator_1)
print(fibonacci_iterator_2)
iterator = 0

fibonacci_number = fibonacci_iterator_1 + fibonacci_iterator_2

while iterator < 100:

    print(fibonacci_number)
    iterator = iterator + 1
    fibonacci_iterator_1 = fibonacci_iterator_2
    fibonacci_iterator_2 = fibonacci_number
    fibonacci_number = fibonacci_iterator_1 + fibonacci_iterator_2
