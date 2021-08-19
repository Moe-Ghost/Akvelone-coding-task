"""
logic to translate stringify
integer value into numeric format
"""
# reference to constant values
import settings


class NumberFormatter:
    """class that converts and validates the input"""

    @staticmethod
    def validating(line):
        """validate input"""

        # validate string length
        if len(line) not in range(2, 2 ** 32 - 1):
            return 'incorrect string length'

        # checks the position of arithmetic signs
        if line[-1] in settings.ALLOWED_ARITHMETICAL_OPERATION_SIGNS:
            return 'incorrect last symbol'

        # validate symbol type
        for i in line:
            if i not in settings.ALLOWED_NUMBERS + settings.ALLOWED_ARITHMETICAL_OPERATION_SIGNS:
                return "incorrect symbol"

        return 1

    @staticmethod
    def parse_int(line):
        """convert string"""
        # variable for storing math operator
        cur = ''

        # creating generator
        for i in line:
            if i in settings.ALLOWED_NUMBERS:
                cur += i
                yield int(cur)
                cur = ''
            else:
                cur = i
