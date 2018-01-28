A=[1,5,12,14,17,24,28,39,44,51,59]
def BS(A,l,r,key):
    c=0
    if l>r:return -1
    m=(l+r)//2
    if A[m]==key:return m
    elif A[m]>key:return BS(A,l,m-1,key)
    else:return BS(A,m+1,r,key)
    
    
key=28
l=0
r=len(A)-1
result=BS(A,l,r,key)
print(result)
