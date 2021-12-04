import datetime

class Item():
    shippingWeight: str
    description: str

    def __init__(self,SpW,Des) -> None:
        super().__init__()
        self.shippingWeight=SpW
        self.description=Des

    def getPriceForQuantily(self):
        pass
    def getTaxi(self):
        pass
    def inStock(self):
        pass

class Payment():
    amount: float

    def __init__(self,Amount) -> None:
        super().__init__()
        self.amount=Amount

class Cash(Payment):
    cashTendered: float

    def __init__(self, Amount, CashTendered) -> None:
        Payment.__init__(self, Amount)
        self.cashTendered=CashTendered

class Check(Payment):
    name: str
    bankID: str

    def __init__(self, Amount, name, bankID) -> None:
        Payment.__init__(self,Amount)
        self.name=name
        self.bankID=bankID

    def authorized(self):
        pass

class Credit(Payment):
    number: str
    type: str
    expDate: str

    def __init__(self, Amount,number, type, expDate) -> None:
        Payment.__init__(self,Amount)
        self.number=number
        self.type=type
        self.expDate=expDate

    def authorized(self):
        pass

class OrderDetail():
    quantily: str
    taxStatus: str
    item: Item

    def __init__(self,Quantily,TaxStatus) -> None:
        super().__init__()
        self.quantily=Quantily
        self.taxStatus=TaxStatus

    def calcSubTotal(self):
        pass
    def calcWeight(self):
        pass
    def calcTaxt(self):
        pass

class Order():
    date: datetime
    status: str
    orderdetail: list[OrderDetail]
    payment: list[Cash,Check,Credit]

    def __init__(self,date,status) -> None:
        super().__init__()
        self.date=date
        self.status=status

    def calcSubTotal(self):
        pass
    def calcTax(self):
        pass
    def calcTotal(self):
        pass
    def calcTotalWeight(self):
        pass


class Customer():
    name: str
    address: str
    order: list[Order]

    def __init__(self,name,address) -> None:
        super().__init__()
        self.name=name
        self.address=address









