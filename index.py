print("WELCOME TO MAYURI CANTEEN")
print("--------------------------")
print()
name = input("Enter your name: ")
roll = input("Enter your roll number: ")
print()
print("MENU")
print("1. Samosa - Rs. 15")
print("2. Maggi - Rs. 50")
print("3. Sandwich - Rs. 40")
print("4. Chowmein - Rs. 60")
print("5. Cold Drink - Rs. 30")
print()
choice = int(input("Enter item number: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Samosa"
    price = 15

elif choice == 2:
    item = "Maggi"
    price = 50

elif choice == 3:
    item = "Sandwich"
    price = 40

elif choice == 4:
    item = "Chowmein"
    price = 60

elif choice == 5:
    item = "Cold Drink"
    price = 30

else:
    print("Invalid choice")
    price = 0

total = price * quantity
print()
print("--------- BILL ---------")
print("Name:", name)
print("Roll Number:", roll)
print("Item:", item)
print("Quantity:", quantity)
print("Price:", price)
print("Total:", total)
print("------------------------")
print("Thank you!")
