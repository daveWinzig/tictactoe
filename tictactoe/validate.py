"""
Helper functions for validating user input.
"""

def doesInputMatch(userInput,*matches):
    """
    Raises exception if userInput does not match an item in matches, otherwise return True.
    """

    if userInput not in matches:
        msg = ", ".join(matches)
        raise Exception("Input must exactly match one of the following: " + msg + ".")

    return True

def isInputIntInRange(userInput, n):
    """
    Raises exception if user input is outside of range, otherwise return True.
    Range is the excluded endpoint of a 0 to n range.
    """

    if userInput not in range(n):
        raise Exception("Input must be an integer number from 0 to " + n + ".")

    return True
