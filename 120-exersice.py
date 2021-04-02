import re

def convertToFahrenheit(degreesC):
    return ((float(degreesC) * 9/5) + 32)


def writeToNewFile(convertedValuesFile, Fahrenheit, convertedFrom):
        convertedValuesFile.write(f'{Fahrenheit}F of {convertedFrom}\n')       


path = input('Plese provide full path of your file with temperatures, which you want to convert into Fahrenheit:')

with open(path, 'r') as file:
    convertedValuesFile = open("Fahrenheit.txt", "w")
    for line in file:
        convertedFrom = re.search("-*\d+[A-Z]", line).group(0)
        if 'C' in line:
            degreesC = line.split('C')
            Fahrenheit = convertToFahrenheit(degreesC[0])
        elif 'F' in line:
            degreesF = line.split('F')
            Fahrenheit = float(degreesF[0])
        else:
            print("You have incorrect value on file")   

        writeToNewFile(convertedValuesFile, Fahrenheit, convertedFrom)        
            
        
   
