'''
Created on 03-Jun-2020

@author: USER
'''
from builtins import list

class Product(object):
    '''
    classdocs
    '''
    __productid=None
    __productname=None
    __productprice=None
    __productquantity=None
    
    def __init__(self, productid, productname, productprice, productquantity):
        self.__productid = productid
        self.__productname = productname
        self.__productprice = productprice
        self.__productquantity = productquantity

    def get_productid(self):
        return self.__productid


    def get_productname(self):
        return self.__productname


    def get_productprice(self):
        return self.__productprice


    def get_productquantity(self):
        return self.__productquantity


    def set_productid(self, value):
        self.__productid = value


    def set_productname(self, value):
        self.__productname = value


    def set_productprice(self, value):
        self.__productprice = value


    def set_productquantity(self, value):
        self.__productquantity = value


    def del_productid(self):
        del self.__productid


    def del_productname(self):
        del self.__productname


    def del_productprice(self):
        del self.__productprice


    def del_productquantity(self):
        del self.__productquantity
        
    def __str__(self):
        return str(self.__productid)+" "+self.__productname+" "+str(self.__productprice)+" "+str(self.__productquantity)
    
    
class Shop:
    
    __productsinshop=()
    __shopid=None
    __shopname=None
    __shoplocation=None
    
    def __init__(self, productsinshop=(), shopid=0, shopname="", shoplocation=""):
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
    
    
    def get_products_based_on_productid(self,productid):
        for index in self.__productsinshop:
            if index.get_productid()==productid:
                print(index)
                break
            
    def update_products(self,productid,productquantity):
        mylist=list(self.__productsinshop)
        for index in mylist:
            if index.get_productid()==productid:
                totalquantity=index.get_productquantity()+productquantity
                index.set_productquantity(totalquantity)
                print(index)
                break
        tuple=tuple(mylist)
        print(tuple)
    
    def sell_products(self,productid,productquantity):
        list=list(self.__productsinshop)
        for index in list:
            if index.get_productid()==productid:
                available_quantity=index.get_productquantity()
                if available_quantity>productquantity:
                    totalbill=index.get_productprice()*productquantity
                    billformat="productid is {} and productquantity is {} and productprice per each product is {} and totalbill is {}"
                    print(billformat.format(productid,productquantity,index.get_productprice(),totalbill))
                    remaining_quantity=available_quantity-productquantity
                    index.set_productquantity(remaining_quantity)
                    print(index)
                    break
        tuple=tuple(list)                          