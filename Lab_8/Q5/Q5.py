import sys


def main(argv):
    file1 = open(argv[1], "r").readlines()
    file2 = open(argv[2], "w")
    a = list(map(int, file1[0].split(",")))
    print("Data inside Input.txt is :\n" + file1[0])
    a.sort()
    for i in range(len(a)):
        a[i] = str(a[i])
    file2.write(",".join(a))
    print("Data inside Output.txt is :\n" + ",".join(a))


if __name__ == "__main__":
    main(sys.argv)
