#POLIMORFIZMI

string_length = len("Hello World")
print(string_length)

list_length = len([1, 6, 3, 4, 5])
print(list_length)

tuple_length = len((1, 6, 3, 4, 5))
print(tuple_length)

#Functions examples of polimorfis, one function used for different data types
def add(x, y):
    return x + y
def contatinate(x, y):
    return str(x) + str(y)
def operate(operation, x, y):
    return operation(x, y)

#use both of them for the operate function
print(operate(add, 1, 2))
print(operate(contatinate, "add strings ", "together"))
