# print("======COmputer Bazar =========")
#print("1,Dell(Rs:20000)" 2.Toshiba(Rs.30000) 3.MAC(Rs:50000))
# Enter qunatity
# Deliver  : Home(Rs.1000) 2.Pickup (Free)
#Packing 
#1. plastic bag (rs:1000) 2.bag (Rs.2000) 3.Gift box (Rs.5000)
#location : ktm(Rs13%) 2.ltp(free) 3.bkt(0%)


productList = {'dell': 20000, 'toshiba' : 30000, 'mac' : 50000 }
deliveryList = {'home':1000, 'pickup' : 0}
packagingList = {'plasticbag' : 1000, 'bag' : 2000, 'giftbox' : 5000}
locationTax = {'ktm' : 13/100*1000, 'ltp' : 0, 'bkt' : 0}


print("\nList of available products \n 1. Dell Rs. 20000 \n 2. Toshiba Rs.30000 \n 3. Mac Rs. 50000")
productName1 = input("Enter the product you want to buy").lower()
productName = productName1.replace(" ", "") 


quantity = int(input("Enter the quantity you want to buy"))


print("Delivery options \n 1. Home Rs.1000 \n 2. Pickup (Free)")
delivery1 = input("Choose a delivery option").lower()
delivery = delivery1.replace(" ", "")



print("Packaging options \n 1. Plastic bag Rs.1000 \n 2. Bag Rs. 2000 \n 3. Gift box Rs 5000")
packaging1  = input("Choose a packaging option").lower()
packaging = packaging1.replace(" ", "")

print("Available delivery locations \n 1. KTM \n 2. LTP \n 3. BKT")
location1 = input("Enter your delivery location").lower()
location = location1.replace(" ", "")



print("\n========================= Computer Bazar =========================\n")
print("\t\t\t\t\t\tAmount")
print(f"Name of the product: {productName.capitalize()}")
print(f"Quantity : {quantity} \t\t\t\t\t{productList[productName] * quantity}")
print(f"Delivery type : {delivery.capitalize()} \t\t\t\t{deliveryList[delivery.lower()]}")
print(f"Packaging type : {packaging.capitalize()}\t\t\t\t{packagingList[packaging]}")
print(f"Delivery location : {location.upper()}")
print(f"Delivery Charge: \t\t\t\t{locationTax[location.lower()]}")

 


total = productList[productName] * quantity + deliveryList[delivery] + packagingList[packaging] + locationTax[location]

print("---------------------------------------------------------")
print(f"Your total is \t\t\t\t\tRs.{total}")






