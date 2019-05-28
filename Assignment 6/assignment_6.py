import turtle
import csv
import os

t = turtle.Turtle()


class GetPoints:
    def __init__(self, file):
        self.list_of_points = []
        with open(file, 'r') as csv_file:
            csv_output = csv.reader(csv_file, delimiter=',')
            for row in csv_output:
                key = float(row[0].strip('()'))
                value = float(row[1].strip('()'))
                item = [key, value]
                self.list_of_points.append(item)
            csv_file.close()
        self.index = len(self.list_of_points)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.index:
            raise StopIteration
        self.current_index = self.current_index + 1
        return self.list_of_points[self.current_index]

    def __str__(self):
        return str(self.list_of_points[self.current_index])

    def iterate_all_points(self):
        for index in range(0, self.index, 1):
            yield self.list_of_points[index]


class PointList:
    def __init__(self, plist):
        self.points = plist

    def minX(self):
        min = self.points[0][0]
        for x in range(1, len(self.points)):
            if self.points[x][0] < min:
                min = self.points[x][0]
        return min

    def minY(self):
        min = self.points[0][1]
        for y in range(1, len(self.points)):
            if self.points[y][1] < min:
                min = self.points[y][1]
        return min

    def maxX(self):
        max = self.points[0][0]
        for x in range(1, len(self.points)):
            if self.points[x][0] > max:
                max = self.points[x][0]
        return max

    def maxY(self):
        max = self.points[0][1]
        for y in range(1, len(self.points)):
            if self.points[y][1] > max:
                max = self.points[y][1]
        return max


def plot(file):
    t = turtle.Turtle()
    screen = turtle.Screen()
    points = GetPoints(file)
    points_list = points.list_of_points
    plist = PointList(points_list)
    screen.setworldcoordinates(plist.minX(), plist.minY(), plist.maxX(), plist.maxY())
    for p in range(len(points_list) - 1):
        t.up()
        t.goto(points_list[p][0], points_list[p][1])
        t.down()
        t.goto(points_list[p + 1][0], points_list[p + 1][1])
    input("Done with {}, Press Return/Enter to continue".format(file))
    turtle.resetscreen()


def main():
    files = [x for x in os.listdir() if x.endswith(".csv")]
    for file in files:
        plot(file)


if __name__ == '__main__':
    main()
