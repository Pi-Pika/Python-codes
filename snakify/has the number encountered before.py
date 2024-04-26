def check_encountered_numbers(sequence):
    encountered = {}
    for num in sequence:
        if num in encountered:
            print("YES")
        else:
            print("NO")
            encountered[num] = True

# Example usage:
sequence = [1, 2, 3, 2, 4, 1, 5]
check_encountered_numbers(sequence)
