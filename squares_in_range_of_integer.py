#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program finds the square of all integers from 0 - an inputted integer


def main():
    # this function finds the squares

    # input
    number_as_string = input("Enter an integer ≥ 0: ")

    # process & output
    try:
        number = float(number_as_string)
        if number == 0:
            print("\n0² = 0")
        elif number > 0:
            integer = int(number_as_string)
            if integer == number:
                print("")
                for loop_counter in range(integer + 1):
                    result = loop_counter ** 2
                    print("{0}² = {1}".format(loop_counter, result))
            else:
                print("\nInvalid. Enter an integer ≥ 0")
        else:
            print("\nInvalid. Enter an integer ≥ 0")
    except (Exception):
        print("\nInvalid. Enter an integer ≥ 0")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
