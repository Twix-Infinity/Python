my_list = []

my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)

my_list.insert(1, 15)

other_list = [50, 60, 70]
my_list.extend(other_list)

del my_list[-1]

my_list.sort()

my_list.index(30)
print("Index of 30 in the list:", my_list.index(30))