'''
Created on 03-Jun-2020

@author: USER
'''
from usinglist.productdetails import Product, Shop
product_object1=Product(1,"AC",30000.0,9)
product_object2=Product(2,"Refrigirator",15000.0,19)
list=[product_object1,product_object2]
shop_object=Shop(list, 9, "abcde", "fghij")
print("Retrieving")
shop_object.get_product_based_on_productid(2)
print("Updating")
shop_object.update_productquantity(1, 9)
print("Deleting")
shop_object.sell_product(2, 5)