import pandas as pd
df=pd.read_csv("C:\\Users\\Akshat\\Desktop\\IP Project\\iatafinal.csv")
print(df)
s=1
while s==1 :
    print("To exit enter 1 or enter")
    i=eval(input("IATA CODE :"))
    sh=df['iataCode']== i
    print(df[sh])
    if i == 1:
        break
 
