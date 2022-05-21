from tkinter import *

some_list= ['a','b','c','b','d','m','n','n']

my_list = sorted(some_list)
 
duplicates = []
for i in my_list:
     if my_list.count(i)>1:
         if i not in duplicates:
             duplicates.append(i)

print(duplicates)