#Excersise: print duplicates in a given list
#please don't use sets for this excersise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates_list = []

for duplicate in some_list:
  if some_list.count(duplicate) > 1:    #count() counts the number of times it sees the object
    if duplicate not in duplicates_list:    #prevents printing double values
      duplicates_list.append(duplicate)

print(duplicates_list)