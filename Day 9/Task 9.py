def integer_square_root(k):
    return (int(k**0.5))
print(integer_square_root(300))

def find(A):
    m=A[0]
    p=0
    for position,i in enumerate(A):
        if i<m:
            m=i
            p=position
    return (p+1)
print(find([4,5,6,7,1,2,3]))
