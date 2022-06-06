# -*- coding: utf-8 -*-
"""
Created on Mon May 23 06:39:35 2022

@author: Y-dee
"""

import random

def testAntForaging(numTimeSteps, boundaryFunction):
# https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
# passing function in as parameter here as change the function applied in different cases    
    
    # ant moves 10cm per timestep. Let 1 timestep = 1second
    #ant lifespan?
    antHill = [0,0]
    antPosition = antHill
    foundFood = False

    time = 0
    timeSteps = numTimeSteps
    
    while time <= timeSteps or foundFood == False:
        
        # generate randomCoin flip - https://www.w3schools.com/python/ref_random_randint.asp
        direction = random.randint(1,4)        
        
        # update position
        if direction == 1: # head north
            antPosition[0]  
            antPosition[1] += 10 
            
        elif direction ==2: # head east
            antPosition[0] += 10
            antPosition[1]
        elif direction == 3: # head south
            antPosition[0]
            antPosition[1] -= 10
        else:   # head west
            antPosition[0] -= 10
            antPosition[1]
        
        #print(antPosition)
        time += 1
        # check x co-ord
        #if abs(antPosition[0]) >= 20:
            #print('Found food')
            #foundFood = True
        #    return time
        #check y co-ord
        #if abs(antPosition[1]) >= 20:
            #print('Found food')
            #foundFood = True
        #    return time
        
        foundFood = boundaryFunction(antPosition)
        
        if foundFood == True:
            return time
        
    return -1

def checkSquareBoundary(antPosition):
            #print(antPosition)
        # check x co-ord
        
        distance = 20
        if abs(antPosition[0]) >= distance:
            #print('Found food')
            #foundFood = True
            return True
        #check y co-ord
        if abs(antPosition[1]) >= distance:
            #print('Found food')
            #foundFood = True
            return True
        else:
            return False
  
def checkDiagonalBoundary(antPosition):
    
    if antPosition[0] + antPosition[1] >= 10:
        return True
    else: 
        return False

def checkGeneralBoundary(antPosition):
    
    import parser

    
    generalEquationLHS = "((x-2.5)/30)**2+((y-2.5)/40)**2"
    equationRHSValue = 1
#   generalEquationLHS = input("Enter equation")
#   equationRHSValue = input("Enter RHS of equation")
    function = parser.expr(generalEquationLHS).compile()
    
    x = antPosition[0]
    y = antPosition[1]
    
    eqnValue = eval(function)
    
    if eqnValue >= equationRHSValue:
        return True
    
    else:
        return False
    

def runSimulation(numSimulations, numTimeSteps, boundaryFunction):
# https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
# passing function in as parameter here as change the function applied in different cases    
    results = []
    cumulativeTime = 0
    noTimesFoodFound = 0
    avgTimeTaken = 0
    
    for i in range(numSimulations):
        timeTaken = testAntForaging(numTimeSteps, boundaryFunction)
        
        # append to list. Not space efficient, as will have many entries. Other ways, but can debug later
        #results.append(timeTaken)        
        
        # now O(1) space efficiency.
        if timeTaken > 0:
            cumulativeTime += timeTaken
            noTimesFoodFound += 1
            
    avgTimeTaken = cumulativeTime/noTimesFoodFound
    
    return avgTimeTaken

def testForConvergence(numSeparateRuns, boundaryFunction, numSimulations, numTimesteps):
    results = []
#avgTime = runSimulation(int(1e6),1e4, checkSquareBoundary)
    for i in range(numSeparateRuns):    
        #avgTime = runSimulation(int(1e4),1e2, checkSquareBoundary)
        avgTime = runSimulation(int(numSimulations),numTimesteps, boundaryFunction)

        print(avgTime)
        results.append(avgTime)
    print(results)
    
if __name__ == "__main__":
    ##TESTS WITH DIFFERENT PARAMETERS
    #testForConvergence(10, checkSquareBoundary, 1e5, 1e3) #(answer: 4.5)
    ##testForConvergence(10, checkDiagonalBoundary, 5e4 ,6e4) ##5e5,8e4 does not termoinate after ~ 7hrs (answer: have not been able to converge). 
                                                            # implement in C++ or Java. Faster language. 
    ##testForConvergence(10, checkGeneralBoundary, 1e4,1e3) #(answer: 14. Also got 14.01 on another run)
    
    
    print(runSimulation(int(1e6),1e4, checkGeneralBoundary))
    #print(runSimulation(int(1e3),1e4, checkDiagonalBoundary))
    
    # check the stability of simulation results by running multiple INSTNACES/ batches
    # plot results with multiple points on scatter graph and see if converging
    #4.5 square boundary
            