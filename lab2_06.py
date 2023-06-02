color_dict = {'red': '#FF0000',
              'green': '#008000',
              'black': '#000000',
              'white': '#FFFFFF'}

sorted_dict = dict(sorted(color_dict.items(), key=lambda x: x[0]))

print("Sorted Dictionary by Key:")
for key, value in sorted_dict.items():
    print(key, ":", value)
