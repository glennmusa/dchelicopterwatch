from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

from dotenv import load_dotenv

local_image_path = "resources/helicopter.jpg"

load_dotenv()
subscription_key = os.getenv('dchwcogsaccountkey')
endpoint = os.getenv('dchwcogsaccountendpoint')

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Describe an Image - local
This example describes the contents of an image with the confidence score.
'''
print("===== Describe an Image =====")

local_image = open(local_image_path, "rb")

description_result = computervision_client.describe_image_in_stream(local_image)

print("Description of local image: ")
if (len(description_result.captions) == 0):
    print("No description detected.")
else:
    for caption in description_result.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()
'''
END - Describe an Image - local
'''

'''
Categorize an Image -  local
This example extracts categories from a local image with a confidence score
'''
print("===== Categorize an Image =====")

local_image = open(local_image_path, "rb")
local_image_features = ["categories"]

categorize_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)

print("Categories from local image: ")
if (len(categorize_results_local.categories) == 0):
    print("No categories detected.")
else:
    for category in categorize_results_local.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))
print()
'''
END - Categorize an Image - local
'''

'''
Tag an Image - local
This example returns a tag (key word) for each thing in the image.
'''
print("===== Tag an Image =====")

local_image = open(local_image_path, "rb")

tags_result_local = computervision_client.tag_image_in_stream(local_image)

print("Tags in the local image: ")
if (len(tags_result_local.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_local.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
END - Tag an Image - local
'''

'''
Detect Color - local
This example detects the different aspects of its color scheme in a local image.
'''
print("===== Detect Color =====")

local_image = open(local_image_path, "rb")
local_image_features = ["color"]

detect_color_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)

print("Getting color scheme of the local image: ")
print("Is black and white: {}".format(detect_color_results_local.color.is_bw_img))
print("Accent color: {}".format(detect_color_results_local.color.accent_color))
print("Dominant background color: {}".format(detect_color_results_local.color.dominant_color_background))
print("Dominant foreground color: {}".format(detect_color_results_local.color.dominant_color_foreground))
print("Dominant colors: {}".format(detect_color_results_local.color.dominant_colors))
print()
'''
END - Detect Color - local
'''

'''
Detect Objects - local
This example detects different kinds of objects with bounding boxes in a local image.
'''
print("===== Detect Objects =====")

local_image_objects = open(local_image_path, "rb")

detect_objects_results_local = computervision_client.detect_objects_in_stream(local_image_objects)

print("Detecting objects in local image:")
if len(detect_objects_results_local.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results_local.objects:
        print("object at location {}, {}, {}, {}".format( \
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))
print()
'''
END - Detect Objects - local
'''

'''
Generate Thumbnail
This example creates a thumbnail.
'''
print("===== Generate Thumbnail =====")

local_image_thumb = open(local_image_path, "rb")

print("Generating thumbnail from a local image...")
# Call the API with a local image, set the width/height if desired (pixels)
# Returns a Generator object, a thumbnail image binary (list).
thumb_local = computervision_client.generate_thumbnail_in_stream(100, 100, local_image_thumb, True)

# Write the image binary to file
with open("resources/thumb.png", "wb") as f:
    for chunk in thumb_local:
        f.write(chunk)

# Uncomment/use this if you are writing many images as thumbnails from a list
# for i, image in enumerate(thumb_local, start=0):
#      with open('thumb_{0}.jpg'.format(i), 'wb') as f:
#         f.write(image)

print("Thumbnail saved to local folder.")
print()
'''
END - Generate Thumbnail
'''

'''
Recognize Printed Text with OCR - local
This example will extract, using OCR, printed text in an image, then print results line by line.
'''
print("===== Detect Printed Text with OCR =====")

local_image_printed_text = open(local_image_path, "rb")

ocr_result_local = computervision_client.recognize_printed_text_in_stream(local_image_printed_text)
for region in ocr_result_local.regions:
    for line in region.lines:
        print("Bounding box: {}".format(line.bounding_box))
        s = ""
        for word in line.words:
            s += word.text + " "
        print(s)
print()
'''
END - Recognize Printed Text with OCR - local
'''

print("End of Computer Vision quickstart.")