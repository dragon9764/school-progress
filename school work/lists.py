#-------------lists-------------------#

shopping_list = ["cheese", "bread", "ham"]
#counts from 0 so 2 is 3rd item
print(shopping_list[2])

#------------item_adding--------------#

print(shopping_list)
shopping_list.append("Chicken")
#adds item to the end ^
print(shopping_list)

#-----------length_of_list------------#

print(len(shopping_list))
#length of shopping list
print(shopping_list[-1])
#prints the last item on list

#----------last_item_removing---------#

shopping_list.pop()
#removes last item from list
print(shopping_list)

#-------------replaceing--------------#

shopping_list[2] = "tests"
print(shopping_list)

#--------------searching--------------#

if "cheese" in shopping_list:
    print("True")
