import datetime
class ItemLine:
    _instance = {}
    def __new__(cls, description, qty, unit_price):
        key = (description, qty, unit_price)
        if key not in cls._instance:
            obj = super().__new__(cls)
            cls._instance[key] = obj
        return cls._instance[key]
    def __init__(self, description, qty, unit_price):
        self.description = description
        self.qty = qty
        self.unit_price = unit_price
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description
    @property
    def qty(self):
        return self.__qty
    @qty.setter
    def qty(self, qty):
        self.__qty = qty
    @property
    def unit_price(self):
        return self.__unit_price
    @unit_price.setter
    def unit_price(self, unit_price):
        self.__unit_price = unit_price
    def calc_line_total(self):
        return self.qty * self.unit_price
    def __str__(self):
        return f"{self.description:15}{self.qty:>15d}{self.unit_price:>15.2f}{self.calc_line_total():>15.2f}"
class Invoices:
    invoice_no = 0
    def __init__(self, items = None):
        Invoices.invoice_no += 1
        self.__invoice_no = Invoices.invoice_no
        self.__invoice_date = datetime.datetime.now()
        self.__items = items if items is not None else []
    def get_invoice_no(self):
        return self.__invoice_no
    def set_invoice_no(self, invoice_no):
        self.__invoice_no = invoice_no
    def get_invoice_date(self):
        return self.__invoice_date
    def set_invoice_date(self, invoice_date):
        self.__invoice_date = invoice_date
    def get_items(self):
        return self.__items
    def set_items(self, items):
        self.__items = items   
    def add_item(self, item):
        self.__items.append(item)
    def remove_items(self, item):
        self.__items.remove(item)
    def calc_total(self):
        total = 0
        for item in self.__items:
            total += item.calc_line_total()
        return total
    def __str__(self):
        dt_string = self.__invoice_date.strftime("%x")
        return f"Invoice no: {self.__invoice_no}\tInvoice date: {dt_string}\tInvoice total: ${self.calc_total()}"
class Customer:
    def __init__(self, name = " ", invoices = None):
        self.__name = name
        self.__invoices = invoices if invoices is not None else []
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_invoices(self):
        return self.__invoices
    def set_invoices(self, invoices):
        self.__invoices = invoices
    def add_invoice(self,invoice):
        self.__invoices.append(invoice)
    def remove_invoice(self, invoice):
        self.__invoices.remove(invoice)
    def __str__(self):
        return f"Customer {self.__name} has the following: "
if __name__ == "__main__":
    item1 = ItemLine("Computers", 2, 1000.0)
    item2 = ItemLine("Mouses", 40, 35.0)
    item3 = ItemLine("Speaker", 500, 20.8)
    item4 = ItemLine("Chairs", 20, 25.5)
    item5 = ItemLine("Calculators", 40, 15.5)
    item6 = ItemLine("Keyboards", 40, 12.2)
    invoice1 = Invoices([item1])
    invoice1.add_item(item2)
    invoice2 = Invoices([item3, item4, item5])
    invoice2.remove_items(item5)
    invoice3 = Invoices([item5])
    invoice3.add_item(item6)
    Thuy = Customer("Thuy", [invoice1])
    Thuy.add_invoice(invoice2)
    Mark = Customer("Mark")
    Mark.add_invoice(invoice3)
    print(Thuy)
    for invoice in Thuy.get_invoices():
        print(invoice)
        print(f"{'Item':15}{'Quantity':>15}{'Unit Price':>15}{'Total':>15}")
        for item in invoice.get_items():
            print(item)
    print()
    print(Mark)
    for invoice in Mark.get_invoices():
        print(invoice)
        print(f"{'Item':15}{'Quantity':>15}{'Unit Price':>15}{'Total':>15}")
        for item in invoice.get_items():
            print(item)
    print("Invoice 1 is invoice 2: ", invoice1 is invoice2)
    print("The total number of invoices: ", Invoices.invoice_no)
