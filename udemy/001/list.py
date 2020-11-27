
my_list = [1, 2, 3]
print(my_list)

my_list = ["one", 2, 3]
print(my_list)

my_list = ["one", "two", "three"]
another_list = ["four", "five"]
print(my_list)
print(another_list)

new_list = my_list + another_list
print(new_list)

new_list[0] = "ONE UPDATED"
print(new_list[1:])
print(new_list[::2])

new_list.append("six")
new_list.append("seven")
print(new_list)

popped_item = new_list.pop()
print(popped_item)

popped_item = new_list.pop(0)
print(popped_item)

sorted_list_numbers = [1,5,6,8,2,7,4]
sorted_list_numbers.sort()
print(sorted_list_numbers)

sorted_list_numbers.reverse()
print(sorted_list_numbers)

sorted_list_letters = ["j","g","h","v","r","u","a"]
sorted_list_letters.sort()
print(sorted_list_letters)

sorted_list_letters.reverse()
print(sorted_list_letters)