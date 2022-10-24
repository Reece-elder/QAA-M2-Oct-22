carFile = open("carSale.csv", "r")

data = carFile.readlines()

# print(data)

companies = []
sales = []

count = 0
for lines in data:
    if count % 2 == 0:
        companies.append(lines.strip())
    else:
        # For every 'lines' which is odd, run the int() converting it to an int
        # convert this data into a list, and append this to our sales
        splitData = lines.strip().split(',')
        sales.append(list(map(int, splitData)))
    count += 1

print(companies)
print(sales) # All sales from Volkswagen in March

# Sum of cars sold in each month
jan = 0
feb = 0
mar = 0
apr = 0
may = 0
jun = 0
jul = 0
aug = 0

for x in sales:
    jan += x[0]
    feb += x[1]
    mar += x[2]

print(jan)
print(feb)
print(mar)