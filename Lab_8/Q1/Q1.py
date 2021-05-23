import sys


def main(argv):
    file1 = open(argv[1], mode='r').readlines()
    file2 = open(argv[2], mode='r').readlines()
    file3 = open(argv[3], mode='w')
    for i in range(len(file1)):
        file3.write(str(int(file1[i][:len(file1[i]) - 1]) * int(file2[i][:len(file2[i]) - 1])) + "\n")


if __name__ == "__main__":
    main(sys.argv)
