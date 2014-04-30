import math 

# some fixed constants

# Row 6
shapeParam = 400.

# Row 9
meanLifetime = 2.83



def runNumbaz(endYear, collectionSize, digitizationCostPerItem, startingYear, digitizationBudgetPerYear, annualPercentageIncreaseInCostOfDigitization, printOut):

    # initialize values
    AnnualCostPerItemWithIncrease = digitizationCostPerItem
    mediaPrevious = collectionSize
    savedPerYearControl3Previous = 0
    savedCumulativelyControl1Previous = 0
    savedCumulativelyControl2Previous = 0
    legacyItemsPermanentlyLostCumulativeControl1Previous = 0 
    legacyItemsPermanentlyLostCumulativePrevious = 0
    finalContentLost = 50000
     
    for year in range(firstYear, endYear+1):
        
        timeElapsed=year-firstYear

        # column B
        media = collectionSize + shapeParam - shapeParam*math.exp(timeElapsed/meanLifetime)
        
        if (media < 0):
            media = 0

        mediaNext = collectionSize + shapeParam - shapeParam*math.exp((timeElapsed+1)/meanLifetime)
        
        if (mediaNext < 0):
            mediaNext = 0

        # column O
        itemsDigitizedPerYearBasedOnAnnualIncreaseInDigitizationCosts = digitizationBudgetPerYear / AnnualCostPerItemWithIncrease

        
        # column D -- savedPerYearControl2
        if (itemsDigitizedPerYearBasedOnAnnualIncreaseInDigitizationCosts > media):
            savedPerYearControl2 = media
        else:
            savedPerYearControl2 = itemsDigitizedPerYearBasedOnAnnualIncreaseInDigitizationCosts

        # column C -- savedPerYearControl1
        if (year >= startingYear):       
            savedPerYearControl1 = savedPerYearControl2
        else:
            savedPerYearControl1 = 0

        # column E -- savedPerYearControl3
        
        if (savedPerYearControl1 + savedPerYearControl3Previous)==0:
            savedPerYearControl3 = 0
        else:
            savedPerYearControl3 = savedPerYearControl2

        # column F -- savedCumulativelyControl1

        if (savedPerYearControl3 <= media):
            savedCumulativelyControl1 = savedPerYearControl3 + savedCumulativelyControl1Previous
        else:
            savedCumulativelyControl1 = (media - savedPerYearControl3) + savedCumulativelyControl1Previous

        # column G -- savedCumulativelyControl2
        if (savedCumulativelyControl1 <= savedCumulativelyControl1Previous):
            savedCumulativelyControl2 = savedCumulativelyControl2Previous
        else:
            savedCumulativelyControl2 = savedCumulativelyControl1

        # column J -- itemsDigitizedInExcessOfTheLoss
        if ((savedPerYearControl3-(mediaPrevious-media)) < 0):
            itemsDigitizedInExcessOfTheLoss = 0
        else:
            itemsDigitizedInExcessOfTheLoss = (savedPerYearControl3-(mediaPrevious-media))

        # column L -- legacyItemsPermanentlyLostAnnualy
        tester = (media - mediaNext) - savedPerYearControl3
        if (tester < 0):
            legacyItemsPermanentlyLostAnnualy = 0
        else:
            legacyItemsPermanentlyLostAnnualy = (media-mediaNext)-savedPerYearControl3

        # column M -- legacyItemsPermanentlyLostCumulativeControl1
        legacyItemsPermanentlyLostCumulativeControl1 = legacyItemsPermanentlyLostAnnualy + legacyItemsPermanentlyLostCumulativeControl1Previous - itemsDigitizedInExcessOfTheLoss

        # column N -- legacyItemsPermanentlyLostCumulative
        if (legacyItemsPermanentlyLostCumulativeControl1 < legacyItemsPermanentlyLostCumulativePrevious):
            legacyItemsPermanentlyLostCumulative = legacyItemsPermanentlyLostCumulativePrevious
        else:
            legacyItemsPermanentlyLostCumulative = legacyItemsPermanentlyLostCumulativeControl1

        #if (year > startingYear): 
        #    if (legacyItemsPermanentlyLostCumulative == legacyItemsPermanentlyLostCumulativePrevious):
        #        finalContentLost = legacyItemsPermanentlyLostCumulative


        #debugging: 
        #print "year, media, L"
        if printOut==True:
            print year, media, legacyItemsPermanentlyLostAnnualy


        # update values
        AnnualCostPerItemWithIncrease = AnnualCostPerItemWithIncrease + annualPercentageIncreaseInCostOfDigitization * AnnualCostPerItemWithIncrease

        mediaPrevious=media

        savedPerYearControl3Previous = savedPerYearControl3
        savedCumulativelyControl1Previous = savedCumulativelyControl1
        savedCumulativelyControl2Previous = savedCumulativelyControl2
        legacyItemsPermanentlyLostCumulativeControl1Previous = legacyItemsPermanentlyLostCumulativeControl1
        legacyItemsPermanentlyLostCumulativePrevious = legacyItemsPermanentlyLostCumulative

    return legacyItemsPermanentlyLostCumulative


# Row 8
collectionSize = 50000

# Row 2
firstYear = 2014

# Row 18
startingYear = 2017

# Row 13
digitizationCostPerItem = 60.

# Column U (note that here is is fractional; on spreadsheet it is in units of 'percent')
annualPercentageIncreaseInCostOfDigitization = .16
 
endYear=2028

startBudget=0 # the starting budget to explore

stepBudget=100 # the step size, in dollars, of budgets to explore

digitizationBudgetPerYear = startBudget
totalLostPrevious=collectionSize*2 

#debugging example:
printOut=True
digitizationBudgetPerYear = 700000
print "example: for digitizationBudgetPerYear = ", digitizationBudgetPerYear
print "\nyear, media, legacyItemsPermanentlyLostAnnualy"
runNumbaz(endYear, collectionSize, digitizationCostPerItem, startingYear, digitizationBudgetPerYear, annualPercentageIncreaseInCostOfDigitization, printOut)


# run the numbers:
print "\nrunning the numbers:"
while (True):
    printOut=False
    totalLost = runNumbaz(endYear, collectionSize, digitizationCostPerItem, startingYear, digitizationBudgetPerYear, annualPercentageIncreaseInCostOfDigitization, printOut)
    if totalLost==totalLostPrevious:
        break
    totalLostPrevious=totalLost
    digitizationBudgetPerYear = digitizationBudgetPerYear + stepBudget

print "minimal annual digitization budget to maximally reduce lost items =", digitizationBudgetPerYear
    

