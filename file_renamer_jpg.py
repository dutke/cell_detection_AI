import glob
import os

# put the relative path to the folder containing your raw_data with annotations
folder = "./doc_data/doc_images"
# search image files
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



# printing all jpg files
res = glob.glob(folder + "*.jpg")

for name in res:
    print(name)