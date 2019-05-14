import csv


class Person:
    def __init__(self, first, last):
        self.first = first.capitalize()
        self.last = last.capitalize()


class Passenger(Person):
    def __init__(self, first, last, plane_row, plane_seat):
        super().__init__(first, last)
        self.plane_row = plane_row
        self.plane_seat = plane_seat

    def __eq__(self, other):
        return self.plane_row == other.plane_row, self.plane_seat == other.plane_seat


class Jet:
    def __init__(self, rows, seats):
        self.jet = []
        jet_seats = []
        for i in range(seats):
            jet_seats.append([])
        for i in range(rows):
            self.jet.append(jet_seats[:])

    def assign(self, manifest):
        success = 0
        fail = 0
        for passenger in manifest:
            try:
                if not self.jet[passenger.plane_row-1][passenger.plane_seat-1]:
                    self.jet[passenger.plane_row-1][passenger.plane_seat-1] = passenger
                    success = success + 1
                else:
                    print('Passenger already seated in Row {}, Seat {}. Cannot seat {} {}'.format(
                        passenger.plane_row, chr(passenger.plane_seat+65), passenger.first, passenger.last))
                    fail = fail + 1
            except IndexError:
                fail = fail + 1
                print("Passenger {}, {} with Row {} and Seat {} is not possible, plane too small.".format(
                    passenger.first, passenger.last, passenger.plane_row, chr(passenger.plane_seat+65)))

        print('Assignments Complete, {} Successes and {} Fails.'.format(success, fail))

    def lookup(self, row, seat):
        return self.jet[row-1][seat-1]


def main():
    jet_rows = 36
    jet_seats = 7
    jet = Jet(jet_rows, jet_seats)
    manifest = []

    with open('Passengers.csv', 'r') as csv_file:
        csv_output = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_output:  # Clears the two lines of header.
            if count > 1:
                last = row[0].strip()
                first = row[1].strip()
                plane_row = int(row[2].strip())
                plane_seat = int(ord(row[3].strip())-65)
                assignment = Passenger(first, last, plane_row, plane_seat)
                manifest.append(assignment)
            else:
                count = count + 1
    csv_file.close()
    jet.assign(manifest)

    lookup_row = int(input("What row would you like to lookup a passenger for?"))
    lookup_seat = int(ord(input("What seat would you like to lookup a passenger for?")))-65
    if not jet.lookup(lookup_row, lookup_seat):
        print('No passenger in row {}, seat {}'.format(lookup_row, chr(lookup_seat+65)))
    else:
        first_name = jet.lookup(lookup_row, lookup_seat).first
        last_name = jet.lookup(lookup_row, lookup_seat).last
        print('Row {}, Seat {} has {} {} sitting in it.'.format(lookup_row, chr(lookup_seat+65), first_name, last_name))


if __name__ == '__main__':
    main()
