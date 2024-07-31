class SevenBoom():

    for i in range (0,50):
        if (i%7==0):
            print (f' boom found {i} by div')
            continue
            # כי לא רוצים ש 7 יודפס פעמיים
        num_as_str= str(i)
        if (num_as_str.count ("7")>0):
            print (f' boom found {i} by count')

