# Write a python programme which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard.


total = 0
list = []
while True:
    number = input("Enter the price or press q to quit: \n")
    list.append(number)
    if number != "q":
        total += int(number)
        print(f"Total so far : {total}")
    else:
        print(f"Thanks for shopping with us! \n Your Total Bill :{total}")
        print("Shrirao Stores".upper())
        n = len(list)
        for i, n in enumerate(range(n-1), start=1):
            print(i, list[n])
        break




        
