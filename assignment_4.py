def big_name(words):
    names_list = []
 
    for word in words:
        names_list.append((len(word), word))
        
    names_list.sort()
    
    print("The name with the longest length is:", names_list[-1][1])
#to test it out    
a = ["Oliver", "Tiffany", "Tyrone", "Fiona"]
