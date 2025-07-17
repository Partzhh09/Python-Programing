jadeja={
    "name": "Ravindra Jadeja",
    "age": 34,
    "runs" : []
}

jadeja["runs"].append(int(input("Enter runs scored by Jadeja: ")))
jadeja["runs"].append(int(input("Enter runs scored by Jadeja: ")))
jadeja["runs"].append(int(input("Enter runs scored by Jadeja: ")))
jadeja["runs"].append(int(input("Enter runs scored by Jadeja: ")))


print(jadeja)

def avg_runs(jadeja):
    return sum(jadeja["runs"]) / len(jadeja["runs"])

print("Average runs scored by Jadeja:", avg_runs(jadeja))


# Jonny = {
#     "name" : "Jonathan Jude Amaral",
#     "profession" : "Gamer",
#     "age" : 25
# }

# print(Jonny)

