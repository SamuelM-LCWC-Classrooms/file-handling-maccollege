

def task_1():
    total = 0
    with open("task_1.txt", "r") as f:
        for line in f:
            total = total + int(line) #Converting each line to an integer and then adding it to the total
    return total
#print(task_1())

def task_2():
    user_food = []
    user_choice = "yes"
    while user_choice == "yes": #While loop which keeps track of how many items wanted and repeats itself until customer doesn't want anymore
        food = input("What would you like to order? ")
        user_choice = input("Would you like to continue adding items? ")
        user_food.append(food) #adds to list
    price_total = 0
    with open("menu.csv", "r") as ital: #Opening file
        for num in ital: #For the text in the file
            data = num.split(",") #Distinguishing splits
            for i in range(len(user_food)): #Checking the amount of times for each food item requested
                if user_food[i] == data[0]: #Checking if value in the list is equal to the first value of the row
                    price = float(data[2].replace("\n", "")) #Checking the last value of each row and removing the \n included in the value
                    price_total += price #Adding to total price
    price_total = round(price_total, 2) #Rounding to 2d.p.
    return price_total #Outputting total price
print(task_2())