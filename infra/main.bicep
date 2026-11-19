// main.bicep — describes Azure resources as code ("Infrastructure as Code").
// Instead of clicking around the Azure Portal, we write what we want here,
// and Azure creates/updates it to match. Nothing is created until you run a deploy command.
//
// This starter creates ONE storage account (cheap, a few cents/month), just to practice.

// ---- Parameters: values you can pass in at deploy time ----
@description('Short project code used in resource names')
param projectCode string = 'ndy'

@description('Environment: dev or prod')
@allowed(['dev', 'prod'])
param environment string = 'dev'

@description('Azure region. Defaults to the region of the resource group.')
param location string = resourceGroup().location

// ---- Variables: values computed inside the file ----
// Storage account names must be globally unique, lowercase, no dashes, 3-24 chars.
// uniqueString() makes a stable random-looking suffix from the resource group ID.
var storageName = toLower('st${projectCode}${environment}${uniqueString(resourceGroup().id)}')

var tags = {
  project: projectCode
  environment: environment
  managedBy: 'bicep'
}

// ---- Resources: the actual Azure things to create ----
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: take(storageName, 24)
  location: location
  tags: tags
  sku: {
    name: 'Standard_LRS'        // cheapest redundancy option
  }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false  // security: nothing is public by default
    supportsHttpsTrafficOnly: true
  }
}

// ---- Outputs: values printed after deployment ----
output storageAccountName string = storage.name
