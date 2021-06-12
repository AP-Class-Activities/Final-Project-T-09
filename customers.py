'''

Usage:
   1) Create a new customer:
        t= Customer(ID, name, family , address, phone, degree)

   2) Print the teacher information:    
        print(t)

    
'''
#add year of birth

class Customer: 
    def __init__(self, id, name, family, address, phone, sex):
        self.__id = id
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
c = Customer(123, 'ali', 'alipour', 'Guilan, Rasht', '09112383822', 'male' )
print(c)






class productsList:
    def __init__(self, roduct = " ", storage = 0, price = 0.0):
        self.product = product
        self.__storage = storage
        self.__price = price
    def getStorage (self):
        return self.__storage 
    def getPrice (self):
        return self.__price
    def display (self):
        print("{0:10s} {1:4d} {2:8.2f}".format(self.product, self.__storage, self.__price))
 from productsListModule import productsList:   
def menu():
        print()
        print("1. Enter a product ")
        print("2. Find the best price ")
        print("3. Delete a product ")
        print("4. Search a product ")
        print("5. Exit ")
        choice = int(input("\n Enter your select (1 - 6)"))
        return choice
      end of menu function
def addtoList(productsList):
    product, storage, price = input("Enter product name, storage, price").split()
    pro = productsList(product, int(storage), float(price))
    prolist.append(pro)
def findMaxprice(prolist):
    mPrice = prolist[0].getPrice()                  #mPrice = first price
    p = 0     #p is the position of the minimum element
    for i in range (1, len(prolist)):
        if prolist[i].getPrice() < mPrice:
            mPrice = prolist[i].getPrice()
            p = i
    print("Product with Minimum price: ")
    print("{0:10s} {1:10s} {2:10s}".format("Product name", "storage", "price"))
    prolist[p].display()
def searchProduct(prolist):
    product = input("Enter the product name to search: ")
    found = False #product not found
    i = 0 #index of list
    while i < len(prolist) and not found :
        if prolist[i].getStorage() == storage:
            found = True
        else: 
            i = i + 1
    if not found:
        print("product with", product, "not found. ")
    else:
        print ("product with " product, "found. ")
        print("{0:10s} {1:10s} {2:10s}".format("Name", "storage", "price"))
        prolist[i].display()
def deleteProduct(prolist):
    storage = input("Enter a product to delete: ")
    found False #product not found
    i = 1 #index of list
    while i < len(prolist) and not found:
        if prolist[i].getStorage() == storage:
            found = True
        else:
            i = i + 1
    if not found:
        print ("Product ", product, "not exist. ")
    else:
        prolist.pop(i) #delete product
        print ("product ", product, "deleted. ")






class basket(object):
    def __init__(self, request):
        #initalize the basket
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            #save an empty basket in the session
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket
    def add(self, product, quantity=1, update_quantity=False):
        #add a product to the basket or update its quantity.
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {"quantity":0, "price":str(product.price)}
        if update_quantity:
            self.basket[product_id]["quantity"] = quantity
        else:
            self.basket[product_id]["quantity"] += quantity
        self.save()
    def save(self):
        #update the session basket
        self.session[settings.BASKET_SESSION_ID] = self.basket
        #mark the session as "modified" to make sure it is saved
        self.session.modified = True
        
        def remove(self, product):
            #remove a product from basket 
            product_id = str(product.id)
            if product_id in self.basket:
                del self.basket[product_id]
                self.save()
        def __iter__(self):
            #iterate over the items in the basket and get the products from the database.
            product_ids = self.basket.keys()
            #get the product objects and add them to the basket
            products = product.objects.filter(id__in=product_ids)
            for product in products:
                self.basket[str(product.id)]["product"] = product
            
            for item in self.basket.values():
                item['price'] = Decimal(item["price"])
                item['total_price'] = item['price']*item['quantity']
                yield item
        def __len__(self):
            #count all itens in the basket
            return sum(item['quantity'] for item in self.basket.values())
        def get_total_price(self):
            return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())
        def clear(self):
            #empty basket
            self.session[settings.BASKET_SESSION_ID] = {}
            self.session.modified = True



    def basket_add(request, product_id):
        basket = basket(request)
        product = get_object_or_404(product, id=product_id)
        form = BasketAddProductForm(request.POST)
        if forn.is_valid():
            cd = form.cleaned_data
            basket.add(product = product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('basket:basket_detail')
    def basket_remove(request, product_id):
        basket = Basket(request)
        product = get_object_or_404(Product, id=product_id)
        basket.remove(product)
        return redirect('basket:basket_detail')

    def basket_detail(request):
        basket = Basket(request)
        for item in basket:
            item['update_quantity_form'] = BasketAddProductForm(initial={'quantity':item['quantity'], 'update':True})
        




    def order_create(request):
        basket = Basket(request)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in basket:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                basket.clear()
                #reset basket
                order_created.delay(order.id)
                
            else:
                form = OrderCreateForm()






class walletManagement:
    def walletlist():
        print()
        print("1. Increase credit ")
        print("2. amount of credit ")
        print("5. Exit ")
        choicee = int(input("\n Enter your select (1 - 3)"))
        return choicee
      end of walletlist function
    def addtoWallet(amountOfCredit):
        IncreasingAmount = input("Enter the amount you want to add to your wallet. ")
        wallet = amountOfCredit(int(IncreasingAmount))
        walletlist.append(wallet)


