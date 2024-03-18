vehicles = []
times = []

with open('vehicles.txt') as file:
    for line in file.readlines():
        parts = line.split()
        clock = (int(parts[0]), int(parts[1]), int(parts[2]))
        times.append(clock)
        vehicles.append(parts[3])

print('Exercise 2:')
start = times[0][0]
end = times[-1][0]
print(end - start + 1, 'hours')

print('Exercise 3:')
previous_hour = -1
for i in range(len(vehicles)):
    current_hour = times[i][0]
    if current_hour != previous_hour:
        print(current_hour, 'hour:', vehicles[i])
        previous_hour = current_hour

print('Exercise 4:')
d = {
    'B': 0,
    'M': 0,
    'K': 0,
    'Cars': 0
}

for v in vehicles:
    if v[0] in d:
        d[v[0]] += 1
    else:
        d['Cars'] += 1

print('Buses:', d['B'])
print('Motorbikes:', d['M'])
print('Trucks:', d['K'])
print('Cars:', d['Cars'])

print('Exercise 5:')


def time_to_seconds(clock):
    return clock[0] * 60 * 60 + clock[1] * 60 + clock[2]


def time_to_timestamp(clock):
    return ':'.join(map(str, clock))


seconds = [time_to_seconds(t) for t in times]
longest_range = [times[0], times[1]]
longest = seconds[1] - seconds[0]

for i in range(len(seconds)):
    difference = seconds[i] - seconds[i - 1]
    if difference > longest:
        longest = difference
        longest_range = [times[i - 1], times[i]]

print(' - '.join(map(time_to_timestamp, longest_range)))


def match_pattern(license_plate, pattern):
    for i in range(len(license_plate)):
        if pattern[i] != '*' and pattern[i] != license_plate[i]:
            return False
    return True


# print('Exercise 6:')
pattern = input('Enter pattern of the license plate: ')
matches = [plate for plate in vehicles if match_pattern(plate, pattern)]
print(matches)

print('Exercise 7:')


def int_to_str_leading_zeros(num):
    s_num = str(num)
    return '0' + s_num if len(s_num) == 1 else s_num


def time_to_timestamp_leading_zeros(clock):
    leading_zeros_clock = map(int_to_str_leading_zeros, clock)
    return ' '.join(leading_zeros_clock)


previous = seconds[0]
checked = [0]
for i, s in enumerate(seconds):
    next_car = previous + 5 * 60
    if s >= next_car:
        checked.append(i)
        previous = s

with open('checked.txt', 'w') as file:
    for index in checked:
        file.write(time_to_timestamp_leading_zeros(times[index]) + ' ' + vehicles[index] + '\n')
