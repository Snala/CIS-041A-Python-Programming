def degrees_to_hex(degree):
    degree = float(degree)
    return int(degree // 22.5)


def combined_hex(item):
    left = format(item[0], 'X')
    right = format(item[1], 'X')
    return left + right


def iterate_list(hex_list):
    output = str()
    for i in hex_list:
        left = i[0]
        right = i[1]
        output = output + bytes.fromhex(combined_hex([degrees_to_hex(left), degrees_to_hex(right)])).decode('utf-8')
    print(output)
    out_file = open('output.txt', 'w')
    out_file.write(output)
    out_file.close()


def main():
    file = open('HexDegrees.csv', 'r')
    hex_degrees_list = []
    for line in file:
        line = line.replace('),(', '\n')
        line = line.rstrip('),').strip('(),')
        for i in line.splitlines():
            i = i.strip()
            i = i.split(',')
            hex_degrees_list.append([float(i[0]), float(i[1])])
    file.close()
    iterate_list(hex_degrees_list)


if __name__ == '__main__':
    main()
