class Dog: 
    """Simple attempt to model a dog"""
    #this can be seen as the constructor in java 
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name= name
        self.age=age

    #simulating a dog sitting in response to a command     
    def sit(self):
        print(f"{self.name} is now sitting.")

    #simulating a dog rolling over in response to a command 
    def roll_over(self):
        print(f"{self.name} is rolling over. ")

my_dog= Dog('Flash',7)
#my_dog.name -> Accessing attributes
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.roll_over() #calling a method from the class Dog by having my_dog object 

your_dog= Dog('Princess', 9)
print(f"{your_dog.name} is {your_dog.age} years old")
your_dog.sit()
