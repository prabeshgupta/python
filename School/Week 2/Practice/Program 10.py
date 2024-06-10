#Merge dictionaries

planets = {
    "Mercury": 1,
    "Venus": 2,
    "Earth" : 3,
    "Mars": 4
}

otherPlanets= {
    "Jupiter": 5,
    "Saturn": 6,
    "Neptune":7,
    "Uranus": 8
}

solarSystem = planets | otherPlanets
print(solarSystem)