
mylist = ["test", "34"]

output = f"tags: {mylist}"
output = output.replace("'", '"')

with open("test_file.txt", "w") as f:
    f.write(output)

# test regex for a number at the beginnning middle and end of string