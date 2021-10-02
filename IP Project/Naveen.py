import pandas as pd
import matplotlib.pyplot as pl
print('Welcome to the Passenger Statistics of the Top 10 Airports!')
print('Hartsfield Jackson Atlanta International Airport, USA ATL')
print('Beijing Capital International Airport, China: PEK')
print('Dubai International Airport, UAE DXB')
print('Tokyo International Airport, Japan: HND')
print('Los Angeles International Airport, USA: LAX')
print("Chicago O Hare International Airport, USA: ORD")
print('London Heathrow Airport, UK  LHR')
print('Hong Kong International Airport, China HKG')
print('Shanghai Pudong International Airport, China: PVG')
print('Paris Charles de Gaulle Airport, France CDG')
while True:
    Cod=input('Enter the IATA Code of the airport:')
    if Cod=='DXB':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Dubai.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='ATL':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Atlanta.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='PEK':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Beijing.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='HND':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Tokyo.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='LAX':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Los Angeles.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='ORD':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Chicago.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='LHR':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\London.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='HKG':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Hong Kong.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='PVG':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Shangai.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
    elif Cod=='CDG':
        data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Paris.csv")
        Year=data['Year']
        Passengers=data['Passengers']
        pl.xlabel('Year')
        pl.ylabel('Passengers per Year')
        pl.bar(Year,Passengers)
        pl.show()
