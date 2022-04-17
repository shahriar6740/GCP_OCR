import io
import os
import pandas as pd
from google.cloud import vision
from fuzzywuzzy import process

client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('demo5.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

gcp_output =[]
for text in texts:
    gcp_output.append(text.description)
gcp_output = list(gcp_output[0].splitlines())


print("\n\nGCP Output:\n\n")
print(gcp_output)
print("\n\nBrand Names:\n")



### read data ####
product_data = pd.read_csv("product_data.csv", usecols=[0], names=['colA'], header=None)
product_list = list(product_data['colA'])
print(product_list)
print("\n\n\nTOtal Matches: \n\n")



matches=[]
for i in gcp_output:

    p = process.extractOne(i,product_list)
    if p[1] >=80:
        matches.append(p[0])

print(matches)

print("\n\n\Count Matches: \n\n")

res = {i:matches.count(i) for i in matches}
print(res)

