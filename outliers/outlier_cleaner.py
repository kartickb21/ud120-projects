#!/usr/bin/python


def outlierCleaner(data):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    print("hello")
    cleaned_data = []
    
    data[3]=0
    ### your code goes here    
    from scipy.spatial import distance
    import pandas as pd
    print(type(data))
    for i in range(0, len(data.index)):
        a = (data[1][i] , data[0][i])
        b = (data[1][i], data[2][i])
        data[3][i] =  distance.euclidean(a,b)
    
    print(data)
    sdata = data.sort(columns=3, ascending=False)
    sdata = sdata.reset_index()
    cl_data = sdata[int(len(sdata)*0.1):]
    
    cl_data = cl_data.loc[:,[1,2,3]]

    return cl_data
    #return cleaned_data

