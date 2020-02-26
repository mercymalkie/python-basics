class calc1:
 def add(a,b):
    return (a+b)
 def mut(a,b):
    return (a*b)

class calc2(calc1):
 def div(a,b):
    return (a/b)
 def sub(a,b):
    return (a-b)


f=calc2
print (f.add(9,10))

