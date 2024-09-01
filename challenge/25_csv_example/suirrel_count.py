import csv
import pandas
import statistics

data_path = './squirrel.csv'

squirrel_source_data = pandas.read_csv(data_path)

gray_fur = len(squirrel_source_data[squirrel_source_data["Primary Fur Color"] == "Gray"])
red_fur = len(squirrel_source_data[squirrel_source_data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(squirrel_source_data[squirrel_source_data["Primary Fur Color"] == "Black"])

print(gray_fur)
print(red_fur)
print(black_fur)

squirrel_data = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Amount": [gray_fur, red_fur, black_fur]
}

squirrel_data_set = pandas.DataFrame(squirrel_data)

squirrel_data_set.to_csv("./squirrel_count.csv")