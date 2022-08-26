

from re import sub


def isSubString(substring, string):
    if ' ' in substring:
        substring = substring.split(" ")[0]
    if (substring.upper() in string) or (substring.lower() in string) or (substring.lower().capitalize() in string):
        return True
    return False


def most_frequent(List):
    return max(set(List), key=List.count)
