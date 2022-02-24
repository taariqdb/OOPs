import csv


class Item:
    Pay_rate = 0.8 #discount for all sale
    all = []
    def __init__(self,Bookname: str,Bookprice: int,Booknos: int):
        #run vaidation using assert option
        assert Bookprice > 0 ,f"Price {Bookprice} is should be greater than 0 "
        assert Booknos > 0, f" Quantity {Booknos} is should be greater than 0"
        self.Bookname = Bookname
        self.Bookprice = Bookprice
        self.Booknos = Booknos
        Item.all.append(self)
    def calculate_total_quantity(self):
        return self.Bookprice * self.Bookqunatity
    def apply_discount(self):
        self.Bookprice = self.Bookprice * self.Pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('books.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                Bookname=item.get('Bookname'),
                Bookprice=int(item.get('Bookprice')),
                Booknos=int(item.get('Booknos')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.Bookname}', {self.Bookprice}, {self.Booknos})"
    
    

        
             