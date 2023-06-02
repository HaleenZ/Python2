def count_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

# Example usage:
input_string = input("Enter a string: ")
result = count_character_frequency(input_string)
print("Character Frequency:")
for char, count in result.items():
    print(f"{char}: {count}")
