#shaftdia.py
"""
there can be a mix of mm and in ->  70mm 3in. 3 1/8in.  as an example don't do the math
there can be mm only.  These are clean.  just take an int of the data and convert to inches
there can be in. only.  these can be messy.  315/16 is supposed to be 3 15/16.  there will be no space

!!!!!  Need to cover all scenarios or merged shaft diameters
merged inch and metric, merged inch, merged metric....

"""
from fractions import Fraction

def mixed_fraction_to_decimal_fractions(mixed_fraction_str):
    inPos = 0
    mmPos = 0
    fractPos = 0
    spacePos = 0
    
    inPos = mixed_fraction_str.find('in')
    mmPos = mixed_fraction_str.find('mm')
    inCount = mixed_fraction_str.count('in' )
    mmCount = mixed_fraction_str.count( 'mm' )
    fractPos = mixed_fraction_str.find('/')
    fractSupPos = mixed_fraction_str.find('u\2044')
    spacePos = mixed_fraction_str.find(' ')

    if inPos != -1 and mmPos == -1:
        if spacePos != -1 and  fractPos != -1:
            #there will be no whole part.  Only 
            if fractPos < spacePos:
                #no space before fraction
                #need to separate whole part, numerator, and denoninator
                mixed_fraction_str = mixed_fraction_str[:inPos]   #trim off in.
                parts = mixed_fraction_str.split("/")
                
                numerator = parts[0]
                denominator = parts[1]
                pos = 0
                while numerator > denominator:
                    pos += 1
                    whole_number = int(mixed_fraction_str[:pos])
                    parts = mixed_fraction_str[pos:].split("/")
                    numerator = parts[0]
                    denominator = parts[1]

                fraction_str = numerator + "/" + denominator
                
            else:
                #I think this is a proper fraction
                #whole part might be zero

                parts = mixed_fraction_str.split(" ")
                whole_number = int(parts[0])  #this can fail if there is no space
                fraction_str = parts[1]

        elif fractPos == -1:
            #either no space or no fractionpart
            #could be just a whole part
            whole_number = 0 #int(mixed_fraction_str[:inPos])
            fraction_str = mixed_fraction_str[:inPos]+"/1"
    elif inPos != -1 and mmPos !=-1 or (inCount > 1 or mmCount >1) or (inCount >0 and mmCount >0):
        #the shaft diameters have been merged into one line and the data is no good. 
        return mixed_fraction_str     #-1.0
    elif inPos == -1 and mmPos != -1:
        whole_number = int(mixed_fraction_str[:mmPos])
        return float (whole_number /25.4)
    
    
    
    fraction_obj = Fraction(fraction_str)
    '''
    pos = 0
    while fraction_obj.numerator >= fraction_obj.denominator:
        #the text has a bad format
        pos += 1   #start with the first character and make it the whole part
        whole_number = int(parts[0][pos:])
        fraction_str = parts[1][:pos]
        fraction_obj = Fraction(fraction_str)
    '''

    # Combine whole number and fraction
    total_fraction = Fraction(whole_number * fraction_obj.denominator + fraction_obj.numerator, fraction_obj.denominator)
    
    return float(total_fraction)

def cleanupFraction(mixed_fraction_str):
    inPos = 0
    mmPos = 0
    fractPos = 0
    spacePos = 0
    
    inPos = mixed_fraction_str.find('in')
    inCount = mixed_fraction_str.count('in' )
    mmCount = mixed_fraction_str.count( 'mm' )
    mmPos = mixed_fraction_str.find('mm')
    fractPos = mixed_fraction_str.find('/')
    spacePos = mixed_fraction_str.find(' ')

    if inCount == 1 and mmCount == 0:
        if spacePos != -1 and  fractPos != -1:
            #there will be no whole part.  Only 
            if fractPos < spacePos:
                #no space before fraction
                #need to separate whole part, numerator, and denoninator
                mixed_fraction_str = mixed_fraction_str[:inPos]   #trim off in.
                parts = mixed_fraction_str.split("/")
                
                numerator = parts[0]
                denominator = parts[1]
                pos = 0
                while numerator > denominator:
                    pos += 1
                    whole_number = int(mixed_fraction_str[:pos])
                    parts = mixed_fraction_str[pos:].split("/")
                    numerator = parts[0]
                    denominator = parts[1]

                fraction_str = numerator + "/" + denominator
                
            else:
                #I think this is a proper fraction
                #whole part might be zero

                parts = mixed_fraction_str.split(" ")
                whole_number = int(parts[0])  #this can fail if there is no space
                fraction_str = parts[1]

        elif fractPos == -1:
            #either no space or no fractionpart
            #could be just a whole part
            whole_number = 0 #int(mixed_fraction_str[:inPos])
            fraction_str = mixed_fraction_str[:inPos]+"/1"
    else:
        return mixed_fraction_str
    
    
    fraction_obj = Fraction(fraction_str)
    

    # Combine whole number and fraction
    total_fraction = Fraction(whole_number * fraction_obj.denominator + fraction_obj.numerator, fraction_obj.denominator)
    
    return total_fraction



def contains_superscript_or_subscript(text):
    # Unicode ranges for common superscripts and subscripts
    superscript_range = (0x00B2, 0x00B3, 0x00B9, 0x2070, 0x2074, 0x2075, 0x2076, 0x2077, 0x2078, 0x2079, 0x207A, 0x207B, 0x207C, 0x207D, 0x207E)
    subscript_range = (0x2080, 0x2081, 0x2082, 0x2083, 0x2084, 0x2085, 0x2086, 0x2087, 0x2088, 0x2089, 0x208A, 0x208B, 0x208C, 0x208D, 0x208E)

    for char in text:
        char_code = ord(char)
        if (char_code in superscript_range) or (char_code in subscript_range):
            return True
    return False








####   TESTER

mixed_fraction = "3 ¾ in."
decimal_result = mixed_fraction_to_decimal_fractions(mixed_fraction)
#mixed_clean = cleanupFraction(mixed_fraction)
print(f"The decimal equivalent of {mixed_fraction} is: {decimal_result}")
#print(f"Cleaned Up Fraction of {mixed_fraction} is: {mixed_clean}")

