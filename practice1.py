# users = [
#         {'username' : 'ram', 'password' : 'ram002'},
#         {'username' : 'sita', 'password' : 'sita002'},
#         {'username' : 'laxmi', 'password' : 'laxmi002'}
#         ]




# input_username = input("Enter your username: ").lower()
# input_password = input("Enter your password: ")
# for data in users:
#     if input_username == data['username']:
#         input_password = input("Enter your password: ").lower()
#         if input_password == data['password']:
#             print("You are logged in")
#             break
#         else:
#             print("Incorrect Password")
#             break

# else:
#     print("Username is incorrect")







# username = input("Enter username")
# password = input("Enter password")

# is_login = False

# for user in users:
#     if username == user['username'] and password == user['password']:
#         is_login = True


# if is_login:
#     print(f"Welcome{username}")
# else:
#     print("Invalid username or password")





# Duplicate Number


# numbers = [10,11,10,30,30,90,80]

# new_number =[]

# for i in numbers:
#     if i not in new_number:
#         new_number.append(i)



# print(new_number)



# category=[
#     {'cid':1,'name':'Electronics'},
#     {'cid':2,'name':'Fashion'},
#     {'cid':3,'name':'Home'}
# ]

# products=[
#     {'pid':1,'name':'Mobile','price':10000,'quantity':5,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':6,'cid':1},
#     {'pid':3,'name':'Shirt','price':1000,'quantity':7,'cid':2},
#     {'pid':4,'name':'T-shirt','price':500,'quantity':9,'cid':2},
#     {'pid':5,'name':'Bed','price':10000,'quantity':6,'cid':3},
#     {'pid':6,'name':'Sofa','price':20000,'quantity':2,'cid':3}
# ]




# for x in category:

#     print(f"\n----------{x['name']}----------\n")
    
    

# for cat in category:
#     cat_id = cat['cid']
#     cat_name = cat['name']

#     print(f"\n---------------{cat_name}---------------")

#     total = 0

#     for prod in products:
#         if prod['cid'] == cat_id:
#             name = prod['name']
#             price = prod['price']
#             quantity = prod['quantity']
#             total_price = price * quantity
#             total+=total_price

#             print(f"\nName : {name}\nPrice : Rs.{price}\nQuantity : {quantity}\nTotal price of {name} is Rs.{total_price}")
        
    
#     print("\n-------------------------------------\n")
#     print(f"Total price of Electronics Rs.{total}")     
    


# 1. Write a Python function to find the maximum of three numbers.


# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20



# def mul(numbers):


#     total=1
#     for i in numbers:
#         total *= i
#     return total




# print(f"The product is {mul([1,2,5,2,2])}")



# def products():
#     data=[
#         {'id':1,'name':'laptop','price':50000,'qty':10},
#         {'id':2,'name':'mobile','price':15000,'qty':20},
#         {'id':3,'name':'tv','price':25000,'qty':15},
#         {'id':4,'name':'watch','price':5000,'qty':50},
#         {'id':5,'name':'shoe','price':500,'qty':100},
#     ]
#     return data





data=[
        {'id':1,'name':'laptop','price':50000,'qty':10},
        {'id':2,'name':'mobile','price':15000,'qty':20},
        {'id':3,'name':'tv','price':25000,'qty':15},
        {'id':4,'name':'watch','price':5000,'qty':50},
        {'id':5,'name':'shoe','price':500,'qty':100},
    ]

ok = int(input("Enter id: "))
for i in range(len(data)-1):
    if data[i]['id'] == 1:
        data.pop(ok-1)
    
print(data)
