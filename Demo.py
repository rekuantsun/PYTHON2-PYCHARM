import datetime

class Item:
    shippingWeight:float
    description:str

    def __init__(self,shippingWeight,description):
        self.shippingWeight=shippingWeight
        self.description=description
    def getpriceofquantity(self):
        pass
    def getTax(self):
        pass
    def instock(self):
        pass
    def getItem(self)->str:
        result ="Van chuyen:"+str(self.shippingWeight)+"\tMo ta:"+self.description
        return result

class OrderDetail:
    quantity:str
    taxStatus:str
    item: Item

    def __init__(self,quantity,taxStatus):
        self.quantity=quantity
        self.taxStatus=taxStatus

    def calcSubtotal(self):
        pass
    def Weight(self):
        pass
    def Tax(self):
        pass
    def lietkeItem(self):
        print("So luong:",self.quantity,"Duoc mua")

class Payment:
    amount:float

    def __init__(self,amount):
        super().__init__()
        self.amount=amount
    def getAmount(self)->str:
        result="Gia: "+str(self.amount)
        return result

class Cash(Payment):
    cashTendered: float

    def __init__(self,amount,cashTendered):
        Payment.__init__(self,amount)
        self.cashTendered=cashTendered
    def getCash(self)->str:
        result= self.getAmount()+"\tTra: "+ str(self.cashTendered)
        return result

class Check(Payment):
    name:str
    bankID:str

    def __init__(self, amount, name, bankID):
        Payment.__init__(self, amount)
        self.name=name
        self.bankID=bankID
    def getcheck(self)->str:
        result=self.getAmount() + "\tTen: " + self.name  + "\tBank ID" + self.bankID
        return result

class Credit(Payment):
    number: str
    type: str
    expDate:str

    def __init__(self,amount,number,type,expDate):
        Payment.__init__(self,amount)
        self.number=number
        self.type=type
        self.expDate=expDate
    def getCredit(self)->str:
        result = self.getAmount() + "\tSo: "+self.number+"\tLoai:"+self.type+"\tNgay:"+self.expDate
        return result


class Order:
    date: datetime
    status: str
    orderDetail:list[OrderDetail]
    payment:list[Cash,Check,Credit]

    def __init__(self,date,status):
        self.date=date
        self.status=status

    def calcSubTotal(self):
        pass
    def calcTax(self):
        pass
    def calcTotal(self):
        pass
    def Totalweight(self):
        pass
    def addOrderDetail(self,chitiet:OrderDetail):
        self.orderDetail.append(chitiet)
    def getOrderDetail(self)->list[OrderDetail]:
        return self.orderDetail
    def addPayment(self,chitra: Cash):
        self.payment.append(chitra)
    def getPayment(self)->list[Payment]:
        return self.payment
    def getOrder(self)->str:
        result="Ngay:"+self.date+"\t Tinh trang:"+self.status+"\tDa mua:"+str(self.orderDetail)+"\tCo gia:"+str(self.payment)
        return result

class Customer:
    name:str
    address:str
    orders:list[Order]

    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.order=[]
    def addOrder(self,donhang:Order):
        self.order.append(donhang)
    def getOrder(self)->list[Order]:
        return self.order
    def getCustomer(self)->str:
        result="Khach hang:"+self.name+"\tDia chi:"+self.address+"\tDa mua:"+str(self.order)
        return result



