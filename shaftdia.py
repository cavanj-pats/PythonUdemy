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
    #get a fraction and clean up so it is whole part hyphen numerator/denominator
    #from inspection the data from the SRB catalog is in the form of
    # only 'in.' one time
    # only 'mm' one time
    # or a combination always starting with mm
    # mm does not need anything other than conversion to decminal inch
    
    inPos = 0
    mmPos = 0
    fractPos = 0
    spacePos = 0
    
    inPos = mixed_fraction_str.find('in')
    mmPos = mixed_fraction_str.find('mm')
    inCount = mixed_fraction_str.count('in' )
    mmCount = mixed_fraction_str.count( 'mm' )
    fractPos = mixed_fraction_str.find('/')
    fractSuperPos = mixed_fraction_str.find('\u2044')
    spacePos = mixed_fraction_str.find(' ')
    fraction_str = ''

    if mmCount == 0 :
        #most common case
        if inCount == 1:
            fraction_str = cleanupFraction(mixed_fraction_str[:inPos].strip())  #remove the 'in.' and any spaces
            mmPart =''
        else:
            parts = mixed_fraction_str.split('in.')  # could fail if the . is missed and only in is captured
            for i in range(len(parts)):
                parts[i] = cleanupFraction(parts[i].strip())
            mmPart = ''

    
    if mmCount == 1 :
        if inCount == 0 :
            mmPart = mixed_fraction_str[:mmPos].strip()  #remove the 'mm'
        else:
            mmParts = mixed_fraction_str.split('mm')
            mmPart = mmParts[0].strip() # the mm part is always first and there is always only one.
            inParts = mmParts[1].strip() #should have one or more inch parts
            parts = inParts.split('in.')
            for i in range(len(parts)):
                parts[i] = cleanupFraction(parts[i].strip())

    strResult = ''
    if mmPart !='' :
        strResult = mmPart + 'mm '
    
    if inCount == 1:
        strResult = strResult + fraction_str+ 'in. '
    else:
        for i in range(len(parts)):
            if parts[i] != '':
                strResult = strResult + parts[i] + 'in. '    

    # once you get here you have metric and a list of clean fractions
    # this data can be returned to clean up the display table 
    # then re-used to convert to decimal
    # 
      
    return strResult
  


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
   
    fractPos = 0
    spacePos = 0
    
    fractPos = mixed_fraction_str.find('/')
    spacePos = mixed_fraction_str.find(' ')
    whole_number = ''
    numerator = ''
    denominator = ''

    pos = mixed_fraction_str.find('\u00BE')
    if pos != -1:
        numerator = '3'
        denominator = '4'
        whole_number = mixed_fraction_str[:pos].strip()

    pos = mixed_fraction_str.find('\u00BC')
    if pos != -1:
        numerator = '1'
        denominator = '4'
        whole_number = mixed_fraction_str[:pos].strip()

    pos = mixed_fraction_str.find('\u00BD')
    if pos != -1:
        numerator = '1'
        denominator = '2'
        whole_number = mixed_fraction_str[:pos].strip()
   
    if mixed_fraction_str.find('/') !=-1:
        if mixed_fraction_str.find(' ') != -1:
            parts = mixed_fraction_str.split(' ')
            whole_number = parts[0]
            fractionPart = parts[1]
        else:
            fractionPart = mixed_fraction_str

        parts = fractionPart.split("/")
    
        numerator = parts[0].strip()
        denominator = parts[1].strip()
        pos = 0
        while whole_number == '' or numerator > denominator:
            pos += 1
            whole_number = (mixed_fraction_str[:pos]) # redo the split
            parts = mixed_fraction_str[pos:].split("/")
            numerator = parts[0]
            denominator = parts[1]
    else: 
        if whole_number == '':
            whole_number = mixed_fraction_str

    if denominator == '' :
        return whole_number
    elif whole_number == '' :
        return numerator + "/" + denominator
    else:
        return whole_number + " " + numerator + "/" + denominator
        
def fraction_to_float(str_clean_fraction):
    #user of this function must send a clean fraction of the form W N/D. (one space)

    if str_clean_fraction.find('/') == -1 :
        return int(str_clean_fraction.strip())
    
    wParts = str_clean_fraction.split(' ')
    wholeNumber = int(wParts[0])
    parts = wParts[1].split('/')
    numerator = int(parts[0])
    denominator = int(parts[1])

    return float(wholeNumber  + numerator / denominator)




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

mixed_fraction = "169mm 415/16 in. 6 15/16 in. 8 in. 3 ¾ in." #6 15/16" #"4" #"315/16" #"3 ¾".   160mm 6 15/16in. 7 in. 
mixed_clean = mixed_fraction_to_decimal_fractions(mixed_fraction)
#decimal_result = mixed_fraction_to_decimal_fractions(mixed_fraction)
#mixed_clean = cleanupFraction(mixed_fraction)
#decimal_result = fraction_to_float(mixed_clean)
#print(f"The decimal equivalent of {mixed_fraction} is: {decimal_result}")
print(f"Cleaned Up Fraction of {mixed_fraction} is: {mixed_clean}")

