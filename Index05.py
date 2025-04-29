def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count
print(main('salom'))