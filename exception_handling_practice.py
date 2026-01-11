#exception handling practice


def fun(a,b):
    try:
        x = a//b
    except Exception as e:
        print(f"An error occured: {e}")
    else:
        return x
    finally:
        print('Complete')
        return 0  #return 0 if there was an exception.  Problem is, this runs every tinme. This doesnt work.


ans = fun(10,2)
print(ans)