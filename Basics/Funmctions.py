# DEFINE A BASIC FUNCTION
# def hello_func(): 
#     print ("hello world!")
#     name = input("what is your name? ")
#     print("Nice to meet you, " , name)


# thats how we define a new function 

# adding parameters to our function: 
# def hello_func(greeting): 
#     print ("hello world!")
#     name = input("what is your name? ")
#     print(greeting, name)

# hello_func("how are you doing")
# hello_func("Hey whats up?")



# function that returns a value -> result is 27 here
# def cube (x):
#     return x*x*x

# result = cube(3) 
# print(result)

# function with default value for a parameter
# def hello_func(greeting, name = None): 
#     print ("hello world!")
#     if name == None:
#      name = input("what is your name? ")
#     print(greeting, name)
# hello_func(name= "Mir", greeting="Nice to meet you")


# function with variable number of parameters
def multi_add(*args): 
    result = 0
    for x in args:
        result = result + x 
    return result

print(multi_add(4, 5, 10, 4, 6, 4*4))
   