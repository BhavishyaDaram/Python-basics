# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips= zips
#         self.pockets=pockets

#     def show(self):
#         print(f"your object details are {self.material},{self.pockets},{self.zips}")
# reebok = Factory("leather",3,2)
# campus = Factory("nylon",3,3)

# reebok.show()

# class Animal:
#     a=12; #attribute
    
#     def __init__(self,age):
#         self.age=age #instance attribute
#     def show(self):#ijnstance meathod
#         print("how are you")#instance meathod
#     @classmethod
#     def hello(cls):
#         print("how are you")
#     @staticmethod
#     def static():
#         print("how are you")
# obj=Animal(12)
# obj.static()

#inheritance 
class Parent:
    def speak(self):
        print("can I speak")
class Child(Parent):
    pass

obj=Child()
obj.speak()