
##Append: Adds its argument as a single element to the end of a list. The length of the list increases by one.

my_list = ['PYTHON', 'for'] 
my_list.append('SIT') 
print (my_list) 

##A list is an object. If you append another list onto a list, the first list will be a single object at the end of the list.

my_list = ['PYTHON', 'for', 'SIT'] 
another_list = [6, 0, 4, 1] 
my_list.append(another_list) 
print (my_list) 

##extend(): Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.

my_list = ['PYTHON', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 
print (my_list) 


##A string is an iterable, so if you extend a list with a string, you’ll append each character as you iterate over the string.


my_list = ['PYTHON', 'for', 6, 0, 4, 1] 
my_list.extend('SIT') 
print (my_list)

##del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.

##pop() :- This method deletes the element at the position mentioned in its arguments.


# Python code to demonstrate the working of 
# del and pop() 

# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8] 

# using del to delete elements from pos. 2 to 5 
# deletes 3,5,4 
del lis[2 : 5] 

# displaying list after deleting 
print ("List elements after deleting are : ",end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using pop() to delete element at pos 2 
# deletes 3 
lis.pop(2) 

# displaying list after popping 
print ("List elements after popping are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 


##insert(a, x) :- This function inserts an element at the position mentioned in its arguments. It takes 2 arguments, position and element to be added at respective position.

##remove() :- This function is used to delete the first occurrence of number mentioned in its arguments.

# Python code to demonstrate the working of 
# insert() and remove() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using insert() to insert 4 at 3rd pos 
lis.insert(3, 4) 

# displaying list after inserting 
print("List elements after inserting 4 are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using remove() to remove first occurrence of 3 
# removes 3 at pos 2 
lis.remove(3) 

# displaying list after removing 
print ("List elements after removing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 


##sort() :- This function sorts the list in increasing order.

##reverse() :- This function reverses the elements of list.

	# Python code to demonstrate the working of 
# sort() and reverse() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using sort() to sort the list 
lis.sort() 

# displaying list after sorting 
print ("List elements after sorting are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using reverse() to reverse the list 
lis.reverse() 

# displaying list after reversing 
print ("List elements after reversing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ")



##extend(b) :- This function is used to extend the list with the elements present in another list. This function takes another list as its argument.
##clear():- This function is used to erase all the elements of list. After this operation, list becomes empty.




# Python code to demonstrate the working of 
# extend() and clear() 

# initializing list 1 
lis1 = [2, 1, 3, 5] 

# initializing list 1 
lis2 = [6, 4, 3] 

# using extend() to add elements of lis2 in lis1 
lis1.extend(lis2) 

# displaying list after sorting 
print ("List elements after extending are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
	
print ("\r") 

# using clear() to delete all lis1 contents 
lis1.clear() 

# displaying list after clearing 
print ("List elements after clearing are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
	
#index() is an inbuilt function in Python, which searches for given element from start of the list and returns the lowest index where the element appears.
# Python3 program for demonstration 
# of list index() method 

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 

# Will print the index of '4' in list1 
print(list1.index(4)) 

list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 

# Will print the index of 'cat' in list2 
print(list2.index('cat')) 

# Python3 program for demonstration 
# of index() method 

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 

# Will print index of '4' in sublist 
# having index from 4 to 8. 
print(list1.index(4, 4, 8)) 

# Will print index of '1' in sublist 
# having index from 1 to 7. 
print(list1.index(1, 1, 7)) 

list2 = ['cat', 'bat', 'mat', 'cat', 
		'get', 'cat', 'sat', 'pet'] 

# Will print index of 'cat' in sublist 
# having index from 2 to 6 
print(list2.index('cat', 2, 6 )) 


# Python3 program for demonstration 
# of index() method 

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 

# Will print index of '4' in sublist 
# having index from 4 to 8. 
print(list1.index(4, 4, 8)) 

# Will print index of '1' in sublist 
# having index from 1 to 7. 
print(list1.index(1, 1, 7)) 

list2 = ['cat', 'bat', 'mat', 'cat', 
		'get', 'cat', 'sat', 'pet'] 

# Will print index of 'cat' in sublist 
# having index from 2 to 6 
print(list2.index('cat', 2, 6 )) 


# Python3 program for demonstration 
# of index() method error 


list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 

# Return ValueError 
print(list1.index(10)) 

#count() is an inbuilt function in Python that returns count of how many times a given object occurs in list.

# Python3 program to count the number of times 
# an object appears in a list using count() method 

list1 = [1, 1, 1, 2, 3, 2, 1] 

# Counts the number of times 1 appears in list1 
print(list1.count(1)) 

list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b'] 

# Counts the number of times 'b' appears in list2 
print(list2.count('b')) 

list3 = ['Cat', 'Bat', 'Sat', 'Cat', 'cat', 'Mat'] 

# Counts the number of times 'Cat' appears in list3 
print(list3.count('Cat')) 



# Python3 program to demonstrate 
# the error in count() method 

list1 = [1, 1, 1, 2, 3, 2, 1] 

# Error when two parameters is passed. 
print(list1.count(1, 2)) 

# Python3 program to count the number of times 
# an object appears in a list using count() method 

list1 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), 
		('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ] 

# Counts the number of times 'Cat' appears in list1 
print(list1.count(('Cat', 'Bat'))) 

# Count the number of times sublist 
# '[1, 2]' appears in list1 
print(list1.count([1, 2])) 


# Python3 program to count the number of times 
# an object appears in a list using count() method 

lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat'] 

# To get the number of occurrences 
# of each item in a list 
print ([ [l, lst.count(l)] for l in set(lst)]) 

# To get the number of occurrences 
# of each item in a dictionary 
print (dict( (l, lst.count(l) ) for l in set(lst))) 


# List of Integers 
numbers = [1, 3, 4, 2] 

# Sorting list of Integers 
numbers.sort() 

print(numbers) 

# List of Floating point numbers 
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68] 

# Sorting list of Floating point numbers 
decimalnumber.sort() 

print(decimalnumber) 

# List of strings 
words = ["Python", "For", "Games"] 

# Sorting list of strings 
words.sort() 

print(words) 


# List of Integers 
numbers = [1, 3, 4, 2] 

# Sorting list of Integers 
numbers.sort(reverse=True) 

print(numbers) 

# List of Floating point numbers 
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68] 

# Sorting list of Floating point numbers 
decimalnumber.sort(reverse=True) 

print(decimalnumber) 

# List of strings 
words = ["Python", "For", "Games"] 

# Sorting list of strings 
words.sort(reverse=True) 

print(words) 


# Python program to demonstrate sorting by user's 
# choice 

# function to return the second element of the 
# two elements passed as the paramater 
def sortSecond(val): 
	return val[1] 

# list1 to demonstrate the use of sorting 
# using using second key 
list1 = [(1,2),(3,3),(1,1)] 

# sorts the array in ascending according to 
# second element 
list1.sort(key=sortSecond) 
print(list1) 

# sorts the array in descending according to 
# second element 
list1.sort(key=sortSecond,reverse=True) 
print(list1) 


# Sometimes, there is a need to reuse any object, hence copy methods are always of a great utility. Python in its language offers a number of ways to achieve this. This particular article aims at demonstrating the copy method present in list. Since list is widely used hence, its copy is also necessary.

# Returns a shallow copy of a list.
# Shallow copy means the any modification in new list won’t be reflected to original list

# Python 3 code to demonstrate 
# working of list.copy() 

# Initializing list 
lis1 = [ 1, 2, 3, 4 ] 

# Using copy() to create a shallow copy 
lis2 = lis1.copy() 

# Printing new list 
print ("The new list created is : " + str(lis2)) 

# Adding new element to new list 
lis2.append(5) 

# Printing lists after adding new element 
# No change in old list 
print ("The new list after adding new element : " + str(lis2)) 
print ("The old list after adding new element to new list : " + str(lis1)) 


# Deep copy means if we modify any of the list, changes are reflected in both the list as they point to the samereference. Whereas in shallow copy, when we add element in any of the list, only that list is modified.


# Python 3 code to demonstrate 
# techniques of deep and shallow copy 
import copy 

# Initializing list 
lis1 = [ 1, 2, 3, 4 ] 

# Using shallow copy techniques to create a shallow copy 
lis2 = lis1.copy() 
lis3 = copy.copy(lis1) 
lis4 = lis1[:] 

# Adding new element to new lists 
lis2.append(5) 
lis3.append(5) 
lis4.append(5) 

# Printing lists after adding new element 
# No change in old list 
print ("The new list created using copy.copy() : " + str(lis2)) 
print ("The new list created using list.copy() : " + str(lis3)) 
print ("The new list created using slicing : " + str(lis4)) 
print ("The old list after adding new element to new list : " + str(lis1)) 

print ("\n") 

# Using deep copy techniques to create a deep copy 
lis2 = lis1 
lis3 = copy.deepcopy(lis1) 

# Adding new element to new lists 
lis2.append(5) 
lis3.append(5) 


# Printing lists after adding new element 
# changes reflected in old list 
print ("The new list created using copy.deepcopy() : " + str(lis2)) 
print ("The new list created using = : " + str(lis3)) 
print ("The old list after adding new element to new list : " + str(lis1)) 



