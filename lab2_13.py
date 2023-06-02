def generate_sublists(lst):
    sublists = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])

    return sublists

# Example usage:
input_list = [1, 2, 3]
result = generate_sublists(input_list)
print("Sublists:")
for sublist in result:
    print(sublist)
