x = "UCA"


def University():
    x = "Khorog State University"
    print(x)


def myFunction():
    global x
    x = "TNU"
    print(x)


University()
myFunction()
print(x)
