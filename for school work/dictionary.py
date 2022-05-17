temp = {
    "brand": "Ford", # string
    "colors": ["Black","red","white"], # list
    "Model": "2005", #int
    "license": False, # boolean
    "doors": 4, # quantity
    4.56: False,
    True: 25     #the key can be anything
}
print(temp)#print everything in the dict
print(type(temp))#prints what temp is (class dict)
print(temp["brand"])#prints only the thing assosiated with the squared bracket
temp['plate'] = 'TP40SV' #adds plate: TP40SV at the end
del temp["license"] #removes the whole key
temp.pop("brand") #also removes the while key
temp.pop("height", -1)#without -1 the program would have an error as height in not in temp
temp["doors"] = temp["doors"] - 2 #removes quantity from key
temp["Model"] = "2004" #replaces key assosiation
print(temp)
temp.popitem()#deletes the last item in temp
print(temp.keys())#prints only the keys
print(temp.values())#prints only the values
#------------------------------------------------------------------------------#
temp2 = {} #does not need to be filled to count as a dict
temp2["food"] = "bread","cheese" #list assosiated with key
print(temp2)
temp.update(temp2)#merges both together (temp 2 takes priority with any dupe keys)