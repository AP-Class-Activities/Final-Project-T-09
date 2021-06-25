'''

Usage:
   1) Create a new customer:
        t= Customer(ID, name, family , address, phone, sex)

   2) Print the teacher information:    
        print(t)

    
'''
#add year of birth

class Customer: 
    def __init__(self, ID, name, family, address, phone, sex):
        self.__id = ID
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone

        if sex not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = sex

    
    #setters and getters
    @property
    def ID(self): 
        return self.__id
    
    @ID.setter
    def ID(self,value): 
        self.__id = value

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def family(self): 
        return self.__family

    @family.setter
    def family(self,value): 
        self.__family = value

    @property
    def address(self): 
        return self.__address
    
    @address.setter
    def address(self,value): 
        self.__address = value

    @property
    def phone(self): 
        return self.__phone

    @phone.setter
    def phone(self,value): 
        self.__phone = value

    @property
    def sex(self): 
        return self.__sex

    @sex.setter
    def sex(self,value): 
        if value not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = value




    def __str__(self): 
        return 'ID: {}   name: {} {}    address: {}   phone: {}     sex: {}   '  .format(self.ID,self.name, self.family, self.address, self.phone, self.sex)




#client code:
c = Customer('testID', 'TestName', 'TestFamily', 'TestAddress', '09122222222', 'male' )
print(c)










'''
Usage:
   1) Create a new product:
        p= Product(code, name, seller, stock, price)

   2) Print the course information:    
        print(c)

    
'''

class Product: 
    def __init__(self,code , name , seller , stock , price):
        self.__code = code
        self.__name = name
        self.__seller = seller
        
        if stock not in range (0, 1000000000):
            raise ValueError('the stock not valid. ')
        
        if price not in range (0, 1000000000): 
            raise ValueError('the price should be in range 0 to 1000000000. ')
        self.__price = price


    ##setters and getters
    @property
    def code(self): 
        return self.__code
    
    @code.setter
    def code(self,value): 
        self.__id = code

    @property
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self,value): 
        self.__id = name

    @property
    def seller(self): 
        return self.__seller

    @seller.setter
    def seller(self,value): 
        self.__name = seller

    @property
    def stock(self): 
        return self.__stock

    @stock.setter
    def stock(self,value): 
        if credits not in range (0, 1000000000): 
            raise ValueError('the stock not valid. ')
        self.__stock = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if price not in range (0, 1000000000):
            raise ValueError('the price should be in range 0 to 1000000000.')
        self.__price = value

        
    def __str__(self): 
        return 'code: {}   name: {}   seller: {}   stock: {}   price:{}'.format(self.code, self.name, self.seller, self.stock, self.price)
    
p = Product('110', 'tv', 'apple', '1000', '20000000')
print(p)