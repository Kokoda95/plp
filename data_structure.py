# Create an empty list.
my_list = []
# Append some elements to a list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# Extend my_list with another list.
my_list.extend([50, 60, 70])
print(my_list)
# Remove the last element from the list.
my_list.remove(70)
print(my_list)
# Sort the list in ascending order.
print(sorted(my_list))
# Print the index of 30 in the list.
print(my_list.index(30))
