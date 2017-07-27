#Lab practical 2
#Michael McDaniel
import tools
#Section 1 and 2
"""
Section 1 should take the two given files, read the contents, take an input and then print out
each unique key and then add up the values for each key and print the totals
"""

"""
Section 2 is simply adding the while loop with conditions to section 1
"""

def totals():
    openFile = open("california.txt", 'r')
    cali = openFile.readlines()
    openFile.close()
    openFile = open("texas.txt", "r")
    texas = openFile.readlines()
    openFile.close()
    texasD ={}
    for line in texas:
        name, num = ":".join(line.split("\t")).split("\n")
        texasD[name] = num.strip()
    caliD ={}
    for line in cali:
        name, num = ":".join(line.split("\t")).split('\n')
        caliD[name] = num.strip()
    while True:
        userIN = input("Which state's totals would you like to compute? ")
        if userIN.lower() == "california":
            print(caliD.items())
            '''this is clearly not correct, it needs to be adding up the values of each dictionary and then
            assigning that running total to the key in a new dictionary which can then be printed out same goes for texas'''
            #for i in range(len(cali)):
                #print(name.strip("\n"))
                #total = 0
                #total += caliD.value()
            break
        elif userIN.lower() == "texas":
            #print(texasD.keys())
            #for i in range(len(texasD)):
                #total = 0
                #total += texasD.value()
            break
        elif userIN.lower() == 'stop':
            break
        else:
            print("Try a different state. ")
"""
section 1 is not working as I could not find a way to make the file output as a dictionary
"""
#main
totals()

#section 3
"""
for section 3 we need to sort the set with .sorted then based on the user input print which
ever table they said with the tools table_print function this would basically work except the fact that I
couldnt get the list into a dictionary
"""

totalsT = {'Cthulu' : 67033, 'Godzilla': 66251, 'The Joker': 63620, 'Dr. Doom': 51248, 'Voldemort' : 39388}
srtTotalsT = sorted(totalsT)
totalsC = {'Cthulu' : 62379, 'Godzilla': 86086, 'The Joker': 39662, 'Dr. Doom': 56279, 'Voldemort' : 61084}
percentsC = 12345
percentsT = 23456
srtTotalsC = sorted(totalsC)
def winner():
    userIN = input("Which state's total would you like to compute? (or STOP) ")
    while True:
        if userIN.lower() == "stop":
            break
        elif userIN.lower() == "texas":
            tools.table_print(data = srtTotalsT, padding = "\t", headers = {"Name, Votes"})
            tools.table_print(data = percentsT, padding = "\t", headers = {'Names', 'Percentages'})
        elif userIN.lower() == "california":
            tools.table_print(data = srtTotalsC, padding = "", headers = {"Name, Votes"})
            tools.table_print(data = percentsC, padding = "\t", headers = {'Names', 'Percentages'})
        else:
            print("Try antoher input: ")
#main
winner()

"""
section 3 works except that I am not sure what to pass headers, clearly it should be taking the keys
from the lists and useing those but I cant seem to get the syntax right
"""

#section 4 is added to section 3
"""
For section 4 I need to reprint the table_print from tools, but the data will be different from last time.
This time I will use the data in column 2 but divide it by the total sum of column 2 which will give a float,
use round(number, 2) with the float in order to round it to a 00.00% format then use that as the data.
"""



'''
This test was clearly a disaster for me, I wanted to go through and clean up my code but I didnt have time.
I also wanted to get my section 1 totaling finished as towards the end I figured out how to made a
dictionary. With that learned I was going to go and remove the hardcoded data in section 3, then actually
make the proper tables. I was close on everthing and look forward to correcting what I could not finish,
but hey at least if both of the conditions are STOP it works like a charm.
'''
