def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    numbers = [2, 5, 8, 11, 14, 17]
    even_numbers = remove_odd_numbers(numbers)
    print("Original list:", numbers)
    print("Even numbers only:", even_numbers)

main()
