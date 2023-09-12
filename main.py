#################################################### FUNCTION IN PYTHON #########################################

# function is a block of code that perform specific task
#
# PARAMETER       : DETAIL
# arg1,...argN    : Regular argument
# *args           : unnamed positional argument
# kw1,..kwN       : keyword only argument
# **kwargs        : the ret of the keyword args
#
# defining and calling a simple function
# def functionName(parameter):
#     statement

def hi():
    print("hello")
hi()

#with paramete
def gree(greet):
    print(greet)
gree("good morning")

#giving default value
def g(greet="good morning"):
    print(greet)


g() #using the default value

g("how are you doing ?") #changing the default value

#do nothing
def dn():
    pass

print(dn())

################# Defining a function ith arbitrary number of arguments ######################################

#Arbitrary number of positional argument (*args) : this takes one * before args

def de(*args):
    for i in args:
        print(i)

de(1,3,2,2,23,4,7,8,9)
li=[1,9,22,3,4,7,6,5]
de(*li)

#you can not uee default value for arbitrary *args
#def de(*args = 9):

########## Arbitrary number of keyword argument (**kwargs) ############

def de(**kwargs):
    for n,v in kwargs.items():
        print(n, v)

# de(v=1,v1=3,v7=7,v9=9,b=3)
dic={'f':7, 'e':4, 'll':'r', 'l':8, 'i':'ll'}
de(**dic)

#you can not provide default value for **kwargs and you cannot call it without the name
#you can mix **kwargs with other opttional and required argument but the order inside the definition matters

#the positional kw arguments comes first (required args) followed
#by arbitrary *args (optional) followed by keyword-only args (required) finally **Kwargs


############################################# LAMBDA FUNCTION #########################################################
def hi():
    print("hello")
hi()
#lambda version
s=lambda :'hello'
print(s())

#passing argument to lambda
ss = lambda d:d.strip().upper()
print(ss("hi bro, hello man"))

#passing arbitrary no. of args and kwargs to lambda
ll=lambda s, *args, **kwargs:print(s,args,kwargs)
ll('wwee','tis', m='mister')

lll = lambda x:3*x
print(lll(7))

#defining a function with optional argument
def hia(na="this is optional"):
    print(na)
hia()
hia('we changed the values')

#Terminology
# Argument  : actual parameter being passed to a function
# Parameter : the receiving variable that is used in a function
def foo(x): # x is a parameter here
    print(x)

foo('hey')
foo('yeah')
foo(7)
x='hey man'
foo(x)

# 'hey', 'yeah', 7 and x are all argument

###################################### Returning values from a function #####################################
def hi():
    return 7
print(hi())
p=hi()
print(p)
#operation ends at the return statement, subsequent statement after return will not be executed
def ff():
    return 99
    print('will not be executed')

print(ff())

#you can return multiple values
def ff():
    return 99,90
print(ff())

#a function without return statement implicitly returns none


###### forcing the use of name parameter
def f(*c, d):
    pass
# f(1,3) #throws error
f(1,d=3) # will not throw error
#all parameter specified after * in a function are keyword

def ggt(c,b,*,n):
    pass
# ggt(7,9,0)#takes two positional argument but three was given

print(ggt(1,2,n=4))


#################### NESTED FUNCTION #############################
def fibonacci(n):
    def step(a,b):
        return b, a+b
    a,b=0,1
    for i in range(10):
        a,b = step(a,b)
    return a

print(fibonacci(4))

def madder(n):
    def adder(x):
        return n+x
    return adder
ad=madder(7)
ads= madder(9)
print(ad(7))
print(ads(3))

def repeat(f,n,x):
    for i in range(n):
        x = f(x)
    return x
print(repeat(ad,7,1))

################ RECURSIVE FUNCTION ###############
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(8))