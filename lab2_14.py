def remove_item(set_data, item):
    set_data.discard(item)  # Using discard()
    # Alternatively, you can use remove() method:
    # set_data.remove(item)

# Example usage:
input_set = {1, 2, 3, 4, 5}
item_to_remove = 3

remove_item(input_set, item_to_remove)
print("Updated Set:", input_set)
