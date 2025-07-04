#call your constructor and destructor 
class employee():
    def __init__(self):
        print("employee hired!")

    def __del__(self):
        print("employee fired!")

def checking():
    print("we will create an object:")
    e=employee()
    print("the object is created:" )
    return e 
e=checking()

