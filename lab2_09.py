def find_index(tuple_data, item):
    try:
        index = tuple_data.index(item)
        return index
    except ValueError:
        return None

# Example usage:
input_tuple = ('a', 'b', 'c', 'd', 'e')
search_item = 'c'
result = find_index(input_tuple, search_item)

if result is not None:
    print(f"The index of '{search_item}' in the tuple is: {result}")
else:
    print(f"'{search_item}' is not found in the tuple.")
