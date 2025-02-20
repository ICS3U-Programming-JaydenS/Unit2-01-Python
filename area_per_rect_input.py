#!/usr/bin/env python3

# Created By: Jayden Smith
# Date: Feb 18, 2025
# This programs calculates the area and perimeter of a rectangle given user input


def main():
    length = int(input("What is the length of the rectangle? (cm) "))
    width = int(input("What is the width of the rectangle? (cm) "))
    print("Area is {}cm^2".format(length * width))
    print("Perimeter is {}cm^2".format((2 * length) + (2 * width)))


if __name__ == "__main__":
    main()
