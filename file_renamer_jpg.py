import glob
import os

folder = "./Dutke/antoineGmal/img3/"
# search text files starting with the word "sales"
pattern = folder + "*.jpg"


# List of the files that match the pattern
result = glob.glob(pattern)


# Iterating the list with the count
count = 1
for file_name in result:
    old_name = file_name
    new_name = folder + str(count) + ".jpg"
    os.rename(old_name, new_name)
    count = count + 1



# printing all jpg and txt files
res = glob.glob(folder + "*.jpg")

for name in res:
    print(name)

