class welcome:
    def __init__ (self,name):
        self.name=name
        
    def greet(self):
        print(f"Hello {self.name} , welcome")
    def ask_pet(self):
        print(f"So your pet name is {self.pet_name}")

user_one=welcome("sudheer")
user_one.greet()
user_one.ask_pet()

user_one=welcome("ram")
user_one.greet()

user_one=welcome("vishnu")
user_one.greet()
