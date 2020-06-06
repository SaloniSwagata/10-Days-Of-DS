def is_unique(input_str):
    L=[]
    for i in input_str:
        i.upper()
        if i not in L:
            L.append(i)
        else:
            if i.isalpha():
                return False
    return True
print(is_unique("abCDE"))
print(is_unique("nonunique"))

def str_to_int(input_str):
    l=len(input_str)
    l-=1
    d={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    number=0
    for i in input_str:
        number+=d[i]*(10**l)
        l-=1
    return number
print(str_to_int("1234"))
