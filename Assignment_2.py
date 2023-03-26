#1
import csv
import array as ARR
array1 = ARR.array('i', [120, 20, 100, 10, 40, 30, 50, 45, 70, 60])
tuple1 = (30, 25, 35, 40, 50, 10, 56)
list1 = ['Rit', 'Dubai', 'Uae', 'Gulf', 'Samir El-Masri', 'Sharjah', 'Abu Dhabi', 'Umm Al Quwain', 'Ajman']
set1 = {'red', 'blue', 'green', 'yellow', 'purple', 'pink', 'brown', 'black'}
dictionary1 = {
    'name': 'Karim',
    'age': 18,
    'address': 'Rim Str. Silcon Oasis',
    'university': 'Rit',
    'college': 'Computer Science',
    'department': 'Data Science',
    'semester': 'Fall',
    'year': 2,
    'credits': 35,
    'gpa': 4.3
}
#Getting the required result in the given csv file
print (array1)
print (tuple1)
print(list1)
print(set1)



#finding through dictionary for the required value
for value in list1:
    if value == 'Fujairah':
        print('found')
        break
else:
        print(None)
    
    for value in set1:
    if value == 'Data Science':
        print('found')
        break
else:
        print(None)


#2(a) for sort in placeby using insertion sort
for x in range(0,len(array1)):
    temp=array1[x]
    -1
    while j>=0 and temp<array1[j]:
        array1[j+1],array1[j]=array1[j],array1[j+1]
        j=j-1

def sortmerge(array):
    if len(array)<=1:
        return array
    midpoint=len(array)//2
    left,right=sortmerge(array[:midpoint]),sortmerge(array[midpoint:])
    return merge(left,right)
def merge(left,right):
    result=[]
    l_point=r_point=0
    while l_point< len(left) and r_point<len(right):
        if left[l_point]<right[r_point]:
            result.append(left[l_point])
            l_point +=1
        else:
            result.append(right[r_point])
            r_point+=1
    result.extend(left[l_point:])
    result.extend(right[r_point:])
    return result

ltuple1=list(tuple1)
exacttuple1=sortmerge(tuple1)
tuple1=tuple(exacttuple1)

def quicksort(seq):
    lngth = len(seq)
    if lngth < 1:
        return seq
    else:
        pivot = seq.pop()

    items_greater = []
    items_lower = []

    for item in seq:
        if item >pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

quicksort(list1)
#2b quick sorting for set1
quicksort(set1)

B_dict1={}
for x in sorted(dict1):
  
  temp=dictionary1[x]
    B_dict1[x]=temp
dictionary1=B_dict1



#2c
with open('assignment2_file.text','w') as file1:
    data=str(array1)+'\n'+str(tuple1)+'\n'+str(list1)+'\n'+str(set1)+'\n'+str(dictionary1)

    file1.write(data)



#3)appending the sorted file
open('assignment2_file.csv', 'a') as A:
    A=csv.assignment(a)
    for x in con:
        temp=[]
        temp.append(x)
        writer.writerow(temp)
    


main()

  
  
    
    
    
    
    
    
    
    
    
