#!/usr/bin/python3
def main():
    a, b = 1, 2
    from add_0 import add
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()
