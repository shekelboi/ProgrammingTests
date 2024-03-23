class Dance:
    def __init__(self, type, girls_name, boys_name):
        self.type = type
        self.girls_name = girls_name
        self.boys_name = boys_name


dances = []

with open('danceprogramme.txt') as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 3):
        dance_type = lines[i]
        girl = lines[i + 1]
        boy = lines[i + 2]
        dances.append(Dance(dance_type, girl, boy))

print('Exercise 2:')
# print('First:', dances[0].type + ',', 'last:', dances[-1].type)
print(f'First {dances[0].type}, last: {dances[-1].type}')

counter = 0
for dance in dances:
    if dance.type == 'samba':
        counter += 1

print('Exercise 3:')
print(counter, 'couples danced samba')

vilma_dances = set()
for dance in dances:
    if dance.girls_name == 'Vilma':
        vilma_dances.add(dance.type)

print('Exercise 4:')
print('Vilma participated in the following dances:', ', '.join(vilma_dances))

print('Exercise 5:')
dance_type = input('Enter the type of dance to check: ')

dance_partners_of_vilma = []
for dance in dances:
    if dance.girls_name == 'Vilma' and dance.type == dance_type:
        dance_partners_of_vilma.append(dance.boys_name)

if dance_partners_of_vilma:
    print(', '.join(dance_partners_of_vilma))
else:
    print('Vilma did not dance samba.')

girls_names = {}
boys_names = {}
for i in range(len(dances)):
    if dances[i].girls_name in girls_names:
        girls_names[dances[i].girls_name] += 1
    else:
        girls_names[dances[i].girls_name] = 0

    if dances[i].boys_name in boys_names:
        boys_names[dances[i].boys_name] += 1
    else:
        boys_names[dances[i].boys_name] = 0

with open('participants.txt', 'w') as file:
    file.write('Girls: ' + ', '.join(girls_names.keys()) + '\n')
    file.write('Boys: ' + ', '.join(boys_names.keys()) + '\n')

highest = max(girls_names.values())
print([girl for girl, value in girls_names.items() if value == highest])
highest = max(boys_names.values())
print([boy for boy, value in boys_names.items() if value == highest])
