import io
import os

import pandas as pd
from google.cloud import vision
from fuzzywuzzy import process

"""
Before stepping further, Set the GCP service json file as your environment variable.
for Mac/Linux:
    export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
for windows:
    follow this link: https://cloud.google.com/vision/docs/detect-labels-image-client-libraries
"""


class Services:
    ### read data ####

    csv_path = os.path.join('api/service/product_data.csv')
    product_data = pd.read_csv(csv_path, usecols=[0], names=['colA'], header=None)
    product_list = list(product_data['colA'])
    #print(product_list)

    def cleanResult(self, texts):

        clean_output = []
        for text in texts:
            clean_output.append(text.description)
        clean_output = list(clean_output[0].splitlines())
        return clean_output

    def callGCP(self, file_name):

        client = vision.ImageAnnotatorClient()
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        gcp_output = self.cleanResult(texts)
        # print(gcp_output)
        return gcp_output

    def getMatches(self, file_name):

        matches = []
        gcp_result = self.callGCP(file_name)
        for output in gcp_result:
            p = process.extractOne(output, self.product_list)
            if p[1] >= 80:
                matches.append(p[0])
        match_result = {i: matches.count(i) for i in matches}
        print(match_result)
        return match_result


if __name__ == "__main__":
    service = Services()

    file_name = os.path.join('media/demo5.jpg')
    result = service.getMatches(file_name)
    print(result)
