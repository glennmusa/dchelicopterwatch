# dchelicopterwatch

An app that tries to identify the helicopters of Washington DC

## What is Computer Vision?

<https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview>

## Getting started

1. Open the repository in the .devcontainer

    <https://code.visualstudio.com/docs/remote/containers-tutorial>

1. Login to Azure CLI

    ```bash
    az login
    ```

1. Run scripts/createcomputervision.sh to create the required Azure resources

    ```bash
    chmod u+x scripts/createcomputervision.sh
    scripts/createcomputervision.sh
    ```

    This script deploys a Resource Group and a Computer Vision Cognitive Services Account and writes the account name, endpoint, and account key to the .env file at the root of the repository.

    This deployment is sourced from this Azure Resource Manager template:

    <https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-cognitive-services-Computer-vision-API/azuredeploy.json>

1. Run quickstart.py from the terminal

    ```python
    python quickstart.py
    ```

    Using the .env file, this script authenticates to the resources created in the previous step and runs through some demonstrations of the ComputerVisionClient.

    Documentation for the ComputerVisionClient:

    <https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision?view=azure-python>

    The full Azure-Samples/cognitive-services-quickstart-code:

    <https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ComputerVisionQuickstart.py>

1. Inspect results in the terminal

    You'll see what the Computer Vision API returns similar to this:

    ```plaintext
    ===== Describe an Image =====
    Description of local image: 
    'a helicopter flying in the sky' with confidence 59.82%

    ===== Categorize an Image =====
    Categories from local image: 
    'sky_object' with confidence 99.61%

    ===== Tag an Image =====
    Tags in the local image: 
    'sky' with confidence 100.00%
    'outdoor' with confidence 99.77%
    'transport' with confidence 99.01%
    'aircraft' with confidence 97.01%
    'helicopter' with confidence 90.45%
    'vehicle' with confidence 86.20%
    'air' with confidence 74.26%
    'airplane' with confidence 57.47%
    'blue' with confidence 56.61%
    'helicopter rotor' with confidence 55.10%
    'engine' with confidence 20.81%
    'fighter' with confidence 13.07%
    'landing' with confidence 11.86%

    ===== Detect Color =====
    Getting color scheme of the local image: 
    Is black and white: False
    Accent color: 2A62A1
    Dominant background color: Grey
    Dominant foreground color: Grey
    Dominant colors: []

    ===== Detect Objects =====
    Detecting objects in local image:
    object at location 1779, 2674, 754, 1253
    object at location 99, 2269, 143, 1389

    ===== Generate Thumbnail =====
    Generating thumbnail from a local image...
    Thumbnail saved to local folder.
    ```

1. Try different source images

    Try different images from the /resources directory and see what results you get by updating [quickstart.py line 14](quickstart.py)

    ```python
    local_image_path = "resources/helicopter.jpg"
    ```

    ```python
    local_image_path = "resources/plane.jpg"
    ```

    ```python
    local_image_path = "resources/birds.jpg"
    ```

    ```python
    local_image_path = "resources/faces.jpg"
    ```

    ```python
    local_image_path = "resources/printed_text.jpg"
    ```
