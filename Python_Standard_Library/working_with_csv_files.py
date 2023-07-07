import csv

# Creating a CSV file
# Cannot use the path class for this
# with open("data.csv", "w") as file: # With means you dont have to close
#    writer = csv.writer(file)
#    writer.writerow(["transaction_id", "product_id", "price"])
#    writer.writerow([1000, 1, 5])
#    writer.writerow([1001, 2, 15])


# Reading a CSV file
with open("data.csv") as file:
   reader = csv.reader(file)
   # print(list(reader))
   for row in reader: # Iterating over the rows
      print(row)