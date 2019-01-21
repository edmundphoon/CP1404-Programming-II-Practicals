"""
CP1404/CP5632 Practical
GPS (Gopher Population Simulator)
"""
import random

MAX_BORN = 0.2 # 20%
MIN_BORN = 0.1 # 10%
MAX_DIE = 0.25 # 25%
MIN_DIE = 0.05 # 5%
INITIAL_POPULATION = 1000

population = INITIAL_POPULATION
year = 1
born_num = 0
die_num = 0

print("Welcome to the Gopher Population Simulator!")
print("Starting population: {}\n".format(str(INITIAL_POPULATION)))

for year in range(1,(10+1),1):
    population_change = 0

    born_percent = random.uniform(MIN_BORN, MAX_BORN)
    born_num = int(population * born_percent)
    population *= (1 + born_percent)

    die_percent = random.uniform(MIN_DIE, MAX_DIE)
    die_num = int(population * die_percent)
    population *= (1 - die_percent)

    print("Year", str(year))
    print("*****")
    print("{} gophers were born. {} died.".format(str(born_num),str(die_num)))
    print("Population: {}\n".format(str(int(population))))

    year += 1