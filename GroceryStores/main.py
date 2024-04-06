import csv
import datetime as dt
from collections import Counter
from math import radians, cos, sin, asin, sqrt


class Location:
    zip_code, plus_four_code = None, None
    longitude, latitude = None, None

    def __init__(self, address, zip_code, coordinates):
        self.address = address
        if zip_code:
            parts = zip_code.split('-')
            self.zip_code = parts[0]
            if len(parts) == 2:
                self.plus_four_code = parts[1]
        if coordinates:
            self.longitude, self.latitude = [float(coordinate) for coordinate in
                                             coordinates.split('(')[1].split(')')[0].split()]

    def is_not_none(self):
        """
        A location is not none if all attributes have some value except for the plus four codes.
        :return: Whether the object's attributes have values (except for the plus four codes).
        """
        return self.address is not None and zip_code is not None and self.has_coordinates()

    def distance(self, latitude, longitude):
        lon1 = radians(self.longitude)
        lon2 = radians(longitude)
        lat1 = radians(self.latitude)
        lat2 = radians(latitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        return c * r

    def has_coordinates(self):
        return self.latitude is not None and self.longitude is not None


class Store:
    last_updated = None

    def __init__(self, store_name, status, last_updated, location):
        self.name = store_name
        self.status = status
        if last_updated:
            self.last_updated = dt.datetime.strptime(last_updated, '%m/%d/%Y\t%I:%M:%S %p')
        self.location = location

    def is_not_none(self):
        return self.name is not None and self.status is not None \
            and self.last_updated is not None and self.location.is_not_none()

    def to_dict(self):
        return {
            'Store Name': self.name,
            'Address': self.location.address,
            'Zip': self.location.zip_code,
            'Plus 4 code': self.location.plus_four_code,
            'Status': self.status,
            'Latitude': self.location.latitude,
            'Longitude': self.location.longitude,
        }


class StoreManager:
    def __init__(self, path):
        self.stores = StoreManager.load_stores(path)

    @staticmethod
    def load_stores(path):
        stores = []
        with open(path) as file:
            for row in csv.DictReader(file):
                location = Location(row['Address'], row['Zip'], row['Location'])
                store = Store(row['Store Name'], row['New status'], row['Last updated'], location)
                stores.append(store)
        return stores

    def stores_with_shortest_name(self):
        shortest_name = min([len(s.name) for s in self.stores])
        return [s for s in self.stores if len(s.name) == shortest_name]

    def stores_with_apostrophe(self):
        return sorted(set([s.name for s in self.stores if "'" in s.name]))

    def categorize_by_zip(self):
        return Counter(s.location.zip_code for s in self.stores if s.location.zip_code)

    def open_stores_with_plus_4_codes(self):
        return len([s for s in self.stores if s.status == 'OPEN' and s.location.plus_four_code])

    def closed_stores(self):
        return [s for s in self.stores if s.status == 'CLOSED']

    def stores_updated_after_1pm(self):
        one_pm = dt.timedelta(hours=13)
        stores_after_1pm = []
        for s in self.stores:
            if s.last_updated:
                current = dt.timedelta(seconds=s.last_updated.second, minutes=s.last_updated.minute,
                                       hours=s.last_updated.hour)
                if current - one_pm >= dt.timedelta(0, 0, 0):
                    stores_after_1pm.append(s)
        return stores_after_1pm

    def average_coordinates(self):
        longitude_sum, latitude_sum = 0, 0
        number_of_coordinates = 0

        for s in self.stores:
            if s.location.has_coordinates():
                number_of_coordinates += 1
                longitude_sum += s.location.longitude
                latitude_sum += s.location.latitude

        return (latitude_sum / number_of_coordinates), (longitude_sum / number_of_coordinates)

    def export_data(self, path):
        with open(path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=sm.stores[0].to_dict().keys())
            writer.writeheader()
            for s in self.stores:
                if s.is_not_none():
                    writer.writerow(s.to_dict())


sm = StoreManager('Grocery_Store_Status.csv')
print('Stores with the shortest names:')
for s in sm.stores_with_shortest_name():
    print(f'{s.name}: {s.location.address}')
print('Stores with apostrophe in their names:')
for s in sm.stores_with_apostrophe():
    print(s)
print('Number of stores by zip code:')
for zip_code, count in sorted(sm.categorize_by_zip().items(), key=lambda t: t[1], reverse=True):
    print(f'{zip_code}: {count}')
print('Stores with apostrophe in their names:')
for s in sm.stores_with_apostrophe():
    print(s)
print('Number of open stores with plus four code:')
print(sm.open_stores_with_plus_4_codes())
print('Names and addresses of closed stores:')
for s in sm.closed_stores():
    print(f'{s.name}: {s.location.address}')
print('Names, zip codes and last update times of closed stores:')
for s in sm.stores_updated_after_1pm():
    print(
        f'{s.name} - {s.location.zip_code if s.location.zip_code else "Missing zip"} - {s.last_updated.strftime("%H:%M:%S")}')

print('Average coordinates:')
latitude, longitude = sm.average_coordinates()
print(latitude, longitude)
print('Distance of different stores from the average')
for s in sm.stores:
    if s.location.has_coordinates():
        print(f'{s.name} ({s.location.zip_code}) - {s.location.distance(latitude, longitude):.2f} km')

print('Exporting non-null data')
sm.export_data('Grocery_Store_Satus_Not_Null.csv')
