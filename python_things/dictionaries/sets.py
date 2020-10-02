"""Learn about sets."""
farm_animals = {'sheep', 'cow', 'hen'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(['lion', 'tiger', 'panther', 'elephant'])
print(wild_animals)

for animal in wild_animals:
    print(animal)

print(id(farm_animals))
print(id(wild_animals))
print(farm_animals)
print(wild_animals)

farm_animals.add('horse')
wild_animals.add('mustang')

print(id(farm_animals))
print(id(wild_animals))
print(farm_animals)
print(wild_animals)

farm_animals_2 = set(['goat', 'chicken', 'horse', 'cow'])

print(farm_animals.union(farm_animals_2))
print(farm_animals.intersection(farm_animals_2))

double_farm = ['goat', 'goat', 'horse', 'horse', 'cow', 'cow']
double_farm_set = set(double_farm)
print(double_farm_set)

print()
print(farm_animals_2 - farm_animals)
