import sys


def main(argv):
    file1 = open(argv[1], mode='r')
    file2 = open(argv[2], mode='w')
    for line in file1:
        a = list(map(int, line.split(",")))
        s = 0
        for i in a:
            s += i
        file2.write(str(s) + '\n')
    file1.close()
    file2.close()


if __name__ == "__main__":
    main(sys.argv)
