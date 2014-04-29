# =if(B$8+$B$6-$B$6*exp(($A52-$B$2)/B$9)>0,B$8+$B$6-$B$6*exp(($A52-$B$2)/B$9),0)
import math 
# Row 8
collectionSize = 50000
# Row 6
shapeParam = 400
# Row 2
startYear = 2014
# Row 9
meanLifetime = 2.83

# Row 18
startingYear = 2017

# Row 13
digitizationCostPerItem = 60

annualPercentageIncreaseInCostOfDigitization = .16

AnnualCostPerItemWithIncrease 

for year in range(2014, 2028):

    timeElapsed=year-startYear
    media = collectionSize + shapeParam - shapeParam*math.exp(timeElapsed/meanLifetime)

    if (media > 0):
         print year, round(media)
