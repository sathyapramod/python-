# Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.
#Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

counter = 100 # integer
miles = 1000.0 # float
name = "Python" # string

print(counter)
print(miles)
print(name)

# Multiple Assignment
 a = b = c = 1

 a,b,c = 1,2,"Python"

#Python numbers
 var1 = 1
 var2 = 20

#Python String
 str = "Hellow World!"

 print(str) # complete string
 print(str[0]) # first char of string
 print(str[2:5]) # char starting from 3rd to 5th
 print(str[2:]) # char string from 3rd
 print( str * 2) # string two times
 print(str + "Test") # concatination

# Python list
 list = ['abcd', 786, 2.23, 'john', 70.2]
 tinylist = [123, 'john']

 print(list)
 print(list[0]) # first element of list
 print(list[1:3]) # 2nd till 3rd
 print(list[2:]) # from 3rd element
 print(tinylist * 2) # list two times
 print(list + tinylist) # concatination of lists

# python Tuple
    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
    tinytuple = (123, 'john')

    print tuple               # Prints the complete tuple
    print tuple[0]            # Prints first element of the tuple
    print tuple[1:3]          # Prints elements of the tuple starting from 2nd till 3rd 
    print tuple[2:]           # Prints elements of the tuple starting from 3rd element
    print tinytuple * 2       # Prints the contents of the tuple twice
    print tuple + tinytuple   # Prints concatenated tuples

# Python Dictionary

 dict = {}
 dict['one'] = "This is one"
 dict[2] = 'this is two'

 tinydict = {'name':'john', 'code':6789, 'dept':'development'}

 print dict['one']       # Prints value for 'one' key
 print dict[2]           # Prints value for 2 key
 print tinydict          # Prints complete dictionary
 print tinydict.keys()   # Prints all the keys
 print tinydict.values() # Prints all the values