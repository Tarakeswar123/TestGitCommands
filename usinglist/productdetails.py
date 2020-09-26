'''
Created on 03-Jun-2020

@author: USER
'''

class Product(object):
    '''
    classdocs
    '''
    __productid=None
    __productname=None
    __productprice=None
    __productqunatity=None
    
    def __init__(self, productid, productname, productprice, productqunatity):
        self.__productid = productid
        self.__productname = productname
        self.__productprice = productprice
        self.__productqunatity = productqunatity


    def get_productid(self):
        return self.__productid


    def get_productname(self):
        return self.__productname


    def get_productprice(self):
        return self.__productprice


    def get_productqunatity(self):
        return self.__productqunatity


    def set_productid(self, value):
        self.__productid = value


    def set_productname(self, value):
        self.__productname = value


    def set_productprice(self, value):
        self.__productprice = value


    def set_productqunatity(self, value):
        self.__productqunatity = value


    def del_productid(self):
        del self.__productid


    def del_productname(self):
        del self.__productname


    def del_productprice(self):
        del self.__productprice


    def del_productqunatity(self):
        del self.__productqunatity

    def __str__(self):
        return str(self.__productid)+" "+self.__productname+" "+str(self.__productprice)+" "+str(self.__productqunatity)
    
    
class Shop:
    
    __products_in_shop=[]
    __shopid=None
    __shopname=None
    __shoploction=None

    def __init__(self, products_in_shop=[], shopid=0, shopname="", shoploction=""):
        self.__products_in_shop = products_in_shop
        self.__shopid = shopid
        self.__shopname = shopname
        self.__shoploction = shoploction

    def get_products_in_shop(self):
        return self.__products_in_shop


    def get_shopid(self):
        return self.__shopid


    def get_shopname(self):
        return self.__shopname


    def get_shoploction(self):
        return self.__shoploction


    def set_products_in_shop(self, value):
        self.__products_in_shop = value


    def set_shopid(self, value):
        self.__shopid = value


    def set_shopname(self, value):
        self.__shopname = value


    def set_shoploction(self, value):
        self.__shoploction = value


    def del_products_in_shop(self):
        del self.__products_in_shop


    def del_shopid(self):
        del self.__shopid


    def del_shopname(self):
        del self.__shopname


    def del_shoploction(self):
        del self.__shoploction
        
    def __str__(self):
        return str(self.__products_in_shop)+" "+str(self.__shopid)+" "+self.__shopname+" "+self.__shoploction    
        
    def get_product_based_on_productid(self,productid):
        for index in self.__products_in_shop:
            if index.get_productid()==productid:
                print(index)
                break
            
    def update_productquantity(self,productid,productquantity):
        for index in self.__products_in_shop:
            if index.get_productid()==productid:
                totalquantity=index.get_productqunatity()+productquantity
                index.set_productqunatity(totalquantity)
                print(index)
                break          
    
    def sell_product(self,productid,productquantity):
        for index in self.__products_in_shop:
            if index.get_productid()==productid:
                available_quantity=index.get_productqunatity()
                if available_quantity>productquantity:
                    totalbill=index.get_productprice()*productquantity
                    billformat="productid is {} and productprice per each product is {} and productquantity is {} and totalbill is {}"
                    print(billformat.format(productid,index.get_productprice(),productquantity,totalbill))
                    remainingquantity=available_quantity-productquantity
                    index.set_productqunatity(remainingquantity)
                    break           
            
        