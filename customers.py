'''

Usage:
   1) Create a new customer:
        t= Customer(ID, name, family , address, phone, sex)

   2) Print the teacher information:    
        print(t)

    
'''

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
#c = Customer('testID', 'TestName', 'TestFamily', 'TestAddress', '09122222222', 'male' )
#print(c)











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
    
#p = Product('110', 'tv', 'apple', '1000', '20000000')
#print(p)




"""
class productsList:
   def __init__(self, product = " ", storage = 0, price = 0.0):
       self.product = product
        self.__storage = storage
        self.__price = price
    def getStorage (self):
        return self.__storage 
    def getPrice (self):
        return self.__price
    def display (self):
        print("{0:10s} {1:4d} {2:8.2f}".format(self.product, self.__storage, self.__price))
        """
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











#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, window):
        window.setObjectName("Form")
        window.resize(466, 347)
        Form = QWidgets.QWidget(window)
        Form.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 371, 31))
        self.label.setObjectName("label")
        self.userlabel = QtWidgets.QLabel(Form)
        self.userlabel.setGeometry(QtCore.QRect(394, 90, 41, 20))
        self.userlabel.setObjectName("userlabel")
        self.passlabel = QtWidgets.QLabel(Form)
        self.passlabel.setGeometry(QtCore.QRect(394, 140, 41, 20))
        self.passlabel.setObjectName("passlabel")
        self.userline = QtWidgets.QLineEdit(Form)
        self.userline.setGeometry(QtCore.QRect(70, 90, 301, 20))
        self.userline.setObjectName("userline")
        self.passline = QtWidgets.QLineEdit(Form)
        self.passline.setGeometry(QtCore.QRect(70, 140, 301, 20))
        self.passline.setObjectName("passline")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(130, 186, 181, 31))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.signinaccount)
        window.setCentralWidget(Form)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def signinaccount(self):
        username = self.userline.text()
        password = self.passline.text()
        users = open('database.txt','a')
        users.write("\n"+username+password)
        users.close()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "درگاه ثبت نام مشتریان"))
        self.userlabel.setText(_translate("Form", "نام کاربری"))
        self.passlabel.setText(_translate("Form", "رمز عبور"))
        self.save.setText(_translate("Form", "ثبت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


# In[ ]:




# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpyy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from front import 3.menu
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, window):
        window.setObjectName("Form")
        window.resize(447, 373)
        Form = QtWidgets.QWidget(window)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 39, 391, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 2, 1, 1)
        self.username = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 2, 1, 1)
        self.UserLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UserLine.setObjectName("UserLine")
        self.gridLayout.addWidget(self.UserLine, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.Login = QtWidgets.QPushButton(Form)
        self.Login.setGeometry(QtCore.QRect(20, 269, 361, 21))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        self.Login.clicked.conecct(self.loginaccount)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 31))
        self.label.setMaximumSize(QtCore.QSize(381, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 310, 371, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        window.setCentralWidget(window)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def gotologin(self):
        self.loginpage = QtWidgets.QMainWindow()
        self.ui = loginpyy.Ui_Form()
        self.ui.setupUi(self.loginpage)
        self.loginpage.show()
        Form.close()
    def gotomenu(self):
        self.menupage = QtWidgets.QMainWindow()
        self.ui = menu.Ui_MainWindow()
        self.menupage.show()
        Form.close()
    def loginaccount(self):
        username = self.UserLine.text()
        password = self.PassLine.text()
        users = open("database.txt", "r")
        users.write("\n"+username+" "+password)
        users.close()
        self.gotologin()
        users=[u.replace('\n','').split() for u in users]
        flag = False
        for i in range(len(users)):
            if username==users[i][0] and [i][1]:
                flag = True
                self.gotomenu()
        if flag==False:
                self.LogLabel.setStyleSheet('color:red;')
                self.LogLabel.setText('ورود ناموفق')    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.password.setText(_translate("Form", "رمز عبور"))
        self.username.setText(_translate("Form", "نام کاربری"))
        self.Login.setText(_translate("Form", "ورود"))
        self.label.setText(_translate("Form", "درگاه ورود مشتریان"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())







# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wishlist = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(10)
        self.wishlist.setFont(font)
        self.wishlist.setObjectName("wishlist")
        self.horizontalLayout.addWidget(self.wishlist)
        self.cart = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(10)
        self.cart.setFont(font)
        self.cart.setObjectName("cart")
        self.horizontalLayout.addWidget(self.cart)
        self.products = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(10)
        self.products.setFont(font)
        self.products.setObjectName("products")
        self.horizontalLayout.addWidget(self.products)
        self.wallet = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(10)
        self.wallet.setFont(font)
        self.wallet.setObjectName("wallet")
        self.horizontalLayout.addWidget(self.wallet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.wishlist.clicked.connect(self.gotowishlist)
        self.cart.clicked.connect(self.gotocart)
        self.products.clicked.connect(self.gotoproducts)
        self.wallet.clicked.connect(self.gotowallet)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.increaseamount.clicked.connect(self.gotowalletincrease)
        self.showamount.clicked.connect(self.gotoamount)

    def gotowishlist(self):
        pass
    def gotocart(self):
        pass
    def gotoproducts(self):
        pass
    def gotowallet(self):
        self.walletmenu =QtWidgets.QMainWindow()
        self.ui = wallet.Ui_MainWindow()
        self.ui.setupUi(self.walletmenu)
        self.walletmenu.show()
        self.MainWindow.close()
    def gotowalletincrease(self):
        pass
    def gotoamount(self):
        pass    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "پنل مشتریان"))
        self.wishlist.setText(_translate("MainWindow", "لیست علاقمندیها"))
        self.cart.setText(_translate("MainWindow", " سبد خرید"))
        self.products.setText(_translate("MainWindow", "نمایش کالاها"))
        self.wallet.setText(_translate("MainWindow", "کیف پول"))


if __name__ == "__main__":
    import sys
    """app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()"""
    sys.exit(app.exec_())








# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wallet.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.increaseamount = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Elm")
        font.setPointSize(10)
        self.increaseamount.setFont(font)
        self.increaseamount.setObjectName("increaseamount")
        self.horizontalLayout.addWidget(self.increaseamount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "کیف پول"))
        self.pushButton_2.setText(_translate("MainWindow", "موجودی حساب"))
        self.increaseamount.setText(_translate("MainWindow", "افزایش موجودی"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

