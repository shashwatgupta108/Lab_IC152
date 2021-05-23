from math import sqrt
import sys


def main(argv):
    a, b, c = int(argv[1]), int(argv[2]), int(argv[3])
    dis = b * b - 4 * a * c
    if dis == 0:
        print("The only solution is %0.1f" % (-b / (2 * a)))
    elif dis > 0:
        print("The solutions are %0.1f and %0.1f" % ((-sqrt(dis) - b) / (2 * a), (sqrt(dis) - b) / (2 * a)))
    else:
        if b != 0:
            print("The solutions are %0.1f+%0.1fj and %0.1f+%0.1fj" % (
                -b / (2 * a), -sqrt(abs(dis)) / (2 * a), -b / (2 * a), sqrt(abs(dis)) / (2 * a)))
        else:
            print("The solutions are %0.1fj and %0.1fj" % (-sqrt(abs(dis)) / (2 * a), sqrt(abs(dis)) / (2 * a)))


if __name__ == "__main__":
    main(sys.argv)
