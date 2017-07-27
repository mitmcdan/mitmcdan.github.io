import donation

# As an example of how to get an amount, this gets 1 donation and prints it out
# Run the program a few times and notice that the amount changes.
# If the code won't run, did you put this file and donation.py in the same directory?
#Make a empty list and add one amount to it
def donationList():
    donLst = [ ]
    amount = donation.get_donation()
    donLst.append(amount)
#keep adding an amount to it until it reaches 200 
    for amt in donLst:
        if len(donLst) < 200:
            amount = donation.get_donation()
            donLst.append(amount)
    return donLst
donLst = donationList()

# Section 2 - Compute basic categories
#Make three different category counts to hold that value
def billCount():
    smCount = 0
    mdCount = 0
    lgCount = 0
#check to see if the amounts fit different sizes
    for amt in donLst:
        if amt <= 5:
            smCount += 1
        elif amt <= 15:
            mdCount += 1
        elif amt >= 16:
            lgCount += 1
    return smCount, mdCount, lgCount

# Section 3 - Compute success or failure
#make a total count
def TotalCount():
    totalAmt = 0
    #Add up the total amounts
    for amt in donLst:
        totalAmt += amt
    #check to see what the totalAmt is equal to
    #see if the goal was meet or not and print the correct response    
    if totalAmt >= 2017:
        print("The total amout of money raised is: $" + str(totalAmt))
        print("The fundraising goal was met!")
    elif totalAmt < 2017:
        print("The total amout of money raised is: $", totalAmt)
        print("The fundraising goal was not met.")
    return totalAmt

# Section 4 - What can you expect from the bank?
#need to check the factors of the total
#get the total amount then use mods
# the goal here was to use each remainder to then mod it and use it again to try and keep a running total
#the issue here is that it wont always be a positivie count so you can end up with negatives
#I realize that this section 4 function barely works however I do understand that I should have made a remainder variable
#then used that remainder to subtract each mod remainder from until it hit 0
def remainder():
    totalAmt = TotalCount()
    runningTotal = totalAmt
    hundredsRem = runningTotal % 100
    hundreds = (totalAmt - hundredsRem) //100
    twentiesRem = hundreds % 20
    twenties = (hundredsRem - twentiesRem) // 20
    tensRem = twenties % 10
    tens = (twentiesRem - tensRem) // 10
    fivesRem = tens % 5
    fives = (tensRem - fivesRem) // 5
    onesRem = tens % 1
    ones = (tensRem - onesRem) // 1
    print("The bank cased this amount out as:")
    print("-----------------------------------------------------------")
    print("$100 bills: ", hundreds)
    print("$20 bills: ", twenties)
    print("$10 bills: ", tens)
    print("$5 bills: ", fives)
    print("$1 bills: ", ones)
    return runningTotal #not used
#print each of the counts with their values
#main section 1
#print("One donation was received, in the amount of:", amount)
#print the full list and then norder it
print("The donation amounts: ", donationList())
print("The donations ordered: ", sorted(donationList()))
#section 2 main
#print the different amounts counted
#main
smCount, mdCount, lgCount = billCount()
print("There were", smCount, "small donations ($5 or less) .")
print("There were", mdCount, "medium donations ($6 - $15) .")
print("There were", lgCount, "large donations ($16 or more) .")
#main function Calls Sections 3 and 4
#Dont need to call Total Count as it was called again with the remainder() function
##TotalCount()
remainder()
#started to turn them into functions, to turn them all into good functions I would need to put the prints inside the functions
#and then simply call each (4) of the function names and then the whole output would appear
