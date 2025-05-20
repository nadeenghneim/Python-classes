import random 
import time 
def randomdate(startdate,enddate):
    dateform="%m/%d/%Y"

    starts= time.mktime(time.strptime(startdate,dateform))
    end=time.mktime(time.strptime(enddate,dateform))
    randoms= random.uniform(starts,end)
    randomdatee=time.strftime(dateform,time.localtime(randoms))

    return randomdatee
print("the random date is:",randomdate("01/01/2021","12/30/2023"))