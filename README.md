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

1. Run quickstart.py

    ```python
    python quickstart.py
    ```

    Using the .env file, this script authenticates to the resources created in the previous step and runs through some demonstrations of the ComputerVisionClient.

    Documentation for the ComputerVisionClient:

    <https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision?view=azure-python>

    The full Azure-Samples/cognitive-services-quickstart-code:

    <https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ComputerVisionQuickstart.py>
