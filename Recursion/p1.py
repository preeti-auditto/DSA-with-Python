# how to print 1 to n using recursion
def print_numbers(i,n):
    if i>n:
        return
    print(i)
    print_numbers(i+1,n)
print_numbers(1,9)