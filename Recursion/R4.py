# Tribonnaci prorgarm using recursion
def tri(n):
    if n==0 or n==1 or n==2:
        return n
    return tri(n-1)+ tri(n-2)+ tri(n-2)
print(tri(6))