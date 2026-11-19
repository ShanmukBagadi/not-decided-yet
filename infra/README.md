# infra/ — Azure Infrastructure as Code (Bicep)

| File | What it is |
|---|---|
| `main.bicep` | Describes the Azure resources (right now: one storage account) |

## Deploying by hand (from your Mac, after `az login`)

```bash
# 1. Create a resource group (a "folder" in Azure that holds related resources)
az group create --name rg-ndy-dev --location eastus

# 2. Preview what WOULD change, without changing anything
az deployment group what-if --resource-group rg-ndy-dev --template-file infra/main.bicep

# 3. Actually deploy
az deployment group create --resource-group rg-ndy-dev --template-file infra/main.bicep

# 4. Clean up everything (deletes the whole resource group)
az group delete --name rg-ndy-dev
```

Always run **what-if** first. It's the "preview" button.
