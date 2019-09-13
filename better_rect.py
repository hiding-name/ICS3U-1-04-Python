#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program area rect


def main():
    side = input("What is side dimension:")
    side2 = input("What is other dimension:")
    area = side * side2
    perimeter = 2 * (side + side2)
    print("The area is:" + format(area))
    print("The perimeter is:" + format(perimeter))


if __name__ == "__main__":
    main()
