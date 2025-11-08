class welcome:
    def __init__ (self,name):
        self.name=name
        
    def greet(self):
        print(f"Hello {self.name} , welcome")

user_one=welcome("sudheer")
user_one.greet()

user_one=welcome("ram")
user_one.greet()

user_one=welcome("vishnu")
user_one.greet()
