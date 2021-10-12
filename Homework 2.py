monthList = {"january":"1","february":"2","march":"3","april":"4","may":"5",
             "june":"6", "july":"7","august":"8","september":"9","october":"10","november":"11",
             "december":"12"
             }
import datetime
today = datetime.date.today()
d1 = today.strftime("%d/%m/%Y")
#print(d1)
inputFile = open('.\inputDates.txt','r')
outputFile = open('.\parsedDates.txt','w')

for each in inputFile:
    if each != -1:
        listAns = each.split()
        if len(listAns) >= 3:
            month = listAns[0]
            day = listAns[1]
            year = listAns[2]
            
            if month.lower() in monthList:
                comma = day[-1]
                if comma == ',' :
                    day = day[:len(day) - 1]
                    monthNumber = monthList[month.lower()]
                    answer = monthNumber + "/" + day + "/" +  year
                    
                
                    x1 = datetime.datetime(int(year),int(monthNumber),int(day))
                    x2 = datetime.datetime(today.year,today.month,today.day)
                    
                    if x2 >= x1:
                                outputFile.write(answer)
                                outputFile.write("\n")

                    
                    


inputFile.close()
outputFile.close()