def buildcar (manu, model, **carinfo):
    """Listing information about  a car."""
    info={}
    for key, value in carinfo.items():
        info[key]= value
    return info

mycar= buildcar('chevrolet', 'impala', year='2013', color= 'white')
print (mycar)