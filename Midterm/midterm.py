import csv


class Guests:
    """ Object containing the guests for the hotel"""
    def __init__(self, first, last):
        self.first_name = first
        self.last = last

    def assign_room(self, room):
        self.rooms = room


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_rooms(self, rooms_low, rooms_hi, room_type):
        [self.rooms.append([i, room_type]) for i in range(rooms_low[0], rooms_hi[1]+1)]

    def assign(self, guest_list):
        success = 0
        fail = 0
        for guest in guest_list:
            need_to_assign = True
            if guest[1] is 'beach':
                count = 0
                while need_to_assign:
                    try:
                        self.rooms.insert(count, guest[0])
                    except IndexError:
                        count = count + 1
                    if count == 19:
                        break
            elif guest[1] is 'lot':
                count = 20
                while need_to_assign:
                    try:
                        self.rooms.insert(count, guest[0])
                    except IndexError:
                        count = count + 1
                    if count == 40:
                        break


def process_guests():
    """Opens the guest file and does stuff with each guest"""
    with open('Guests.csv', 'r') as csv_file:
        csv_output = csv.reader(csv_file, delimiter=',')
        result = []
        for row in csv_output:
            last = row[0].strip()
            first = row[1].strip()
            facing = 'beach' if '*' in first else 'lot'
            result.append([Guests(last, first.strip('*')), facing])
        csv_file.close()
    return result


def main():
    """Main function, where the program begins"""
    lot_rooms = (1, 20)
    beach_rooms = (21, 40)
    new_hotel = Hotel()
    new_hotel.add_rooms(lot_rooms[0], lot_rooms[1], 'lot')
    new_hotel.add_rooms(beach_rooms[0], beach_rooms[1], 'beach')
    guest_list = process_guests()
    new_hotel.assign(guest_list)


if __name__ == '__main__':
    main()
