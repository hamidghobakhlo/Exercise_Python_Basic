# MiniProject_Product
# Select + Alt + Tab
# Select + Shift + Tab
#------------------------Function----------------------------
def help():
        help_text = """
        Tasks:
        - add: Adds a new product.
        - remove: Removes a specified product.
        - edit: Edits a product.
        - search: Searches for a product.
        - display: Displays all products.
        - buy: Buys a product.
        - help: Displays this help text.
        - exit: Exits the program.
        """
        print(help_text)

def add(name):
    if name not in product_names:
        product_names.append(name)
        product_is_bought.append(False)
        product_prices.append(None)
        print("added!")
    else:
        print(f"{name} : already exists!")

def display():
    if len(product_names) == 0:
        print("Empty!")
    for i, p in enumerate(product_names):
        bought = product_is_bought[i]
        price = product_prices[i]
        print(f"{i+1}){p} ==> bought: {bought},price: {price}") 

def remove(name):
    if name in product_names:
        index = product_names.index(name)
        product_names.pop(index)
        product_is_bought.pop(index)
        product_prices.pop(index)
        print("removed!")
    else:
        print(f"{name} : not found!")

def edit(old_name):
    if old_name in product_names:
        new_name = input("Product name:")
        if new_name not in product_names:
            ind = product_names.index(old_name)
            product_names[ind] = new_name
            new_price = int(input("New price: "))
            if product_prices[ind] != None:
                product_prices[ind] = new_price
            else:
                print("Not purchased!")  
            print("edited!")
        else:
            print(f"{new_name}: already exists!")
    else:
        print(f"{old_name}: not found!")

def search(name):
    if name in product_names:
        index = product_names.index(name)
        bought = product_is_bought[index]
        price = product_prices[index]
        print(f"{name} ==> bought: {bought},price: {price}") 
    else:
        print(f"{name}: not found!")

def details():
    total = len(product_names)
    not_purchased = product_is_bought.count(False)
    purchased = product_is_bought.count(True)
    print(f"Total products: {total}")
    print(f"Purchased: {purchased}")
    print(f"Not purchased: {not_purchased}")
    prices = []
    for i in product_prices:
        if i:
            prices.append(i)
    print(f"Sum: {sum(prices)}")

def buy(name):
    if name in product_names:
        price = int(input(f"price of {name}: "))
        # edit
        ind = product_names.index(name)
        product_prices[ind] = price
        product_is_bought[ind] = True
        print("bought!") 
    else:
        print(f"{name}: not found!")
#------------------------Main----------------------------

product_names = []
product_is_bought = []
product_prices = []
for i in range(100):
    answer = input("help, add, display, edit, remove, search, buy, details, exit : ")
    if answer == "help":
        help()

    elif answer == "add":
        name = input("Product name: ")
        add(name)

    elif answer == "display":
        display()

    elif answer == "edit":
        old_name = input("Product name: ")
        edit(old_name)

    elif answer == "remove":
        name = input("Product name: ")
        remove(name)

    elif answer == "search":
        name = input("Product name: ")
        search(name)

    elif answer == "buy":
        name = input("Product name: ")
        buy(name)

    elif answer == "details":
        details()

    elif answer == "exit":
        break
    elif answer =="":
        continue
    else:
        print(f"{answer} Command not found!")