import os
os.system('cls')

option = 0 
inventory = []

def addProduct(name, quantity, price, code):    
    os.system('cls')
    product = {"name": name, "quantity": quantity, "price": price, "code": code} 
    inventory.append(product) 
    print("Product added successfully.")

def showInventory(): 
    os.system('cls')
    for product in inventory: 
        print('Name:', product["name"]) 
        print("Quantity: ", product["quantity"]) 
        print("Price: $", product["price"])
        print("Code: ", product["code"])
        print("--------------")

def searchProduct(code): 
    os.system('cls')
    for product in inventory: 
        if product["code"] == code: 
            print("Product found:") 
            print("Name: ", product["name"]) 
            print("Quantity: ", product["quantity"]) 
            print("Price: $", product["price"]) 
            print("Code: ", product["code"])

while option != 4: 
    option = int(input("Enter an option:\n1. Add product \n2. Show inventory \n3. Search product \n4. Exit \n")) 
    if option == 1: 
        os.system('cls')
        name = input("Product Name: ") 
        quantity = int(input("Quantity: ")) 
        price = float(input("Price: $")) 
        code = float(input("Code: "))
        addProduct(name, quantity, price, code) 

    if option == 2: 
        os.system('cls')
        showInventory() 

    if option == 3: 
        os.system('cls')
        code = float(input("Product Code: "))
        os.system('cls')
        searchProduct(code) 

if option == 4: 
    os.system('cls')
    print("Exiting the program...") 

else: 
    print("Invalid option. Please try again.")   
print("Program terminated.")
