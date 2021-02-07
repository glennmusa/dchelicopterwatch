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

local_image_path = "resources/faces.jpg"

load_dotenv()
subscription_key = os.getenv('dchwcogsaccountkey')
endpoint = os.getenv('dchwcogsaccountendpoint')

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Describe an Image - local
This example describes the contents of an image with the confidence score.
'''
print("===== Describe an Image - local =====")

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
print("===== Categorize an Image - local =====")

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
print("===== Tag an Image - local =====")

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
Detect Faces - local
This example detects faces in a local image, gets their gender and age, 
and marks them with a bounding box.
'''
print("===== Detect Faces - local =====")

local_image = open(local_image_path, "rb")
local_image_features = ["faces"]

detect_faces_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)

print("Faces in the local image: ")
if (len(detect_faces_results_local.faces) == 0):
    print("No faces detected.")
else:
    for face in detect_faces_results_local.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))
print()
'''
END - Detect Faces - local
'''

'''
Detect Adult or Racy Content - local
This example detects adult or racy content in a local image, then prints the adult/racy score.
The score is ranged 0.0 - 1.0 with smaller numbers indicating negative results.
'''
print("===== Detect Adult or Racy Content - local =====")

local_image = open(local_image_path, "rb")
local_image_features = ["adult"]

detect_adult_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)

print("Analyzing local image for adult or racy content ... ")
print("Is adult content: {} with confidence {:.2f}".format(detect_adult_results_local .adult.is_adult_content, detect_adult_results_local .adult.adult_score * 100))
print("Has racy content: {} with confidence {:.2f}".format(detect_adult_results_local .adult.is_racy_content, detect_adult_results_local .adult.racy_score * 100))
print()
'''
END - Detect Adult or Racy Content - local
'''

'''
Detect Color - local
This example detects the different aspects of its color scheme in a local image.
'''
print("===== Detect Color - local =====")

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
Detect Domain-specific Content - local
This example detects celebrites and landmarks in local images.
'''
print("===== Detect Domain-specific Content - local =====")

local_image = open(local_image_path, "rb")

detect_domain_results_celebs_local = computervision_client.analyze_image_by_domain_in_stream("celebrities", local_image)

print("Celebrities in the local image:")
if len(detect_domain_results_celebs_local.result["celebrities"]) == 0:
    print("No celebrities detected.")
else:
    for celeb in detect_domain_results_celebs_local.result["celebrities"]:
        print(celeb["name"])

local_image_path_landmark = "resources/landmark.jpg"
local_image_landmark = open(local_image_path_landmark, "rb")

detect_domain_results_landmark_local = computervision_client.analyze_image_by_domain_in_stream("landmarks", local_image_landmark)
print()

print("Landmarks in the local image:")
if len(detect_domain_results_landmark_local.result["landmarks"]) == 0:
    print("No landmarks detected.")
else:
    for landmark in detect_domain_results_landmark_local.result["landmarks"]:
        print(landmark["name"])
print()
'''
END - Detect Domain-specific Content - local
'''

'''
Detect Image Types - local
This example detects an image's type (clip art/line drawing).
'''
print("===== Detect Image Types - local =====")

local_image_path_type = "resources/type-image.jpg"
local_image_type = open(local_image_path_type, "rb")
local_image_features = [VisualFeatureTypes.image_type]

detect_type_results_local = computervision_client.analyze_image_in_stream(local_image_type, local_image_features)

print("Type of local image:")
if detect_type_results_local.image_type.clip_art_type == 0:
    print("Image is not clip art.")
elif detect_type_results_local.image_type.line_drawing_type == 1:
    print("Image is ambiguously clip art.")
elif detect_type_results_local.image_type.line_drawing_type == 2:
    print("Image is normal clip art.")
else:
    print("Image is good clip art.")

if detect_type_results_local.image_type.line_drawing_type == 0:
    print("Image is not a line drawing.")
else:
    print("Image is a line drawing")
print()
'''
END - Detect Image Types - local
'''

'''
Detect Objects - local
This example detects different kinds of objects with bounding boxes in a local image.
'''
print("===== Detect Objects - local =====")

local_image_path_objects = "resources/objects.jpg"
local_image_objects = open(local_image_path_objects, "rb")

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
Detect Brands - local
This example detects common brands like logos and puts a bounding box around them.
'''
print("===== Detect Brands - local =====")

local_image_path_shirt = "resources/gray-shirt-logo.jpg"
local_image_shirt = open(local_image_path_shirt, "rb")

local_image_features = ["brands"]

detect_brands_results_local = computervision_client.analyze_image_in_stream(local_image_shirt, local_image_features)

print("Detecting brands in local image: ")
if len(detect_brands_results_local.brands) == 0:
    print("No brands detected.")
else:
    for brand in detect_brands_results_local.brands:
        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format( \
        brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \
        brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))
print()
'''
END - Detect brands - local
'''

'''
Generate Thumbnail
This example creates a thumbnail from both a local and URL image.
'''
print("===== Generate Thumbnail =====")

local_image_path_thumb = "resources/objects.jpg"
local_image_thumb = open(local_image_path_objects, "rb")

print("Generating thumbnail from a local image...")
# Call the API with a local image, set the width/height if desired (pixels)
# Returns a Generator object, a thumbnail image binary (list).
thumb_local = computervision_client.generate_thumbnail_in_stream(100, 100, local_image_thumb, True)

# Write the image binary to file
with open("thumb_local.png", "wb") as f:
    for chunk in thumb_local:
        f.write(chunk)

# Uncomment/use this if you are writing many images as thumbnails from a list
# for i, image in enumerate(thumb_local, start=0):
#      with open('thumb_{0}.jpg'.format(i), 'wb') as f:
#         f.write(image)

print("Thumbnail saved to local folder.")
print()


'''
Batch Read File, recognize handwritten text - local
This example extracts text from a handwritten local image, then prints results.
This API call can also recognize remote image text (shown in next example, Batch Read File - remote).
'''
print("===== Batch Read File - local =====")

local_image_handwritten_path = "resources/handwritten_text.jpg"
local_image_handwritten = open(local_image_handwritten_path, "rb")

# Call API with image and raw response (allows you to get the operation location)
recognize_handwriting_results = computervision_client.batch_read_file_in_stream(local_image_handwritten, raw=True)
# Get the operation location (URL with ID as last appendage)
operation_location_local = recognize_handwriting_results.headers["Operation-Location"]
# Take the ID off and use to get results
operation_id_local = operation_location_local.split("/")[-1]

while True:
    recognize_handwriting_result = computervision_client.get_read_operation_result(operation_id_local)
    if recognize_handwriting_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

if recognize_handwriting_result.status == OperationStatusCodes.succeeded:
    for text_result in recognize_handwriting_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()
'''
END - Batch Read File - local
'''

'''
Recognize Printed Text with OCR - local
This example will extract, using OCR, printed text in an image, then print results line by line.
'''
print("===== Detect Printed Text with OCR - local =====")

local_image_printed_text_path = "resources/printed_text.jpg"
local_image_printed_text = open(local_image_printed_text_path, "rb")

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