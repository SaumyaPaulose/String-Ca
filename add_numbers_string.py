from click._unicodefun import click
import re


def add(string_numbers):
    """Get the sum of numbers in the given string.
        Negative numbers are not allowed.
        Numbers above 1000 are ignored when calculating the sum.

        :param string_numbers: string of numbers
        :return: sum value in int
    """

    sum_string_numbers = 0
    numbers = re.findall("-?\d+", string_numbers)

    for number in numbers:
        if isinstance(int(number), int):
            if int(number) > 0:
                if int(number) <= 1000:
                    sum_string_numbers = sum_string_numbers + int(number)
            else:
                raise ValueError('Negative numbers not allowed. Aborting.')
    return sum_string_numbers


if __name__ == "__main__":

    str_number_provided = click.prompt('Enter the string of numbers:', type=str)
    if "\\n" == str_number_provided[-2:]:
        raise ValueError('The provided string of numbers should not end in \\n. Aborting.')

    sum_value = add(string_numbers=str_number_provided)
    print "\n"
    print "The string of numbers provided is : " + str_number_provided
    print "The sum of numbers in the given string is : " + str(sum_value)
