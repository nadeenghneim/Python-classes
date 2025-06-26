#call your constructor and destructor 
class employee():
    def __init__(self):
        print("employee hired!")

    def __del__(self):
        print("employee fired!")

e=employee()

