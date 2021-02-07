import os
import sys

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
subscription_key = os.getenv('dchwcogsaccountkey')
endpoint = os.getenv('dchwcogsaccountendpoint')
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_path = "resources/helicopter.jpg"

image = open(image_path, "rb")
tags_result = computervision_client.tag_image_in_stream(image)

caption="I don't know what it is."

if (len(tags_result.tags) > 0):
    for tag in tags_result.tags:
        if tag.name == "helicopter" :                        
            if tag.confidence * 100 > 90 :
                print("That's a helicopter.")
            else :
                print("That could be a helicopter?")
                print("I'm like {:.2f}% confident it could be.".format(tag.confidence * 100))                        
            sys.exit()
    image = open(image_path, "rb")
    description_result = computervision_client.describe_image_in_stream(image)    
    if (len(description_result.captions) > 0):        
        caption="I think it's " + description_result.captions[0].text + "."
    print("That's not a helicopter.")
    print(caption)
else:
    print(caption)
