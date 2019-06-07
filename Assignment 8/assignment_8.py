class ProductClass:
    def __init__(self, product, cost):
        self.product = product
        self.cost = cost


class ProcessFile:
    def __init__(self, file):
        self.product_dictionary = dict()
        self.file = file

    def insert(self, barcode, product_id):
        """Inserts the key, unless it already exists."""
        try:
            self.product_dictionary[barcode]
        except KeyError:
            self.product_dictionary[barcode] = product_id
        finally:
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

    def __str__(self):
        return str(self.product_dictionary)


if __name__ == '__main__':
    start = ProcessFile('Products.csv')
    start.process()
    print(start)
