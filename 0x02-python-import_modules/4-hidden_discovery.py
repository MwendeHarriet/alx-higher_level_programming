#!/usr/bin/python3
import hidden_4 as names


def main():
    name = dir(names)
    for i in name:
        if i[:2] == "__":
            continue
        else:
            print(i)


if __name__ == "__main__":
    main()
