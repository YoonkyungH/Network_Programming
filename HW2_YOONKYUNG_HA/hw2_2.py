a = int(input('input a: '))
b = int(input('input b: '))

while(b != 0):
    if a < b:   # 무조건 a>b이도록 만듦
        a, b = b, a

    (a, b) = (b, (a % b))
    
print(a)
