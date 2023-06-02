def get_elements(tuple_data):
    fourth_element = tuple_data[3]
    fourth_from_last_element = tuple_data[-4]
    return fourth_element, fourth_from_last_element

# Example usage:
input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = get_elements(input_tuple)
print("4th Element:", result[0])
print("4th Element from Last:", result[1])
