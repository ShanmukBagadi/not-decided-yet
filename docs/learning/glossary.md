# Glossary: plain-English explanations

New terms get added here as the project grows.

---

## Git & GitHub

**Git**: A tool that records the history of your files. Each saved snapshot is a *commit*.
You can always go back to an earlier commit.

**Repository (repo)**: A project folder tracked by git, including its full history.

**Commit**: A saved snapshot with a message describing what changed.

**Branch**: A parallel line of work. `main` is the official version; you make a branch to
try changes without breaking `main`.

**Push / Pull**: *Push* uploads your commits to GitHub; *pull* downloads others' commits.

**Pull Request (PR)**: A request to merge a branch into `main`. Others (or AI) review it first,
and CI checks run on it.

---

## GitHub Actions

**GitHub Actions**: Automation that runs on GitHub's computers when something happens
(e.g. you push code). Defined in YAML files in `.github/workflows/`.

**Workflow → Job → Step**: A *workflow* is the whole file. It has *jobs* (each runs on its own
fresh virtual machine), and each job has *steps* (individual commands).

**CI (Continuous Integration)**: Automatically testing every change so bugs are caught early.

**CD (Continuous Deployment)**: Automatically deploying to Azure after checks pass. We'll add this later.

**Secrets (in GitHub)**: Encrypted values (like Azure IDs) stored in repo settings and given to
workflows. They're never visible in code or logs.

---

## Python tooling

**uv**: A very fast tool that installs Python, creates a virtual environment, and installs libraries.
It replaces `pip`, `venv`, and `pyenv` in one tool.

**Virtual environment (`.venv/`)**: A private folder of libraries just for this project, so
projects don't conflict with each other.

**Dependency**: A library your code uses (e.g. `python-dotenv`).

**pytest**: Runs your tests. A *test* is a small function that checks your code gives the expected result.

**ruff**: A *linter* (finds likely bugs and bad patterns) and *formatter* (makes code style consistent).

**pre-commit**: Runs checks automatically every time you `git commit`.

**gitleaks**: Scans for accidentally committed passwords and keys.

---

## Azure

**Azure Portal**: The website (portal.azure.com) where you click to manage Azure. Good for
exploring, but we prefer code (Bicep) for creating things so it's repeatable.

**Tenant**: Your organization's identity "home" in Microsoft (Entra ID). Holds users, groups, apps.
Your Outlook/Teams accounts live here too. Identified by a **Tenant ID**.

**Subscription**: A billing account for Azure resources. Everything you create costs money against
a subscription. Identified by a **Subscription ID**.

**Resource Group**: A folder inside a subscription grouping related resources. Delete the group
and everything in it is deleted.

**Resource**: Anything you create in Azure: storage account, web app, database, AI service...

**Region / Location**: The physical data-center area where a resource runs (e.g. `eastus`).

**Azure CLI (`az`)**: A command-line tool for controlling Azure from your terminal.
`az login` signs you in.

**Entra ID (formerly Azure Active Directory)**: Microsoft's identity system for sign-in and permissions.

---

## Infrastructure as Code

**Infrastructure as Code (IaC)**: Describing cloud resources in text files instead of clicking in
the portal. Benefits: repeatable, reviewable, version-controlled, easy to delete and recreate.

**Bicep**: Microsoft's language for Azure IaC. You write *what* you want; Azure figures out
*how* to create or update it. Converts to ARM JSON behind the scenes.

**Parameter / Variable / Output (Bicep)**: *Parameters* are inputs you pass in; *variables*
are computed values inside the file; *outputs* are results printed after deploy.

**what-if**: A preview showing what a deployment *would* change, without changing anything.

---

## Identity for automation

**Service Principal**: An identity for an *app or robot* (not a human). GitHub Actions uses one to
log in to Azure and deploy. You give it only the permissions it needs.

**App Registration**: The definition of an app in Entra ID. Creating one also creates its
Service Principal. Needed for both GitHub→Azure deploys and Microsoft Graph access.

**OIDC / Federated credential**: A way for GitHub Actions to log in to Azure **without storing
a password**. Azure trusts GitHub to vouch for "this is a workflow from repo X". This is the safest
option and the one we'll use.

**RBAC (Role-Based Access Control)**: Azure's permission system. You assign *roles* (e.g. Reader,
Contributor) to identities on a *scope* (subscription, resource group).

**Least privilege**: Give every identity only the minimum permissions it needs.

---

## Microsoft 365

**Microsoft Graph**: One API to access Microsoft 365 data: Outlook mail and calendar, Teams messages,
users, files. Our Python code will use it to work with Outlook and Teams.

**API**: A way for programs to talk to each other, usually over HTTPS.

---

## AI

**LLM (Large Language Model)**: An AI model that understands and generates text, like Claude or GPT.

**Azure OpenAI / Azure AI Foundry**: Azure services for using AI models inside your Azure tenant.

**MCP (Model Context Protocol)**: A standard "plug" that lets an AI assistant use outside tools
and data. An *MCP server* exposes tools (e.g. "list my Azure resources", "read my Outlook
email") that an AI like Claude can call. Think USB-C for AI: one standard connector for many devices.
**Why we'd use it here:** with an Azure MCP server, Claude could look up your actual Azure
resources while helping you code; with a Microsoft 365 MCP server, it could read Teams or Outlook.
We haven't added any yet. We'll add them once the project idea is decided.

**Agent**: An AI that can take actions (run tools, edit files) in steps toward a goal, not just chat.
