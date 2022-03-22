import glob
import os

# put the relative path to the folder containing your raw_data with annotations
folder = "./darknet/doc_data/doc_images"
# search text files with an "F" in the name to prevent renaming "classes.txt"
pattern = folder + "*F*.txt"


# List of the files that match the pattern
result = glob.glob(pattern)


# Iterating the list with the count
count = 1
for file_name in result:
    old_name = file_name
    new_name = folder + str(count) + ".txt"
    os.rename(old_name, new_name)
    count = count + 1



# printing all txt files
res = glob.glob(folder + "*.txt")

for name in res:
    print(name)