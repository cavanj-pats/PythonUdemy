#qsplit.py


def splitPN(text, char):
    """
    Finds all occurrences of a character in a string using enumerate.

    Args:
        text (str): The string to search within.
        char (str): The character to find.

    Returns:
        list: A list of indices where the character is found.
    """
    locations = []
    strPart = ""   #initiate heare so that it can be used
      #remove leading and trailing white space
    strSplit = text.strip().split(char)
    spidx = 0

    if text.find('Bearing') != -1 :
        return text    #it's a header row
    
    for sp in strSplit:
        if sp != '':
            strPart = strPart + char + sp
            if spidx+1 != len(strSplit):
                strPart = strPart + " / "
        spidx += 1
   
    return strPart
   
    """
        part = 0
    for index, c in enumerate(text):
        if c == char:
            locations.append(index)

    if len(locations) > 1:
        for s in locations:
            if s != 0:
                if part == 0:
                    strPart = text[:(s-1)]
                    part = s
                else:
                    strPart = strPart +  " / " + text[part:][:(s-1)]
    else:
        strPart = text

   
    """

"""
my_string = " QVFNL15V065SQVFNL15V207SQVFNL15V208S   "
search_char = "Q"
#indices = find_all_occurrences_enumerate(my_string, search_char)
#print(f"Occurrences of '{search_char}' in '{my_string}': {indices}")
print("Part String: ", find_all_occurrences_enumerate(my_string, search_char))
"""