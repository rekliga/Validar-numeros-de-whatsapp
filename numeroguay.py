
def guay(n1):
    value = 0
    for i in range(1,n1):
        value +=i
        print(value,n1)
        if value == n1:
            print("es guay")
            break
        elif value > n1:
            print("no es guay")        
            break

guay(20)

         
