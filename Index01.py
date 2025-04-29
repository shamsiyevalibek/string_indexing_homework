def main(s):
    """
    The string variable s is given. Return the first character.
    If the string is empty, return "Empty string".
    
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if s == "":
        return "Empty string"
    else:
        return s[0]
print(main("salom"))
