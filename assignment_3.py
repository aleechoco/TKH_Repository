names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
longest_name = len(names_list[0]) 
for name in names_list:
    if len(name)>longest_name:
         print (name + " is the longest name in the list.")
    else:
        x = len(names_list[0])
        longest_name = len(names_list[x + 1])
print (longest_name)
