#Formatted Printing

'''
    ASCII Codes
    bicameral language has upper case and lowercase characters
    A - 65 ... Z -90
    a - 97 ... z-122
    0 ... 9   ascii codes are 48 ... 57

    all codes are 0 ... 127

    ord('A') # will return the ASCII Code
    chr(65) #will return A

    UNICODE - other languages

    UTF - 8   8, 16, 32 bit
    UTF -16    16, 32 bit
    UTF - 32  32 bit only
    (also 1, 2, 4 byte)
    unicode.org
   # s = '\u03b1\u03b2\u03b3'
    digraphs formed by using two codes to make one letter that is made up of two characters
    planes i think are a range of codes



    #escape sequence characters
        #\n \f \t \b \r \a \v      # \\  \\ \' \"
        

    #escape sequence printable and non-printable
    \xhh  example \x41 for letter a   two digit hexadecimal
    \uxxxx  \u0041  four digit hexadecimal
    \Uxxxxxxxx   eight digit unicode/hexadecimal
    \N{name}    #name is in the unicode database
    \N{dollar sign}
    UTF

    print(  sep  file   flush)

    control characters for formatted printed
    %s sring
    $d decimal %i integer %o. octal  %x hexadecimal 
    %f float %F float %g General %e Scientific %E Scientific

    poop

'''


print ('Step1\fStep2\fStep3')
