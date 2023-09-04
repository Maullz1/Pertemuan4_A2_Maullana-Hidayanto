x = int(input())
y = int(input())
z = int(input())

if x > y and x > z :
    if y > z:
        print(y)
    else :
        print(z)
elif y > x and y > z :
    if x > z:
        print(x)
    else :
        print(z)
else :
    if x > y:
        print(x)
    else :
        print(y)