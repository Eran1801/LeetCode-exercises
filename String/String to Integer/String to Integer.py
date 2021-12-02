def myAtoi(s: str) -> int:

    if s is None or len(s) < 1:
        return 0

    # Max and Min values for the integers
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    s = s.lstrip()

    # Counter
    i = 0
    # Flag to indicate if the number is negative or positive
    isNegative = len(s) > 1 and s[0] == '-'
    isPositive = len(s) > 1 and s[0] == '+'

    if isNegative:
        i += 1
    elif isPositive:
        i += 1

    # This will store the converted number
    number = 0
    # Loop for each numeric character in the string iff numeric characters are leading
    # characters in the string
    while i < len(s) and '0' <= s[i] <= '9':
        number = number * 10 + int(s[i])
        i += 1

    if isNegative:
        number = -number

    # Edge cases
    if number < INT_MIN:
        return INT_MIN
    if number > INT_MAX:
        return INT_MAX
    return number
