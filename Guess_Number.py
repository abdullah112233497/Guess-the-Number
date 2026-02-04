import random
computer=random.randint(1,100)
user=-1
attempt=1
while (user!=computer):
    user=int(input("Enter the number: "))
    if user==computer:
        print(f"You Won!!!,you guess the correct :{computer} in {attempt}")
        attempt+=1

    elif(user<computer):
        attempt+=1
        print("Enter higher number.")
    elif(user>computer):
        attempt+=1
        print("Enter Lower number.")

    
