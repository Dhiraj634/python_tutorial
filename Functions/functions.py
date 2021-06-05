# defining a function with no parameter
def myFunction():
    print("Hello I am myFunction")


myFunction()  # calling the Function


# defining a function with one parameter
def myFunctionWithArgs(name):
    print(f"Hello I am {name}")


myFunctionWithArgs("ABCD")  # calling a Function with one argument


# defining a function with two parameter
def print_name(firstName, lastName):
    print(f"Hello I am {firstName} {lastName}")


print_name("First", "Second")  # calling the Function with two argument


# defining a function with variable number of parameter
def multiArgument(*args):
    print("Type of args : ", type(args))
    print(args)


multiArgument("first", "second", "third")  # Calling function with 3 argument
# Calling function with 4 argument
multiArgument("first", "second", "third", "fourth")

print_name(firstName="First", lastName="Second")  # Keyword Argument
print_name(lastName="Second", firstName="First")  # Keyword Argument


# Defining a function with multiKeyword argument
def multiKeywordArgument(**multiArg):
    print("Type of multiArg : ", type(multiArg))
    print(multiArg)


# Calling function with 3 keyword argument
multiKeywordArgument(physics=60, chemistry=70, mathematics=90)
# Calling function with 4 keywprd argument
multiKeywordArgument(physics=60, chemistry=70, mathematics=90, biology=75)


# Define a  function with default parameter
def printNTimes(name, n=1):
    print(name * n)


printNTimes("HA", 3)
printNTimes("HA")


# Defining a function that return a value to the caller function
def average(*args):
    return sum(args)/len(args)


# average(50,60,70,80,920) return the calculated average value to the caller
averageValue = average(50, 60, 70, 80, 90)
print("Average value = ", averageValue)


# Defining a function that calls itself i.e. recursion
def recursion(num):
    if(num == 0):
        return
    print(num)
    recursion(num-1)
    # uncomment below print and comment the above one and analyse the result
    # print(num)


recursion(10)
