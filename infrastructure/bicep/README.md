# Azure Bicep Demonstration

This folder demonstrates Infrastructure as Code for a minimal Azure App Service deployment.

The file is intentionally small but shows:

- declarative infrastructure;
- source control;
- HTTPS-only configuration;
- minimum TLS configuration;
- disabled FTP;
- automated syntax/build validation in GitHub Actions.

## Validate Locally

```bash
az bicep build --file main.bicep
```

## Deployment

Actual Azure deployment is optional.

This public repository does not contain credentials or require paid cloud resources.

If deployed in a personal Azure environment, use an approved authenticated context and review cost before deployment.
