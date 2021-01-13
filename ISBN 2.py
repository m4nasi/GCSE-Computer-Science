print("Please enter you ISBN number")
ISBNNumber = input("?")
for x in ISBNNumber:
    #result = prod(ISBNNumber)
    number = x 
    print(number)
#print(Number)

def multiplyList(ISBNNumber):  
    result = 1
    for x in ISBNNumber: 
        result = int(result) * x
    return result

print(multiplyList(ISBNNumber)) 

#remainder = number % 10
#modulo = 10 - remainder
#print(modulo)
