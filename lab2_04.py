def count_repeated_characters(string):
    count = {}
    
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    repeated_chars = {char: freq for char, freq in count.items() if freq > 1}
    
    return repeated_chars

# Example usage:
input_string = input("Enter a string: ")
result = count_repeated_characters(input_string)
print("Repeated Characters:")
for char, freq in result.items():
    print(f"{char}: {freq}")
