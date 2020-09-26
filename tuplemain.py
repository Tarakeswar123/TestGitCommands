'''
Created on 03-Jun-2020

@author: USER
'''
from usingtuple.productdetails import Product,Shop
product_object1=Product(1,"Ac",30000.0,9)
product_object2=Product(2,"Refrigirator",15000.0,19)
tuple=(product_object1,product_object2)
shop_object=Shop(tuple,9,"abcde","fghij")
print("Retrieve")
shop_object.get_products_based_on_productid(2)
print("Updating")
shop_object.update_products(2, 9)
print("Deleting")
shop_object.sell_products(2, 5)