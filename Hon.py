l= [9,14,12,3,74,15]
print('Before')

for value in l:
    print(value)
print("After")


for loops with range search.py
ylist=[2.3,7.3,6.4,7.8,22.4]
target=6.4
present=False
for value in range (len(ylist)):
    if ylist[value]==target:
        print(target, 'is in the list')
        present = True
if present==False:
    #print(target,'is not in the list')
z=[2,3,1,4,6,2,8,3]
sml =z[0]
for var in z:
    if var< sml:
        sml = var
print('The smallest value in the list is =',sml)
mylist=[1,2,3]

#Append
mylist.append(4)
print('After appending 4 using append():', mylist)

#Extend
anlist=[5,6,7]
mylist.extend(anlist)
print('After extending using extend():', mylist)

Insert
mylist.insert(2,10)#insert 10 at index 2
print('After inserting 10 at index 2 using insert():', mylist)

remove
mylist.remove(3)
print('After removing 3 using remove():',mylist)

a=['Iron man','Black panther', 'Thor']
a.append('Hulk')
a.append('Dr.strange')
a.insert (1,'Spiderman')
a.insert (3,'Black widow')
print('Update avengers list is:', a)