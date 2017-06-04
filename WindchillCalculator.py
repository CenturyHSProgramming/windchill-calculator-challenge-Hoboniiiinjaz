# WindchillCalculator.py
# Your job is to write a function in BMICalculator.py (call
# it **calculateWindchill()** that calculates the windchill # factor based on the New Wind Chill Index from 
# Calculator.net (http://www.calculator.net/wind-chill-calculator.html)

# Define Function below
# be sure to return an integer
import math

def calculateWindchill(v, t):
    windChill = int(35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16))
    return math.floor(windChill)

if __name__ == '__main__':
    answer = calculateWindchill(10, 2)
    print(answer)
