def recursion_01(k):
    if(k>0):
        result=k+recursion_01(k-2)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion Example Results")
recursion_01(10)
