class ProductClass:
    def __init__(self, name, cost):
        self.name = name
        self.cost = float(cost)


class ProcessProducts:
    def __init__(self, file):
        self.product_dictionary = dict()
        self.file = file

    def insert(self, barcode, product_id):
        """Inserts the key, unless it already exists."""
        try:
            self.product_dictionary[barcode]
        except KeyError:
            self.product_dictionary[barcode] = product_id
        else:
            print('Barcode {} already exists.  If you wish to update, run call ProccessFile.update() instead of insert'.
                  format(barcode))

    def update(self, barcode, product_id):
        """Inserts the key, overwriting if it already exists."""
        self.product_dictionary[barcode] = product_id

    def process(self):
        """Process the specified CSV file"""
        with open(self.file, 'r') as csv_file:
            for line in csv_file:
                split_line = line.strip().split(",")
                barcode = split_line[0].strip()
                product = split_line[1].strip()
                cost = split_line[2].strip()
                product_id = ProductClass(product, cost)
                self.insert(barcode, product_id)

    def lookup(self, item):
        try:
            product = self.product_dictionary[item]
        except ValueError:
            raise ValueError('Item does not exist!')
        else:
            return product.name, product.cost

    def __str__(self):
        return str(self.product_dictionary)


if __name__ == '__main__':
    start = ProcessProducts('Products.csv')
    start.process()
    with open('Carts.csv', 'r') as shopping_cart:
        for cart_item in shopping_cart:
            print("Start of new cart:")
            cart_total = float()
            split_cart = cart_item.strip().split(",")
            for i in split_cart:
                entry = start.lookup(i)
                cart_total = cart_total + entry[1]
                print('\t%-20s $%.2f' % (entry[0], entry[1]))
            print("\nCart Total:\t{}\n\n".format(cart_total))
