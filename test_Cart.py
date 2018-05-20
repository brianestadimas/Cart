import unittest
import io
import sys
from Cart import *                                          #Cart.py should be in same directory

class CartUnitTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()                                  #Calling constructor as variable             
        self.capturedOutput = io.StringIO()                 #Set up captured print output
        sys.stdout = self.capturedOutput                    #from method
    
    def test_addCorrectProductTest(self):
        self.cart.addProduct("Makanan",5)                   #add and show product
        self.cart.showCart()
        self.assertEqual(self.capturedOutput.getvalue(),    #get captured output and compare
                         "Makanan(5)\n")

    def test_addIncorrectProductTest(self):
        self.cart.addProduct("Makanan","a")                 #wrong method(string,int)
        self.assertEqual(self.capturedOutput.getvalue(),    #captured output and compare 
                         "Quantity Product Salah\n")

    def test_addMoreProduct(self):
        self.cart.addProduct("Makanan",5)
        self.cart.addProduct("Makanan",10)                  #add multiple products
        self.cart.showCart()                                #print output captured
        self.assertEqual(self.capturedOutput.getvalue(),    #compare with captured output
                         "Makanan(15)\n")

    def test_removeProduct(self):                               #remove product from list
        self.assertIsNone(self.cart.removeProduct("Makanan"))   #show null, when correct

    def test_removeProductIncorrect(self):
        self.cart.removeProduct("Minuman")                  #product not found in list
        self.assertEqual(self.capturedOutput.getvalue(),    #compare output
                         "Product tidak ditemukan\n")

    def test_showCart(self):
        self.cart.addProduct("Makanan",5)                   #add multiple product and test
        self.cart.addProduct("Minuman",2)
        self.cart.showCart()
        self.assertEqual(self.capturedOutput.getvalue(),"Makanan(5)\nMinuman(2)\n")


if __name__ == '__main__':
    unittest.main()
