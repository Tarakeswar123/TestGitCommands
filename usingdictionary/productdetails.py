'''
Created on 03-Jun-2020

@author: USER
'''

class Product(object):
    '''
    classdocs
    '''
    __productname=None
    __productprice=None
    __productquantity=None
    
    def __init__(self, productname, productprice, productquantity):
        self.__productname = productname
        self.__productprice = productprice
        self.__productquantity = productquantity


    def get_productname(self):
        return self.__productname


    def get_productprice(self):
        return self.__productprice


    def get_productquantity(self):
        return self.__productquantity

    def set_productname(self, value):
        self.__productname = value


    def set_productprice(self, value):
        self.__productprice = value


    def set_productquantity(self, value):
        self.__productquantity = value


    def del_productname(self):
        del self.__productname


    def del_productprice(self):
        del self.__productprice


    def del_productquantity(self):
        del self.__productquantity
        
    def __str__(self):
        return self.__productname+" "+str(self.__productprice)+" "+str(self.__productquantity)    
        
    
class Shop:
    
    __productsinshop={}
    __shopid=None
    __shopname=None
    __shoplocation=None

    def __init__(self, productsinshop={}, shopid=0, shopname="", shoplocation=""):
        self.__productsinshop = productsinshop
        self.__shopid = shopid
        self.__shopname = shopname
        self.__shoplocation = shoplocation

    def get_productsinshop(self):
        return self.__productsinshop


    def get_shopid(self):
        return self.__shopid


    def get_shopname(self):
        return self.__shopname


    def get_shoplocation(self):
        return self.__shoplocation


    def set_productsinshop(self, value):
        self.__productsinshop = value


    def set_shopid(self, value):
        self.__shopid = value


    def set_shopname(self, value):
        self.__shopname = value


    def set_shoplocation(self, value):
        self.__shoplocation = value


    def del_productsinshop(self):
        del self.__productsinshop


    def del_shopid(self):
        del self.__shopid


    def del_shopname(self):
        del self.__shopname


    def del_shoplocation(self):
        del self.__shoplocation
        
    def __str__(self):
        return str(self.__productsinshop)+" "+str(self.__shopid)+" "+self.__shopname+" "+self.__shoplocation
    
    
    def get_product_based_on_productid(self,productid):
        for key,value in self.__productsinshop.items():
            if key==productid:
                print(value)
                break
            
    def update_product(self,productid,productquantity):
        for key,value in self.__productsinshop.items():
            if key==productid:
                totalquantity=value.get_productquantity()+productquantity
                value.set_productquantity(totalquantity)
                print(value)
                break
            
    def sell_products(self,productid,productquantity):
        for key, value in self.__productsinshop.items():
            if key==productid:
                available_quantity=value.get_productquantity()
                if available_quantity>productquantity:
                    totalbill=value.get_productprice()*productquantity
                    billformat="productid is {} and productquantity is {} and productprice per each product is {} and totalbill is {}"
                    print(billformat.format(productid,productquantity,value.get_productprice(),totalbill))
                    remaining_quantity=available_quantity-productquantity
                    value.set_productquantity(remaining_quantity)
                    print(value)
                    break        
                        
    