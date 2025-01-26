import time

def ooola():
    return "This is a normal function"


def slow():
    counter = 0

    for i in range (0, 5, 1):
        time.sleep(2)
        counter += i
        print(counter)
    
    #return("El endpount expero exitosamente")