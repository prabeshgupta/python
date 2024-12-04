#Array: Collection of elements

# Array Format
my_array =  [1,2,3,4,5,6,7,8]

#Access array element using index
print(my_array[2])

#Array slicing
print(my_array[3:6])

#Slicing with steps
print(my_array[2:7:2])

#Print all elements
print(my_array[:])

#Print all elements in reverse order
print(my_array[::-1])

#Print from given index to end
print(my_array[3:])

#Print from starting to given index
print(my_array[:4])

#Add element to array
my_array += [10]
print(my_array)

my_array2= [11,12,13]
my_array+=my_array2
print(my_array)

my_array.append(15)
print(my_array)

#Insert element in specified index
my_array.insert(4, 40)
print(my_array)

#Remove the last element
my_array.pop()
print(my_array)

#Remove the element of specified index
my_array.pop(4)
print(my_array)

#Remove the element (First Occurance)
my_array.remove(13)
print(my_array)

#Length of array
print(len(my_array))


#Sets: Collection of unique elements

#Set Format
my_set_a = {1,3,5,7,7,9}
my_set_b = {2,3,4,6,7,9,0,3}

print(my_set_a)

#Union
print(my_set_a.union(my_set_b))

#Intersection
print(my_set_a.intersection(my_set_b))

#A only
print(my_set_a - my_set_b)


#Dictionary: Stores data in key value pairs.

#Dictionary Format
my_dict= {
    'name':'Prabesh',
    'age': 22,
    'height': 5.10
}

print(my_dict)

#Add key value pair
my_dict['programmer']= True
print(my_dict)

#Add key value pairs
my_dict.update({'country': 'Nepal', 'blood_group': 'B+'})
print(my_dict)

#Delete key value pair by passing key
my_dict.pop('name')
print(my_dict)