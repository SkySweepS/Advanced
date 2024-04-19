def reverse_numbers(numbers):
    reversed_nums = []
    while numbers:
        int_i = numbers.pop()
        reversed_nums.append(int_i)

    return print(" ".join(reversed_nums))


reverse_numbers(input().split(" "))
