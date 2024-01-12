
### Closures ###

def reglaInvde3(original_value):
    def por(value, value2):
        return value * value2 / original_value
    return por


add_closure_percengate = reglaInvde3(100)

print(add_closure_percengate(50,30))
print((reglaInvde3(5))(10,23))


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


from functools import reduce

print(reduce(sum_two_values, numbers))



# 06_ file_handling

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
