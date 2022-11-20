import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"].max())


# data_dict =data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list
# print(temp_list)



#Create a dataframe from scratch

data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [76,56,65]
}
df = pandas.DataFrame(data_dict)
print(df.students)
# df.to_csv("new_data.csv")

