import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, Bookname: str, Bookprice: float, Booknos=0):
        # Run validations to the received arguments
        assert Bookprice >= 0, f"Price {Bookprice} is not greater than or equal to zero!"
        assert Booknos >= 0, f"Quantity {Booknos} is not greater or equal to zero!"

        # Assign to self object
        self.Bookname = Bookname
        self.Bookprice = Bookprice
        self.Booknos = Booknos

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.Bookprice * self.Booknos

    def apply_discount(self):
        self.Bookprice = self.Bookprice * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Books.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                Bookname=item.get('Bookname'),
                Bookprice=float(item.get('Bookprice')),
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
        return f"{self.__class__.__name__}('{self.Bookname}', {self.Bookprice}, {self.Booknos})"


class Book(Item):
    def __init__(self, Bookname: str, Bookprice: int, nos=0, stolen_papers=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            Bookname, Bookprice, nos
        )

        # Run validations to the received arguments
        assert stolen_papers >= 0, f"Broken Phones {stolen_papers} is not greater or equal to zero!"

        # Assign to self object
        self.stolen_papers = stolen_papers

Book1 = Book("HarryPotter", 500, 5, 1)

print(Item.all)