def count_multiples(numbers, multiples):
    count_dict = {}

    for multiple in multiples:
        count_dict[multiple] = 0

    for number in numbers:
        for multiple in multiples:
            if number % multiple == 0:
                count_dict[multiple] += 1

    return count_dict

numbers = list(map(int, input("Enter the numbers (space-separated): ").split()))
multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count_dict = count_multiples(numbers, multiples)
print(count_dict)
