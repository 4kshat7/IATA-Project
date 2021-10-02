from clrprint import *         #pip install clrprint
import pandas as pd            #pip install pandas
import matplotlib.pyplot as pl #pip install matplotlip
import csv
from csv import writer
import numpy as np
import time           #To delay execution (looks good with it)
import webbrowser
#######################################################################################################################################################################
clrprint("\t\t\tWELCOME TO THE IATA DATA Guide ",clr='r')
print('--------------------------------------------------------------------------')
clrprint("The IATA is the trade assosciation of the world's airlines representing some 290 airlines or 82% of total air traffic. ",clr='y')
clrprint("IATA supports many aviation activity and help formulate industry policy on critical aviation issues.",clr='y')
print('--------------------------------------------------------------------------')

df=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\iatafinaldog.csv",encoding="ISO-8859-1")
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
while True:
    clrprint("To exit from the program  enter 'exit'",clr='r')
    opt=clrinput('Enter "1" if u want to see IATA DATA HANDLER or \nEnter "2" for PASSANGER STATISTICS OF TOP 10 AIRPORTS or \nEnter "3" for STATISTICS ON DIFFERENT TYPES OF AIRPORTS IN THE WORLD or \nEnter "4" to access civilian Flight Radar and Ground conditions at Airport (Requires ISP connection):',clr='g')
    opt=opt.upper()
    if opt=='1':
        time.sleep(0.5)
        clrprint('\t\t    WELCOME TO THE IATA AIRPORTS FINDER',clr='y')
        clrprint('\t\tWe provide data for more than 7200 Airports',clr='default')
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        print(df)
        
        mal=clrinput('What do u want to do (add or remove or show):',clr='g')
        mal=mal.upper()
        if mal=='ADD':
           newcode=input('Code:')
           newcode=newcode.upper()
           newairport=input('airport:')
           newlocation=input('location:')
           newcountry=input('Country:')
           newrow=[newcode,newairport,newlocation,newcountry]
           row_contents = [newcode,newairport,newlocation,newcountry]
           append_list_as_row('iatafinaldog.csv', row_contents)
           df=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\iatafinaldog.csv",encoding="ISO-8859-1")
           
        elif mal=='REMOVE':
            del_iata=input(str('Insert the iataCode to remove:'))
            del_iata=del_iata.upper()
            for(row_index,row_value) in df.iterrows():
                for idel in row_value:
                    if del_iata==idel:
                       yon=clrinput('Are you sure u want to remove yes/no:',clr='p')
                       yon=yon.upper()
                       if yon=='YES':
                                 df=df.drop([row_index],axis=0)
                                 clrprint(row_index,'has been deleted',clr='y')
                                 df.to_csv("C:\\Users\\Akshat\\Desktop\\IP Project\\iatafinaldog.csv",index=False)
                       else:
                           clrprint('Nothing has been removed',clr='r')
                           break
            else:
                clrprint('iata not found',clr='r')

        elif mal=='SHOW':
            while True:
                clrprint("\nTo exit enter 'exit'",clr='red')
                iata=(clrinput("IATA CODE:",clr='m'))
                iata=iata.upper()
                
                pd.set_option('display.max_columns', 500)
                pd.set_option('display.width', 1000)
                sh=df['iataCode']== iata
                a=df[sh]
                if iata == 'EXIT':
                    break
                elif a.empty==True:
                    clrprint("\t\t\tAirport not Found ! Please enter another IATA code",clr='r')    
                else:
                    time.sleep(0.5)
                    print('\n')
                    print(a)
                    print('\n')
                
#######################################################################################################################################################################
    elif opt=='2':
        time.sleep(0.5)
        clrprint('\t\tWelcome to the Passenger Statistics of the Top 10 Airports!',clr='y')
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
            clrprint("To exit enter 'exit'",clr='red')
            Cod=clrinput("\nEnter the IATA Code of the airport:",clr='m')
            Cod=Cod.upper()
            if Cod=='DXB':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Dubai.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Dubai")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='ATL':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Atlanta.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Atlanta")
                pl.ylim(90000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='PEK':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Beijing.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Beijing")
                pl.ylim(80000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='HND':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Tokyo.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Tokyo")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='LAX':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Los Angeles.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Los Angeles")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='ORD':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Chicago.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Chicago")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='LHR':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\London.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for London Heathrow")
                pl.ylim(70000000,80000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='HKG':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Hong Kong.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Hong Kong")
                pl.ylim(50000000,80000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='PVG':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Shangai.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Shanghai")
                pl.ylim(40000000,80000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='CDG':
                data=pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\Paris.csv")
                Year=data['Year']
                Passengers=data["Passengers"]
                pl.xlabel("Year")
                pl.ylabel("Passengers per Year in 10 millions")
                pl.title("Yearly Passengers for Paris")
                pl.ylim(60000000,70000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()

            elif Cod=='EXIT':
                break
            else:
                clrprint('ERROR ,Please enter from the iata code given above',clr='red')
                continue
#######################################################################################################################################################################
    elif opt == '3':
        dd =pd.read_csv("C:\\Users\\AKSHAT\\Desktop\\IP Project\\pie.csv",encoding="ISO-8859-1")
        csfont = {'fontname':'Comic Sans MS'}
        lab=dd['Category']
        s = (0.05, 0.2, 0.2, 0.2,0.2,0.2)
        patches, texts=pl.pie(dd['Total Number'],shadow=False, startangle=90,wedgeprops   = { 'linewidth' : 0.5, 'edgecolor' : "black" },frame= True)
        pl.legend(patches, lab, loc="best")
        pl.title('Different types of airports in the world',**csfont,size=12,color='r')
        pl.axis('equal')
        time.sleep(0.5)
        print(dd)
        pl.show()

        object=('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
        x_pos=np.arange(len(object))
        y=[80,72,55,38,71,63,94,90,99,86,83,91]
        pl.plot(x_pos,y,color='b')
        pl.xticks(x_pos,object)
        pl.xlabel("Months")
        pl.ylabel("Passenger Traffic in %")
        pl.grid(True)
        pl.title("Monthly Passenger Traffic (2019)")
        pl.show()
################################################################################################################################
    elif opt == '4':
        print("Find airports and track flights")
        arp=clrinput("IATA CODE:",clr='m')
        s=arp.lower()
        clrprint("Realtime global flight tracking ",clr='w')
        clrprint("Source: www.flightradar24.com",clr='b')
        time.sleep(2)
        if s=='exit':
            continue
        else:
            webbrowser.open(("https://www.flightradar24.com/airport/"+s))
        time.sleep(2)
        
    elif opt == 'EXIT':
        clrprint("Thank you for using IATA DATA guide !",clr='w')
        break
    else:
        continue
