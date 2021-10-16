import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import collections 
 
#===== Merging two excel files==== 
df = pd.DataFrame() 
 
for f in ['2009maharashtraresults.xlsx', '2014maharashtraresults.xlsx']: 
    data = pd.read_excel(f, 'Sheet1') #this loop merges the two excel sheets into one. 
    df = df.append(data) 
df.to_excel("combineddata.xlsx")#resultant data is stored in this third excel sheet 
data = pd.read_excel("combineddata.xlsx") 
print(data) 
 
plt.figure(figsize=(8, 4)) 
plt.scatter( 
    data['PARTYNAME'], 
    data['SEATS'], 
    c='blue' 
) 
plt.xlabel("Party)") 
plt.ylabel("Seats Won") 
plt.xticks(rotation=90) # to print party names vertically 
plt.show() 
 
#=============================================================== ============== 
final_Data = {} 
 
for i in data['PARTYNAME']: 
     x = i 
     t1 = (data[(data.PARTYNAME == x) & (data.YEAR == 2009)].SEATS).tolist() #retriving seats of similar partyname & at the same time 
     t2 = (data[(data.PARTYNAME == x) & (data.YEAR == 2014)].SEATS).tolist() #retriving seats of similar partyname & at the same time converting it to List from panda.Series datatype 
     t3 = t1 + t2 #combining both the list element into 1 list instead of adding here because either t1 or t2 can be empty as their record can be absent in dataset 
     print("--------------") 
     print ("Name of Party =", i) 
     print ("NUMBER OF SEATS =", int(sum(t3)))    #sum() function will add all the elements present into the list 
     final_Data.update({i : int (sum(t3))}) #adding data to dictionary for further processing 
# =============================================================== 
plt.bar(final_Data.keys(), final_Data.values() ,  color='green') 
plt.xlabel("Party)") 
plt.ylabel("Seats Won") 
plt.xticks(rotation=90) 
print("THE CHANGE IS PERFORMANCE IS AS FOLLOWS") 
for i in data['PARTYNAME']: 
     x = i 
     t2 = (data[(data.PARTYNAME == x) & (data.YEAR == 2014)].SEATS).tolist() 
     t1 = (data[(data.PARTYNAME == x) & (data.YEAR == 2009)].SEATS).tolist() #retriving seats of similar partyname & at the same time converting it to List from panda.Series datatype 
      
     diff = t1[0] - sum(t2[0:]) 
     if diff > 0: 
           print ("Party Name :", x) 
           print ("loss  from 2009 to 2014 = ",int(diff) ) 
     else: 
         if diff<0: 
             
             print ("Party Name :",x) 
             print ("Gain  from 2009 to 2014 = ",abs(int(diff)))#Abs is used as we dont want negative values to be displayed 
         else: 
             print ("Party Name :",x )
             print ("No change  from 2009 to 2014 = ",int(diff) )