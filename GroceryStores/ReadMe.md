# Grocery Stores in Chicago

The following dataset (`Grocery_Store_Status.csv`) has been obtained from [data.gov](https://catalog.data.gov/dataset/grocery-store-status) about the statuses of different grocery stores in Chicago.

## Breakdown of the data

The dataset contains the following columns:

- Store name - the name of the store
- Address - the address of the store
- Zip - the zip code of the store in 5 digits or ZIP+4 format (note that this data may be missing and the plus 4 code is not part of the ZIP but rather an extension to give more precision about the location)
- New status - the status of the store (typically either OPEN or CLOSED)
- Last updated - a date, the last time the store's status was updated (this data may be missing for some stores)
- Location - the precise coordinates (longitude and latitude) of the store, (this data may be missing for some stores)

# Tasks

## Load the data

Create a class (or classes) to organize the data. Load the data from the CSV file (you are free to use any approach, I recommend using a [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader)) while creating new objects using the class(es) you defined.

Processing the last update time as a datetime object can be a bit tricky, please refer to the formatting codes of strptime [here](https://www.nbshare.io/notebook/510557327/Strftime-and-Strptime-In-Python/) at the bottom of the page. Note that there is 2 spaces between the date and the time in the input file.

## Find the stores with the shortest names

Create a function that returns the stores with the shortest names. Display the stores and their corresponding addresses.

## Find stores that have an apostrophe in their names

Create a function that returns all the stores that have an apostrophe (`'`) in their names. Only return unique store names in alphabetically ascending order.

## Categorize the stores by ZIP codes

Create a function that returns the number of stores by ZIP codes. Exclude stores that do not have a ZIP code specified.

## Number of open stores with plus-four-codes

Create a function that returns the number of open stores that have additional plus-four-codes besides their ZIP code.

## Names of the closed stores

Create a function that returns the names and addresses of the closed stores.

## Stores updated after 1 PM

Create a function that returns the stores that were updated after 1 PM. Display the names and ZIP codes of these stores along with their last update time in a nice formatted manner (only display the time part). Indicate if the ZIP code of the store is missing.

# Additional tasks

## Average coordinates

Find the average coordinates of the stores.

## Distance of the stores from the average coordinates

Find the distance of the stores from the average coordinates. To calculate the distance, feel free to use the [following function](https://www.geeksforgeeks.org/program-distance-two-points-earth/).

Display the names and ZIP codes of the stores along with their distance from the average coordinates in KMs (round it to two decimal points). Indicate if the ZIP code of the store is missing.

# Eliminate None values and export the data

Eliminate attributes that have None values (except for the plus 4 code) and create separate fields for longitude and latitude