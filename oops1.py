#initialize the class
class employee:
    #special method/magic method/dunder method -constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id =11
        self.sal =30000
        self.des ="HP"
        print("attributes/data has been initailized")

    def travel(self,destination):
        print("this travel function was called manually")
        print(f"employ is travelling to {destination}")
#create an object/instance of the class
sam=employee()
#print attributes
print(sam.id)
print(sam.sal)
print(sam.des)
#calling amethod
sam.travel("haryana")
print(type(sam))