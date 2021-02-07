#!/bin/bash

PGM=`basename $0`

if ! command -v az &> /dev/null
then
    echo "${PGM} Azure CLI could not be found. This script requires Azure CLI."
    echo "${PGM} Install instructions here: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli"
    exit
fi

rgName=${1:-dchelicopterwatchrg}
rgLocation=${2:-eastus}

timestamp=$(date +%s)
deploymentName="${rgName}${timestamp}"

az group create \
    --name "$rgName" \
    --location "$rgLocation" \

az deployment group create \
    --name "$deploymentName" \
    --resource-group "$rgName" \
    --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-cognitive-services-Computer-vision-API/azuredeploy.json"

cogsAccountName=$(az deployment group show \
    --name "$deploymentName" \
    --resource-group "$rgName" \
    --query properties.parameters.accountName.value \
    --output tsv)

cogsAccountEndpoint=$(az cognitiveservices account show \
    --name "$cogsAccountName" \
    --resource-group "$rgName" \
    --query "properties.endpoint" \
    --output tsv)

cogsAccountKey=$(az cognitiveservices account keys list \
    --name "$cogsAccountName" \
    --resource-group "$rgName" \
    --query "key1" \
    --output tsv)    

echo "Created a Cognitive Services Account: ${cogsAccountName}"
echo "Cognitive Services Account Endpoint: ${cogsAccountEndpoint}"
echo "Cognitive Services Account key: ${cogsAccountKey}"

touch ../.env
echo "dchwcogsaccountname=${cogsAccountName}" | tee ../.env
echo "dchwcogsaccountendpoint=${cogsAccountEndpoint}" | tee -a ../.env
echo "dchwcogsaccountkey=${cogsAccountKey}" | tee -a ../.env
