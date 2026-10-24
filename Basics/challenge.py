def count_numbers(which, numbers):
    if which != "even" and which != "odd":
        return -1

    result = 0

    for num in numbers:
        if which == "even" and num % 2 == 0:
            result += 1
        elif which == "odd" and num % 2 != 0:
            result += 1

    return result


print(count_numbers("even", [7, 2, 13, 65]))  # 1
print(count_numbers("ODD", [1, 3, 5, 6]))     # -1
print(count_numbers("prime", [1, 2, 3]))      # -1
print(count_numbers("Even", [0]))             # -1


