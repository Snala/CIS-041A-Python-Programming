import matplotlib.pyplot as plt
import os


def plot(file):
    t = list()
    s = list()
    output_file = file[:-4]
    output_file = str(output_file) + '.png'

    with open(file, 'r') as csv_file:
        for line in csv_file:
            line = line.strip().strip('()').split(',')
            t.append(float(line[0].strip()))
            s.append(float(line[1].strip()))

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='x-axis', ylabel='y-axis',
           title='Plot from {}'.format(file))
    ax.grid()

    fig.savefig(output_file)
    plt.show()


def main():
    files = [x for x in os.listdir() if x.endswith(".csv")]
    for file in files:
        plot(file)


main()
