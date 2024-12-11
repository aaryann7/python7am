# def message():
#     print("Hello, World")

# message()

# def add(x,y):
#     print(x+y)

# add(10,20)


# def rep(data, time):
#     for i in range(time):
#         print(data)

# rep('ram',10)

# def mul(*numbers):
#     total = 0
#     x = 0
#     # for i in numbers:
#     #     total+=i
#     # print(total)

#     while x<len(numbers):
#         total += numbers[x]
#         x = x + 1
#     print(total)


# mul(1,2,3,4,5,6,7,8,9,10)





# def triangle(x):
#     for i in range(1,x):
#         print("*"*i)


# triangle(5)




# def x (data):
#     y = []
#     z =[]
#     for i in data:
#         if i not in y:
#             y.append(i)
#         else:
#             z.append(i)
        
#     print(z)

# x([1,2,3,1,3,4,5,6,6,5])




# def take_value():
#     p = int(input("Enter principal: "))
#     t = int(input("Enter time: "))
#     r = int(input("Enter rate: "))
#     return p,t,r

# def calculator():
#     p,t,r = take_value()
#     return (p*t*r)/100

# def display():
#     print(f"Simple interest is {calculator()}")


# display()

    

# def products():
#     data=[
#         {'id':1,'name':'laptop','price':50000,'qty':10},
#         {'id':2,'name':'mobile','price':15000,'qty':20},
#         {'id':3,'name':'tv','price':25000,'qty':15},
#         {'id':4,'name':'watch','price':5000,'qty':50},
#         {'id':5,'name':'shoe','price':500,'qty':100},
#     ]
#     return data


# def add_product(id,name,price,qty): 
#     data = products() 
#     add_item = dict(id = id , name = name, price = price  , qty =  qty )
#     data.append(add_item)
#     return data


# def update_product():

#     take_id= int(input("Enter the id of the product you want to update: "))
#     data = products()
#     for i in data:
#         if i['id'] == take_id:
#             change_item = int(input("1.Name \n2.Price \n3.Quantity\n"))
#             if change_item == 1:
#                 update_item = input("Enter the name: ")
#                 i['name'] = update_item
#             if change_item == 2:
#                 update_item = input("Enter the price: ")
#                 i['price'] = int(update_item)
#             if change_item == 3:
#                 update_item = input("Enter the quantity: ")
#                 i['qty'] = int(update_item)
#         else:
#             print("Enter a valid id")
#             break
        
#     return data     

   

            
    
# def get_by_id(id):
#     data = products()
#     for i in data:
#         if id == i['id']:
#             return i
        


# def delete_product(id):
#     data  = products()
#     for i in range(len(data)-1):
#         if id == data[i]['id']:
#             data.pop(id-1)
                    

#     return data


# def get_all(data):
#     print("id\tname\tprice\tqty")
#     for product in data:
#         print(f"{product['id']}\t{product['name']}\t{product['price']}\t{product['qty']}")



# new_product = products()
# print(add_product(10,'jacket',100,3))
# get_all(new_product)
# print(update_product())
# print(get_by_id(3))
# print(delete_product(1))
# get_all(new_product)





    




# def products():
#     data=[
#         {'id':1,'name':'laptop','price':50000,'qty':10},
#         {'id':2,'name':'mobile','price':15000,'qty':20},
#         {'id':3,'name':'tv','price':25000,'qty':15},
#         {'id':4,'name':'watch','price':5000,'qty':50},
#         {'id':5,'name':'shoe','price':500,'qty':100},
#     ]
#     return data




# def display_info(data):
#     print("id\tname\tprice\tqty")
#     for product in data:
#         print(f"{product['id']}\t{product['name']}\t{product['price']}\t{product['qty']}")


# def add_item(data,new_item):
#     data.append(new_item)
#     print(f"{new_item['name']} added.")

# def delete_item(data,id):
#     for product in data:
#         if product['id'] == id:
#             data.remove(product)
#             print(f"{product['name']} removed.")
#             return
#     print(f"Product with ID {id} not found ")

# def update_items(data,id,updated_items):
#     for product in data:
#         if product['id'] == id:
#             product.update(updated_items)
#             print(f"Product ID {product['id']} updated.")
#             return
#         print(f"Product ID {product['id']} not found.")




# product_list = products()
# display_info(product_list)

# new_item = {'id': 6, 'name': 'tablet', 'price': 20000, 'qty': 30}
# add_item(product_list, new_item)
# display_info(product_list)

# delete_item(product_list,3)
# display_info(product_list)

# updated_items = {'price': 60000, 'qty': 8}
# update_items(product_list,1,updated_items)
# display_info(product_list)


# def message():
#     yield "Hello"
#     yield "World"
#     yield "Python"



# def student():
#     def info(name):
#         return f"I am {name}"
#     return info


# obj = student()
# print(obj('name'))


# decorater

def y_zero_check(anyfunction):
    def inner(x,y):
        if y == 0:
            return "y is zero"
        else:
            return anyfunction(x,y)
    return inner

def x_zero_check(anyfunction):
    def inner(x,y):
        if x == 0:
            return "x is zero"
        else:
            return anyfunction(x,y)
    return inner



@y_zero_check
@x_zero_check
def div(x,y):
    return x/y

print(div(5,0))



# import math
# import datetime
# import os
# import sys
# exception handling


