import sys
import os


def main(argv):
    file1 = open(argv[1], "r").readlines()
    file2 = open(argv[2], "w")
    if len(file1) < 3:
        print("File has less than 3 lines")
        file2.write("File has less than 3 lines")
    else:
        file2.write(file1[2])
    os.remove(argv[1])


if __name__ == "__main__":
    main(sys.argv)
