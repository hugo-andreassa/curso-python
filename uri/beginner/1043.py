
entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

if a+b > c and b+c > a and a+c > b:
    peri = a + b + c
    print("Perimetro = {p:1.1f}".format(p=peri))
else:
    area = .5*(a+b)*c
    print("Area = {a:1.1f}".format(a=area))

