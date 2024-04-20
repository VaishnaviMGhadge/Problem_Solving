dict1={1:'Shreya',2:"vaishnavi",3:'purva'}
print(dict1)     # dictionary creation
print(dict1[1]) # accesing the value for the key 
dict1[1]='Pooja'
print(dict1)
dict1.pop(1) ## deletin the items 
print(dict1)
print(dict1.values()) # getting the values 
print(dict1.keys()) # getting the keys
print(dict1.values())

print("*******")

if 2 in dict1.keys():
    print(dict1[2])


value = dict1.get(2, 'default_value')
print(value)


for key,value in dict1.items():
    print(key,value)
