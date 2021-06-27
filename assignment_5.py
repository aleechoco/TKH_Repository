names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

def split(names_list):
    even_list = []
    odd_list = []
    for word in names_list:
        if (len(word) % 2 == 0):
            even_list.append(word.replace(word[0],'b'))
        else:
            odd_list.append(word.replace(word[-1],'c'))
    print("Even:", even_list)
    print("Odd:", odd_list)
    return even_list
    print (even_list)





