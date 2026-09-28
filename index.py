print("================================")
print("   WELCOME TO MAYURI CANTEEN")
print("================================")

# Student details
name = input("Enter your name: ")
roll = input("Enter your roll number: ")

# Menu
print("---------- MENU ----------")
print("1. Samosa - Rs. 15")
print("2. Maggi - Rs. 50")
print("3. Sandwich - Rs. 40")
print("4. Chowmein - Rs. 60")
print("5. Cold Drink - Rs. 30")

# Order
choice = int(input("\nEnter item number: "))
quantity = int(input("Enter quantity: "))

# Item and price
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
    print("Invalid item number")
    item = "Invalid"
    price = 0

# Calculate bill
total = price * quantity

# Final bill
print("\n========== FINAL BILL ==========")
print("Name     :", name)
print("Roll No. :", roll)
print("Item     :", item)
print("Price    : Rs.", price)
print("Quantity :", quantity)
print("Total    : Rs.", total)
print("================================")
print("Thank you for visiting!")

