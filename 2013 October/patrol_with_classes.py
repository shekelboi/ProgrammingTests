import datetime as dt


class Vehicle:
    def __init__(self, timestamp: dt.timedelta, license_plate: str):
        self.timestamp = timestamp
        self.license_plate = license_plate

    def get_datetime(self):
        return dt.datetime(1970, 1, 1) + self.timestamp

    def get_formatted_time(self, separator=' '):
        return self.get_datetime().strftime(f'%H{separator}%M{separator}%S')


def vehicle_from_text(text):
    parts = text.split()
    delta = dt.timedelta(hours=int(parts[0]), minutes=int(parts[1]), seconds=int(parts[2]))
    return Vehicle(delta, parts[3])


def delta_to_datetime(delta):
    return dt.datetime(1970, 1, 1) + delta


with open('vehicles.txt') as file:
    data = file.read().splitlines()
    vehicles = [vehicle_from_text(line) for line in data]

print('Exercise 2:')
shift = vehicles[-1].timestamp - vehicles[0].timestamp
print(f'The shift was {delta_to_datetime(shift).hour + 1} hour(s) long')

print('Exercise 3:')
checked = [vehicles[0]]
for i in range(1, len(vehicles)):
    if delta_to_datetime(checked[-1].timestamp).hour != delta_to_datetime(vehicles[i].timestamp).hour:
        checked.append(vehicles[i])

print('\n'.join([f'{v.get_datetime().hour} hour: {v.license_plate}' for v in checked]))

print('Exercise 4:')
d = {
    'Buses': 0,
    'Trucks': 0,
    'Motorbikes': 0,
    'Cars': 0
}
for v in vehicles:
    if v.license_plate[0] == 'B':
        d['Buses'] += 1
    elif v.license_plate[0] == 'K':
        d['Trucks'] += 1
    elif v.license_plate[0] == 'M':
        d['Motorbikes'] += 1
    else:
        d['Cars'] += 1

for k, v in d.items():
    print(f'{k}: {v}')

print('Exercise 5:')
longest_vehicles = [vehicles[0], vehicles[1]]
longest = vehicles[1].timestamp - vehicles[0].timestamp
for i in range(1, len(vehicles)):
    difference = vehicles[i].timestamp - vehicles[i - 1].timestamp
    if difference > longest:
        longest = difference
        longest_vehicles = [vehicles[i - 1], vehicles[i]]

print(' - '.join([v.get_formatted_time(separator=':') for v in longest_vehicles]))

print('Exercise 6:')
pattern = input('Enter a license plate: ')
matches = []
if len(pattern) == len(vehicles[0].license_plate):
    for v in vehicles:
        match = True
        for i in range(len(pattern)):
            if pattern[i] != '*' and pattern[i] != v.license_plate[i]:
                match = False
                break
        if match:
            matches.append(v.license_plate)
print(matches)

print('Exercise 7:')
checked = [vehicles[0]]
for i in range(1, len(vehicles)):
    if vehicles[i].timestamp >= checked[-1].timestamp + dt.timedelta(minutes=5):
        checked.append(vehicles[i])

with open('checked.txt', 'w') as file:
    for v in checked:
        file.write(f'{v.get_formatted_time()} {v.license_plate}\n')
