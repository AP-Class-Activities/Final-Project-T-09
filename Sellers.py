
class Seller:
    def __init__(self, id, name, family, address, phone, sex, year, email, password):
        self.__id = id
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__password = password

        if id > 9999999999 or id < 1000000000:
            raise ValueError('id number should contain 10 digits')
        self.__id = id


        if sex not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female]')
        self.__sex = sex


        if year > 1380 or year < 1330: 
            raise ValueError('you must be at least 20 years old')
        self.__year = year


        if password < 10000000:
            raise ValueError('password should be at least 8 characters')



    #setters and getters
    @property
    def ID(self): 
        return self.__id
    
    @ID.setter
    def ID(self,value):
        if id > 9999999999 or id < 1000000000:
            raise ValueError('id number should contain 10 digits')
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
    

    @property
    def year(self): 
        return self.__year

    @year.setter
    def year(self,value): 
        if value > 1380 or value < 1330: 
            raise ValueError('you must be at least 20 years old')
        self.__year = value


    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self, value):
        self.__email = value

    
    @property
    def Password(self):
        return self.__password

    @Password.setter
    def Password(self, value):
        if password < 10000000:
            raise ValueError('password should be at least 8 characters')
        self.__password = value



    def __str__(self): 
        return 'ID: {}   name: {} {}    address: {}   phone: {}   sex: {}    year: {}    email:{}    password:{}'\
            .format(self.ID,self.name, self.family, self.address, self.phone, self.sex, self.year, self.email, self.password)




