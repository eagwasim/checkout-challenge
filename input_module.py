import re


def parse_input(arguments):
    """
       The parse_input method returns the arguments in a string array with its values in upper case
       :return:
    """
    parsed_arguments = re.compile("[^A-Za-z]+").split(arguments)
    return [argument.upper() for argument in parsed_arguments]
