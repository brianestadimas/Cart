class Cart():
    #Declaring class with product as dictionary, constructor
    def __init__(self):
        self.product = {}
        
    #Adding productCode as key and quantity as value, void
    def addProduct(self, productCode, quantity):
        #Check if quantity integer and more than 
        if (type(quantity)!=int) or (quantity<=0):
            print ("Quantity Product Salah")
            return
        
        #check if the key exist
        if productCode in self.product:
            self.product[productCode] += quantity
        else :
             self.product[productCode] = quantity
        
    def removeProduct(self, productCode):
        #Check if key exist in dictionary, for this cascading case
        #use try-except
        try :
            del self.product[productCode]
        except KeyError :
            print ("Product tidak ditemukan")

    #Printing dictionary with loop, void
    def showCart(self):
        for key in self.product:
            print(key + "(" + str(self.product[key]) + ")")
