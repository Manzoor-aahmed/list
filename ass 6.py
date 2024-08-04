def sum_of_list(numbers):
    return sum(numbers)
a =[1,5,6,8,4]
print(sum_of_list(a))



tuple=(2,8,9,7,6,6)
a = min(tuple)
print(a)


def square_set(number):
    return{i*i for i in number}
set={6,7,8,9,0}
squared_number=square_set(set)
print(squared_number)


def get_items(dictionary):
    return list(dictionary.items())
dict={'name': 'ambreen','city':'karachi'}
items_list =get_items(dict)
print(items_list)