category=[
    {'cid':1,'name':'Electronics'},
    {'cid':2,'name':'Fashion'},
    {'cid':3,'name':'Home'}
]

products=[
    {'pid':1,'name':'Mobile','price':10000,'quantity':5,'cid':1},
    {'pid':2,'name':'Laptop','price':50000,'quantity':6,'cid':1},
    {'pid':3,'name':'Shirt','price':1000,'quantity':7,'cid':2},
    {'pid':4,'name':'Tshirt','price':500,'quantity':9,'cid':2},
    {'pid':5,'name':'Bed','price':10000,'quantity':6,'cid':3},
    {'pid':6,'name':'Sofa','price':20000,'quantity':2,'cid':3}
]



for x in category:

    print(f"\n\n----------{x['name']}----------")
    total = 0
    

    for y in products:
        
        if x['cid'] == y['cid']:
            print(f"\nName : {y['name']}\nPrice: {y['price']}\nQuantity : {y['quantity']}")
            total_price = y['quantity'] * y['price']
            print(f"Total Price: Rs.{total_price}")
            total += total_price
        

    print("-------------------------")
    print(f"Total is {total}")

    

            




