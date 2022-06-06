# OptiverAntHillSimulation - Quant Researcher Puzzle

## What the project does

The script answers the following questions:

### OPTIVER QUANT RESEARCHER PUZZLE - https://www.optiver.com/working-at-optiver/career-opportunities/5841549002/

"Can you solve this puzzle? 

An ant leaves its anthill in order to forage for food. It moves with the speed of 10cm per second, but it doesn't know where to go, therefore every second it moves randomly 10cm directly north, south, east or west with equal probability.

1. If the food is located on east-west lines 20cm to the north and 20cm to the south, as well as on north-south lines 20cm to the east and 20cm to the west from the anthill, how long will it take the ant to reach it on average?
2. What is the average time the ant will reach food if it is located only on a diagonal line passing through (10cm, 0cm) and (0cm, 10cm) points?
3. Can you write a program that comes up with an estimate of average time to find food for any closed boundary around the anthill? What would be the answer if food is located outside an defined by ( (x – 2.5cm) / 30cm )2 + ( (y – 2.5cm) / 40cm )2 < 1 in coordinate system where the anthill is located at (x = 0cm, y = 0cm)? Provide us with a solution rounded to the nearest integer."


## Methodology
Questions 1 and 2 are answered using Python scripts to simulate trials of the ants. 
Question 3 was coded in Java. A lower-level language was required to achieved a large enough number of simulations so that results began to converge. Total simulations 100million. Python was far too slow for this, especially as it was running on only 1 core.

- Defined boundary in each question
- Simulated the ant's random walk to find food
- Found E(time to find food) using the law of large numbers - ran a large number of simulations and checked that the expected value converged on a particular value

# Answers
1. 4.5 seconds (2sf) - ran 100,000 simulations in python. Each simulation had up to 1,000 timesteps.
2. 252 seconds (3sf) - ran 100 million simulations to arrive at this answer. 
3. 14.0 seconds (3sf) - ran 1 million simulations in python. Each simulation had up to 10,000 timesteps.
