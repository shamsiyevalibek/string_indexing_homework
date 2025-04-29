def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s) == 0:
        return "Empty string"
    elif len(s) == 1:
        return s + s  # faqat 1 ta belgi bo‘lsa, o‘zi bilan o‘zi
    else:
        return s[0] + s[-1]
print(main('salm'))