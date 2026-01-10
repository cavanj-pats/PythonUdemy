#nested.py

def Outer():

    def Inner():
        print('Inner')
    
    print('Outer')
    Inner()



Outer()
#function Inner is "sheilded" from use.  It can only be used from Outer function
