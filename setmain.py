'''
Created on 03-Jun-2020

@author: USER
'''
from usingset.productdetails import Product,Shop
product_object1=Product(1,"AC",30000.0,9)
product_object2=Product(2,"Refrigirator",15000.0,19)
set={product_object1,product_object2}
shop_object=Shop(set,9,"abcde","fghij")
print("Retrieve")
shop_object.get_product_based_on_productid(1)
print("Updating")
shop_object.update_productquantity(2, 9)
print("Deleting")
shop_object.sell_product(2, 9)