'''
Created on 03-Jun-2020

@author: USER
'''
from usingdictionary.productdetails import Product,Shop
product_object1=Product("Ac",30000.0,9)
product_object2=Product("Refrigirator",15000.0,19)
dict={1:product_object1,2:product_object2}
shop_object=Shop(dict,9,"abcde","fghij")
print("Retrieve")
shop_object.get_product_based_on_productid(1)
print("Updating")
shop_object.update_product(2, 9)
print("Deleting")
shop_object.sell_products(2, 9)